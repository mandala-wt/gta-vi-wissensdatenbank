# CLAUDE.md – Dauerhafte Projektanweisungen für Claude

Lies zuerst **[AGENTS.md](AGENTS.md)**. Die Regeln dort (Status, Quellen, Spoilerstufen, GTA V ≠ GTA VI) gelten vollständig. Hier stehen nur Ergänzungen für Claude (Claude Code, Claude-Projekte).

## Projekt in Kürze

- Deutschsprachige Wissensdatenbank zu **GTA VI (PS5)**, Release 19.11.2026. Zielgruppe: Konsolen-Anfänger.
- Endnutzung: Voice-Coach (ChatGPT-Projekt, alternativ Claude/Grok). Anleitung: [berater/voice-coach-anleitung.md](berater/voice-coach-anleitung.md).
- Reine Dokumentation: Markdown + JSON + kleine Python-Skripte (nur Standardbibliothek).

## Arbeitsablauf bei Änderungen

1. Arbeite auf einem Feature-Branch, nie direkt auf `main`.
2. Neue Quellen → in die passende Datei unter `quellen/notizen/` eintragen, dann `python3 tools/build_sources.py`.
3. Wissen ändern → passende Datei in `wissen/` (S0) oder `spoiler/` (S1/S2), Kopfblock-Datum aktualisieren.
4. `daten/*.json` synchron halten (z. B. `missionen.json` mit `spoiler/missionen/`).
5. `GESAMTANLEITUNG.md` anpassen, wenn sich Kernaussagen ändern.
6. `python3 tools/qc_check.py` muss ohne Fehler durchlaufen.
7. `python3 tools/build_coach_paket.py` ausführen, damit der Export aktuell ist.
8. Eintrag in `CHANGELOG.md`, offene Punkte in `ROADMAP.md`.
9. Pull Request zur Prüfung, nicht selbst mergen.

## Verbote

- Keine Webseite veröffentlichen, keine produktiven Dienste starten.
- Keine kostenpflichtigen API-Aufrufe ohne ausdrückliche Zustimmung des Nutzers.
- Keine Secrets ins Repo.
- Keine Inhalte aus `spoiler/` in `wissen/`, `GESAMTANLEITUNG.md` oder `berater/export/coach-paket-spoilerfrei.md`.
- Keine Komplettübernahme fremder Guides. Eigene Worte, Quelle angeben.

## Neue Nutzer-Inhalte verarbeiten

- PDFs → `quellen/pdf/`, Screenshots → `quellen/screenshots/`, Beobachtungen → `eigene-inhalte/spielbeobachtungen/`, Fragen → `eigene-inhalte/nutzerfragen/`.
- Beim Einarbeiten eine Quellen-ID mit Präfix `U` vergeben (z. B. `U-001`, Typ „Nutzerbeobachtung“). Eine einzelne Beobachtung gilt als 🟡. Bestätigt eine offizielle Quelle sie, wird sie ✅.
- Häufige Nutzerfragen → in `wissen/15-faq.md` aufnehmen.

## Ton

Deutsch, kurz, anfängerfreundlich, Tasten mit DualSense-Namen (Kreuz, Kreis, Quadrat, Dreieck, L1/L2/R1/R2/L3/R3, Touchpad, Options).
