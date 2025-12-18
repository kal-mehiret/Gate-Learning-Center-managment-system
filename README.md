GATE Learning Center Management System

A modern, full-featured Learning Management System (LMS) built with Django, featuring role-based access control, PostgreSQL database, and a beautiful Jazzmin admin interface.

Features
     Role-Based Access Control: Separate interfaces for Students, Instructors, and Administrators
     Course Management: Create, manage, and organize courses with materials and assignments
     Assignment System: Students submit assignments, instructors grade them
     Grade Tracking: Comprehensive grade management and reporting
    Modern Admin Interface: Jazzmin-powered admin dashboard with dark/light mode
     PostgreSQL Database: Robust and scalable database backend
     Deployment Ready: Configured for Railway, Render, and PythonAnywhere

Project Structure:

    gate-learning-center/

    apps/: Django applications
    users/: Custom user model and authentication
    courses/: Course creation and management
    enrollments/: Student enrollment system
    materials/: Learning material upload/management
    assignments/: Assignment creation and submission
    grades/: Grade tracking and reporting
    config/: Django configuration (settings, urls, wsgi)
    templates/: HTML templates with role-based organization
    admin/: Administrator templates
    courses/: Course-related pages
    instructor/: Instructor dashboard and tools
    student/: Student dashboard and views
    users/: Authentication pages (login, registration)
    static/: Static assets (CSS, JS, images)
    .env.example: Environment variables template
    requirements.txt: Python dependencies
    Procfile: Deployment configuration
    build.sh: Build script for deployment
    manage.py: Django management script

Quick Start

Prerequisites

Python 3.8+

PostgreSQL 12+

Git

Installation

Clone the repository:
git clone https://github.com/yourusername/gate-learning-center.git

cd gate-learning-center

Create and activate a virtual environment:
On Windows:
python -m venv venv
venv\Scripts\activate
On macOS/Linux:
python -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Configure environment variables:
cp .env.example .env
Edit .env with your database credentials

Set up the database:
python manage.py migrate
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Access the application:
    Main site: http://127.0.0.1:8000
    Admin panel: http://127.0.0.1:8000/admin
    Student dashboard: http://127.0.0.1:8000/student/dashboard
    Instructor dashboard: http://127.0.0.1:8000/instructor/dashboard
    Environment Variables
    Create a .env file in the project root:

SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=gate_learning_db
DB_USER=gate_user
DB_PASSWORD=your-secure-password
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1

Database Setup (PostgreSQL)

    Install PostgreSQL on your system

    Create database and user:
    CREATE DATABASE gate_learning_db;
    CREATE USER gate_user WITH PASSWORD 'your-password';
    GRANT ALL PRIVILEGES ON DATABASE gate_learning_db TO gate_user;

Admin Interface (Jazzmin)

     Modern, responsive design with sidebar navigation
     Dark/light mode toggle
     Customizable UI with visual builder
     Role-based menu items
     Enhanced search functionality
     Access at /admin after setting up your superuser

User Roles

    Role: Student
    Dashboard: /student/dashboard
    Permissions: View courses, submit assignments, check grades

    Role: Instructor
    Dashboard: /instructor/dashboard
    Permissions: Manage courses, create assignments, grade submissions

    Role: Administrator
    Dashboard: /admin
    Permissions: Full system access via Jazzmin admin