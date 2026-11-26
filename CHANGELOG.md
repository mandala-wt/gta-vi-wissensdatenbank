# CHANGELOG

Alle Änderungen an der Wissensdatenbank. Format: neueste oben. Datumsformat JJJJ-MM-TT.

## [0.1.0] – 2026-11-26 – Erstaufbau

Branch `claude/gta-vi-ps5-knowledge-base-ku8nos`, Pull Request zur Prüfung.

### Hinzugefügt
- Projektgerüst: `README.md`, `CLAUDE.md`, `AGENTS.md`, `INDEX.md`, `SOURCES.md` (automatisch erzeugt), `ROADMAP.md`, dieses Changelog.
- **17 Wissensbereiche** in `wissen/` (S0, spoilerfrei) und Bereich 18 (KI-Berater) in `berater/`.
- **Spoilerbereich** `spoiler/` mit 5 Kapiteldateien für Missionen (S1) und 5 für Story (S2).
- **GESAMTANLEITUNG.md**: zusammenhängende, spoilerfreie Einsteigeranleitung.
- **Strukturierte Daten** in `daten/`: `missionen.json` (148 Einträge), `einstellungen.json` (135), `orte.json` (12), `fahndungsstufen.json` (2, nur belegte Eckpunkte).
- **Voice-Coach**: Einrichtungsanleitung (ChatGPT-Projekt + iPhone + AirPods), System-Prompt, Spielerprofil-Vorlage, Gedächtnis-Konzept, Antwortbeispiele, Export-Paket `berater/export/`.
- **Quellen**: 116 Quellen (A: 30, B: 39, C: 32, V: 9, P: 6) mit URL, Abrufdatum und Erreichbarkeit.
- **Werkzeuge** (Python, nur Standardbibliothek): `tools/qc_check.py`, `tools/build_sources.py`, `tools/build_coach_paket.py`, `tools/setup.sh`.
- **Qualität**: `qualitaet/checkliste.md`, `qualitaet/pruefbericht.md`, `qualitaet/qc-ergebnis.md`, `qualitaet/abschlussbericht.md`.
- Ordner und Vorlagen für eigene Inhalte (PDFs, Screenshots, Spielbeobachtungen, Nutzerfragen).

### Geprüft/korrigiert durch Projektleitung
- Widerspruch „Anzahl Speicherplätze“ (14 vs. 15 manuelle) in `wissen/15-faq.md` und Gesamtanleitung ergänzt.
- „Day-One-Patch 1.002.001“ richtiggestellt: Laut Agent A war das ein Vorab-Update vor Release.
- Stichproben-Gegenprüfung (30 FPS ohne Performance-Modus, Rennen auf L3 / Classic-Schema) mit unabhängigen Quellen P-003 bis P-006 bestätigt.
- Formulierung in `wissen/13-kinomodus-autofahrt.md` angepasst, um einen Fehlalarm der Spoiler-Prüfung zu beheben.
