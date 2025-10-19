<template>
  <div v-if="isLoading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    <div v-for="n in 6" :key="n" class="bg-surface rounded-2xl border border-border-subtle shadow-xl overflow-hidden">
      <Skeletor height="192px" />
      <div class="p-6">
        <Skeletor width="60%" height="28px" class="mb-2" />
        <Skeletor width="100%" height="40px" class="mb-4" />
        <div class="flex justify-between items-center">
          <Skeletor width="30%" height="24px" />
        </div>
      </div>
    </div>
  </div>
  <div v-else-if="error" class="p-6 text-center text-red-500">{{ error }}</div>
  <div v-else-if="menuItems.length === 0" class="p-6 text-center text-body">هیچ آیتمی در منو یافت نشد.</div>
  <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    <div v-for="item in menuItems" :key="item.id" class="bg-surface rounded-2xl border border-border-subtle shadow-xl overflow-hidden">
      <img :src="item.image" :alt="item.name" class="w-full h-48 object-cover">
      <div class="p-6">
        <h3 class="text-lg font-semibold text-heading mb-2">{{ item.name }}</h3>
        <p class="text-body text-sm mb-4 whitespace-pre-wrap">{{ item.description }}</p>
        <div class="flex justify-between items-center">
          <span class="text-action font-bold">{{ item.price }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useToast } from 'vue-toastification';
import { MENU_API } from '@/config/api';

const menuItems = ref([]);
const isLoading = ref(true);
const error = ref(null);
const toast = useToast();

const fetchMenuItems = async () => {
  isLoading.value = true;
  error.value = null;
  try {
    const response = await fetch(MENU_API.LIST);
    if (!response.ok) {
      throw new Error('Failed to fetch menu items.');
    }
    menuItems.value = await response.json();
  } catch (err) {
    error.value = err.message;
    toast.error(err.message);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchMenuItems();
});
</script>
