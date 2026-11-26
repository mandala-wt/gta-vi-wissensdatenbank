# Qualitäts-Checkliste (vor jedem Pull Request)

## Automatisch (`python3 tools/qc_check.py`)

- [ ] Pflichtdateien vorhanden
- [ ] Keine toten internen Links
- [ ] Alle JSON-Dateien gültig
- [ ] Alle zitierten Quellen-IDs in SOURCES.md definiert
- [ ] Wissensdateien mit Kopfblock (S0, Stand, Version)
- [ ] Spoilerdateien mit Warnung am Anfang
- [ ] Keine Missionstitel (außer der ersten Mission) in spoilerfreien Dateien

## Manuell

- [ ] Jede neue Aussage hat einen Status (✅/🟡/❓/❌)
- [ ] ✅ nur bei offizieller Quelle oder ≥ 2 unabhängigen Fachmedien
- [ ] Kein GTA-V-Wissen ohne ❓-Hinweis
- [ ] Widersprüche mit `⚠️ Widerspruch:` markiert
- [ ] Spielversion/Patchstand angegeben, wenn relevant
- [ ] Keine längeren wörtlichen Übernahmen aus fremden Guides
- [ ] GESAMTANLEITUNG.md stimmt mit Detaildateien überein
- [ ] Coach-Paket neu gebaut (`python3 tools/build_coach_paket.py`)
- [ ] CHANGELOG.md ergänzt
