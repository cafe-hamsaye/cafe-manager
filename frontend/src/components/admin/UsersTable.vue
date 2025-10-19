<template>
  <div class="bg-surface rounded-2xl border border-border-subtle shadow-xl overflow-hidden">
    <div class="px-6 py-4 border-b border-border-subtle">
      <h2 class="text-lg font-semibold text-heading">لیست کاربران</h2>
    </div>

    <div class="overflow-x-auto">
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
          <!-- Loading State -->
          <template v-if="isLoading">
            <tr v-for="n in 5" :key="`skel-${n}`">
              <td class="px-6 py-4"><Skeletor width="100%" /></td>
              <td class="px-6 py-4"><Skeletor width="100%" /></td>
              <td class="px-6 py-4"><Skeletor width="100%" /></td>
              <td class="px-6 py-4"><Skeletor width="100%" /></td>
            </tr>
          </template>

          <!-- Error State -->
          <template v-else-if="error">
            <tr>
              <td colspan="4" class="px-6 py-10 text-center text-red-500">{{ error }}</td>
            </tr>
          </template>

          <!-- Empty State -->
          <template v-else-if="users.length === 0">
            <tr>
              <td colspan="4" class="px-6 py-10 text-center text-body">هیچ کاربری یافت نشد.</td>
            </tr>
          </template>

          <!-- Data Rows -->
          <template v-else>
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
          </template>
        </tbody>
      </table>
    </div>

    <!-- Confirmation Modal -->
    <template v-if="areModalsMounted">
      <confirmation-modal 
        v-model="showConfirmDeleteModal" 
        title="تایید حذف کاربر" 
        :message="`آیا از حذف کاربر '${userToDelete?.first_name} ${userToDelete?.last_name}' اطمینان دارید؟`"
        @confirm="deleteUser" 
      />
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useToast } from 'vue-toastification';
import { USERS_API } from '@/config/api';
import ConfirmationModal from '@/components/layout/ConfirmationModal.vue';

const users = ref([]);
const isLoading = ref(true);
const error = ref(null);
const toast = useToast();

const showConfirmDeleteModal = ref(false);
const userToDelete = ref(null);
const areModalsMounted = ref(false);

const getAuthHeaders = () => {
  const token = JSON.parse(localStorage.getItem('admin_token'))?.access;
  return { Authorization: `Bearer ${token}` };
};

const fetchUsers = async () => {
  isLoading.value = true;
  error.value = null;
  try {
    const response = await axios.get(USERS_API.LIST, { headers: getAuthHeaders() });
    users.value = response.data;
  } catch (err) {
    error.value = 'دریافت لیست کاربران با خطا مواجه شد.';
    toast.error(error.value);
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
    const response = await axios.delete(USERS_API.DELETE(userToDelete.value.id), { headers: getAuthHeaders() });
    toast.success(response.data.message);
    fetchUsers();
  } catch (err) {
    toast.error('حذف کاربر با خطا مواجه شد.');
  } finally {
    userToDelete.value = null;
    showConfirmDeleteModal.value = false;
  }
};

onMounted(() => {
  fetchUsers();
  areModalsMounted.value = true;
});
</script>