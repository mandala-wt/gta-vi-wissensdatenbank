# Spoiler-Bereich – GTA VI

> ⚠️ **SPOILERWARNUNG.** Alles unterhalb dieses Ordners verrät Missionsnamen (S1) oder Handlung (S2).
> Spoilerfreie Hilfe findest du in [`wissen/`](../wissen/08-missionen-uebersicht.md).

> **Stand:** 2026-11-26 · **Spielversion:** Launch-Version (Release 19.11.2026, PS5) · Statuslegende und Regeln: [AGENTS.md](../AGENTS.md)

## So funktioniert das Spoilersystem

| Stufe | Inhalt | Ort | Für den Voice-Coach |
|---|---|---|---|
| **S0** | Spoilerfrei: Steuerung, Systeme, allgemeine Tipps, Figuren und Setting nur aus offiziellem Vor-Release-Marketing | [`wissen/`](../wissen/) | Immer nutzbar |
| **S1** | Leichte Spoiler: Missionsnamen, Reihenfolge, Kapitelstruktur, Freischaltungen | [`spoiler/missionen/`](missionen/) | Nur auf ausdrückliche Nachfrage („Wie heißt die nächste Mission?“) und nur bis zum aktuellen Kapitel des Spielers |
| **S2** | Story-Spoiler: Handlung, Wendungen, Schicksale von Figuren | [`spoiler/story/`](story/) | Nur, wenn der Spieler ausdrücklich Handlung erfahren will, und nie über sein aktuelles Kapitel hinaus |

Regeln:

- Jede Datei beginnt mit einer Spoilerwarnung und nennt ihre Stufe.
- Kapiteldateien sind **kumulativ**: Kapitel *n* setzt Wissen aus Kapitel 1 bis *n−1* voraus.
- Missionsnamen, deren Titel selbst die Handlung verrät, sind in den S1-Dateien **eingeklappt** und in [`daten/missionen.json`](../daten/missionen.json) mit `"spoilerstufe": "S2"` markiert.
- Der Berater fragt zuerst, in welchem Kapitel der Spieler ist (oder liest es aus [`eigene-inhalte/`](../eigene-inhalte/)), und verrät nichts darüber hinaus.

## Kapitelstruktur (S1)

- 🟡 Die Story besteht laut Guides aus **5 Kapiteln**. Dexerto, VGC und Red Bull zählen den Prolog zu Kapitel 1 [C-010] [C-012] [C-014], GTABase und Beebom führen ihn als eigenen Abschnitt [C-008] [C-011]. Hier zählt er zu Kapitel 1.
- 🟡 Eine offizielle Missionsliste von Rockstar gibt es nicht. Die Listen stammen aus Guide-Seiten und Fachmedien und unterscheiden sich in der Zählweise (91 bis 118 Einträge, siehe [08-missionen-uebersicht](../wissen/08-missionen-uebersicht.md#widerspr%C3%BCche)).

## Index

| Kapitel | Englischer Name (✅) | Kern-Missionen (91er-Liste) | Missionen (S1) | Handlung (S2) |
|---|---|---|---|---|
| 1 | Just Like Paradise | 22 (inkl. Prolog) | [missionen/kapitel-01.md](missionen/kapitel-01.md) | [story/kapitel-01.md](story/kapitel-01.md) |
| 2 | Paradise Lost | 11 | [missionen/kapitel-02.md](missionen/kapitel-02.md) | [story/kapitel-02.md](story/kapitel-02.md) |
| 3 | Tits Ass Drug Money | 26 | [missionen/kapitel-03.md](missionen/kapitel-03.md) | [story/kapitel-03.md](story/kapitel-03.md) |
| 4 | Vice City, Baby | 25 | [missionen/kapitel-04.md](missionen/kapitel-04.md) | [story/kapitel-04.md](story/kapitel-04.md) |
| 5 | Top of the World, Ma | 7 | [missionen/kapitel-05.md](missionen/kapitel-05.md) | [story/kapitel-05.md](story/kapitel-05.md) |

Quellen der Kapitelnamen: [C-010] [C-008] [C-011] [C-014] (in allen vier übereinstimmend). Quellenliste: [`quellen/notizen/quellen-agent-c.md`](../quellen/notizen/quellen-agent-c.md).

## Maschinenlesbare Daten

[`daten/missionen.json`](../daten/missionen.json) enthält 148 Einträge: 91 Kern-Missionen plus Zusatzeinträge aus GTABase, Beebom und VGC. Bei den Zusatzeinträgen ist `reihenfolge` nur eine Sortiernummer *nach* den Kern-Missionen des Kapitels und keine belegte Spielreihenfolge. Felder: `id`, `kapitel`, `reihenfolge`, `titel_en`, `titel_de` (laut Red Bull DE, 🟡), `typ`, `spielfigur` (laut GTABase, 🟡), `spoilerstufe`, `status`, `quellen`.

## Verwandte Bereiche

- [Missionen finden – spoilerfrei](../wissen/08-missionen-uebersicht.md)
- [Figuren – spoilerfrei](../wissen/09-story-charaktere.md)
- [Tipps & Tricks](../wissen/14-tipps-tricks.md)
- [FAQ](../wissen/15-faq.md)
