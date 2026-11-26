#!/usr/bin/env python3
"""Baut SOURCES.md aus den Quellentabellen in quellen/notizen/*.md.

Jede Notizdatei enthält eine Tabelle mit der Kopfzeile
| ID | Titel | Herausgeber | Typ | URL (vollständig) | Abgerufen am | Erreichbar? | Bemerkung |
Doppelte IDs werden gemeldet (die erste gewinnt).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTIZEN = ROOT / "quellen" / "notizen"
ROW_RE = re.compile(r"^\|\s*([ABCVPU])-(\d{3})\s*\|.*\|\s*$")
GRUPPEN = {
    "A": "A – Steuerung, Einstellungen, Technik, Patches",
    "B": "B – Spielsysteme, Welt, Fahrzeuge, Wirtschaft, Kampf, Polizei",
    "C": "C – Missionen, Story, Tipps, FAQ",
    "V": "V – Voice-Coach und KI-Werkzeuge",
    "P": "P – Projektleitung und Nachprüfung",
    "U": "U – Eigene Beobachtungen des Nutzers",
}
KOPF = "| ID | Titel | Herausgeber | Typ | URL | Abgerufen am | Erreichbar? | Bemerkung |\n|---|---|---|---|---|---|---|---|"


def main() -> int:
    zeilen: dict[str, list[tuple[int, str]]] = {k: [] for k in GRUPPEN}
    gesehen: dict[str, str] = {}
    doppelt = []
    for f in sorted(NOTIZEN.glob("*.md")):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = ROW_RE.match(line.strip())
            if not m:
                continue
            qid = f"{m.group(1)}-{m.group(2)}"
            if qid in gesehen:
                doppelt.append(f"{qid} ({gesehen[qid]} und {f.name})")
                continue
            gesehen[qid] = f.name
            zeilen[m.group(1)].append((int(m.group(2)), line.strip()))

    out = ["# SOURCES – Quellenverzeichnis", "",
           "> **Automatisch erzeugt** von `tools/build_sources.py` aus `quellen/notizen/*.md`. Bitte dort ändern, nicht hier.",
           "> „Erreichbar? = nein“ oder „nur Suchergebnis“ bedeutet: Die Seite wurde **nicht** vollständig geprüft. Aussagen daraus sind höchstens 🟡.",
           "", f"**Anzahl Quellen:** {len(gesehen)}", ""]
    for k, titel in GRUPPEN.items():
        out += [f"## {titel}", ""]
        if zeilen[k]:
            out += [KOPF] + [l for _, l in sorted(zeilen[k])]
        else:
            out.append("_(noch keine)_")
        out.append("")
    (ROOT / "SOURCES.md").write_text("\n".join(out), encoding="utf-8")
    print(f"SOURCES.md geschrieben: {len(gesehen)} Quellen")
    if doppelt:
        print("WARNUNG doppelte IDs:", "; ".join(doppelt))
    return 0


if __name__ == "__main__":
    sys.exit(main())
