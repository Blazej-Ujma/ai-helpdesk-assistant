# Day 05 – Deployment / Public Release

**Date / Datum:** 03.08.2026

---

# Goal / Ziel

## EN

The goal of Day 05 was to deploy the AI Helpdesk Assistant on a dedicated Linux server and make it publicly accessible over the internet.

Instead of running only on my local computer, the application should run permanently as a background service and be reachable through a secure HTTPS connection.

## DE

Das Ziel von Tag 05 war es, den AI Helpdesk Assistant auf einem eigenen Linux-Server bereitzustellen und öffentlich über das Internet erreichbar zu machen.

Die Anwendung sollte nicht mehr nur lokal auf meinem Computer laufen, sondern dauerhaft als Hintergrunddienst ausgeführt und über eine sichere HTTPS-Verbindung erreichbar sein.

---

# Debian Server Setup

## EN

A new Debian 13 virtual machine was created on my Proxmox server.

Configuration:

- 2 CPU Cores
- 4 GB RAM
- 20 GB Storage
- VirtIO Network Adapter
- SSH Server
- No graphical desktop environment

The lightweight installation keeps the server efficient and only installs the software required for the project.

## DE

Auf meinem Proxmox-Server wurde eine neue Debian-13-VM erstellt.

Konfiguration:

- 2 CPU-Kerne
- 4 GB RAM
- 20 GB Speicher
- VirtIO-Netzwerkkarte
- SSH-Server
- Keine grafische Desktopoberfläche

Durch die schlanke Installation werden nur die Komponenten installiert, die für das Projekt benötigt werden.

---

# Preparing the Server

## EN

After installing Debian, the server was prepared for the application.

Installed software:

- Git
- Python 3
- pip
- Python Virtual Environment
- curl
- cloudflared

The GitHub repository was cloned to the server.

A Python virtual environment was created and all project dependencies were installed.

During deployment I discovered that two required Python packages were missing from the `requirements.txt` file:

- openai
- python-dotenv

After updating the dependency list and redeploying the project, the application started successfully.

## DE

Nach der Installation von Debian wurde der Server vorbereitet.

Installierte Software:

- Git
- Python 3
- pip
- Python Virtual Environment
- curl
- cloudflared

Das GitHub-Repository wurde auf den Server geklont.

Anschließend wurde eine virtuelle Python-Umgebung erstellt und alle Projektabhängigkeiten installiert.

Während des Deployments fiel auf, dass zwei benötigte Bibliotheken in der `requirements.txt` fehlten:

- openai
- python-dotenv

Nach der Korrektur der Datei konnte die Anwendung erfolgreich gestartet werden.

---

# Environment Configuration

## EN

The OpenAI API key is stored inside a local `.env` file.

The file was securely copied to the Debian server.

The `.env` file is intentionally excluded from GitHub because API keys must never be published.

## DE

Der OpenAI-API-Key wird in einer lokalen `.env`-Datei gespeichert.

Diese Datei wurde sicher auf den Debian-Server übertragen.

Die `.env`-Datei befindet sich bewusst nicht im GitHub-Repository, da geheime API-Schlüssel niemals veröffentlicht werden dürfen.

---

# Running as a Linux Service

## EN

Instead of starting the application manually every time, a systemd service was created.

Advantages:

- Starts automatically after boot
- Runs permanently in the background
- Automatically restarts after crashes
- Easy administration using Linux commands

Useful commands:

```bash
sudo systemctl status ai-helpdesk
sudo systemctl restart ai-helpdesk
journalctl -u ai-helpdesk -f
```

## DE

Damit die Anwendung nicht nach jedem Neustart manuell gestartet werden muss, wurde ein eigener systemd-Dienst erstellt.

Vorteile:

- Automatischer Start beim Hochfahren
- Dauerhafte Ausführung im Hintergrund
- Automatischer Neustart nach Fehlern
- Einfache Verwaltung über Linux-Befehle

Nützliche Befehle:

```bash
sudo systemctl status ai-helpdesk
sudo systemctl restart ai-helpdesk
journalctl -u ai-helpdesk -f
```

---

# Public Deployment with Cloudflare Tunnel

## EN

To make the AI Helpdesk publicly accessible without opening router ports, Cloudflare Tunnel was used.

A personal developer domain was registered:

```
blazejujma.dev
```

The tunnel securely forwards internet traffic to the FastAPI application running locally on port 8000.

Architecture:

```
Internet
      │
Cloudflare
      │
Cloudflare Tunnel
      │
Debian 13 VM
      │
FastAPI
      │
AI Helpdesk Assistant
```

Public URL:

```
https://helpdesk.blazejujma.dev
```

## DE

Damit der AI Helpdesk ohne Portfreigaben im Router öffentlich erreichbar ist, wurde Cloudflare Tunnel eingerichtet.

Dafür wurde die persönliche Entwickler-Domain registriert:

```
blazejujma.dev
```

Der Tunnel leitet alle Anfragen sicher an die lokal laufende FastAPI-Anwendung auf Port 8000 weiter.

Architektur:

```
Internet
      │
Cloudflare
      │
Cloudflare Tunnel
      │
Debian 13 VM
      │
FastAPI
      │
AI Helpdesk Assistant
```

Öffentliche URL:

```
https://helpdesk.blazejujma.dev
```

---

# Result / Ergebnis

## EN

The AI Helpdesk Assistant is now publicly available on the internet.

The application runs continuously on a Debian server hosted inside my own Proxmox environment and is protected by Cloudflare.

The deployment was successfully tested from a smartphone using the mobile network.

## DE

Der AI Helpdesk Assistant ist jetzt öffentlich im Internet erreichbar.

Die Anwendung läuft dauerhaft auf einer Debian-VM innerhalb meiner eigenen Proxmox-Umgebung und wird über Cloudflare abgesichert.

Das Deployment wurde erfolgreich mit einem Smartphone über das Mobilfunknetz getestet.

---

# Lessons Learned / Erkenntnisse

## EN

During deployment I learned:

- How to deploy a Python web application to Linux
- How to create and manage systemd services
- How Cloudflare Tunnel works
- Why dependency management is important
- Why secret files such as `.env` should never be uploaded to GitHub
- How to publish a local application securely without opening router ports

## DE

Während des Deployments habe ich gelernt:

- Wie eine Python-Webanwendung auf Linux bereitgestellt wird
- Wie systemd-Dienste erstellt und verwaltet werden
- Wie Cloudflare Tunnel funktioniert
- Warum eine saubere Verwaltung von Abhängigkeiten wichtig ist
- Warum geheime Dateien wie `.env` niemals auf GitHub gehören
- Wie eine lokale Anwendung sicher veröffentlicht werden kann, ohne Ports am Router freizugeben

---

# Current Project Status

✅ FastAPI Backend

✅ HTML / CSS / JavaScript Frontend

✅ FAQ Knowledge Base

✅ GPT-5 Integration

✅ Conversation Memory

✅ Automatic Ticket Creation

✅ Debian Server

✅ systemd Service

✅ Cloudflare Tunnel

✅ Public HTTPS Deployment

**Live Demo**

https://helpdesk.blazejujma.dev