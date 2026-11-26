# Prüfbericht – Abschließende Qualitätskontrolle

> **Datum:** 2026-11-26 · **Prüfer:** Projektleitung (Claude) · **Gegenstand:** Version 0.1.0 (Erstaufbau)
> Automatisches Ergebnis: [qc-ergebnis.md](qc-ergebnis.md) · Checkliste: [checkliste.md](checkliste.md)

## Ergebnis auf einen Blick

| Prüfpunkt | Methode | Ergebnis |
|---|---|---|
| Struktur / Pflichtdateien | `tools/qc_check.py` | ✅ alle vorhanden |
| Interne Links | `tools/qc_check.py` (alle relativen Links in 54 Markdown-Dateien) | ✅ 0 tote Links |
| JSON-Daten | `tools/qc_check.py` (4 Dateien, 297 Einträge) | ✅ gültig, alle Quellen-IDs aufgelöst |
| Quellen | Alle zitierten IDs in SOURCES.md definiert | ✅ 104 zitierte IDs, alle definiert · ⚠️ 12 Quellen recherchiert, aber nicht zitiert (unkritisch) |
| Quellenangaben | URL + Abrufdatum + Erreichbarkeit je Quelle | ✅ 116 Quellen vollständig erfasst, 37 davon nicht oder nur teilweise lesbar und als solche markiert |
| Statuskennzeichnung | Zählung der Marker | ✅ alle Wissensdateien enthalten Statusmarker. Überwiegend 🟡, weil das Spiel neu ist |
| Spoilerschutz automatisch | Missionstitel aus `missionen.json` in S0-Dateien gesucht | ✅ keine Treffer (ein Fehlalarm behoben) |
| Spoilerschutz manuell | Suche nach Handlungswörtern in `wissen/`, `GESAMTANLEITUNG.md`, `berater/` | ✅ keine Handlungsdetails. `09` enthält nur offizielles Marketing |
| Spoilerwarnungen | Kopf aller Dateien in `spoiler/` | ✅ vorhanden. 4 handlungsverratende Missionstitel sind eingeklappt und im JSON als S2 markiert |
| Widersprüche | Abgleich zwischen den Agenten | ✅ in den Dateien markiert, siehe unten |
| Faktencheck (Stichprobe) | Gegenprüfung durch Projektleitung mit unabhängigen Quellen | ✅ 2 von 2 bestätigt (30 FPS / kein Performance-Modus; Rennen L3 + Classic-Schema) |
| GTA-V-Übertragungen | Eigener Abschnitt „Aus GTA V bekannt – NICHT bestätigt“ in jeder Wissensdatei | ✅ |
| Urheberrecht | Stichproben: eigene Formulierungen, keine Komplettübernahmen | ✅ Missionslisten bestehen nur aus Titeln plus eigenem Ein-Satz-Ziel |

## Widersprüche zwischen Quellen bzw. Agenten (Auswahl)

| Thema | Positionen | Behandlung |
|---|---|---|
| Taste Figurenwechsel | Steuerkreuz rechts drücken (VGC) · Steuerkreuz rechts halten + R1 (Gfinity, Player.One) · Steuerkreuz rechts halten = Kriminalprofil (GTA BOOM) | in 01, 05, 14, 15 markiert, Nutzerprüfung in ROADMAP |
| Springen | Kreuz (2 geprüfte Quellen) vs. Quadrat (SEO-Seiten) | in 01 markiert |
| Speicherplätze | 14 manuelle + Autosave (VGC) vs. 15 manuelle + Autosave | in 05, 14, 15 und Gesamtanleitung markiert |
| Day-One-Patch | 1.002.001 als „Day-One“ bezeichnet vs. Vorab-Update am 16.11. | in 16 richtiggestellt |
| Vorab-Download | 10.11. (offiziell) vs. 12.11. (Medien) | offizielle Angabe hat Vorrang |
| Missionsanzahl | 91 / 92 / 109 / 118 je nach Zählweise | in Spoiler-README erklärt |
| Standardwerte | Deadzone 4/5, Motion-Blur-Bereich, Zerstückelung an/aus | in 02 markiert |
| Kartengröße | ca. 3× RDR2 vs. 2× GTA V | in 12 markiert, keine offizielle Angabe |
| Folgen von Tod/Verhaftung | Gebühren und Waffenverlust unterschiedlich beschrieben | in 11 markiert |

## Bekannte Schwächen

- 🟡 überwiegt: Bei einem eine Woche alten Spiel gibt es kaum offizielle Detaildokumentation. Das ist ehrlich gekennzeichnet, aber keine Schwäche der Arbeit.
- Die vollständigste Einstellungsliste (A-010) stammt aus der Xbox-Version. Für PS5 wird Gleichheit angenommen (🟡).
- Menünamen meist englisch. Die deutschen Bezeichnungen im Spiel sind noch nicht erfasst.
- Die Kurzfassungen in `09`, `14`, `15` und `08` haben keine Statusmarker in jeder Zeile. Status und Quelle stehen in den Detailtabellen derselben Datei.
