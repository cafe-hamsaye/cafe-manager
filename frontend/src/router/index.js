import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '../pages/LandingPage.vue';
import AuthPage from '../pages/AuthPage.vue';
import DashboardPage from '../pages/DashboardPage.vue';
import AdminLoginPage from '../pages/AdminLoginPage.vue';
import AdminDashboardPage from '../pages/AdminDashboardPage.vue';
import ManageUsersPage from '../pages/ManageUsersPage.vue';
import ManageMenuPage from '../pages/ManageMenuPage.vue';
import MenuPage from '../pages/MenuPage.vue';
import NotFoundPage from '../pages/NotFoundPage.vue'; // Import the new 404 page

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
    meta: { requiresAuth: true } // Protected route for users
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
    meta: { requiresAdmin: true } // Protected route for admins
  },
  {
    path: '/admin-panel/users',
    name: 'ManageUsers',
    component: ManageUsersPage,
    meta: { requiresAdmin: true } // Protected route for admins
  },
  {
    path: '/admin-panel/menu',
    name: 'ManageMenu',
    component: ManageMenuPage,
    meta: { requiresAdmin: true } // Protected route for admins
  },
  {
    path: '/menu',
    name: 'Menu',
    component: MenuPage,
  },
  // Catch-all route must be last
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFoundPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation Guard
router.beforeEach((to, from, next) => {
  const requiresAdmin = to.matched.some(record => record.meta.requiresAdmin);
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  
  const adminToken = localStorage.getItem('admin_token');
  const userToken = localStorage.getItem('user_token');

  if (requiresAdmin && !adminToken) {
    // Redirect to admin login if not authenticated as admin
    next({ name: 'AdminLogin' });
  } else if (requiresAuth && !userToken) {
    // Redirect to user login if not authenticated as user
    next({ name: 'Auth' });
  } else {
    // Otherwise, allow navigation
    next();
  }
});

export default router;
