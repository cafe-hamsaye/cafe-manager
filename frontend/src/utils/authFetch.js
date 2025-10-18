import { AUTH_API } from '@/config/api';

const getAdminToken = () => {
  const tokenString = localStorage.getItem('admin_token');
  return tokenString ? JSON.parse(tokenString) : null;
};

const setAdminToken = (tokens) => {
  localStorage.setItem('admin_token', JSON.stringify(tokens));
};

const logoutAdmin = () => {
  localStorage.removeItem('admin_token');
  window.location.href = '/admin'; // Redirect to admin login
};

let isRefreshing = false;
let failedQueue = [];

const processQueue = (error, token = null) => {
  failedQueue.forEach(prom => {
    if (error) {
      prom.reject(error);
    } else {
      prom.resolve(token);
    }
  });
  failedQueue = [];
};

const authFetch = async (url, options = {}) => {
  let token = getAdminToken();
  if (token) {
    options.headers = {
      ...options.headers,
      'Authorization': `Bearer ${token.access}`,
    };
  }

  let response = await fetch(url, options);

  if (response.status === 401) {
    if (isRefreshing) {
      return new Promise((resolve, reject) => {
        failedQueue.push({ resolve, reject });
      })
      .then(newAccessToken => {
        options.headers['Authorization'] = `Bearer ${newAccessToken}`;
        return fetch(url, options);
      });
    }

    isRefreshing = true;
    const refreshToken = token?.refresh;
    if (!refreshToken) {
      logoutAdmin();
      return Promise.reject(new Error('Session expired. Please log in again.'));
    }

    try {
      const refreshResponse = await fetch(AUTH_API.TOKEN_REFRESH, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refresh: refreshToken }),
      });

      if (!refreshResponse.ok) {
        throw new Error('Failed to refresh token.');
      }

      const newTokens = await refreshResponse.json();
      setAdminToken({ access: newTokens.access, refresh: refreshToken }); // Keep the old refresh token if not rotated
      processQueue(null, newTokens.access);
      
      // Retry the original request
      options.headers['Authorization'] = `Bearer ${newTokens.access}`;
      response = await fetch(url, options);

    } catch (e) {
      processQueue(e, null);
      logoutAdmin();
      return Promise.reject(e);
    } finally {
      isRefreshing = false;
    }
  }

  return response;
};

export default authFetch;
