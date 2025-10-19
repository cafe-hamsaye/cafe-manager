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
  const requiresAdmin = to.matched.some(record => record.meta.requiresAdmin);
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const requiresStaff = to.matched.some(record => record.meta.requiresStaff);

  const adminToken = localStorage.getItem(AUTH_TOKEN_KEYS.ADMIN);
  const userToken = localStorage.getItem(AUTH_TOKEN_KEYS.USER);
  const userData = JSON.parse(localStorage.getItem(AUTH_TOKEN_KEYS.USER_DATA));

  if (requiresAdmin && !adminToken) {
    // Redirect to admin login if not authenticated as admin
    next({ name: 'AdminLogin' });
  } else if (requiresAuth && !userToken) {
    // Redirect to user login if not authenticated as user
    next({ name: 'Auth' });
  } else if (requiresStaff && (!userData || !userData.is_cafe_staff)) {
    // Redirect to dashboard if user is not a staff member
    next({ name: 'Dashboard' });
  } else {
    // Otherwise, allow navigation
    next();
  }
});

export default router;
