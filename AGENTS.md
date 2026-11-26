# AGENTS.md – KI-übergreifende Projektanweisungen

Diese Datei gilt für **alle** KI-Systeme (Claude, ChatGPT/Codex, Grok, Gemini …), die an dieser Wissensdatenbank arbeiten oder sie als Wissensquelle nutzen.

## Zweck des Repos

Deutschsprachige, quellenbasierte Wissensdatenbank zu **Grand Theft Auto VI auf der PlayStation 5** für einen Konsolen-Anfänger. Sie dient als Grundlage für einen persönlichen KI-Spielberater (Voice-Coach).

## Grundregeln (verbindlich)

1. **Nichts erfinden.** Keine Missionen, Tastenbelegungen, Menüpunkte, Fahrzeuge, Preise oder Mechaniken ohne Quelle.
2. **GTA V ≠ GTA VI.** Wissen aus GTA V / GTA Online darf nur mit Status `Plausibel` oder `Unbestätigt` und dem Hinweis „aus GTA V übertragen, für GTA VI nicht bestätigt“ erscheinen.
3. **Jede Aussage hat einen Status** (siehe unten) und – außer bei `Unbestätigt` ohne Quelle – mindestens eine Quellen-ID.
4. **Quellen** stehen in [`SOURCES.md`](SOURCES.md) mit vollständiger URL und Abrufdatum. War eine Quelle nicht erreichbar, wird das so vermerkt – niemals so tun, als sei sie geprüft.
5. **Keine Übernahme fremder Anleitungen.** Eigene, knappe Formulierungen; höchstens kurze Zitate mit Quellenangabe.
6. **Spoilerschutz.** Story- und Missionsdetails gehören ausschließlich in [`spoiler/`](spoiler/README.md). Dateien unter `wissen/` sind spoilerfrei (Stufe S0).
7. **Widersprüche** zwischen Quellen werden mit `⚠️ Widerspruch:` markiert und beide Versionen samt Quelle genannt.
8. **Versionsstand** angeben: Spielversion/Patch, auf den sich eine Aussage bezieht, falls bekannt.

## Status-Kennzeichnung

| Kürzel | Bedeutung | Wann verwenden |
|---|---|---|
| ✅ **Bestätigt** | Offizielle Quelle (Rockstar, PlayStation) **oder** ≥ 2 unabhängige seriöse Fachmedien übereinstimmend | Für Antworten des Beraters ohne Einschränkung nutzbar |
| 🟡 **Plausibel** | Eine seriöse Quelle oder konsistente Community-Berichte, nicht offiziell bestätigt | Berater nennt es mit „vermutlich“ / „laut Berichten“ |
| ❓ **Unbestätigt** | Gerücht, Einzelbericht, aus GTA V übertragen, oder Quelle nicht erreichbar | Berater sagt ausdrücklich, dass es unsicher ist |
| ❌ **Widerlegt** | Durch offizielle oder bessere Quelle widerlegt | Nur zur Richtigstellung erwähnen |

Schreibweise im Text: `✅ Aussage … [A-003]` bzw. in Tabellen eine Status- und eine Quellenspalte.

## Spoilerstufen

| Stufe | Inhalt | Ort |
|---|---|---|
| **S0** | Spoilerfrei: Steuerung, Einstellungen, Systeme, allgemeine Tipps, Grundsetting aus Trailern/offiziellem Marketing | `wissen/` |
| **S1** | Leichte Spoiler: Missionsnamen, Kapitelstruktur, Freischaltungen nach Fortschritt | `spoiler/missionen/` |
| **S2** | Storyspoiler: Handlung, Wendungen, Schicksale von Figuren | `spoiler/story/` (nach Kapitel getrennt) |

## Quellen-IDs

- Format: `<Präfix>-<dreistellige Nummer>`, z. B. `A-001`.
- Präfixe: `A` = Steuerung/Einstellungen/Technik, `B` = Systeme/Welt/Wirtschaft, `C` = Story/Missionen/Tipps/FAQ, `V` = Voice-Coach/KI-Tools, `P` = Projektleitung/Nachprüfung, `U` = Nutzer-eigene Beobachtungen.
- Neue Quellen in `SOURCES.md` in der richtigen Gruppe anhängen, IDs niemals neu vergeben.

## Dateikonventionen

- Markdown, UTF-8, deutsche Sprache, Dateinamen in Kleinbuchstaben mit Bindestrichen, ohne Umlaute.
- Jede Wissensdatei beginnt mit dem Kopfblock aus [`vorlagen/wissensbereich-vorlage.md`](vorlagen/wissensbereich-vorlage.md).
- Strukturierte Daten als JSON in `daten/` (gültiges JSON, UTF-8).
- Interne Links immer relativ.
- Nach Änderungen: `python3 tools/qc_check.py` ausführen und Eintrag in `CHANGELOG.md` ergänzen.

## Für KI-Berater (Nutzung zur Laufzeit)

Wer diese Datenbank als Berater nutzt, folgt [`berater/system-prompt.md`](berater/system-prompt.md): kurz, deutsch, spoilerbewusst, Status-ehrlich.
