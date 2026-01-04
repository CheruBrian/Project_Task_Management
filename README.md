Task Management System
Overview

The Task Management System is a backend application built with Django that allows users to create, manage, and track tasks efficiently. Each user can manage their own tasks, update task details, mark tasks as complete or incomplete, and delete tasks when no longer needed.

The project demonstrates best practices in Django project structure, database modeling, authentication, and CRUD operations.

Features

User authentication (login and registration)

Create, read, update, and delete (CRUD) tasks

Mark tasks as complete or incomplete

Secure user-specific task access

Admin panel for managing users and tasks

Scalable project structure ready for API extension

Technologies Used

Python 3

Django

HTML / CSS (for templates, if applicable)

Project Structure
task_management/
│
├── manage.py
│
├── task_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── db.sqlite3
└── README.md

Getting Started
Prerequisites

Ensure you have the following installed:

Python 3.10+

pip

virtualenv (recommended)

Installation

Clone the repository:

git clone https://github.com/your-username/task_management.git


Navigate into the project directory:

cd task_management


Create and activate a virtual environment:

Windows

python -m venv venv
venv\Scripts\activate


Linux / macOS

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install django

Database Setup

Run migrations to set up the database:

python manage.py makemigrations
python manage.py migrate


Create a superuser:

python manage.py createsuperuser

Running the Application

Start the development server:

python manage.py runserver


Open your browser and visit:

http://127.0.0.1:8000/


Admin panel:

http://127.0.0.1:8000/admin/

Usage

Log in or register as a user

Create new tasks with relevant details

Update task status as complete or incomplete

Edit or delete tasks as needed

Admin users can manage all tasks via the Django admin interface

Future Improvements

REST API using Django REST Framework

Task prioritization and due dates

Search and filtering

Frontend integration (React or Vue)

User roles and permissions

License

This project is intended for educational and demonstration purposes.

Author

Cheru
