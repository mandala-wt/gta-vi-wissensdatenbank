# Voice-Coach für GTA VI auf der PS5 – Anleitung für Anfänger

> **Stand:** 2026-11-26 · Für: iPhone + AirPods + PS5 · Kein Raspberry Pi, kein Terminal, kein Slack.
> Aussagen über Apps ändern sich schnell. Unsichere Punkte sind mit 🟡/❓ markiert, Quellen in [SOURCES.md](../SOURCES.md) (V-xxx).

## 1. Die Lösung in einem Satz

**Ein ChatGPT-Projekt „GTA VI Coach“ mit Anweisungen und dieser Wissensdatenbank als Dateien. Vor dem Zocken startest du auf dem iPhone den Sprachmodus, legst das Handy weg und sprichst über die AirPods.** Bild und Ton vom Spiel laufen ganz normal über den Fernseher.

```
 PS5 ──HDMI──► Fernseher (Bild + Spielton)
 iPhone (ChatGPT-App, Voice läuft im Hintergrund) ◄──Bluetooth──► AirPods (deine Stimme + Antworten)
```

## 2. Welches Tool und warum

| Option | Empfehlung | Warum |
|---|---|---|
| **ChatGPT-Projekt + Voice** | ⭐ **Hauptlösung** | ✅ Voice funktioniert in Projekten und nutzt dabei Projekt-Anweisungen, Dateien und frühere Chats im Projekt [V-001, V-003]. 🟡 Die Einstellung „Hintergrund-Gespräche“ (Background conversations) lässt das Gespräch weiterlaufen, wenn du die App verlässt oder den Bildschirm sperrst [V-001]. Du nutzt ChatGPT schon. |
| Custom GPT | ❌ **Nicht mehr empfehlenswert** | 🟡 OpenAI plant laut seinen Release Notes, Custom GPTs einzustellen [V-001]. ✅ Die alten Sprachmodi „Advanced“ und „Standard“ werden am **11.12.2026** abgeschaltet [V-001]. Eine neue Lösung darauf aufzubauen lohnt sich nicht. |
| Claude-Projekt + Voice | Alternative | 🟡 Claude hat auf iOS einen Sprachmodus (Beta) [V-004]. ⚠️ Ob Voice die Projekt-Dateien nutzt, ist in den Quellen widersprüchlich [V-005]. Claude eignet sich sehr gut zum **Pflegen** der Wissensdatenbank (dieses Repo). |
| Grok Voice | Alternative | 🟡 Grok hat Voice und Memory [V-007, V-008]. ❓ Ein Hinweis im App Store sagt, dass ein eigener Kommunikationsstil die Websuche im Voice-Modus abschalten kann [V-009]. Projektdateien lassen sich weniger einfach einbinden. |

**Fazit:** Nimm **ChatGPT** für den Voice-Coach. Mit **Claude** (Code oder App) pflegst du später die Wissensdatenbank.

## 3. Schritt für Schritt (ca. 20 Minuten, einmalig)

### Schritt 1 – Projekt anlegen
1. Öffne die ChatGPT-App (oder chatgpt.com am Computer, dort ist es bequemer).
2. Seitenleiste → **Projekte** → **Neues Projekt** → Name: `GTA VI Coach`.
3. 🟡 Falls angeboten, wähle bei Memory **„nur Projekt“** (project-only memory). Dann vermischt sich das Spielwissen nicht mit deinen anderen Chats [V-001].

### Schritt 2 – Anweisungen einfügen
1. Im Projekt → **Anweisungen** (Instructions).
2. Kopiere den kompletten Block aus [system-prompt.md](system-prompt.md) hinein.
3. Ergänze unten deinen ausgefüllten Steckbrief aus [spielerprofil-vorlage.md](spielerprofil-vorlage.md).

### Schritt 3 – Wissen hochladen
1. Lade im Projekt unter **Dateien** diese Dateien hoch:
   - `berater/export/coach-paket-spoilerfrei.md` (alles Spoilerfreie in einer Datei)
   - [GESAMTANLEITUNG.md](../GESAMTANLEITUNG.md)
2. **Nicht** den Ordner `spoiler/` hochladen. Wenn du später Hilfe zu einer Mission brauchst, lädst du nur die Kapiteldatei hoch, die du gerade spielst. So kann der Coach nichts verraten, was er gar nicht kennt.

> Die Export-Datei erstellt man mit `python3 tools/build_coach_paket.py`. Wer kein Terminal nutzen will, öffnet die fertige Datei auf GitHub (Ordner `berater/export/`) → **Download raw file**.

### Schritt 4 – Sprachmodus einstellen (iPhone)
1. ChatGPT-App → Einstellungen → **Voice / Sprache**.
2. 🟡 **Hintergrund-Gespräche (Background conversations)** einschalten [V-001].
3. Eine Stimme wählen, die du gut verstehst. Die Sprache ist Deutsch (die App erkennt sie automatisch).

### Schritt 5 – Testlauf ohne Spiel
1. Projekt öffnen → neuer Chat **im Projekt** → Wellen-Symbol (Voice) antippen.
2. Sag: *„Test. Wie ziele ich in GTA 6?“* Die Antwort sollte kurz und deutsch sein und ehrlich sagen, wenn etwas unsicher ist.
3. Sperre den Bildschirm und frag weiter. Läuft das Gespräch weiter, ist alles richtig eingestellt.

### Schritt 6 – Beim Zocken
1. **Vor** dem Spielstart: Voice im Projekt-Chat starten, iPhone weglegen.
2. Frag einfach in die AirPods, z. B. *„Wie werde ich die Polizei los?“*
3. Wenn der Coach auf Geräusche vom Fernseher reagiert: Fernseher etwas leiser stellen, AirPods-Mikrofon nutzen (nicht das iPhone-Mikrofon) und das Handy weiter weg vom Fernseher legen. ❓ Ob das Stummschalten per AirPods-Stiel im ChatGPT-Voice funktioniert, ist nicht belegt – einfach ausprobieren.
4. 🟡 ChatGPT beendet ein Hintergrund-Gespräch, wenn es länger still ist und du auf Nachfrage nicht antwortest [V-001]. Dann tippst du einmal kurz aufs Handy (z. B. in einer Ladepause).

## 4. Dem Coach die Grundlagen geben

| Was | Wo | Wie |
|---|---|---|
| **Rolle & Antwortstil** | Projekt-Anweisungen | [system-prompt.md](system-prompt.md) |
| **Wissen über dich** | Ende der Projekt-Anweisungen | [spielerprofil-vorlage.md](spielerprofil-vorlage.md) ausfüllen |
| **Spielwissen** | Projekt-Dateien | Coach-Paket + Gesamtanleitung |
| **Spielfortschritt** | Im Gespräch | *„Merk dir: Ich bin jetzt in Kapitel 3.“* |
| **Laufendes Lernen** | Memory + Notizen | siehe [gedaechtnis.md](gedaechtnis.md) |

## 5. Was realistisch ist – und was Overkill wäre

**Realistisch und sinnvoll**
- Kurze Fragen per Sprache beantworten lassen, ohne Pause und ohne Controller wegzulegen.
- Antworten auf Grundlage dieser Wissensdatenbank, mit Hinweis, wenn etwas unsicher ist.
- Merken von Spielstil, Kapitel und wiederkehrenden Problemen (Memory im Projekt).
- Spoilerschutz: Der Coach kennt nur die Kapitel, die du hochgeladen hast.

**Möglich, aber nicht nötig**
- Den Fernseher mit der iPhone-Kamera zeigen (Live-Video). Das ist umständlich, weil du das Handy halten musst.
- Ein Siri- oder Action-Button-Kurzbefehl zum Starten des Sprachmodus. ❓ Dafür gibt es keine belegte Anleitung, und ein Fingertipp vor dem Spiel reicht.

**Overkill (nicht machen)**
- Raspberry Pi, eigene Server, eigene API-Programmierung oder Discord-/Slack-Bots.
- Ein dauerhaftes Mitschneiden des Bildschirms mit automatischer Analyse.
- Mehrere KI-Apps gleichzeitig. Bleib bei **einem** Coach.

**Grenzen**
- Der Coach sieht dein Spiel nicht. Sag ihm, wo du bist und was passiert.
- Das Spiel ist am 19.11.2026 erschienen. Vieles ist noch unbelegt, und Patches ändern Dinge.
- Die Sprachmodi der Apps ändern sich laufend. Diese Anleitung bitte regelmäßig prüfen (siehe [ROADMAP.md](../ROADMAP.md)).
