# Wie sich der Coach Dinge merkt

Der Coach hat drei „Gedächtnisse“. Für Anfänger reicht es, alle drei zu kennen. Einrichten musst du nur zwei davon.

| Gedächtnis | Wo | Was gehört hinein | Wer pflegt es |
|---|---|---|---|
| **1. Feste Anweisungen** | Projekt-Anweisungen | Rolle, Antwortstil, Steckbrief | du (selten ändern) |
| **2. Memory der App** | automatisch, im Projekt | Fortschritt, Vorlieben, wiederkehrende Fragen | der Coach, wenn du „Merk dir …“ sagst |
| **3. Wissensdatenbank** | Projekt-Dateien / dieses Repo | geprüftes Spielwissen mit Quellen | Repo-Pflege (z. B. mit Claude) |

## Nützliche Sprachbefehle

- „Merk dir: Ich bin jetzt in Kapitel 2, letzte Mission war …“
- „Merk dir: Zielhilfe steht auf voll, das funktioniert gut.“
- „Was weißt du über meinen Spielstil?“
- „Vergiss, dass ich …“
- „Zusammenfassung“ → am Ende einer Sitzung, danach optional: „Merk dir die wichtigsten Punkte.“

## Erkenntnisse aus dem Spiel zurück ins Repo bringen

1. Am Ende einer Sitzung: „Gib mir die neuen Erkenntnisse dieser Sitzung als Stichpunkte.“
2. Die Stichpunkte als Datei in `eigene-inhalte/spielbeobachtungen/` ablegen, z. B. `2026-11-30.md`. Vorlage: [vorlagen/spielbeobachtung-vorlage.md](../vorlagen/spielbeobachtung-vorlage.md).
3. Bei der nächsten Pflege (z. B. mit Claude) werden sie geprüft und mit Status `U` (Nutzerbeobachtung) in die Wissensdatei übernommen.

> 🟡 Laut OpenAI kann der neue Sprachmodus (GPT-Live) Memory nutzen [V-001]. Wie zuverlässig er sich etwas im laufenden Voice-Gespräch merkt, ist nicht belegt. Wichtige Dinge deshalb zusätzlich in den Steckbrief schreiben.
