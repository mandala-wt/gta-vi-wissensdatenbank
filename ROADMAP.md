# ROADMAP – Weitere Aufgaben

Priorität: 🔴 hoch · 🟠 mittel · 🟢 niedrig

## Sofort durch den Nutzer (beim Spielen, je 1–5 Minuten)

- 🔴 **Einstellungsmenü abfotografieren** (alle 8 Reiter, PS5-Share-Taste → Screenshot) und nach `quellen/screenshots/` legen. Damit lassen sich Menünamen auf Deutsch und Standardwerte sicher bestätigen.
- 🔴 **Steuerung prüfen:** Options → Settings → Control Scheme. Klären: Springen (Kreuz oder Quadrat?), Figurenwechsel (Steuerkreuz rechts drücken oder halten + R1?), Kriminalprofil.
- 🟠 Spielversion notieren: PS5-Startbildschirm → Spiel markieren → Options → Informationen.
- 🟠 Anzahl Speicherplätze zählen (14 oder 15 manuelle?).

## Recherche

- 🔴 Offizielle Rockstar-Patchnotes beobachten (Newswire, support.rockstargames.com) → `wissen/16-updates-aenderungen.md`.
- 🔴 Deutsche Menü- und Missionsnamen im Spiel erfassen (bisher meist Englisch bzw. nur aus einer deutschen Quelle).
- 🟠 Fahndungsstufen 2–5 einzeln belegen → `daten/fahndungsstufen.json`.
- 🟠 Fahrzeug- und Waffenlisten mit Preisen (erst wenn mehrere seriöse Quellen vorliegen).
- 🟠 Immobilien, Garagen und Geschäfte kaufen: ja oder nein?
- 🟠 Schnellreise jenseits von RydeMe (Taxi?) klären.
- 🟢 Gyro-Steuerung, Ego-Perspektive, Button-Remapping, Schwierigkeitsgrad.
- 🟢 Online-Modus: Ankündigungen beobachten.
- 🟢 Nicht erreichbare Quellen später erneut abrufen (Rockstar-Figurenseiten, Rockstar-Support-Artikel zu Einstellungen, Forbes, TweakTown, KeenGamer, Dot Esports).

## Voice-Coach

- 🔴 ChatGPT-Voice nach der Umstellung am **11.12.2026** prüfen (Advanced/Standard Voice werden abgeschaltet): Funktionieren Projekte, Dateien, Hintergrund-Gespräch und Memory weiterhin? → `berater/voice-coach-anleitung.md` aktualisieren.
- 🟠 Ausprobieren und dokumentieren: AirPods-Stiel zum Stummschalten, Siri- oder Action-Button-Kurzbefehl zum Starten.
- 🟠 Nach 2–3 Spielsitzungen: häufigste Fragen in `wissen/15-faq.md` übernehmen.
- 🟢 Alternative mit Claude-Projekt testen und vergleichen.

## Technik/Pflege

- 🟠 Bei jedem Patch: `16-updates-aenderungen.md`, `17-bekannte-fehler.md` und betroffene Bereiche prüfen, Coach-Paket neu bauen.
- 🟢 Optional: GitHub Action, die `tools/qc_check.py` bei jedem Pull Request ausführt (kostenlos, ohne externe Dienste).
