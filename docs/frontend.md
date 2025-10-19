# Frontend Project Structure

This document outlines the structure of the Vue.js frontend project.

```
frontend/
├── node_modules/           # Directory where npm installs project dependencies
├── src/                    # Main source code for the Vue application
│   ├── components/         # Reusable Vue components
│   │   ├── admin/          # Components for the admin panel
│   │   │   ├── UsersTable.vue
│   │   │   ├── MenuItemModal.vue
│   │   │   ├── MenuTable.vue
│   │   │   ├── StaffTable.vue
│   │   │   └── StaffModal.vue
│   │   ├── auth/           # Components related to authentication
│   │   ├── layout/         # Layout components (Header, Footer, StaffHeader, ...)
...
│   ├── pages/              # Main page components for different routes
│   │   ├── ...
│   │   ├── AdminDashboardPage.vue
│   │   ├── StaffLoginPage.vue
│   │   └── StaffDashboardPage.vue
│   ├── router/             # Vue Router configuration
│   │   └── index.js
│   ├── utils/              # Utility functions
│   │   └── authFetch.js
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
    -   **`components/layout/`**: This folder now contains specialized headers (`DashboardHeader`, `AdminHeader` with corrected item alignment), a reusable `UserProfileMenu`, and a `BackButton` used on auth pages. It also includes reusable modal components: `BaseModal.vue` for the basic modal structure and `ConfirmationModal.vue` for showing confirmation dialogs.
    -   **`config/`**: Contains configuration files. `api.js` is used to configure the base URL for the backend API, making it easy to change. It now includes endpoints for the menu API. `constants.js` stores constant values used throughout the application, such as local storage keys.
    -   **`css/`**: For global CSS styles. `main.css` contains styles that apply to the entire application.
    -   **`pages/`**: These are the main components mapped to routes. This now includes `DashboardPage` for users, and `AdminLoginPage` and `AdminDashboardPage` for administrators. The admin dashboard now dynamically renders management components like `UsersTable` and `MenuTable`.
    -   **`router/`**: This directory contains the Vue Router configuration. `index.js` defines all the application routes and maps them to the corresponding page components. It now includes routes for menu management and the public menu page.
    -   **`utils/`**: This directory contains utility functions. `authFetch.js` is a utility for making authenticated API requests, handling token refresh, and logout.
    -   **`components/admin/`**: This folder contains components that are specific to the admin panel, such as the `UsersTable.vue` for managing users, `MenuTable.vue` for managing menu items, `MenuItemModal.vue` for adding and editing menu items, `StaffTable.vue` for managing staff, and `StaffModal.vue` for the staff form.
    -   **`components/Menu.vue`**: A component that displays the menu to regular users.
    -   **`App.vue`**: The root component of the application. It has been updated with logic to conditionally render the correct header (generic, dashboard, or admin) based on the current route, and to hide the header/footer on the authentication page.
    -   **`main.js`**: The entry point for the application. It initializes Vue, sets up the router, and mounts the root `App.vue` component to the `index.html` file. It now also configures the `vue-final-modal` plugin.

-   **`index.html`**: The main HTML page for the single-page application. The Vue app is mounted into an element within this file.

-   **`package.json`**: This file is crucial for managing the project's dependencies and defining npm scripts (e.g., `npm run dev`, `npm run build`).

-   **`package-lock.json`**: An automatically generated file that records the exact version of every installed dependency, ensuring consistent installations across different environments.

-   **`vite.config.js`**: The configuration file for Vite, the build tool used for the frontend. It allows you to customize the development server, build process, and more.
