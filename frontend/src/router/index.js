import { createRouter, createWebHistory } from 'vue-router';
import { AUTH_TOKEN_KEYS } from '@/config/constants';
import LandingPage from '@/pages/LandingPage.vue';
import AuthPage from '@/pages/AuthPage.vue';
import DashboardPage from '@/pages/DashboardPage.vue';
import AdminLoginPage from '@/pages/AdminLoginPage.vue';
import AdminDashboardPage from '@/pages/AdminDashboardPage.vue';


import NotFoundPage from '@/pages/NotFoundPage.vue';

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
    meta: { requiresAuth: true } // For all authenticated users
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
    meta: { requiresAdmin: true }
  },
  {
    path: '/admin-panel/attendance',
    name: 'AttendanceQRCode',
    component: () => import('@/pages/AttendanceQRCodePage.vue'),
    meta: { requiresAdmin: true }
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
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const requiresAdmin = to.matched.some(record => record.meta.requiresAdmin);

  const userToken = localStorage.getItem(AUTH_TOKEN_KEYS.USER);
  const adminToken = localStorage.getItem(AUTH_TOKEN_KEYS.ADMIN);

  if (requiresAdmin && !adminToken) {
    return next({ name: 'AdminLogin' });
  }

  if (requiresAuth && !userToken) {
    return next({ name: 'Auth' });
  }

  next();
});

export default router;
