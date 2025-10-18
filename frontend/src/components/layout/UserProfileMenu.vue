<template>
  <div class="relative">
    <button @click="toggleMenu" class="flex items-center space-x-2 focus:outline-none">
      <span class="text-sm font-medium text-heading">پروفایل</span>
      <svg class="h-5 w-5 text-body" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </button>

    <transition
      enter-active-class="transition ease-out duration-100"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <div v-if="isMenuOpen" class="absolute left-0 mt-2 w-48 bg-surface rounded-lg shadow-lg border border-border-subtle z-50">
        <div class="py-1">
          <button @click="logout" class="w-full text-right px-4 py-2 text-sm text-body hover:bg-input-bg">
            خروج از سیستم
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const isMenuOpen = ref(false);
const router = useRouter();

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const logout = () => {
  // Remove both user and admin tokens to ensure a clean logout
  localStorage.removeItem('user_token');
  localStorage.removeItem('admin_token');

  console.log('User logged out');
  isMenuOpen.value = false;
  router.push('/');
};
</script>
