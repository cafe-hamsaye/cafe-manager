<template>
  <div class="bg-surface rounded-2xl border border-border-subtle shadow-xl overflow-hidden">
    <div class="px-6 py-4 border-b border-border-subtle">
      <h2 class="text-lg font-semibold text-heading">لیست کاربران</h2>
    </div>
    <div v-if="isLoading" class="p-6 text-center text-body">در حال بارگذاری...</div>
    <div v-else-if="error" class="p-6 text-center text-red-500">{{ error }}</div>
    <div v-else class="overflow-x-auto">
      <table class="min-w-full text-sm text-right">
        <thead class="bg-input-bg">
          <tr>
            <th class="px-6 py-3 font-medium text-heading">نام</th>
            <th class="px-6 py-3 font-medium text-heading">نام خانوادگی</th>
            <th class="px-6 py-3 font-medium text-heading">شماره تلفن</th>
            <th class="px-6 py-3 font-medium text-heading">عملیات</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-border-subtle">
          <tr v-if="users.length === 0">
            <td colspan="4" class="px-6 py-10 text-center text-body">هیچ کاربری یافت نشد.</td>
          </tr>
          <tr v-for="user in users" :key="user.id">
            <td class="px-6 py-4 text-body">{{ user.first_name }}</td>
            <td class="px-6 py-4 text-body">{{ user.last_name }}</td>
            <td class="px-6 py-4 text-body" style="direction: ltr; text-align: right;">{{ user.phone_number }}</td>
            <td class="px-6 py-4">
              <button @click="confirmDeleteUser(user)" class="text-red-500 hover:text-red-700 transition-colors font-medium">
                حذف
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { USERS_API } from '@/config/api';
import { useToast } from 'vue-toastification';

const users = ref([]);
const isLoading = ref(true);
const error = ref(null);
const toast = useToast();

// Helper to get the token from localStorage
const getAuthToken = () => {
  // Assuming the admin token is stored here after login
  const tokenData = JSON.parse(localStorage.getItem('admin_token'));
  return tokenData ? tokenData.access : null;
};

const fetchUsers = async () => {
  isLoading.value = true;
  error.value = null;
  try {
    const token = getAuthToken();
    if (!token) {
      throw new Error('Authentication token not found.');
    }

    const response = await fetch(USERS_API.LIST, {
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Failed to fetch users.');
    }

    users.value = await response.json();

  } catch (err) {
    error.value = err.message;
    toast.error(err.message);
  } finally {
    isLoading.value = false;
  }
};

const confirmDeleteUser = (user) => {
  if (window.confirm(`آیا از حذف کاربر "${user.first_name} ${user.last_name}" اطمینان دارید؟`)) {
    deleteUser(user.id);
  }
};

const deleteUser = async (userId) => {
  try {
    const token = getAuthToken();
    if (!token) {
      throw new Error('Authentication token not found.');
    }

    const response = await fetch(USERS_API.DELETE(userId), {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    });

    if (!response.ok && response.status !== 204) { // 204 No Content is a success status
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Failed to delete user.');
    }

    toast.success('کاربر با موفقیت حذف شد.');
    // Refresh the user list
    fetchUsers();

  } catch (err) {
    toast.error(err.message);
  }
};

onMounted(() => {
  fetchUsers();
});
</script>