#!/usr/bin/env python3
"""Erzeugt Upload-Dateien für den Voice-Coach (ChatGPT-/Claude-Projekt).

  python3 tools/build_coach_paket.py                 → berater/export/coach-paket-spoilerfrei.md
  python3 tools/build_coach_paket.py --bis-kapitel 3 → zusätzlich berater/export/coach-paket-bis-kapitel-03.md
                                                       (enthält Spoilerdateien NUR bis einschließlich Kapitel 3)

Nur Python-Standardbibliothek. Es werden keine Netzwerkzugriffe oder API-Aufrufe gemacht.
"""
from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPORT = ROOT / "berater" / "export"


def lesen(p: Path) -> str:
    text = p.read_text(encoding="utf-8")
    # Relative Links funktionieren im Upload nicht – Linkziel entfernen, Text behalten
    return re.sub(r"(?<!!)\[([^\]]+)\]\((?![a-z]+:)[^)]+\)", r"\1", text)


def kapitel_nr(p: Path) -> int | None:
    m = re.search(r"kapitel-(\d+)", p.stem)
    return int(m.group(1)) if m else None


def bauen(dateien: list[Path], titel: str, hinweis: str) -> str:
    teile = [f"# {titel}", "", f"> Erzeugt am {date.today().isoformat()} aus dem Repo gta-vi-wissensdatenbank. {hinweis}",
             "> Statuslegende: ✅ bestätigt · 🟡 plausibel · ❓ unbestätigt · ❌ widerlegt. Quellen-IDs siehe SOURCES.md im Repo.", ""]
    for f in dateien:
        teile += ["", "---", f"<!-- Datei: {f.relative_to(ROOT).as_posix()} -->", "", lesen(f).strip(), ""]
    return "\n".join(teile) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bis-kapitel", type=int, default=None)
    args = ap.parse_args()
    EXPORT.mkdir(parents=True, exist_ok=True)

    basis = sorted((ROOT / "wissen").glob("*.md"))
    ziel = EXPORT / "coach-paket-spoilerfrei.md"
    ziel.write_text(bauen(basis, "GTA VI Coach – Wissenspaket (spoilerfrei)",
                          "Enthält KEINE Story- oder Missionsspoiler."), encoding="utf-8")
    print(f"geschrieben: {ziel.relative_to(ROOT)} ({len(basis)} Dateien)")

    if args.bis_kapitel is not None:
        n = args.bis_kapitel
        spoiler = []
        for ordner in ("missionen", "story"):
            for f in sorted((ROOT / "spoiler" / ordner).glob("kapitel-*.md")):
                k = kapitel_nr(f)
                if k is not None and k <= n:
                    spoiler.append(f)
        ziel2 = EXPORT / f"coach-paket-bis-kapitel-{n:02d}.md"
        ziel2.write_text(bauen(spoiler, f"GTA VI Coach – Missionen & Story bis Kapitel {n}",
                               f"⚠️ SPOILER bis einschließlich Kapitel {n}. Nichts aus späteren Kapiteln."), encoding="utf-8")
        print(f"geschrieben: {ziel2.relative_to(ROOT)} ({len(spoiler)} Dateien)")


if __name__ == "__main__":
    main()
