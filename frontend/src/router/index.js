import { createRouter, createWebHistory } from 'vue-router';
import { AUTH_TOKEN_KEYS } from '@/config/constants';

// Page Components
import LandingPage from '@/pages/LandingPage.vue';
import AuthPage from '@/pages/AuthPage.vue';
import DashboardPage from '@/pages/DashboardPage.vue';
import AdminLoginPage from '@/pages/AdminLoginPage.vue';
import AdminDashboardPage from '@/pages/AdminDashboardPage.vue';
import StaffLoginPage from '@/pages/StaffLoginPage.vue';
import StaffDashboardPage from '@/pages/StaffDashboardPage.vue';
import NotFoundPage from '@/pages/NotFoundPage.vue';

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: LandingPage,
  },
  // User Auth
  {
    path: '/auth',
    name: 'Auth',
    component: AuthPage,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardPage,
    meta: { requiresAuth: true, requiresUser: true }
  },
  // Staff Auth
  {
    path: '/staff',
    name: 'StaffLogin',
    component: StaffLoginPage,
  },
  {
    path: '/staff-panel',
    name: 'StaffDashboard',
    component: StaffDashboardPage,
    meta: { requiresAuth: true, requiresStaff: true }
  },
  // Admin Auth
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
  // 404 Not Found
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
  const requiresStaff = to.matched.some(record => record.meta.requiresStaff);
  const requiresUser = to.matched.some(record => record.meta.requiresUser);

  const adminToken = localStorage.getItem(AUTH_TOKEN_KEYS.ADMIN);
  const userToken = localStorage.getItem(AUTH_TOKEN_KEYS.USER);
  const staffToken = localStorage.getItem(AUTH_TOKEN_KEYS.STAFF);

  // Admin routes
  if (requiresAdmin && !adminToken) return next({ name: 'AdminLogin' });

  // General auth routes
  if (requiresAuth && !userToken && !staffToken && !adminToken) return next({ name: 'Auth' });

  // Role-specific routes
  if (requiresStaff && !staffToken) return next({ name: 'StaffLogin' });
  if (requiresUser && !userToken) return next({ name: 'Auth' });

  // Redirect logged-in users from login pages
  if (to.name === 'Auth' && userToken) return next('/dashboard');
  if (to.name === 'StaffLogin' && staffToken) return next('/staff-panel');
  if (to.name === 'AdminLogin' && adminToken) return next('/admin-panel');

  next();
});

export default router;