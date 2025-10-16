const API_BASE_URL = 'http://localhost:8000/api';

export const AUTH_API = {
  REGISTER: `${API_BASE_URL}/auth/register/`,
  LOGIN: `${API_BASE_URL}/auth/login/`,
  ADMIN_LOGIN: `${API_BASE_URL}/auth/admin/login/`,
  GET_USER: `${API_BASE_URL}/auth/user`,
};

export const USERS_API = {
  LIST: `${API_BASE_URL}/auth/users/`,
  DELETE: (userId) => `${API_BASE_URL}/auth/users/${userId}/`,
};

export const EXAM_API = {
  GET_ALL: `${API_BASE_URL}/exams`,
  GET_PURCHASED: `${API_BASE_URL}/exams/purchased`,
  PURCHASE: (examId) => `${API_BASE_URL}/exams/${examId}/purchase`,
};
