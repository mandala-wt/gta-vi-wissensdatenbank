# GTA VI – PS5 Wissensdatenbank 🎮

Deutschsprachige, quellenbasierte Wissensdatenbank zu **Grand Theft Auto VI auf der PlayStation 5**. Sie ist für **Konsolen-Anfänger** gedacht und dient als Grundlage für einen **persönlichen KI-Voice-Coach** (iPhone + AirPods).

> **Stand:** 2026-11-26 · **Spiel erschienen:** 19.11.2026 (PS5, Xbox Series X|S) · Das Spiel ist neu, viele Details sind noch nicht gesichert. Jede Aussage trägt deshalb einen Status.

## Schnellstart

| Ich will … | Dann lies … |
|---|---|
| **den Voice-Coach einrichten** | [berater/voice-coach-anleitung.md](berater/voice-coach-anleitung.md) |
| das Wichtigste auf einen Blick | [GESAMTANLEITUNG.md](GESAMTANLEITUNG.md) |
| ein bestimmtes Thema | [INDEX.md](INDEX.md) (alle 18 Wissensbereiche) |
| Hilfe zu einer Mission (Spoiler!) | [spoiler/README.md](spoiler/README.md) |
| wissen, woher eine Aussage stammt | [SOURCES.md](SOURCES.md) |

## Statuslegende

| | Bedeutung |
|---|---|
| ✅ | **Bestätigt**: offizielle Quelle oder mehrere seriöse Fachmedien |
| 🟡 | **Plausibel**: eine seriöse Quelle oder übereinstimmende Community-Berichte |
| ❓ | **Unbestätigt**: Gerücht, Einzelbericht oder aus GTA V übertragen |
| ❌ | **Widerlegt** |

## Spoilerschutz

- `wissen/`, `GESAMTANLEITUNG.md` und `berater/` sind **spoilerfrei** (S0).
- Missionsnamen (S1) und Handlung (S2) liegen nur in [`spoiler/`](spoiler/README.md), getrennt nach Kapiteln.
- Für den Coach lädst du nur die Spoilerdateien bis zu deinem aktuellen Kapitel hoch.

## Aufbau

```
README.md              ← du bist hier
GESAMTANLEITUNG.md     zentrale, zusammenhängende Anleitung (spoilerfrei)
INDEX.md               Verzeichnis aller Wissensbereiche
AGENTS.md / CLAUDE.md  Regeln für KI-Systeme
SOURCES.md             Quellenverzeichnis (automatisch erzeugt)
CHANGELOG.md / ROADMAP.md
wissen/                18 Wissensbereiche (S0)
spoiler/               Missionen (S1) und Story (S2) nach Kapitel
daten/                 strukturierte JSON-Daten
berater/               Voice-Coach: Anleitung, System-Prompt, Profil, Export
quellen/               Quellennotizen, eigene PDFs, Screenshots
eigene-inhalte/        deine Spielbeobachtungen und Fragen
qualitaet/             Checkliste, Prüfbericht, Abschlussbericht
vorlagen/              Vorlagen für neue Dateien
tools/                 Prüf- und Export-Skripte (Python, ohne Zusatzpakete)
```

## Pflege (für Fortgeschrittene oder Claude)

```bash
python3 tools/build_sources.py      # SOURCES.md aus quellen/notizen/ erzeugen
python3 tools/qc_check.py           # Qualitätsprüfung
python3 tools/build_coach_paket.py  # Upload-Datei für den Coach erzeugen (optional: --bis-kapitel 3)
```

## Hinweise

Inoffizielles Fan-Projekt ohne Verbindung zu Rockstar Games, Take-Two oder Sony. Marken gehören ihren Inhabern. Inhalte sind eigene Zusammenfassungen mit Quellenangabe.
