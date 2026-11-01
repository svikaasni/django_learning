# 🛒 Storefront — Django Learning Project

A beginner Django project built while learning the Django web framework. It includes a `playground` app for experimenting with views, templates, URL routing, and the Django Debug Toolbar.

---

## 🧰 Tech Stack

| Tool | Version |
|---|---|
| Python | 3.12 |
| Django | 6.1.x |
| django-debug-toolbar | latest |
| Database | SQLite3 (default) |
| Package Manager | Pipenv |

---

## 📁 Project Structure
storefront/ ├── manage.py # Django management script ├── Pipfile # Pipenv dependencies ├── Pipfile.lock ├── db.sqlite3 # SQLite database ├── storefront/ # Core Django project config │ ├── settings.py │ ├── urls.py # Root URL configuration │ ├── asgi.py │ └── wsgi.py └── playground/ # Experimental Django app ├── views.py # View functions (say_hello, etc.) ├── urls.py # App-level URL patterns ├── models.py ├── admin.py ├── apps.py └── templates/ └── hello.html # HTML template

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have the following installed:
- Python 3.12 (https://www.python.org/downloads/)
- Pipenv (https://pipenv.pypa.io/en/latest/)

    pip install pipenv

### 2. Clone the Repository

    git clone https://github.com/svikaasni/django_learning.git
    cd django_learning

### 3. Install Dependencies

    pipenv install

### 4. Activate the Virtual Environment

    pipenv shell

### 5. Apply Migrations

    python manage.py migrate

### 6. Run the Development Server

    python manage.py runserver

Visit: http://127.0.0.1:8000/

---

## 🔗 URL Routes

| URL | Description |
|---|---|
| /admin/ | Django Admin Panel |
| /playground/hello/ | Renders the hello template |
| /__debug__/ | Django Debug Toolbar |

---

## 🛠️ Django Debug Toolbar

This project uses django-debug-toolbar to inspect SQL queries, templates, signals, and more during development.
It is accessible at /__debug__/ and appears as a side panel when viewing pages in the browser.

---

## 📚 Concepts Practiced

- Setting up a Django project with django-admin startproject
- Creating Django apps with startapp
- Writing function-based views (FBVs)
- Rendering HTML templates with context data
- Configuring URL patterns with path() and include()
- Using pipenv for virtual environment management
- Integrating third-party packages (Django Debug Toolbar)

---

## ⚠️ Important Notes

- Do not use the development server in production. Use a production WSGI/ASGI server (e.g., Gunicorn, Uvicorn).
- The db.sqlite3 file is included for local development only.

---

## 👤 Author

Vikaasni
Learning Django — one manage.py command at a time. 🐍

---

## 📄 License

This project is for educational purposes only.
