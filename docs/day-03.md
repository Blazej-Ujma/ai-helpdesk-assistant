# Day 03 – Interactive Chat, FastAPI Backend & Knowledge Base

**Date / Datum:** 29.07.2026

---

# Goal / Ziel

## EN

Today's goal was to transform the first static webpage into a functional AI Helpdesk prototype.

The focus was not only on creating a modern chat interface, but also on connecting the frontend to a real FastAPI backend. Instead of generating responses directly inside JavaScript, the application should now communicate with the backend through an API.

Another major objective was to improve the overall project structure by separating the support knowledge from the application logic. For this purpose, an external JSON knowledge base was introduced. This makes the application easier to maintain and allows new support topics to be added without modifying the Python code.

Finally, the search algorithm was improved to recognize multiple keywords for each support topic, making the assistant more flexible and closer to a real IT helpdesk.

---

## DE

Das Ziel des heutigen Tages war es, aus der ersten statischen Webseite einen funktionierenden AI-Helpdesk-Prototypen zu entwickeln.

Der Schwerpunkt lag nicht nur auf einer modernen Chat-Oberfläche, sondern auch auf der Anbindung des Frontends an ein echtes FastAPI-Backend. Anstatt Antworten direkt in JavaScript zu erzeugen, kommuniziert die Anwendung nun über eine API mit dem Backend.

Ein weiterer wichtiger Schritt war die Verbesserung der Projektstruktur. Dafür wurde das Supportwissen vom eigentlichen Programmcode getrennt und erstmals in einer externen JSON-Datei gespeichert. Dadurch lässt sich die Wissensdatenbank später erweitern, ohne Änderungen am Python-Code vorzunehmen.

Zusätzlich wurde die Suchlogik verbessert, sodass mehrere Schlüsselwörter dieselbe Supportantwort auslösen können. Dadurch reagiert der Helpdesk deutlich flexibler auf unterschiedliche Formulierungen.

---

# Completed / Erledigt

## EN

### User Interface

The visual appearance of the application was finalized.

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

---

### Interactive Chat

The application now behaves like a real chat application.

Implemented features:

- sending messages without reloading the page
- dynamically creating chat messages
- automatic clearing of the input field
- automatic focus on the input field
- automatic scrolling to the latest message
- typing indicator ("AI is typing...")

---

### FastAPI Backend

The frontend is now connected to a real backend.

Implemented features:

- created the first FastAPI application
- created the `/chat` API endpoint
- received user messages through HTTP POST requests
- validated requests using Pydantic
- returned responses as JSON
- connected JavaScript with FastAPI using the Fetch API

---

### External Knowledge Base

The support knowledge was moved into a separate JSON file.

Implemented improvements:

- created the first `faq.json`
- loaded the knowledge base automatically on application startup
- removed hardcoded responses from the Python source code
- separated application logic from support data

---

### Improved Keyword Search

The search logic was redesigned.

Instead of supporting only one keyword per topic, every support entry now contains multiple keywords.

Example:

- password
- login
- sign in
- credentials

All of these return the same helpdesk response.

This makes the assistant much more flexible when processing user requests.

---

### Testing

Every feature was tested after implementation.

Successfully tested support topics:

- Password Reset
- Login Problems
- Outlook
- Email
- VPN
- Remote Access

Unknown requests correctly return the default response.

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

Vor der endgültigen Version wurden verschiedene Layouts getestet.

---

### Interaktive Chatfunktion

Die Anwendung verhält sich nun wie ein echter Chat.

Umgesetzt wurden:

- Nachrichten ohne Neuladen der Seite senden
- dynamisches Erstellen neuer Chatnachrichten
- automatisches Leeren des Eingabefelds
- automatischer Fokus auf das Eingabefeld
- automatisches Scrollen zur neuesten Nachricht
- Anzeige „AI is typing...“

---

### FastAPI-Backend

Das Frontend kommuniziert nun mit einem echten Backend.

Umgesetzt wurden:

- Erstellung der ersten FastAPI-Anwendung
- Erstellung des `/chat`-API-Endpunkts
- Empfang von Benutzernachrichten per HTTP-POST
- Validierung der Daten mit Pydantic
- Rückgabe der Antworten als JSON
- Verbindung zwischen JavaScript und FastAPI über die Fetch-API

---

### Externe Wissensdatenbank

Die Supportinformationen befinden sich nun in einer separaten JSON-Datei.

Umgesetzt wurden:

- Erstellung der ersten `faq.json`
- automatisches Laden der Wissensdatenbank beim Start der Anwendung
- Auslagerung aller Supportantworten aus dem Python-Code
- Trennung von Programmcode und Supportdaten

---

### Verbesserte Suchlogik

Die Suchfunktion wurde erweitert.

Jedes Supportthema kann nun mehrere Schlüsselwörter enthalten.

Beispielsweise führen die Begriffe

- password
- login
- sign in
- credentials

alle zur gleichen Antwort.

Dadurch reagiert der Helpdesk flexibler auf unterschiedliche Formulierungen der Benutzer.

---

### Tests

Alle Funktionen wurden nach jeder Änderung getestet.

Erfolgreich getestet wurden:

- Passwort zurücksetzen
- Login-Probleme
- Outlook
- E-Mail
- VPN
- Remote Access

Unbekannte Anfragen liefern eine Standardantwort, wenn keine passende Lösung gefunden wurde.

---

# What I Learned / Was ich gelernt habe

## EN

Today I learned:

- how JavaScript communicates with FastAPI
- how REST API endpoints work
- how JSON data is exchanged between frontend and backend
- how Pydantic validates incoming requests
- how external JSON files can be used as a knowledge base
- how nested loops improve keyword searching
- why separating data from application logic makes software easier to maintain
- why testing every small step reduces debugging time

---

## DE

Heute habe ich gelernt:

- wie JavaScript mit FastAPI kommuniziert
- wie REST-API-Endpunkte funktionieren
- wie JSON zwischen Frontend und Backend ausgetauscht wird
- wie Pydantic eingehende Daten validiert
- wie externe JSON-Dateien als Wissensdatenbank verwendet werden
- wie verschachtelte Schleifen die Schlüsselwortsuche verbessern
- warum die Trennung von Daten und Programmcode Software wartbarer macht
- warum konsequentes Testen nach jeder kleinen Änderung Fehler schneller aufdeckt

---

# Challenges / Herausforderungen

## EN

During development several small problems occurred, mainly related to Python indentation, JSON structure and frontend-backend communication.

Each issue was solved by testing every small implementation step immediately before continuing.

Working incrementally proved to be much more efficient than changing many parts of the project at once.

---

## DE

Während der Entwicklung traten einige kleinere Probleme auf, insbesondere bei der Python-Einrückung, der Struktur der JSON-Datei sowie bei der Kommunikation zwischen Frontend und Backend.

Alle Probleme konnten durch konsequentes Testen nach jeder kleinen Änderung schnell gefunden und behoben werden.

Der schrittweise Entwicklungsprozess hat erneut gezeigt, dass kleine, nachvollziehbare Änderungen das Debugging erheblich erleichtern.

---

# Next Steps / Nächster Schritt

## EN

The next milestone is implementing an automatic IT ticket system for unknown support requests.

After that, the OpenAI API will be integrated so the assistant can generate intelligent answers whenever no matching FAQ entry is found.

---

## DE

Als Nächstes wird ein automatisches Ticketsystem für unbekannte Supportanfragen implementiert.

Anschließend wird die OpenAI-API integriert, sodass der Helpdesk intelligente Antworten generieren kann, wenn keine passende FAQ gefunden wird.

---

## Automatic Ticket Creation

The first version of an automatic IT ticket system was implemented.

Whenever the knowledge base cannot find a matching solution, the backend now creates a support ticket automatically.

Implemented features:

- automatic ticket creation
- sequential ticket numbers
- local ticket storage in `tickets.json`
- ticket status (`open`)
- confirmation message displayed in the chat

This simulates a typical workflow of an internal IT helpdesk.

---

## Automatische Ticketerstellung

Die erste Version eines automatischen IT-Ticketsystems wurde implementiert.

Findet die Wissensdatenbank keine passende Lösung, erstellt das Backend nun automatisch ein Support-Ticket.

Umgesetzt wurden:

- automatische Ticketerstellung
- fortlaufende Ticketnummern
- lokale Speicherung in `tickets.json`
- Ticketstatus (`open`)
- Bestätigung im Chat nach erfolgreicher Erstellung

Dadurch ähnelt der Ablauf bereits einem typischen internen IT-Helpdesk.

---

# What I Learned / Was ich gelernt habe

## EN

Additional topics learned today:

- how JSON files can be used as a simple database
- how Python writes data permanently to JSON files
- how sequential ticket numbers can be generated
- how backend data persists between multiple requests
- how to debug routing and indentation issues in FastAPI

---

## DE

Zusätzlich habe ich heute gelernt:

- wie JSON-Dateien als einfache Datenbank genutzt werden können
- wie Python Daten dauerhaft in JSON-Dateien speichert
- wie fortlaufende Ticketnummern erzeugt werden
- wie Backend-Daten zwischen mehreren Anfragen erhalten bleiben
- wie sich Routing- und Einrückungsfehler in FastAPI systematisch debuggen lassen

---

# Challenges / Herausforderungen

## EN

During implementation, a Python indentation error temporarily prevented the application from starting. Additionally, the home route was accidentally removed, resulting in HTTP 404 errors.

Both issues were solved by debugging the application step by step, checking the registered FastAPI routes and carefully correcting the code structure.

This demonstrated once again how important incremental development and systematic debugging are during software development.

---

## DE

Während der Implementierung führte ein Python-Einrückungsfehler zunächst dazu, dass die Anwendung nicht mehr gestartet werden konnte. Zusätzlich wurde versehentlich die Startseiten-Route entfernt, wodurch HTTP-404-Fehler entstanden.

Beide Probleme konnten durch systematisches Debugging, das Überprüfen der registrierten FastAPI-Routen sowie das schrittweise Korrigieren des Codes behoben werden.

Dadurch wurde erneut deutlich, wie wichtig kleine Entwicklungsschritte und ein strukturierter Debugging-Prozess bei der Softwareentwicklung sind.

---

# Current Project Status / Aktueller Projektstand

- ✅ Interactive web interface
- ✅ FastAPI backend
- ✅ JSON knowledge base
- ✅ Keyword-based FAQ search
- ✅ Automatic IT ticket creation
- ⏳ OpenAI API integration
- ⏳ Final presentation

---

# Next Steps / Nächster Schritt

## EN

The next milestone is integrating the OpenAI API.

The application will first search the local knowledge base. If no suitable answer is found, the request will be forwarded to the OpenAI API. If the AI still cannot resolve the problem, an IT support ticket will be created automatically.

---

## DE

Als nächster Meilenstein folgt die Integration der OpenAI-API.

Die Anwendung durchsucht zunächst die lokale Wissensdatenbank. Wird dort keine passende Antwort gefunden, wird die Anfrage an die OpenAI-API weitergeleitet. Kann auch die KI das Problem nicht lösen, wird automatisch ein IT-Support-Ticket erstellt.