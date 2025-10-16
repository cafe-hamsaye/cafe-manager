# Frontend Project Structure

This document outlines the structure of the Vue.js frontend project.

```
frontend/
├── node_modules/           # Directory where npm installs project dependencies
├── src/                    # Main source code for the Vue application
│   ├── components/         # Reusable Vue components
│   │   ├── auth/           # Components related to authentication
│   │   └── layout/         # Layout components (Header, Footer, Background, DashboardHeader, AdminHeader, UserProfileMenu, BackButton)
│   ├── config/             # Configuration files (e.g., API endpoint settings)
│   │   └── api.js
│   ├── css/                # CSS stylesheets
│   │   └── main.css
│   ├── pages/              # Main page components for different routes
│   │   ├── AuthPage.vue
│   │   ├── LandingPage.vue
│   │   ├── DashboardPage.vue
│   │   ├── AdminLoginPage.vue
│   │   └── AdminDashboardPage.vue
│   ├── router/             # Vue Router configuration
│   │   └── index.js
│   ├── App.vue             # The root Vue component
│   └── main.js             # The entry point of the application
│
├── index.html              # The main HTML file that hosts the Vue app
├── package.json            # Lists project dependencies and npm scripts
├── package-lock.json       # Records the exact versions of dependencies
└── vite.config.js          # Configuration file for Vite
```

## File and Folder Descriptions

-   **`node_modules/`**: This directory contains all the JavaScript packages and dependencies that the project relies on. It is managed by npm and is excluded from version control.

-   **`src/`**: This is the heart of the Vue application, containing all the source code.
    -   **`components/layout/`**: This folder now contains specialized headers (`DashboardHeader`, `AdminHeader`), a reusable `UserProfileMenu` with a logout function, and a `BackButton` for specific pages.
    -   **`config/`**: Contains configuration files. `api.js` is used to configure the base URL for the backend API, making it easy to change.
    -   **`css/`**: For global CSS styles. `main.css` contains styles that apply to the entire application.
    -   **`pages/`**: These are the main components mapped to routes. This now includes `DashboardPage` for users, and `AdminLoginPage` and `AdminDashboardPage` for administrators.
    -   **`router/`**: This directory contains the Vue Router configuration. `index.js` defines all the application routes and maps them to the corresponding page components.
    -   **`App.vue`**: The root component of the application. It has been updated with logic to conditionally render the correct header (generic, dashboard, or admin) based on the current route, and to hide the header/footer on the authentication page.
    -   **`main.js`**: The entry point for the application. It initializes Vue, sets up the router, and mounts the root `App.vue` component to the `index.html` file.

-   **`index.html`**: The main HTML page for the single-page application. The Vue app is mounted into an element within this file.

-   **`package.json`**: This file is crucial for managing the project's dependencies and defining npm scripts (e.g., `npm run dev`, `npm run build`).

-   **`package-lock.json`**: An automatically generated file that records the exact version of every installed dependency, ensuring consistent installations across different environments.

-   **`vite.config.js`**: The configuration file for Vite, the build tool used for the frontend. It allows you to customize the development server, build process, and more.
