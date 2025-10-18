const API_BASE_URL = 'http://localhost:8000/api';

export const AUTH_API = {
  REGISTER: `${API_BASE_URL}/auth/register/`,
  LOGIN: `${API_BASE_URL}/auth/login/`,
  ADMIN_LOGIN: `${API_BASE_URL}/auth/admin/login/`,
  TOKEN_REFRESH: `${API_BASE_URL}/auth/token/refresh/`,
  GET_USER: `${API_BASE_URL}/auth/user`,
};

export const USERS_API = {
  LIST: `${API_BASE_URL}/auth/users/`,
  DELETE: (userId) => `${API_BASE_URL}/auth/users/${userId}/`,
};

export const MENU_API = {
  LIST: `${API_BASE_URL}/menu/`,
  CREATE: `${API_BASE_URL}/menu/`,
  UPDATE: (itemId) => `${API_BASE_URL}/menu/${itemId}/`,
  DELETE: (itemId) => `${API_BASE_URL}/menu/${itemId}/`,
};
