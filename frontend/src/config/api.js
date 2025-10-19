export const API_BASE_URL = 'https://stunning-memory-r4694jwj7gjpfprj7-8000.app.github.dev/api';

export const AUTH_API = {
  REGISTER: `${API_BASE_URL}/auth/register/`,
  LOGIN: `${API_BASE_URL}/auth/login/`,
  ADMIN_LOGIN: `${API_BASE_URL}/auth/admin/login/`,
  TOKEN_REFRESH: `${API_BASE_URL}/auth/token/refresh/`,
  GET_USER: `${API_BASE_URL}/auth/user/`,
};

export const USERS_API = {
  LIST: `${API_BASE_URL}/auth/users/`,
  UPDATE: (userId) => `${API_BASE_URL}/auth/users/${userId}/`,
  DELETE: (userId) => `${API_BASE_URL}/auth/users/${userId}/`,
};

export const MENU_API = {
  LIST: `${API_BASE_URL}/menu/`,
  CREATE: `${API_BASE_URL}/menu/`,
  UPDATE: (itemId) => `${API_BASE_URL}/menu/${itemId}/`,
  DELETE: (itemId) => `${API_BASE_URL}/menu/${itemId}/`,
};

export const STAFF_API = {
  LIST: `${API_BASE_URL}/staff/`,
  CREATE: `${API_BASE_URL}/staff/`,
  UPDATE: (staffId) => `${API_BASE_URL}/staff/${staffId}/`,
  DELETE: (staffId) => `${API_BASE_URL}/staff/${staffId}/`,
  LOGIN: `${API_BASE_URL}/staff/login/`,
  ME: `${API_BASE_URL}/staff/me/`,
};

export const ATTENDANCE_API = {
  QR_CODE: `${API_BASE_URL}/attendance/qr-code/`,
  RECORD: `${API_BASE_URL}/attendance/record/`,
};

export const ATTENDANCE_API = {
  QR_CODE: `${API_BASE_URL}/attendance/qr-code/`,
  RECORD: `${API_BASE_URL}/attendance/record/`,
};

