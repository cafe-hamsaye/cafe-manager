<template>
  <div class="bg-surface rounded-2xl border border-border-subtle shadow-xl overflow-hidden">
    <div class="px-6 py-4 border-b border-border-subtle flex justify-between items-center">
      <h2 class="text-lg font-semibold text-heading">مدیریت کارکنان</h2>
      <button @click="openModal()" class="px-4 py-2 bg-action text-white rounded-lg hover:bg-action-hover transition-colors">افزودن کارمند</button>
    </div>

    <div class="overflow-x-auto">
      <table class="min-w-full text-sm text-right">
        <thead class="bg-input-bg">
          <tr>
            <th class="px-6 py-3 font-medium text-heading">شماره</th>
            <th class="px-6 py-3 font-medium text-heading">آخرین ورود</th>
            <th class="px-6 py-3 font-medium text-heading">عملیات</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-border-subtle">
          <template v-if="isLoading">
            <tr v-for="n in 5" :key="`skel-${n}`">
              <td class="px-6 py-4"><Skeletor width="100%" /></td>
              <td class="px-6 py-4"><Skeletor width="100%" /></td>
              <td class="px-6 py-4"><Skeletor width="100%" /></td>
            </tr>
          </template>
          <template v-else-if="error">
            <tr>
              <td colspan="3" class="px-6 py-10 text-center text-red-500">{{ error }}</td>
            </tr>
          </template>
          <template v-else-if="staffList.length === 0">
            <tr>
              <td colspan="3" class="px-6 py-10 text-center text-body">هیچ کارمندی یافت نشد.</td>
            </tr>
          </template>
          <template v-else>
            <tr v-for="staff in staffList" :key="staff.id">
              <td class="px-6 py-4 text-body">{{ staff.number }}</td>
              <td class="px-6 py-4 text-body">{{ staff.last_login ? new Date(staff.last_login).toLocaleString('fa-IR') : '-' }}</td>
              <td class="px-6 py-4 space-x-4 space-x-reverse">
                <button @click="openModal(staff)" class="text-blue-500 hover:text-blue-700">ویرایش</button>
                <button @click="openConfirmDeleteModal(staff)" class="text-red-500 hover:text-red-700">حذف</button>
              </td>
            </tr>
          </template>
        </tbody>
      </table>
    </div>

    <template v-if="areModalsMounted">
      <StaffModal v-model="isModalOpen" :staff="selectedStaff" @save="handleSave" />
      <ConfirmationModal v-model="showConfirmDeleteModal" title="تایید حذف" :message="`آیا از حذف کارمند با شماره '${staffToDelete?.number}' اطمینان دارید؟`" @confirm="deleteStaff" />
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useToast } from 'vue-toastification';
import { STAFF_API } from '@/config/api';
import StaffModal from './StaffModal.vue';
import ConfirmationModal from '@/components/layout/ConfirmationModal.vue';

const staffList = ref([]);
const isLoading = ref(true);
const error = ref(null);
const isModalOpen = ref(false);
const selectedStaff = ref(null);
const showConfirmDeleteModal = ref(false);
const staffToDelete = ref(null);
const toast = useToast();
const areModalsMounted = ref(false);

const getAuthHeaders = () => {
  const token = JSON.parse(localStorage.getItem('admin_token'))?.access;
  if (!token) {
    toast.error("Admin token not found. Please log in again.");
    return {};
  }
  return { Authorization: `Bearer ${token}` };
};

const fetchStaff = async () => {
  isLoading.value = true;
  error.value = null;
  try {
    const response = await axios.get(STAFF_API.LIST, { headers: getAuthHeaders() });
    staffList.value = response.data;
  } catch (err) {
    error.value = 'Failed to fetch staff list.';
    toast.error(err.response?.data?.detail || error.value);
  } finally {
    isLoading.value = false;
  }
};

const openModal = (staff = null) => {
  console.log('Opening modal for:', staff);
  selectedStaff.value = staff;
  isModalOpen.value = true;
};

const handleSave = () => {
  isModalOpen.value = false;
  fetchStaff();
};

const openConfirmDeleteModal = (staff) => {
  staffToDelete.value = staff;
  showConfirmDeleteModal.value = true;
};

const deleteStaff = async () => {
  if (!staffToDelete.value) return;
  try {
    await axios.delete(STAFF_API.DELETE(staffToDelete.value.id), { headers: getAuthHeaders() });
    toast.success('Staff member deleted successfully.');
    fetchStaff(); // Refresh the list
  } catch (err) {
    toast.error(err.response?.data?.detail || 'Failed to delete staff member.');
  } finally {
    showConfirmDeleteModal.value = false;
    staffToDelete.value = null;
  }
};

onMounted(() => {
  fetchStaff();
  areModalsMounted.value = true;
});
</script>
