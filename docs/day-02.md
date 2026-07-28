# Day 02 – FastAPI Setup / Erste Webanwendung

**Date / Datum:** 28.07.2026

---

## Goal / Ziel

**EN**

The goal of today was to set up the technical foundation of the project and create the first working web application. Instead of writing as much code as possible, I focused on building a clean and understandable foundation for the following development days.

In addition, I defined the way I want to work on this project. Every new feature should first be understood before it is implemented. Instead of simply copying code, every feature will be explained, implemented, tested and documented step by step.

**DE**

Das Ziel des heutigen Tages war es, das Projekt technisch aufzusetzen und eine erste funktionierende Webanwendung zu erstellen. Dabei stand nicht im Vordergrund, möglichst viel Code zu schreiben, sondern eine saubere Grundlage für die nächsten Entwicklungstage zu schaffen.

Außerdem wurde die Zusammenarbeit für dieses Projekt festgelegt. Jeder Schritt soll verstanden werden. Neue Funktionen werden nicht einfach kopiert, sondern gemeinsam entwickelt, getestet und dokumentiert.

---

## Completed / Erledigt

**EN**

### Project Planning

At the beginning of the day, I reduced the scope of the project to a realistic prototype that can be completed within one week and still be explained during an apprenticeship interview.

The project will focus on:

- FastAPI as the backend
- HTML, CSS and JavaScript as the frontend
- A local FAQ database (`faq.json`)
- OpenAI integration at a later stage
- A simulated ticket system
- Docker support at the end of the project

This keeps the project understandable and avoids unnecessary complexity.

### GitHub Repository

The GitHub repository and the basic project structure were prepared.

The following files were created:

- `README.md`
- `requirements.txt`
- `Dockerfile`
- `docker-compose.yml`
- `.env.example`
- `.gitignore`
- `docs/`

I also decided to document every development day separately.

### Project Structure

The application was organized into separate folders for the backend, frontend and future knowledge base.

```text
app/
│
├── main.py
├── knowledge/
│   └── faq.json
├── static/
│   ├── style.css
│   └── script.js
└── templates/
    └── index.html
```

### Python Environment

A virtual Python environment was created.

```bash
python3 -m venv .venv
```

Afterwards it was activated.

```bash
source .venv/bin/activate
```

This keeps the project dependencies separated from the operating system.

### Installed Packages

The following libraries were installed:

- FastAPI
- Uvicorn
- Jinja2

The dependencies were saved using:

```bash
pip freeze > requirements.txt
```

### First FastAPI Application

I created my first FastAPI application.

At first the application returned a simple JSON response. After successfully testing this version, I changed the project to use HTML templates.

### HTML Templates

Instead of returning JSON, the application now renders HTML pages using Jinja2 templates.

The `main.py` file loads `index.html` from the `templates` folder.

This creates the foundation for the future user interface.

### First Working Website

The application was started with:

```bash
uvicorn app.main:app --reload
```

The first webpage was successfully displayed in the browser under:

```
http://127.0.0.1:8000
```

The complete request flow now looks like this:

```text
Browser
   │
   ▼
FastAPI
   │
   ▼
Jinja2 Template
   │
   ▼
HTML Page
   │
   ▼
Browser
```

---

**DE**

### Projektplanung

Zu Beginn des Tages wurde der Umfang des Projekts bewusst reduziert.

Da der AI Helpdesk Assistant innerhalb einer Woche entsteht und für einen Ausbildungsbewerber realistisch wirken soll, wurde auf unnötig komplexe Architekturen verzichtet.

Stattdessen konzentriert sich das Projekt auf:

- FastAPI als Backend
- HTML, CSS und JavaScript als Frontend
- lokale FAQ-Datei (`faq.json`)
- spätere OpenAI-Anbindung
- simulierte Ticketerstellung
- Docker zum Abschluss des Projekts

Dadurch bleibt das Projekt übersichtlich und nachvollziehbar.

### GitHub-Projekt

Das GitHub-Repository wurde vorbereitet und die grundlegende Projektstruktur angelegt.

Unter anderem wurden folgende Dateien erstellt:

- `README.md`
- `requirements.txt`
- `Dockerfile`
- `docker-compose.yml`
- `.env.example`
- `.gitignore`
- `docs/`

Außerdem wurde beschlossen, jeden Entwicklungstag separat zu dokumentieren.

### Projektstruktur

Für die eigentliche Anwendung wurde folgende Struktur erstellt:

```text
app/
│
├── main.py
├── knowledge/
│   └── faq.json
├── static/
│   ├── style.css
│   └── script.js
└── templates/
    └── index.html
```

Diese Struktur trennt Backend, Frontend und spätere Wissensdaten sauber voneinander.

### Python-Entwicklungsumgebung

Es wurde eine virtuelle Python-Umgebung erstellt.

```bash
python3 -m venv .venv
```

Anschließend wurde sie aktiviert.

```bash
source .venv/bin/activate
```

Dadurch bleiben alle Projektabhängigkeiten vom restlichen System getrennt.

### Installierte Bibliotheken

Für den ersten Prototyp wurden folgende Pakete installiert:

- FastAPI
- Uvicorn
- Jinja2

Danach wurde die Datei `requirements.txt` automatisch erzeugt.

```bash
pip freeze > requirements.txt
```

### Erste FastAPI-Anwendung

Anschließend wurde die erste FastAPI-Anwendung erstellt.

Zunächst wurde eine einfache API getestet, die beim Aufruf der Startseite lediglich eine JSON-Antwort zurückgegeben hat.

Nachdem dieser Test erfolgreich war, wurde die Anwendung auf HTML umgestellt.

### HTML-Templates

Anstelle einer JSON-Ausgabe verwendet das Projekt nun Jinja2-Templates.

Die Datei `main.py` lädt jetzt die Datei `index.html` aus dem Ordner `templates`.

Dadurch ist die Grundlage geschaffen, später eine vollständige Benutzeroberfläche für den AI Helpdesk Assistant zu entwickeln.

### Erste Webseite erfolgreich gestartet

Der Entwicklungsserver wurde mit Uvicorn gestartet.

```bash
uvicorn app.main:app --reload
```

Anschließend konnte die Webseite erfolgreich unter

```
http://127.0.0.1:8000
```

im Browser geöffnet werden.

Damit war der erste vollständige Durchlauf erfolgreich:

```text
Browser
   │
   ▼
FastAPI
   │
   ▼
Jinja2 Template
   │
   ▼
HTML-Seite
   │
   ▼
Browser
```

---

## What I Learned / Was ich gelernt habe

**EN**

Today I gained a much better understanding of how a web application works.

I learned:

- how a FastAPI application is structured
- what a route (`@app.get("/")`) is
- that a route is only executed when the browser sends a request
- how Jinja2 renders HTML templates
- why templates are useful
- why virtual environments are important
- how Uvicorn works
- why `--reload` is useful during development
- how the backend and frontend communicate

The most important lesson today was understanding that starting the server does not execute the `home()` function automatically. The function is only called when the browser requests the page.

**DE**

Heute habe ich deutlich besser verstanden, wie eine Webanwendung grundsätzlich aufgebaut ist.

Ich habe gelernt:

- wie eine FastAPI-Anwendung aufgebaut ist
- was eine Route (`@app.get("/")`) ist
- dass eine Route erst ausgeführt wird, wenn der Browser eine Anfrage sendet
- wie Jinja2 HTML-Templates rendert
- warum Templates verwendet werden
- warum virtuelle Umgebungen sinnvoll sind
- wie Uvicorn den Entwicklungsserver startet
- warum `--reload` die Entwicklung erleichtert
- wie Backend und Frontend zusammenarbeiten

Besonders wichtig war für mich zu verstehen, dass nicht der Server selbst die Funktion `home()` startet, sondern erst eine Anfrage des Browsers.

---

## Challenges / Herausforderungen

**EN**

One of today's biggest challenges was understanding how FastAPI processes requests. I also learned how HTML templates are connected to the backend and why a clean project structure makes future development much easier.

**DE**

Während des Aufbaus mussten einige kleinere Probleme gelöst werden.

Dazu gehörten unter anderem:

- die richtige Projektstruktur wählen
- Templates korrekt einbinden
- FastAPI richtig konfigurieren
- den Entwicklungsserver starten
- überprüfen, ob die HTML-Seite korrekt geladen wird

Alle Probleme konnten erfolgreich gelöst werden.

---

## Next Steps / Nächster Schritt

**EN**

Tomorrow I will start building the user interface.

The next tasks are:

- connect the CSS file
- create a modern layout
- design the chat area
- prepare the FAQ system
- begin the first interactive frontend features

**DE**

Als Nächstes wird die Benutzeroberfläche weiterentwickelt.

Geplant sind:

- CSS einbinden
- modernes Layout erstellen
- Chatbereich gestalten
- FAQ-Datei einlesen
- erste Chatfunktion entwickeln

Mit diesen Schritten entwickelt sich die aktuelle Testseite nach und nach zu einem einfachen AI Helpdesk Assistant.