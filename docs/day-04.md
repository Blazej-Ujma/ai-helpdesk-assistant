# Day 04 – OpenAI Integration & Intelligent Helpdesk Workflow

**Date / Datum:** 03.08.2026

---

# Goal / Ziel

## EN

Today's goal was to transform the AI Helpdesk Assistant from a rule-based chatbot into an intelligent assistant.

The application should continue using the local FAQ knowledge base for common IT problems while being able to answer completely new questions with the OpenAI API.

Another important objective was implementing a simple IT ticket system as a fallback whenever the AI service is unavailable.

---

## DE

Das Ziel des heutigen Tages war es, den AI Helpdesk Assistant von einem regelbasierten Chatbot zu einem intelligenten Assistenten weiterzuentwickeln.

Die Anwendung sollte weiterhin die lokale FAQ-Wissensdatenbank für häufige IT-Probleme nutzen und zusätzlich mit der OpenAI-API völlig neue Fragen beantworten können.

Ein weiterer wichtiger Schritt war die Implementierung eines einfachen IT-Ticketsystems als Fallback, falls der KI-Dienst nicht verfügbar ist.

---

# Completed / Erledigt

## EN

### OpenAI API Integration

The application is now connected to the OpenAI API.

Implemented features:

- installed the official OpenAI Python SDK
- created a secure `.env` configuration
- loaded the API key using `python-dotenv`
- connected FastAPI to the OpenAI API
- successfully tested the API connection
- generated AI responses directly inside the web application

---

### Intelligent Request Workflow

The request handling was redesigned.

Current workflow:

1. The user sends a request.
2. The backend searches the local FAQ knowledge base.
3. If a matching FAQ is found, the stored answer is returned immediately.
4. If no FAQ matches, the request is forwarded to the OpenAI API.
5. If the AI service is unavailable, an IT support ticket is created automatically.

This combines fast predefined answers with flexible AI-generated responses.

---

### Automatic Ticket System

The first ticket system was completed.

Implemented features:

- automatic ticket creation
- sequential ticket numbers
- local storage inside `tickets.json`
- ticket status (`open`)
- automatic fallback if the AI service is unavailable

---

### Prompt Engineering

A dedicated system prompt was created for the AI assistant.

The assistant was instructed to:

- answer in simple English
- use short troubleshooting steps
- avoid unnecessary technical terminology
- recommend contacting IT support when administrator privileges are required

This makes the responses easier to understand for users with limited technical knowledge.

---

### Security

The OpenAI API key is now stored securely.

Implemented improvements:

- `.env` for local configuration
- `.env.example` for GitHub
- API key excluded from version control using `.gitignore`

---

## DE

### OpenAI-API-Integration

Die Anwendung ist nun mit der OpenAI-API verbunden.

Umgesetzt wurden:

- Installation des offiziellen OpenAI-Python-SDKs
- sichere Konfiguration über eine `.env`-Datei
- Laden des API-Schlüssels mit `python-dotenv`
- Verbindung zwischen FastAPI und der OpenAI-API
- erfolgreicher Test der API-Verbindung
- KI-generierte Antworten direkt in der Webanwendung

---

### Intelligenter Anfrageablauf

Die Verarbeitung von Benutzeranfragen wurde erweitert.

Der aktuelle Ablauf:

1. Der Benutzer sendet eine Anfrage.
2. Das Backend durchsucht die lokale FAQ-Wissensdatenbank.
3. Wird ein passender Eintrag gefunden, wird die gespeicherte Antwort zurückgegeben.
4. Gibt es keinen Treffer, wird die Anfrage an die OpenAI-API weitergeleitet.
5. Ist der KI-Dienst nicht verfügbar, wird automatisch ein IT-Support-Ticket erstellt.

Dadurch werden schnelle Standardantworten mit flexiblen KI-Antworten kombiniert.

---

### Automatisches Ticketsystem

Das erste Ticketsystem wurde fertiggestellt.

Umgesetzt wurden:

- automatische Ticketerstellung
- fortlaufende Ticketnummern
- lokale Speicherung in `tickets.json`
- Ticketstatus (`open`)
- automatischer Fallback bei Ausfall des KI-Dienstes

---

### Prompt Engineering

Für den KI-Assistenten wurde ein eigener System-Prompt entwickelt.

Die KI wurde angewiesen:

- in einfachem Englisch zu antworten
- kurze Lösungsschritte auszugeben
- unnötige Fachbegriffe zu vermeiden
- bei Administratorrechten den IT-Support zu empfehlen

Dadurch werden die Antworten verständlicher, insbesondere für Benutzer mit wenig technischem Hintergrund.

---

### Sicherheit

Der OpenAI-API-Schlüssel wird nun sicher gespeichert.

Umgesetzt wurden:

- `.env` für die lokale Konfiguration
- `.env.example` für GitHub
- Ausschluss des API-Schlüssels über `.gitignore`

---

# What I Learned / Was ich gelernt habe

## EN

Today I learned:

- how to connect a FastAPI application to the OpenAI API
- how environment variables improve security
- how AI can be combined with a local knowledge base
- how fallback mechanisms increase application reliability
- how prompt engineering influences AI responses
- how API integrations are tested step by step

---

## DE

Heute habe ich gelernt:

- wie eine FastAPI-Anwendung mit der OpenAI-API verbunden wird
- wie Umgebungsvariablen die Sicherheit verbessern
- wie eine KI mit einer lokalen Wissensdatenbank kombiniert werden kann
- wie Fallback-Mechanismen die Zuverlässigkeit einer Anwendung erhöhen
- wie Prompt Engineering die Antworten der KI beeinflusst
- wie API-Integrationen Schritt für Schritt getestet werden

---

# Challenges / Herausforderungen

## EN

During development several configuration and debugging issues occurred.

The OpenAI SDK had to be configured correctly inside the virtual environment, the API key had to be loaded securely from the `.env` file, and several Python indentation errors had to be resolved.

By testing every small implementation step individually, all issues were solved successfully.

---

## DE

Während der Entwicklung traten mehrere Konfigurations- und Debugging-Probleme auf.

Das OpenAI-SDK musste korrekt in der virtuellen Umgebung eingerichtet werden, der API-Schlüssel sicher aus der `.env`-Datei geladen werden und mehrere Python-Einrückungsfehler mussten behoben werden.

Durch konsequentes Testen nach jeder kleinen Änderung konnten alle Probleme erfolgreich gelöst werden.

---

# Current Project Status / Aktueller Projektstand

- ✅ Interactive web interface
- ✅ FastAPI backend
- ✅ JSON knowledge base
- ✅ Keyword-based FAQ search
- ✅ OpenAI API integration
- ✅ Automatic IT ticket creation
- ⏳ Online deployment
- ⏳ Final presentation

---

# Next Steps / Nächster Schritt

## EN

The next milestone is deploying the application online and preparing the final presentation.

Future improvements could include multilingual support, allowing employees to communicate with the helpdesk in different languages while using the same backend knowledge base and AI system.

---

## DE

Als nächster Meilenstein folgt das Online-Hosting der Anwendung sowie die Vorbereitung der Abschlusspräsentation.

Eine mögliche zukünftige Erweiterung ist die Unterstützung mehrerer Sprachen. Dadurch könnten Mitarbeiter in ihrer jeweiligen Sprache mit dem Helpdesk kommunizieren, während dieselbe Wissensdatenbank und dieselbe KI im Hintergrund genutzt werden.