<template>
  <div class="bg-surface rounded-2xl border border-border-subtle shadow-xl overflow-hidden">
    <!-- Header and Table -->
    <div class="px-6 py-4 border-b border-border-subtle flex justify-between items-center">
      <h2 class="text-lg font-semibold text-heading">مدیریت منو</h2>
      <button @click="openAddItemModal" class="px-4 py-2 bg-action text-white rounded-lg hover:bg-action-hover transition-colors">افزودن آیتم جدید</button>
    </div>
    <div v-if="isLoading" class="p-6 text-center text-body">در حال بارگذاری...</div>
    <div v-else-if="error" class="p-6 text-center text-red-500">{{ error }}</div>
    <div v-else class="overflow-x-auto">
      <table class="min-w-full text-sm text-right">
        <thead class="bg-input-bg">
          <tr>
            <th class="px-6 py-3 font-medium text-heading">تصویر</th>
            <th class="px-6 py-3 font-medium text-heading">نام</th>
            <th class="px-6 py-3 font-medium text-heading">توضیحات</th>
            <th class="px-6 py-3 font-medium text-heading">قیمت</th>
            <th class="px-6 py-3 font-medium text-heading">عملیات</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-border-subtle">
          <tr v-if="menuItems.length === 0">
            <td colspan="4" class="px-6 py-10 text-center text-body">هیچ آیتمی در منو یافت نشد.</td>
          </tr>
          <tr v-for="item in menuItems" :key="item.id">
            <td class="px-6 py-4"><img :src="item.image" class="w-16 h-16 object-cover rounded-md"/></td>
            <td class="px-6 py-4 text-body">{{ item.name }}</td>
            <td class="px-6 py-4 text-body whitespace-pre-wrap">{{ item.description }}</td>
            <td class="px-6 py-4 text-body">{{ item.price }}</td>
            <td class="px-6 py-4">
              <button @click="openEditItemModal(item)" class="text-blue-500 hover:text-blue-700 transition-colors font-medium ml-4">ویرایش</button>
              <button @click="openConfirmDeleteModal(item)" class="text-red-500 hover:text-red-700 transition-colors font-medium">حذف</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modals (pre-warmed) -->
    <template v-if="areModalsMounted">
      <menu-item-modal v-model="showMenuItemModal" :is-edit="isEdit" :item="selectedItem" @submit="handleMenuItemSubmit" />
      <confirmation-modal v-model="showConfirmDeleteModal" title="تایید حذف" message="آیا از حذف این آیتم اطمینان دارید؟" @confirm="deleteMenuItem" />
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import { useToast } from 'vue-toastification';
import { MENU_API } from '@/config/api';
import authFetch from '@/utils/authFetch';
import MenuItemModal from './MenuItemModal.vue';
import ConfirmationModal from '../layout/ConfirmationModal.vue';

const menuItems = ref([]);
const isLoading = ref(true);
const error = ref(null);
const toast = useToast();

const showMenuItemModal = ref(false);
const showConfirmDeleteModal = ref(false);
const isEdit = ref(false);
const selectedItem = ref({});
const areModalsMounted = ref(false); // Controls mounting

const fetchMenuItems = async () => {
  isLoading.value = true;
  error.value = null;
  try {
    const response = await authFetch(MENU_API.LIST);
    if (!response.ok) {
      throw new Error('دریافت لیست آیتم‌های منو با خطا مواجه شد.');
    }
    menuItems.value = await response.json();
  } catch (err) {
    error.value = err.message;
    toast.error(err.message);
  } finally {
    isLoading.value = false;
  }
};

const openAddItemModal = async () => {
  isEdit.value = false;
  selectedItem.value = {};
  await nextTick();
  showMenuItemModal.value = true;
};

const openEditItemModal = async (item) => {
  isEdit.value = true;
  selectedItem.value = { ...item };
  await nextTick();
  showMenuItemModal.value = true;
};

const openConfirmDeleteModal = (item) => {
  selectedItem.value = item;
  showConfirmDeleteModal.value = true;
};

const handleMenuItemSubmit = async (formData) => {
  const itemId = formData.get('id'); // FormData doesn't have item.id directly
  const url = isEdit.value ? MENU_API.UPDATE(itemId) : MENU_API.CREATE;
  const method = isEdit.value ? 'PUT' : 'POST';

  try {
    const response = await authFetch(url, {
      method,
      body: formData, // No Content-Type header needed, browser sets it for FormData
    });
    const data = await response.json();
    if (!response.ok) {
      const errorMessages = Object.values(data).flat().join('\n');
      throw new Error(errorMessages || 'ذخیره آیتم منو با خطا مواجه شد.');
    }
    toast.success(data.message);
    fetchMenuItems();
  } catch (err) {
    toast.error(err.message);
  }
};

const deleteMenuItem = async () => {
  try {
    const response = await authFetch(MENU_API.DELETE(selectedItem.value.id), {
      method: 'DELETE',
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || 'حذف آیتم منو با خطا مواجه شد.');
    }
    toast.success(data.message);
    fetchMenuItems();
  } catch (err) {
    toast.error(err.message);
  }
};

onMounted(() => {
  fetchMenuItems();
  areModalsMounted.value = true; // Pre-warm modals
});
</script>
