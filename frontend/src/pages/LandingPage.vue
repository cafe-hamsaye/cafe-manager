<template>
  <div class="text-center py-20 px-4">
    <!-- Main Content -->
    <div v-if="!uiState.showMenuOnLanding">
      <h1 class="text-4xl font-bold text-heading mb-4">به کافه ما خوش آمدید</h1>
      <p class="text-lg text-body mb-8">بهترین قهوه و شیرینی در شهر</p>
      <router-link to="/auth" class="bg-action text-white px-8 py-3 rounded-full text-lg font-medium hover:bg-action-hover transition-colors">
        شروع کنید
      </router-link>
    </div>

    <!-- Menu View -->
    <div v-else>
      <div class="flex justify-between items-center mb-8">
        <h2 class="text-3xl font-bold text-heading">منوی ما</h2>
        <button @click="uiState.showMenuOnLanding = false" class="inline-flex items-center space-x-2 space-x-reverse text-body hover:text-heading transition-colors duration-300">
          <span>بازگشت</span>
          <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
        </button>
      </div>
      <Menu />
    </div>
  </div>
</template>

<script setup>
import { uiState } from '@/store/ui';
import Menu from '@/components/Menu.vue';
</script>
