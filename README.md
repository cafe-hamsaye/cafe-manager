# Cafe Manager

Cafe Manager is a comprehensive, full-stack web application designed to streamline cafe operations. It features a user-friendly interface for customers and a powerful admin panel for administrators to manage the menu and users. The frontend is built with Vue.js, and the backend is powered by Django.

## Features

- **User Authentication:** Secure registration and login for customers.
- **Admin Authentication:** Separate, secure login for administrators.
- **Staff Authentication:** Separate, secure login for staff members.
- **Menu Display:** A public page for anyone to view the cafe's menu.
- **User Dashboard:** A dedicated dashboard for logged-in users.
- **Admin Panel:** A powerful interface for administrators to:
  - Manage all registered users (view, update, delete).
  - Manage all menu items (create, view, update, delete).
  - Manage staff members with separate credentials (create, view, update, delete).
- **RESTful API:** A well-documented API for seamless communication between the frontend and backend.

## Technologies Used

- **Backend:**
  - Django & Django REST Framework
  - Simple JWT for authentication
  - SQLite (for development) & MySQL (for production)
- **Frontend:**
  - Vue.js & Vite
  - Vue Router for navigation
  - Feather Icons for UI elements
  - Vue Toastification for notifications

## Project Documentation

For detailed information about the project, including setup instructions and a complete API reference, please refer to the documentation in the `docs` folder:

- **[About This Project](./docs/about.md):** A comprehensive guide to setting up and running both the frontend and backend.
- **[API Documentation](./docs/api.md):** Detailed documentation for all backend API endpoints.
- **[Backend Structure](./docs/backend.md):** An overview of the Django project structure.
- **[Frontend Structure](./docs/frontend.md):** An overview of the Vue.js project structure.