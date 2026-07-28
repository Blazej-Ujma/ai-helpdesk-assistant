# Glossary

## Repository

A repository (repo) is the main folder of a project.

It contains the source code, documentation and the complete Git history.

---

## Commit

A commit is a saved snapshot of the project.

Think of it like saving your progress in a video game.

Example:

```bash
git commit -m "Add Day 01 documentation"
```

---

## Push

`git push` uploads your local commits to GitHub.

This makes your latest changes available online.

---

## Pull

`git pull` downloads the latest changes from GitHub to your local computer.

---

## Branch

A branch is an independent version of your project.

Developers use branches to work on new features without affecting the main project.

---

## Clone

`git clone` creates a local copy of a GitHub repository.

Example:

```bash
git clone https://github.com/username/project.git
```

---

## Markdown (.md)

Markdown is a simple language used to write documentation.

GitHub automatically formats Markdown files.

Examples:

- README.md
- day-01.md
- glossary.md

---

## FastAPI

FastAPI is a modern Python framework for building APIs and web applications.

It is the main framework used in this project.

---

## API

API stands for **Application Programming Interface**.

An API allows two applications to communicate with each other.

Example:

A website sends a request to the backend through an API.

---

## Backend

The backend is the part of an application that runs on the server.

It processes requests, stores data and returns responses.

---

## Frontend

The frontend is the part of an application that users can see and interact with.

Examples include buttons, forms and web pages.

---

## Endpoint

An endpoint is a specific URL of an API.

Example:

```
http://localhost:8000/
```

Each endpoint performs a specific task.

---

## Route

A route tells FastAPI what should happen when a user visits a specific URL.

Example:

```python
@app.get("/")
```

---

## JSON

JSON stands for **JavaScript Object Notation**.

It is a lightweight format used to store and exchange data.

Example:

```json
{
  "question": "How do I reset my password?",
  "answer": "Contact the IT department."
}
```

---

## Docker

Docker is a platform that packages an application together with everything it needs to run.

This package is called a container.

---

## Container

A container is an isolated environment where an application runs.

It contains the application, its libraries and all required dependencies.

---

## Virtual Environment (.venv)

A virtual environment is an isolated Python environment for one project.

It keeps project dependencies separate from other Python projects.

Example:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Dependency

A dependency is a library or package that a project needs to work.

Example:

- FastAPI
- Uvicorn

---

## Package

A package is a collection of Python code that provides additional functionality.

Packages are installed with `pip`.

Example:

```bash
pip install fastapi
```

---

## Framework

A framework is a collection of tools and rules that helps developers build applications faster.

FastAPI is a Python framework.

# Commands Reference

## git add .

Adds all changed files to the staging area.

**Syntax**

```bash
git add .
```

**Explanation**

- `git` → Git program
- `add` → Add changes to the staging area
- `.` → All changed files in the current project

---

## git commit -m

Creates a new commit (saved snapshot).

**Syntax**

```bash
git commit -m "Commit message"
```

**Explanation**

- `git` → Git program
- `commit` → Create a saved snapshot
- `-m` → Message
- `"Commit message"` → Description of the commit

Example:

```bash
git commit -m "Add glossary documentation"
```

---

## git push

Uploads your local commits to GitHub.

**Syntax**

```bash
git push
```

**Explanation**

- `git` → Git program
- `push` → Upload commits to the remote repository

---

## git pull

Downloads the latest changes from GitHub.

**Syntax**

```bash
git pull
```

**Explanation**

- `git` → Git program
- `pull` → Download the latest commits from GitHub

## pip freeze

Lists all installed Python packages and their exact versions.

**Syntax**

```bash
pip freeze
```

**Explanation**

- `pip` → Python package manager
- `freeze` → Lists all installed packages with their versions

Example output:

```text
fastapi==0.116.1
uvicorn==0.35.0
```

---

## pip freeze > requirements.txt

Saves all installed packages and their versions into the `requirements.txt` file.

**Syntax**

```bash
pip freeze > requirements.txt
```

**Explanation**

- `pip` → Python package manager
- `freeze` → Lists installed packages
- `>` → Redirects the output into a file
- `requirements.txt` → Stores all required project dependencies

**Why is this useful?**

Other developers can install the exact same packages with:

```bash
pip install -r requirements.txt
```