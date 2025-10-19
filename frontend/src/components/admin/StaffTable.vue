<template>
  <div class="bg-surface rounded-2xl border border-border-subtle shadow-xl overflow-hidden">
    <div class="px-6 py-4 border-b border-border-subtle flex justify-between items-center">
      <h2 class="text-lg font-semibold text-heading">مدیریت کارکنان</h2>
      <button @click="openModal()" class="px-4 py-2 bg-action text-white rounded-lg hover:bg-action-hover transition-colors">افزودن کارمند</button>
    </div>
    <div v-if="isLoading" class="p-6 text-center text-body">در حال بارگذاری...</div>
    <div v-else-if="error" class="p-6 text-center text-red-500">{{ error }}</div>
    <div v-else class="overflow-x-auto">
      <table class="min-w-full text-sm text-right">
        <thead class="bg-input-bg">
          <tr>
            <th class="px-6 py-3 font-medium text-heading">شماره</th>
            <th class="px-6 py-3 font-medium text-heading">آخرین ورود</th>
            <th class="px-6 py-3 font-medium text-heading">عملیات</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-border-subtle">
          <tr v-for="staff in staffList" :key="staff.id">
            <td class="px-6 py-4 text-body">{{ staff.number }}</td>
            <td class="px-6 py-4 text-body">{{ staff.last_login ? new Date(staff.last_login).toLocaleString('fa-IR') : '-' }}</td>
            <td class="px-6 py-4 space-x-4 space-x-reverse">
              <button @click="openModal(staff)" class="text-blue-500 hover:text-blue-700">ویرایش</button>
              <button @click="confirmDelete(staff)" class="text-red-500 hover:text-red-700">حذف</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <StaffModal v-if="isModalOpen" :staff="selectedStaff" @close="closeModal" @save="fetchStaff" />
    <ConfirmationModal v-if="showConfirmDelete" v-model="showConfirmDelete" title="تایید حذف" message="آیا از حذف این کارمند اطمینان دارید؟" @confirm="deleteStaff" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useToast } from 'vue-toastification';
import StaffModal from './StaffModal.vue';
import ConfirmationModal from '@/components/layout/ConfirmationModal.vue';

const staffList = ref([]);
const isLoading = ref(true);
const error = ref(null);
const isModalOpen = ref(false);
const selectedStaff = ref(null);
const showConfirmDelete = ref(false);
const staffToDelete = ref(null);
const toast = useToast();

const fetchStaff = async () => {
  isLoading.value = true;
  try {
    const response = await axios.get('/api/staff/', { headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('admin_token')).access}` } });
    staffList.value = response.data;
  } catch (err) {
    error.value = 'Failed to fetch staff';
    toast.error(error.value);
  } finally {
    isLoading.value = false;
  }
};

const openModal = (staff = null) => {
  selectedStaff.value = staff;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
  selectedStaff.value = null;
};

const confirmDelete = (staff) => {
  staffToDelete.value = staff;
  showConfirmDelete.value = true;
};

const deleteStaff = async () => {
  try {
    await axios.delete(`/api/staff/${staffToDelete.value.id}/`, { headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('admin_token')).access}` } });
    toast.success('کارمند با موفقیت حذف شد');
    fetchStaff();
  } catch (err) {
    toast.error('حذف کارمند با خطا مواجه شد');
  }
};

onMounted(fetchStaff);
</script>
