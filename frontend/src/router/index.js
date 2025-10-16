import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '../pages/LandingPage.vue';
import AuthPage from '../pages/AuthPage.vue';
import DashboardPage from '../pages/DashboardPage.vue';
import AdminLoginPage from '../pages/AdminLoginPage.vue';
import AdminDashboardPage from '../pages/AdminDashboardPage.vue';
import ManageUsersPage from '../pages/ManageUsersPage.vue';

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: LandingPage,
  },
  {
    path: '/auth',
    name: 'Auth',
    component: AuthPage,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardPage,
    // meta: { requiresAuth: true } // Example for protected route
  },
  {
    path: '/admin',
    name: 'AdminLogin',
    component: AdminLoginPage,
  },
  {
    path: '/admin-panel',
    name: 'AdminDashboard',
    component: AdminDashboardPage,
    // meta: { requiresAdmin: true } // Example for protected route
  },
  {
    path: '/admin-panel/users',
    name: 'ManageUsers',
    component: ManageUsersPage,
    // meta: { requiresAdmin: true } // Example for protected route
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
