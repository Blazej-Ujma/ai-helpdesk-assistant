# Day 03 – Frontend Development & User Interaction / Frontend-Entwicklung & Benutzerinteraktion

**Date / Datum:** 29.07.2026

---

# Goal / Ziel

## EN

Today's goal was to transform the static webpage into an interactive AI Helpdesk prototype. The focus was on improving the user interface, implementing JavaScript functionality and creating the first simulated AI conversation without using the backend yet.

## DE

Das Ziel des heutigen Tages war es, die bisher statische Webseite in einen interaktiven AI-Helpdesk-Prototypen zu verwandeln. Der Schwerpunkt lag auf der Weiterentwicklung der Benutzeroberfläche, der Implementierung von JavaScript-Funktionen sowie der ersten simulierten KI-Konversation – zunächst noch ohne Backend.

---

# Completed / Erledigt

## EN

### User Interface

The visual design of the application was finalized.

The interface now includes:

- modern dark theme
- responsive header with online status
- centered chat card
- welcome message
- quick action buttons
- message input field
- send button
- chat bubble layout

Several layouts were tested before selecting the final design.

### Interactive Chat

The application now behaves like a real chat interface.

Implemented features:

- sending messages without reloading the page
- dynamically creating chat messages
- automatic clearing of the input field
- automatic focus on the input field
- automatic scrolling to the latest message

### Simulated AI Assistant

The first local AI assistant was implemented completely in JavaScript.

Current workflow:

1. The user sends a message.
2. The message appears immediately in the chat.
3. "AI is typing..." is displayed.
4. After a short delay, the assistant responds automatically.
5. Different responses are returned depending on the detected topic.

Currently supported topics:

- Password Reset
- Outlook
- VPN
- General IT Issues

### JavaScript Improvements

The JavaScript code was restructured to make future development easier.

Implemented improvements:

- response texts stored inside a dedicated object
- keyword detection using `includes()`
- case-insensitive matching with `toLowerCase()`
- reusable response handling
- preparation for a future FAQ database

The current logic can later be moved to FastAPI with only minimal changes.

---

## DE

### Benutzeroberfläche

Das Design der Anwendung wurde fertiggestellt.

Die Oberfläche besitzt nun:

- modernes Dark-Theme
- responsiven Header mit Online-Status
- zentrierte Chat-Karte
- Begrüßungsbereich
- Quick-Action-Buttons
- Eingabefeld
- Send-Button
- Chat-Sprechblasen

Während der Entwicklung wurden verschiedene Layouts getestet, bevor das endgültige Design ausgewählt wurde.

### Interaktive Chatfunktion

Die Anwendung verhält sich nun wie ein echter Chat.

Umgesetzt wurden:

- Nachrichten ohne Neuladen der Seite senden
- dynamisches Erstellen neuer Chatnachrichten
- automatisches Leeren des Eingabefelds
- automatischer Fokus auf das Eingabefeld
- automatisches Scrollen zur neuesten Nachricht

### Simulierter KI-Assistent

Der erste lokale KI-Assistent wurde vollständig mit JavaScript umgesetzt.

Der aktuelle Ablauf:

1. Der Benutzer sendet eine Nachricht.
2. Die Nachricht erscheint sofort im Chat.
3. „AI is typing...“ wird angezeigt.
4. Nach einer kurzen Verzögerung erscheint automatisch eine Antwort.
5. Je nach erkanntem Thema wird eine unterschiedliche Antwort ausgegeben.

Aktuell unterstützte Themen:

- Passwort zurücksetzen
- Outlook
- VPN
- allgemeine IT-Probleme

### Verbesserungen im JavaScript

Der JavaScript-Code wurde übersichtlicher aufgebaut und auf zukünftige Erweiterungen vorbereitet.

Umgesetzt wurden:

- Antworten in einem eigenen Objekt gespeichert
- Schlüsselworterkennung mit `includes()`
- Umwandlung in Kleinbuchstaben mit `toLowerCase()`
- wiederverwendbare Antwortlogik
- Vorbereitung auf eine spätere FAQ-Datenbank

Die aktuelle Logik kann später nahezu unverändert in das FastAPI-Backend übernommen werden.

---

# What I Learned / Was ich gelernt habe

## EN

Today I learned:

- how JavaScript communicates with HTML
- how event listeners work
- how dynamic HTML elements are created
- how chat messages can be generated without reloading the page
- how simple rule-based AI responses work
- how JavaScript objects help organize data
- how automatic scrolling improves usability
- how clean code structure simplifies future backend integration

---

## DE

Heute habe ich gelernt:

- wie JavaScript mit HTML zusammenarbeitet
- wie Event Listener funktionieren
- wie HTML-Elemente dynamisch erstellt werden
- wie Chatnachrichten ohne Neuladen der Seite erzeugt werden
- wie einfache regelbasierte KI-Antworten funktionieren
- wie JavaScript-Objekte Daten übersichtlich speichern
- wie automatisches Scrollen die Benutzerfreundlichkeit verbessert
- warum eine saubere Code-Struktur die spätere Backend-Integration erleichtert

---

# Challenges / Herausforderungen

## EN

Several interface concepts were tested before selecting the final layout.

During development several small JavaScript and CSS issues occurred, including missing brackets, incorrect CSS selectors and unsaved files.

Each issue was solved by testing every small change immediately instead of changing many things at once.

This iterative workflow made debugging much easier and highlighted the importance of careful testing during development.

---

## DE

Während der Entwicklung wurden verschiedene Layouts getestet, bevor das endgültige Design ausgewählt wurde.

Außerdem traten einige kleinere JavaScript- und CSS-Probleme auf, unter anderem fehlende Klammern, falsche CSS-Selektoren sowie nicht gespeicherte Dateien.

Alle Probleme konnten durch konsequentes Testen nach jeder kleinen Änderung schnell gefunden und behoben werden.

Dieser schrittweise Entwicklungsprozess zeigte erneut, wie wichtig regelmäßiges Testen während der Entwicklung ist.

---

# Next Steps / Nächster Schritt

## EN

The next milestone is connecting the frontend to the FastAPI backend.

The JavaScript frontend will send messages to a `/chat` endpoint.

The backend will then read responses from a local `faq.json` knowledge base before integrating the OpenAI API in a later stage.

## DE

Als Nächstes wird das Frontend mit dem FastAPI-Backend verbunden.

Das JavaScript sendet die Benutzernachricht künftig an einen `/chat`-Endpunkt.

Das Backend wird die Antworten anschließend aus einer lokalen `faq.json` laden, bevor später die OpenAI-API integriert wird.