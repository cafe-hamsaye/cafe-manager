<template>
  <header class="bg-surface/80 backdrop-blur-lg sticky top-0 z-50 border-b border-border-subtle">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-20">
        <!-- Right Section: Title & Menu -->
        <div class="flex items-center space-x-8 space-x-reverse">
          <router-link to="/dashboard" class="text-xl font-bold text-heading">
            داشبورد کاربر
          </router-link>
          <div class="border-l border-border-subtle h-6"></div>
          <router-link to="/dashboard?view=menu" class="text-sm font-medium text-body hover:text-heading transition-colors">
            منو
          </router-link>
          <button v-if="isStaff" @click="showScannerModal = true" class="text-sm font-medium text-body hover:text-heading transition-colors">
            اسکن QR کد
          </button>
        </div>

        <!-- Left Section: Profile -->
        <div>
          <UserProfileMenu />
        </div>
      </div>
    </div>
    <QRCodeScannerModal :show="showScannerModal" @close="showScannerModal = false" />
  </header>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import UserProfileMenu from './UserProfileMenu.vue';
import QRCodeScannerModal from '@/components/attendance/QRCodeScannerModal.vue';
import { AUTH_TOKEN_KEYS } from '@/config/constants';

const isStaff = ref(false);
const showScannerModal = ref(false);

onMounted(() => {
  const userData = JSON.parse(localStorage.getItem(AUTH_TOKEN_KEYS.USER_DATA));
  if (userData && userData.is_cafe_staff) {
    isStaff.value = true;
  }
});
</script>
