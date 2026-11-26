#!/usr/bin/env python3
"""Qualitätsprüfung der GTA-VI-Wissensdatenbank (nur Python-Standardbibliothek).

Prüft:
  1. Pflichtdateien und -ordner vorhanden
  2. Interne Markdown-Links zeigen auf existierende Dateien
  3. JSON-Dateien in daten/ sind gültig
  4. Verwendete Quellen-IDs (z. B. [A-001]) sind in SOURCES.md definiert
  5. Wissensdateien haben Kopfblock (Spoilerstufe, Kurzfassung)
  6. Spoilerdateien haben eine Warnung am Anfang
  7. Spoiler-Leck-Heuristik: Missionstitel aus daten/missionen.json in spoilerfreien Dateien

Aufruf:  python3 tools/qc_check.py [--report qualitaet/qc-ergebnis.md]
Exit-Code 1 bei Fehlern, 0 bei nur Warnungen.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PFLICHT = [
    "README.md", "CLAUDE.md", "AGENTS.md", "SOURCES.md", "CHANGELOG.md", "ROADMAP.md",
    "INDEX.md", "GESAMTANLEITUNG.md", "wissen", "spoiler", "quellen", "berater", "qualitaet",
    "daten", "eigene-inhalte", "berater/system-prompt.md", "spoiler/README.md",
]

# Spoilerfreie Bereiche (dürfen keine Missionstitel enthalten)
SPOILERFREI = ["wissen", "berater", "GESAMTANLEITUNG.md", "README.md", "INDEX.md"]

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
QID_RE = re.compile(r"\b([ABCVPU]-\d{3})\b")
QDEF_RE = re.compile(r"^\|\s*([ABCVPU]-\d{3})\s*\|", re.M)
STATUS = {"✅": "bestätigt", "🟡": "plausibel", "❓": "unbestätigt", "❌": "widerlegt"}


def md_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def strip_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", help="Ergebnis zusätzlich als Markdown speichern")
    args = ap.parse_args()

    fehler: list[str] = []
    warnungen: list[str] = []
    statistik: dict[str, dict[str, int]] = {}

    # 1. Pflichtdateien
    for p in PFLICHT:
        if not (ROOT / p).exists():
            fehler.append(f"Pflichtdatei/-ordner fehlt: {p}")

    # 4. Quellen-Definitionen
    sources = ROOT / "SOURCES.md"
    definiert = set(QDEF_RE.findall(sources.read_text(encoding="utf-8"))) if sources.exists() else set()
    benutzt: dict[str, set[str]] = {}

    for f in md_files():
        rel = f.relative_to(ROOT).as_posix()
        text = f.read_text(encoding="utf-8")
        body = strip_code(text)

        beispiel = rel.startswith("vorlagen/") or rel in ("AGENTS.md", "CLAUDE.md", "qualitaet/qc-ergebnis.md")

        # 2. Links (Vorlagen enthalten Platzhalter-Links)
        for ziel in ([] if rel.startswith("vorlagen/") else LINK_RE.findall(body)):
            if re.match(r"^[a-z]+:", ziel) or ziel.startswith("#"):
                continue
            pfad = ziel.split("#", 1)[0]
            if not pfad:
                continue
            if not (f.parent / pfad).resolve().exists():
                fehler.append(f"{rel}: toter Link → {ziel}")

        # 4. Quellen-IDs (Quellenlisten selbst ausgenommen)
        if not rel.startswith("quellen/notizen/") and rel != "SOURCES.md" and not beispiel:
            for qid in QID_RE.findall(body):
                benutzt.setdefault(qid, set()).add(rel)

        # Status-Statistik
        statistik[rel] = {name: body.count(sym) for sym, name in STATUS.items()}

        # 5. Kopfblock Wissensdateien
        if rel.startswith("wissen/"):
            if "Spoilerstufe" not in text[:600]:
                fehler.append(f"{rel}: Kopfblock ohne 'Spoilerstufe'")
            if "Kurzfassung" not in text:
                warnungen.append(f"{rel}: Abschnitt 'Kurzfassung für den Voice-Coach' fehlt")
            if "S0" not in text[:600]:
                fehler.append(f"{rel}: Wissensdatei nicht als S0 gekennzeichnet")

        # 6. Spoilerwarnung
        if rel.startswith("spoiler/") and rel != "spoiler/README.md":
            if "spoiler" not in text[:500].lower():
                fehler.append(f"{rel}: keine Spoilerwarnung am Dateianfang")

    for qid, orte in sorted(benutzt.items()):
        if qid not in definiert:
            fehler.append(f"Quellen-ID {qid} nicht in SOURCES.md definiert (benutzt in: {', '.join(sorted(orte))})")
    unbenutzt = sorted(definiert - set(benutzt))
    if unbenutzt:
        warnungen.append(f"{len(unbenutzt)} Quellen in SOURCES.md werden nirgends zitiert: {', '.join(unbenutzt[:15])}{' …' if len(unbenutzt) > 15 else ''}")

    # 3. JSON
    missionen = []
    for j in sorted((ROOT / "daten").glob("*.json")):
        try:
            data = json.loads(j.read_text(encoding="utf-8"))
            if j.name == "missionen.json" and isinstance(data, list):
                missionen = data
            if isinstance(data, list):
                fehlend = sorted({q for e in data if isinstance(e, dict) for q in (e.get("quellen") or []) if q not in definiert})
                if fehlend:
                    fehler.append(f"daten/{j.name}: Quellen-IDs nicht in SOURCES.md: {', '.join(fehlend)}")
        except json.JSONDecodeError as e:
            fehler.append(f"daten/{j.name}: ungültiges JSON ({e})")

    # 7. Spoiler-Leck-Heuristik (erste Mission ist erlaubt)
    titel = set()
    for m in missionen:
        if not isinstance(m, dict) or m.get("reihenfolge") == 1 and m.get("kapitel") in (0, 1):
            continue
        for key in ("titel_en", "titel_de"):
            t = m.get(key)
            if isinstance(t, str) and len(t) >= 6:
                titel.add(t)
    for bereich in SPOILERFREI:
        pfad = ROOT / bereich
        dateien = [pfad] if pfad.is_file() else sorted(pfad.rglob("*.md")) if pfad.exists() else []
        for f in dateien:
            text = f.read_text(encoding="utf-8")
            for t in titel:
                if re.search(r"(?<!\w)" + re.escape(t) + r"(?!\w)", text):
                    warnungen.append(f"Mögliches Spoiler-Leck: Missionstitel '{t}' in {f.relative_to(ROOT).as_posix()}")

    # Ausgabe
    total = {name: sum(s[name] for s in statistik.values()) for name in STATUS.values()}
    zeilen = ["# QC-Ergebnis", "",
              f"- Markdown-Dateien: {len(statistik)}",
              f"- Definierte Quellen: {len(definiert)} · zitierte Quellen-IDs: {len(benutzt)}",
              f"- Statusmarker gesamt: " + ", ".join(f"{k} {v}" for k, v in total.items()),
              f"- Fehler: {len(fehler)} · Warnungen: {len(warnungen)}", ""]
    if fehler:
        zeilen += ["## Fehler", ""] + [f"- {x}" for x in fehler] + [""]
    if warnungen:
        zeilen += ["## Warnungen", ""] + [f"- {x}" for x in warnungen] + [""]
    zeilen += ["## Statusmarker je Wissensdatei", "", "| Datei | ✅ | 🟡 | ❓ | ❌ |", "|---|---|---|---|---|"]
    for rel, s in statistik.items():
        if rel.startswith(("wissen/", "spoiler/")) or rel == "GESAMTANLEITUNG.md":
            zeilen.append(f"| {rel} | {s['bestätigt']} | {s['plausibel']} | {s['unbestätigt']} | {s['widerlegt']} |")
    ausgabe = "\n".join(zeilen) + "\n"
    print(ausgabe)
    if args.report:
        (ROOT / args.report).write_text(ausgabe, encoding="utf-8")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
