# 12. Karte, Navigation und Schnellreisen

> **Spoilerstufe:** S0 (spoilerfrei) · **Stand:** 2026-11-26 · **Spielversion:** PS5 Release-Version (19.11.2026), Patchstand unbekannt
> **Statuslegende:** ✅ Bestätigt · 🟡 Plausibel · ❓ Unbestätigt · ❌ Widerlegt – Details in [AGENTS.md](../AGENTS.md)

## Kurzfassung für den Voice-Coach

- Das Spiel spielt im fiktiven US-Bundesstaat **Leonida** (an Florida angelehnt) mit der Großstadt **Vice City**. ✅ [B-001, B-005]
- Sechs große Regionen: Vice City, Leonida Keys, Grassrivers, Port Gellhorn, Ambrosia und Mount-Kalaga-Nationalpark. ✅ [B-006, B-007]
- Die Karte ist anfangs **verdeckt** („Nebel“) und deckt sich durch Erkunden auf – auch aus der Luft. 🟡 [B-011, B-027]
- Schnellreisen gibt es über die Mitfahr-App **RydeMe** auf dem Handy; die Fahrt kann man gegen Aufpreis überspringen. 🟡 [B-016]
- Polizei und Gegner sind **nicht** als Punkte auf der Minikarte – Augen offen halten. 🟡 [B-015, B-028]

## Details

### Leonida und Regionen

| Region | Kurzbeschreibung | Status | Quelle |
|---|---|---|---|
| Leonida | Fiktiver Bundesstaat, „Vice City, USA“, „die dunkelste Seite des sonnigsten Ortes Amerikas“. | ✅ | B-001, B-004, B-005 |
| Vice City | Großstadt (Miami-Vorbild); laut Rockstar-Text Glamour, Hektik und Gier Amerikas in einer Stadt. | ✅ | B-006, B-007 |
| Leonida Keys | Tropische Inselkette (Florida-Keys-Vorbild), Bars, Boote; laut Rockstar „gefährliche Gewässer“. | ✅ | B-006, B-007 |
| Grassrivers | Sumpf-/Feuchtgebiet (Everglades-Vorbild) mit Alligatoren. | ✅ | B-006, B-007 |
| Port Gellhorn | Ehemaliger Urlaubsort an der „vergessenen Küste“, heruntergekommen. | ✅ | B-006, B-007 |
| Ambrosia | „Herz von Leonida“: Fabriken, „Old School“-Werte, Biker-Gang. | ✅ | B-006, B-007 |
| Mount Kalaga National Park | Naturgebiet mit Jagd, Angeln, Offroad-Strecken. | ✅ | B-006, B-007, B-005 |

Weitere offizielle Ortsnamen (PlayStation-Seite, ohne Beschreibung): Gambit Bay (Angelgebiet), Washington Beach, Watson Bay (Paradise Garage, Ultimate Edition), Lake Leonida, Stockyard. ✅ Namen [B-004, B-005] – Lage und Art ❓.

Strukturierte Liste: [`daten/orte.json`](../daten/orte.json)

- 🟡 Leonida umfasst laut Tests Großstadt, Land, Nationalparks, Kleinstädte, Industriegebiete und Unterwasserbereiche; Küste für Boote/Tauchen. [B-008, B-011]
- 🟡 Vice City ist früh im Spiel sichtbar. [B-008]
- ❓ Kartengröße: Angaben schwanken („ca. 3× Red Dead Redemption 2“ laut Vorab-Berichten; „doppelt so groß wie GTA V“ laut Suchauszug). [B-013, B-039] – keine offizielle Zahl geprüft.

### Kartenfunktionen

- 🟡 Die Weltkarte startet mit verdeckten Bereichen („Fog of War“), die durch Erkunden – auch per Flugzeug – aufgedeckt werden. [B-011, B-027]
- 🟡 Die Kartenanzeige zeigt Gebäude in 3D (inkl. Ein-/Ausgängen). [B-012, B-028]
- 🟡 Minikarte im Stil einer Handy-Navi-App; Anzeige wählbar: immer, nur bei aktivem Wegpunkt, als Kompass oder aus. Wegpunkte auch ohne Öffnen der großen Karte setzbar. [B-028] (Vorab-Stand)
- 🟡 Keine Gegner-/Polizeisymbole auf der Minikarte; stattdessen blinkende Bereiche. [B-015, B-028]
- ❓ PS5: Karte über das **Touchpad** öffnen (oder Options → Karte); X = Ziel setzen. Nur Suchauszüge, nicht geprüft. [B-038] → mit [Steuerung](01-steuerung-dualsense.md) abgleichen.

### Navigation / GPS

- 🟡 Bei gesetztem Ziel zeigt die Minikarte eine Route. [B-028]
- 🟡 Während einer Fahndung kann die Route fehlen, bis die Polizei abgehängt ist. [B-011]
- Automatisches Fahren zum Ziel: siehe [Kinomodus & Autofahrt](13-kinomodus-autofahrt.md).

### Schnellreisen

| Option | Aussage | Status | Quelle |
|---|---|---|---|
| RydeMe (Mitfahr-App) | Laut VGC die einzige „klassische“ Schnellreise. Handy (Steuerkreuz oben) → RydeMe → Ziel: Safehouse, Kartenmarkierung oder neues Ziel. | 🟡 | B-016 |
| Voraussetzung | RydeMe braucht ein Bankkonto, das man früh in der Story erhält. | 🟡 | B-016 |
| Überspringen | Fahrt live mitfahren, gegen Aufpreis beschleunigen oder für +100 $ ganz überspringen. | 🟡 | B-016 |
| Taxi | Ein Taxidienst („Paradise Taxi“) soll schon vorher nutzbar sein. | ❓ | B-017 (nicht erreichbar), B-038 (Suchauszug) |
| Busse/Züge | Busse und Züge fahren nach Fahrplan. | 🟡 | B-009 |

## Aus GTA V bekannt – für GTA VI NICHT bestätigt

- ❓ Taxi rufen und Fahrt per Taste überspringen (GTA V) – in GTA VI ähnlich über RydeMe, Details siehe oben.
- ❓ Komplett aufgedeckte Karte ab Spielbeginn (GTA V) – in GTA VI laut Berichten **nicht** so.

## Widersprüche

- ⚠️ Widerspruch: **Einzige Schnellreise?** – VGC: RydeMe sei die einzige klassische Schnellreise [B-016]; Suchauszüge nennen zusätzlich ein Taxi („Paradise Taxi“) [B-017, B-038]. Nicht geprüft.
- ⚠️ Widerspruch: **Kartengröße** – „3× RDR2“ [B-013, B-039] vs. „doppelt GTA V“ (Suchauszug, Quelle nicht geöffnet).

## Offene Fragen / Wissenslücken

- Offizielle Kartengröße und offizielle Übersichtskarte (ob Rockstar eine druckbare Karte veröffentlicht hat: widersprüchliche Suchauszüge, nicht geprüft).
- Fahrpreise von RydeMe/Taxi.
- Vollständige Kartenlegende und Symbole.
- Offizielle Rockstar-Ortsseiten nicht direkt erreichbar (B-003 = 404); Regionstexte nur über Fachmedien.

## Verwandte Bereiche

- [Steuerung DualSense](01-steuerung-dualsense.md)
- [Spielmechaniken](05-spielmechaniken.md)
- [Fahrzeuge & Tuning](06-fahrzeuge-tuning.md)
- [Polizei & Fahndung](11-polizei-fahndung.md)
- [Kinomodus & Autofahrt](13-kinomodus-autofahrt.md)
- [Tipps & Tricks](14-tipps-tricks.md)
