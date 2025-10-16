# Backend Project Structure

This document outlines the structure of the Django backend project.

```
backend/
├── .env                    # Environment variables (local)
├── .env.example            # Example environment variables
├── authentication/         # Django app for handling user authentication
│   ├── management/         # Custom Django commands
│   │   └── commands/
│   │       └── create_admin.py
│   ├── migrations/         # Database migrations for the authentication app
│   ├── __init__.py
│   ├── admin.py            # Django admin configuration for the app
│   ├── apps.py             # App configuration
│   ├── models.py           # Database models (custom User model)
│   ├── serializers.py      # DRF serializers for the User model
│   ├── tests.py            # App-specific tests
│   ├── urls.py             # URL patterns for the authentication API
│   └── views.py            # Views that handle API requests (register, login, etc.)
│
├── cafe_manager_backend/   # Main Django project configuration
│   ├── __init__.py
│   ├── asgi.py             # ASGI config for asynchronous servers
│   ├── settings.py         # Django project settings (database, installed apps, etc.)
│   ├── urls.py             # Root URL patterns for the project
│   └── wsgi.py             # WSGI config for synchronous servers
│
├── venv/                   # Python virtual environment directory
│
├── db.sqlite3              # SQLite database file for development
├── manage.py               # Django's command-line utility for administrative tasks
└── requirements.txt        # List of Python dependencies for the project
```

## File and Folder Descriptions

-   **`.env` / `.env.example`**: These files are used to manage environment variables. `.env` is for local development (and is ignored by Git), while `.env.example` serves as a template.

-   **`authentication/`**: This is a Django app dedicated to user authentication. It contains all the logic for user registration, login, and management for both regular users and admins.
    -   **`management/commands/create_admin.py`**: A custom management command to create the initial admin user from credentials stored in the `.env` file.
    -   **`models.py`**: Defines the database models. It includes the custom `User` model (using phone number as a username) and the new `Admin` model for system administrators.
    -   **`serializers.py`**: Contains DRF serializers to convert model instances to/from JSON. The `UserSerializer` now also handles backend validation for password confirmation.
    -   **`views.py`**: Holds the API views. The `AdminLoginView` has been refactored to use a standard method for JWT generation. The views also now return standardized Persian success messages.
    -   **`urls.py`**: Defines the specific URL patterns for the authentication app, including the new `/api/auth/admin/login/` endpoint.

-   **`cafe_manager_backend/`**: This directory is the main container for the Django project's configuration.
    -   **`settings.py`**: The most important file here. It contains all the project's configuration, such as database settings, installed apps, middleware, and authentication settings.
    -   **`urls.py`**: The root URL configuration. It includes the URLs from the `authentication` app under the `/api/auth/` path.

-   **`venv/`**: This folder contains the Python virtual environment, which includes the Python interpreter and all the installed packages for this project. It is excluded from version control.

-   **`db.sqlite3`**: The SQLite database file used during development. It is excluded from version control.

-   **`manage.py`**: A command-line utility that lets you interact with this Django project in various ways (e.g., running the server, creating migrations, running tests).

-   **`requirements.txt`**: A text file that lists all the Python packages that the project depends on (e.g., Django, Djangorestframework).
