<template>
  <div class="bg-surface rounded-2xl border border-border-subtle shadow-xl overflow-hidden">
    <div class="px-6 py-4 border-b border-border-subtle flex justify-between items-center">
      <h2 class="text-lg font-semibold text-heading">مدیریت منو</h2>
      <button @click="openAddItemModal" class="px-4 py-2 bg-action text-white rounded-lg hover:bg-action-hover transition-colors">افزودن آیتم جدید</button>
    </div>

    <div class="overflow-x-auto">
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
          <!-- Loading State -->
          <template v-if="isLoading">
            <tr v-for="n in 5" :key="`skel-${n}`">
              <td class="px-6 py-4"><Skeletor circle size="64" /></td>
              <td class="px-6 py-4"><Skeletor width="100%" /></td>
              <td class="px-6 py-4"><Skeletor width="100%" /></td>
              <td class="px-6 py-4"><Skeletor width="100%" /></td>
              <td class="px-6 py-4"><Skeletor width="100%" /></td>
            </tr>
          </template>

          <!-- Error State -->
          <template v-else-if="error">
            <tr>
              <td colspan="5" class="px-6 py-10 text-center text-red-500">{{ error }}</td>
            </tr>
          </template>

          <!-- Empty State -->
          <template v-else-if="menuItems.length === 0">
            <tr>
              <td colspan="5" class="px-6 py-10 text-center text-body">هیچ آیتمی در منو یافت نشد.</td>
            </tr>
          </template>

          <!-- Data Rows -->
          <template v-else>
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
          </template>
        </tbody>
      </table>
    </div>

    <!-- Modals -->
    <template v-if="areModalsMounted">
      <menu-item-modal v-model="showMenuItemModal" :is-edit="isEdit" :item="selectedItem" @submit="handleMenuItemSubmit" />
      <confirmation-modal v-model="showConfirmDeleteModal" title="تایید حذف" :message="`آیا از حذف آیتم '${selectedItem?.name}' اطمینان دارید؟`" @confirm="deleteMenuItem" />
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import axios from 'axios';
import { useToast } from 'vue-toastification';
import { MENU_API } from '@/config/api';
import MenuItemModal from './MenuItemModal.vue';
import ConfirmationModal from '@/components/layout/ConfirmationModal.vue';

const menuItems = ref([]);
const isLoading = ref(true);
const error = ref(null);
const toast = useToast();

const showMenuItemModal = ref(false);
const showConfirmDeleteModal = ref(false);
const isEdit = ref(false);
const selectedItem = ref(null);
const areModalsMounted = ref(false);

const getAuthHeaders = () => {
  const token = JSON.parse(localStorage.getItem('admin_token'))?.access;
  return { Authorization: `Bearer ${token}` };
};

const fetchMenuItems = async () => {
  isLoading.value = true;
  error.value = null;
  try {
    const response = await axios.get(MENU_API.LIST);
    menuItems.value = response.data;
  } catch (err) {
    error.value = 'دریافت لیست آیتم‌های منو با خطا مواجه شد.';
    toast.error(error.value);
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
  const itemId = formData.get('id');
  const url = isEdit.value ? MENU_API.UPDATE(itemId) : MENU_API.CREATE;
  const method = isEdit.value ? 'patch' : 'post';

  try {
    const response = await axios({
      method,
      url,
      data: formData,
      headers: {
        ...getAuthHeaders(),
        'Content-Type': 'multipart/form-data',
      },
    });
    toast.success(response.data.message);
    fetchMenuItems();
  } catch (err) {
    const errorMessages = Object.values(err.response.data).flat().join('\n');
    toast.error(errorMessages || 'ذخیره آیتم منو با خطا مواجه شد.');
  }
};

const deleteMenuItem = async () => {
  try {
    const response = await axios.delete(MENU_API.DELETE(selectedItem.value.id), { headers: getAuthHeaders() });
    toast.success(response.data.message);
    fetchMenuItems();
  } catch (err) {
    toast.error('حذف آیتم منو با خطا مواجه شد.');
  } finally {
    showConfirmDeleteModal.value = false;
    selectedItem.value = null;
  }
};

onMounted(() => {
  fetchMenuItems();
  areModalsMounted.value = true;
});
</script>
