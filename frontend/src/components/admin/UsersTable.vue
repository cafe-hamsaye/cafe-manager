<template>
  <div class="bg-surface rounded-2xl border border-border-subtle shadow-xl overflow-hidden">
    <div class="px-6 py-4 border-b border-border-subtle">
      <h2 class="text-lg font-semibold text-heading">لیست کاربران</h2>
    </div>
    <div v-if="isLoading" class="overflow-x-auto">
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
          <tr v-for="n in 5" :key="n">
            <td class="px-6 py-4"><Skeletor width="100%" /></td>
            <td class="px-6 py-4"><Skeletor width="100%" /></td>
            <td class="px-6 py-4"><Skeletor width="100%" /></td>
            <td class="px-6 py-4"><Skeletor width="100%" /></td>
          </tr>
        </tbody>
      </table>
    </div>
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
            <td colspan="5" class="px-6 py-10 text-center text-body">هیچ کاربری یافت نشد.</td>
          </tr>
          <tr v-for="user in users" :key="user.id">
            <td class="px-6 py-4 text-body">{{ user.first_name }}</td>
            <td class="px-6 py-4 text-body">{{ user.last_name }}</td>
            <td class="px-6 py-4 text-body" style="direction: ltr; text-align: right;">{{ user.phone_number }}</td>
            <td class="px-6 py-4 space-x-4 space-x-reverse">
              <button @click="openConfirmDeleteModal(user)" class="text-red-500 hover:text-red-700 transition-colors font-medium">
                حذف
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- Confirmation Modal -->
    <confirmation-modal 
      v-if="showConfirmDeleteModal"
      v-model="showConfirmDeleteModal" 
      title="تایید حذف کاربر" 
      :message="`آیا از حذف کاربر '${userToDelete.first_name} ${userToDelete.last_name}' اطمینان دارید؟`"
      @confirm="deleteUser" 
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { USERS_API } from '@/config/api';
import { useToast } from 'vue-toastification';
import authFetch from '@/utils/authFetch';
import ConfirmationModal from '@/components/layout/ConfirmationModal.vue';

const users = ref([]);
const isLoading = ref(true);
const error = ref(null);
const toast = useToast();

// State for the confirmation modal
const showConfirmDeleteModal = ref(false);
const userToDelete = ref(null);

const fetchUsers = async () => {
  isLoading.value = true;
  error.value = null;
  try {
    const response = await authFetch(USERS_API.LIST);
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'دریافت لیست کاربران با خطا مواجه شد.');
    }
    users.value = await response.json();
  } catch (err) {
    console.error('fetchUsers error:', err);
    error.value = err.message;
    toast.error(err.message);
  } finally {
    isLoading.value = false;
  }
};



const openConfirmDeleteModal = (user) => {
  userToDelete.value = user;
  showConfirmDeleteModal.value = true;
};

const deleteUser = async () => {
  if (!userToDelete.value) return;
  try {
    const response = await authFetch(USERS_API.DELETE(userToDelete.value.id), {
      method: 'DELETE',
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || 'حذف کاربر با خطا مواجه شد.');
    }
    toast.success(data.message);
    fetchUsers(); // Refresh the list
  } catch (err) {
    console.error('deleteUser error:', err);
    toast.error(err.message);
  } finally {
    userToDelete.value = null; // Reset
  }
};

onMounted(() => {
  fetchUsers();
});
</script>