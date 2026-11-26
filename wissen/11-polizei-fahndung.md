# 11. Polizei und Fahndungssystem

> **Spoilerstufe:** S0 (spoilerfrei) · **Stand:** 2026-11-26 · **Spielversion:** PS5 Release-Version (19.11.2026), Patchstand unbekannt
> **Statuslegende:** ✅ Bestätigt · 🟡 Plausibel · ❓ Unbestätigt · ❌ Widerlegt – Details in [AGENTS.md](../AGENTS.md)

## Kurzfassung für den Voice-Coach

- Die Fahndung geht bis **sechs Sterne** (GTA V: fünf). ✅ [B-012, B-013, B-014]
- Die Polizei kommt nur, wenn ein Verbrechen **gemeldet** wird – durch Zeugen, Alarm oder Kameras. ✅ [B-009, B-014]
- Die Polizei merkt sich, **wie du aussiehst und was du fährst**. Kleidung wechseln und Auto tauschen hilft beim Entkommen. ✅ [B-009, B-011, B-013, B-014]
- Die Sterne zeigen den Zustand: hohl = Polizei kennt dich nicht, blinkend = Sichtkontakt verloren. 🟡 [B-014, B-015]
- Polizisten erscheinen **nicht** als Punkte auf der Minikarte – selbst umschauen. 🟡 [B-015, B-028]
- Bei Tod oder Verhaftung verlierst du dein Bargeld – also vorher einzahlen. 🟡 [B-015, B-024]

## Details

### Fahndungsstufen und Sternanzeige

| Thema | Aussage | Status | Quelle |
|---|---|---|---|
| Anzahl | Bis zu 6 Sterne. | ✅ | B-012, B-013, B-014 |
| Steigerung | Wenige Sterne = wenige Streifen; 6 Sterne = militarisierte Reaktion, Verfolgung über die ganze Karte. | 🟡 | B-014 |
| Weiß, gefüllt | Polizei hat direkten Sichtkontakt. | 🟡 | B-014 (ähnlich B-015) |
| Weiß, blinkend | Sichtkontakt verloren, Polizei sucht. | 🟡 | B-014, B-015 |
| Hohl | Polizei sucht, hat aber keine Beschreibung von dir. | 🟡 | B-014, B-015 |
| Rot | Nähe eines Tatorts, Polizei weiß nicht, wo du bist (Engadget) bzw. „Heat“-Bereich (GTABase). | 🟡 | B-014, B-015 |
| Zustände | „Cops Responding“ (gemeldet, unterwegs), „Suspect Unknown“, „In Pursuit“, „Visual Lost“, „Heat“. | 🟡 | B-015 |

Eine Liste je Stufe 1–6 mit belegtem Inhalt gibt es nicht; siehe [`daten/fahndungsstufen.json`](../daten/fahndungsstufen.json) (nur belegte Eckpunkte).

### Zeugen, Meldungen, Kameras

- ✅ Verbrechen müssen gemeldet werden, damit die Fahndung steigt; Rockstar (Rob Nelson, Rockstar North): Der Funk weiß sehr genau Bescheid. [B-014]
- ✅ Zeugen, Überwachungskameras und Schüsse verstärken die Verfolgung; Sicherheits-/Verkehrskameras können dein Gesicht erfassen. [B-009, B-010]
- ✅ Polizei gibt Beschreibungen per Funk weiter. [B-009, B-011]
- 🟡 Tracker in gestohlenen Autos alarmieren die Polizei. [B-009, B-021]
- 🟡 Kleinere Unfälle können wütende Passanten auf den Plan rufen. [B-010]

### „Heat“ – was die Polizei über dich weiß

- ✅ Symbole zeigen, was die Polizei über dich weiß; dieses Wissen kann bestehen bleiben, auch wenn die Sterne weg sind. [B-014]
- 🟡 Symbol-Arten laut Guide: Aussehen, Outfit, Fahrzeug, sichtbare Waffe, Partner, Videoüberwachung (CCTV; „Cloud-CCTV“ nicht zerstörbar). [B-015]
- 🟡 Gegenmittel: Kleidung wechseln (Outfits im Kofferraum), Maske/Accessoires/Frisur, Auto umlackieren oder tauschen, Waffe wegstecken, Jason und Lucia trennen, Kamera vor Ort zerstören. [B-011, B-013, B-015]
- 🟡 Blutflecken machen erkennbar; Duschen im Safehouse entfernt sie. [B-015]

### Entkommen

- ✅ Sichtlinie brechen, Auto und Kleidung wechseln. [B-009, B-011, B-013]
- 🟡 Verstecken (Büsche, Wald, ducken in einem stehenden Auto, im Kofferraum). [B-013, B-015]
- 🟡 Auf Reifen schießen ist wirksam; Polizisten töten verschärft die Reaktion. [B-013, B-015]
- 🟡 Hubschrauber und Hundestaffeln (K9) sind im Einsatz. [B-011, B-015]
- 🟡 Selbst 5 Sterne lassen sich abschütteln (z. B. Verstecken in einem Bahngelände). [B-008]
- 🟡 Focus-Modus hilft, Polizisten zu orten. [B-015]
- 🟡 Während einer Fahndung zeigt das GPS teils keine Route, bis du die Polizei los bist. [B-011]

### Folgen von Verhaftung („Busted“) und Tod („Wasted“)

- 🟡 Bargeld in der Tasche weg, nicht eigene Waffen weg, Beutetaschen wahrscheinlich weg. [B-015, B-024]
- 🟡 Bei Verhaftung zusätzlich kleine BuckMe-Gebühr; das gefahrene Auto wird beschlagnahmt. [B-024]
- 🟡 Eigene Waffen sind im Kofferraum des persönlichen Autos oder im Ammu-Nation-Waffenspind zurückholbar. [B-015, B-024]
- 🟡 Wiedereinstieg an einem nahe gelegenen sicheren Ort. [B-024]
- 🟡 Losreißen, bevor die Handschellen klicken, ist möglich – erhöht aber die Fahndung. [B-024]

### Criminal Profile und Polizei

- 🟡 Dein Criminal Profile beeinflusst, wie aggressiv die Polizei dich verfolgt. [B-009] → siehe [Spielmechaniken](05-spielmechaniken.md)

## Aus GTA V bekannt – für GTA VI NICHT bestätigt

- ❓ Sichtkegel der Polizei auf der Minikarte (GTA V) – in GTA VI laut Berichten **keine** Polizeisymbole auf der Minikarte [B-015, B-028] (🟡).
- ❓ Krankenhaus-/Anwaltskosten in fester Höhe (GTA V) – für GTA VI nicht belegt.
- ❓ Pay 'n' Spray löscht die Fahndung sofort (GTA V) – in GTA VI nur als Mittel gegen das Fahrzeug-Merkmal beschrieben [B-015]; sofortiges Löschen nicht belegt.

## Widersprüche

- ⚠️ Widerspruch: **Rote Sterne** – Engadget: Nähe eines Tatorts, Polizei kennt Standort nicht [B-014]; GTABase: „Heat“-Bereich um letzten bekannten Ort nach dem Abhängen [B-015]. Ähnliche Bedeutung, unterschiedlich beschrieben.
- ⚠️ Widerspruch: **Waffen nach Verhaftung** – laut einem Suchauszug alles konfisziert, laut [B-024]/[B-015] nur nicht eigene Waffen.
- ⚠️ Widerspruch: **Gebühr bei Tod** – [B-015] ja, [B-024] nur bei Verhaftung.

## Offene Fragen / Wissenslücken

- Welche Taten genau welche Sternstufe auslösen (nicht offiziell dokumentiert).
- Offizielle Rockstar-Beschreibung der Sternfarben (nur Fachmedien/Fanseite).
- GamesRadar-Artikel [B-029, B-030] nicht auslesbar – nicht geprüft.
- Ob „Heat“-Gebiete zeitlich ablaufen und wie lange.

## Verwandte Bereiche

- [Spielmechaniken](05-spielmechaniken.md)
- [Fahrzeuge & Tuning](06-fahrzeuge-tuning.md)
- [Geld & Wirtschaft](07-geld-wirtschaft.md)
- [Waffen & Kampf](10-waffen-kampf.md)
- [Karte & Navigation](12-karte-navigation.md)
- [Tipps & Tricks](14-tipps-tricks.md)
