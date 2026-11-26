# Abschlussbericht – GTA VI PS5 Wissensdatenbank (Version 0.1.0)

> **Datum:** 2026-11-26 · **Branch:** `claude/gta-vi-ps5-knowledge-base-ku8nos` · **Stand des Spiels:** erschienen am 19.11.2026, letzter bekannter PS5-Patch 01.002.002 (🟡)

## 1. Durchgeführte Arbeiten

1. **Ist-Analyse:** Das Repo war leer (nur README). Release-Stand geprüft: GTA VI ist seit 19.11.2026 erhältlich, es gibt also echte Spielinhalte zu dokumentieren.
2. **Regelwerk zuerst:** `AGENTS.md` (Status, Quellen-IDs, Spoilerstufen S0/S1/S2, Verbot von GTA-V-Übertragungen) und eine Vorlage für alle Wissensdateien, damit drei Agenten einheitlich arbeiten.
3. **Parallele Recherche** durch drei Agenten (siehe Abschnitt 2) mit getrennten Dateien und getrennten Quellen-ID-Präfixen, damit es keine Überschneidungen gibt.
4. **Voice-Coach-Recherche** durch die Projektleitung (aktueller Stand von ChatGPT-, Claude- und Grok-Voice) und Erstellung von Bereich 18 (`berater/`).
5. **Automatisierung:** Skripte für Quellenverzeichnis, Qualitätsprüfung und Coach-Export.
6. **Zusammenführung:** Gesamtanleitung, Index, Quellenverzeichnis, Abgleich der Widersprüche zwischen den Agenten.
7. **Qualitätskontrolle:** automatische Prüfung (0 Fehler), manuelle Spoiler-Prüfung, Faktencheck-Stichproben, siehe [pruefbericht.md](pruefbericht.md).

## 2. Beteiligte Agenten

| Agent | Aufgabe | Bereiche | Ergebnis |
|---|---|---|---|
| **Projektleitung** | Planung, Regelwerk, Voice-Coach, Automatisierung, Zusammenführung, QC | 18 + Gesamtanleitung | 15 Quellen (V/P) |
| **Agent A** – Technik & Steuerung | Recherche + Dokumentation | 1, 2, 3, 4, 13, 16, 17 | 7 Dateien, `einstellungen.json` (135 Einträge), 30 Quellen |
| **Agent B** – Spielsysteme & Welt | Recherche + Dokumentation | 5, 6, 7, 10, 11, 12 | 6 Dateien, `orte.json`, `fahndungsstufen.json`, 39 Quellen |
| **Agent C** – Story, Missionen & Tipps | Recherche + Dokumentation, Spoiler-Trennung | 8, 9, 14, 15 + `spoiler/` | 4 + 11 Dateien, `missionen.json` (148 Einträge), 32 Quellen |
| Hilfsagent (Web-Abruf) | Prüfung der OpenAI-Release-Notes | 18 | Grundlage für V-001 |

Höchstens drei Recherche-Agenten liefen gleichzeitig.

## 3. Verwendete Quellen

**116 Quellen** in [SOURCES.md](../SOURCES.md), davon 19 offizielle (Rockstar, PlayStation/Sony, OpenAI, Apple), rund 75 Fachmedien und Fachseiten (u. a. VGC, IGN, Push Square, Eurogamer, Digital Foundry über Zweitquellen, GameStar/Red Bull DE, Beebom, GTABase) sowie 15 Community- und Guide-Seiten. Jede Quelle hat URL, Abrufdatum und eine Angabe, ob sie erreichbar war.

## 4. Bestätigte Erkenntnisse (✅, Auswahl)

- Release am 19.11.2026 für PS5 und Xbox Series X|S. Nur PS5, keine PS4-Version. Einzelspieler, kein Online-Modus angekündigt. USK 18.
- Bis zu 212 GB Speicherbedarf. Auch die Box enthält nur einen Download-Code.
- Sprachausgabe nur Englisch, Texte und Untertitel auf Deutsch.
- 30 FPS auf allen Konsolen, kein Performance-Modus. Die PS5 Pro bietet bessere Bildqualität (PSSR, raytracing-Schatten).
- DualSense: Haptik, adaptive Trigger, Lautsprecher, Tempest 3D Audio.
- Drei Steuerungsschemata (Default, Classic, Left-Handed). Im Default-Schema rennt man mit L3. Touchpad = Karte, Options = Pause-Menü.
- 8 Einstellungsreiter. Zielhilfe: Lock-On, Partial oder Free Aim. Accessible Combat und Reduced Vehicle Damage sind wählbar.
- Hauptfiguren Lucia und Jason. Den Figurenwechsel schaltet die Story frei.
- Leonida mit Vice City und sechs Regionen.
- Fahndung bis 6 Sterne. Die Polizei reagiert erst auf Meldungen und merkt sich Kleidung, Aussehen und Fahrzeug.
- Dauerhaftes „Criminal Profile“. Focus-Zeitlupe. Präziseres Zielen als in GTA V.
- Bargeld und Bankkonto getrennt, nur die Bank ist sicher. Fahrzeuge brauchen Sprit. Autodiebstahl über Minispiel, manche Autos mit Tracker.
- 5 Kapitel. 90 Missionsnamen ✅ in mindestens zwei unabhängigen Quellen (nur im Spoiler-Bereich).
- ChatGPT: „Advanced“ und „Standard Voice“ werden am 11.12.2026 abgeschaltet (OpenAI, wörtlich geprüft).

## 5. Offene Wissenslücken

- Keine **offizielle Tastenliste** und keine **offiziellen Patchnotes** von Rockstar.
- **Deutsche Menü- und Missionsnamen** im Spiel nicht erfasst.
- **Fahndungsstufen 2–5** im Einzelnen, **Preise**, **Fahrzeug- und Waffenlisten**, **Immobilien und Geschäfte**.
- **Kartengröße** offiziell, weitere **Schnellreise** neben RydeMe.
- Gyro-Steuerung, Ego-Perspektive, Schwierigkeitsgrad, Button-Remapping, Grenzen von Auto Drive.
- Exakte Freischaltung des **Figurenwechsels** und seine Taste.
- Handlung (S2) nur aus wenigen Quellen (höchstens 🟡).
- Voice-Coach: Verhalten von ChatGPT-Voice nach dem 11.12.2026. Stummschalten per AirPods-Stiel.

## 6. Nicht überprüfbare Informationen

- **Nicht erreichbar:** Rockstar-Figurenseiten und vermutete Ortsseite (404), Rockstar-Support-Artikel zu Einstellungen und Vorbestellung (503), Forbes (403), TweakTown (403), Dot Esports (403), KeenGamer (500), Gameboost (403). Von der Rockstar-Newswire war jeweils nur der Titel lesbar, von mehreren GamesRadar- und PC-Gamer-Artikeln nur die Überschrift.
- **Nur über Suchauszüge bekannt** (höchstens 🟡/❓): u. a. IBTimes, Gfinity, allthings.how, TechSpot, mehrere Voice-Coach-Quellen.
- **Herkunft unklar:** Die Fehlerliste zu Patch 01.002.002.
- **Plattform-Annahme:** Die vollständigste Einstellungsliste stammt aus der Xbox-Version.
- Insgesamt 37 Quellen sind als „nicht“ oder „nur teilweise“ geprüft gekennzeichnet. Aus ihnen wurde nichts als ✅ übernommen, sofern es keine zweite Quelle gab.

## 7. Erstellte Dateien

| Bereich | Dateien |
|---|---|
| Projekt | `README.md`, `CLAUDE.md`, `AGENTS.md`, `INDEX.md`, `SOURCES.md`, `CHANGELOG.md`, `ROADMAP.md`, `GESAMTANLEITUNG.md` |
| Wissen (S0) | `wissen/01-…` bis `wissen/17-…` (17 Dateien) |
| Spoiler | `spoiler/README.md`, `spoiler/missionen/kapitel-01…05.md`, `spoiler/story/kapitel-01…05.md` |
| Daten | `daten/missionen.json`, `daten/einstellungen.json`, `daten/orte.json`, `daten/fahndungsstufen.json` |
| Berater (18) | `berater/voice-coach-anleitung.md`, `system-prompt.md`, `spielerprofil-vorlage.md`, `gedaechtnis.md`, `antwortbeispiele.md`, `export/coach-paket-spoilerfrei.md` |
| Quellen | `quellen/README.md`, `quellen/notizen/quellen-agent-a.md`, `-b.md`, `-c.md`, `quellen-projektleitung.md`, Ordner `pdf/`, `screenshots/` |
| Qualität | `qualitaet/checkliste.md`, `pruefbericht.md`, `qc-ergebnis.md`, `abschlussbericht.md` |
| Eigene Inhalte | `eigene-inhalte/README.md`, Ordner `spielbeobachtungen/`, `nutzerfragen/` |
| Vorlagen | `vorlagen/wissensbereich-vorlage.md`, `spielbeobachtung-vorlage.md`, `nutzerfrage-vorlage.md` |
| Werkzeuge | `tools/qc_check.py`, `tools/build_sources.py`, `tools/build_coach_paket.py`, `tools/setup.sh` |

## 8. Empfehlungen zur weiteren Pflege

1. **Selbst im Spiel nachsehen:** Die Menüs zu fotografieren ist die schnellste Art, viele 🟡 in ✅ zu verwandeln (Präfix `U`). Siehe [ROADMAP.md](../ROADMAP.md).
2. **Nach jedem Patch:** Bereiche 16 und 17 prüfen, Coach-Paket neu bauen (`python3 tools/build_coach_paket.py`).
3. **Am 11.12.2026:** Den Voice-Coach nach der ChatGPT-Voice-Umstellung testen und die Anleitung anpassen.
4. **Alle 2–4 Wochen:** Nicht erreichbare Quellen erneut abrufen und Wissenslücken in der ROADMAP abarbeiten.
5. **Immer:** `python3 tools/qc_check.py` vor jedem Pull Request ausführen. Änderungen ins CHANGELOG eintragen. Spoiler nur in `spoiler/`.
6. **Optional:** Die QC als kostenlose GitHub Action automatisieren.
