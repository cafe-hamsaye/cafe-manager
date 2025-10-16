# About This Project

This document provides a comprehensive guide to setting up, running, and understanding the Cafe Manager project. The project consists of a Django backend and a Vue.js frontend.

---

## Backend (Django)

The backend is built with Django and Django REST Framework, providing a RESTful API for the frontend.

### Environment Setup

1.  **Navigate to the `backend` directory:**
    ```sh
    cd backend
    ```

2.  **Create a Python virtual environment:**
    This isolates the project's dependencies from your global Python installation.
    ```sh
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   On Windows:
        ```sh
        venv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
    After activation, you will see `(venv)` at the beginning of your command prompt.

4.  **Configure Environment:**
    Create a `.env` file by copying the example file.
    ```sh
    # In the `backend` directory
    cp .env.example .env
    ```
    Then, fill in the necessary values in the `.env` file, such as `ADMIN_USERNAME` and `ADMIN_PASSWORD`.

5.  **Install dependencies:**
    Install all the required Python packages using pip.
    ```sh
    pip install -r requirements.txt
    ```

### Database Setup

-   **Development:** By default, the project uses **SQLite** for development. The database file `db.sqlite3` will be created in the `backend` directory when you run the migrations.

-   **Production:** For production, the project is configured to use **MySQL**. You need to set the following environment variables (e.g., in a `.env` file):
    -   `NODE_ENV=production`
    -   `DB_HOST`
    -   `DB_PORT`
    -   `DB_USER`
    -   `DB_PASSWORD`
    -   `DB_NAME`

### Running the Backend Server

1.  **Apply database migrations:**
    This command creates the necessary database tables based on the models defined in the code.
    ```sh
    python manage.py migrate
    ```

2.  **Create the initial admin user:**
    This command reads the credentials from your `.env` file and creates the first admin user.
    ```sh
    python manage.py create_admin
    ```

3.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The backend server will start running at `http://127.0.0.1:8000/`.

---

## Frontend (Vue.js)

The frontend is a single-page application (SPA) built with Vue.js and Vite.

### Environment Setup

1.  **Navigate to the `frontend` directory:**
    ```sh
    cd frontend
    ```

2.  **Install dependencies:**
    Install all the required JavaScript packages using npm.
    ```sh
    npm install
    ```

### Running the Frontend Server

1.  **Run the development server:**
    This command starts the Vite development server with hot-reloading.
    ```sh
    npm run dev
    ```
    The frontend application will be available at `http://localhost:5173/` (the port may vary).

### Building for Production

To create an optimized build of the frontend for production, run:
```sh
npm run build
```
The production-ready files will be generated in the `frontend/dist` directory.

---

## API Documentation

Detailed documentation for all backend API endpoints, including request/response formats and error codes, is available in the [API Documentation](./api.md) file.
