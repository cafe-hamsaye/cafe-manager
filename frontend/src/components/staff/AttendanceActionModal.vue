<template>
  <BaseModal :model-value="modelValue" @update:model-value="(val) => emit('update:modelValue', val)" title="ثبت تردد">
    <div class="p-4 text-center">
      <p class="text-body mb-8 text-lg">لطفا نوع تردد خود را انتخاب کنید:</p>
      <div class="grid grid-cols-2 gap-4">
        <button @click="emit('confirm', 'in')" class="w-full p-4 rounded-lg bg-green-500 text-white text-xl font-bold hover:bg-green-600 transition-colors flex items-center justify-center space-x-2 space-x-reverse">
          <span>ورود</span>
          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" /></svg>
        </button>
        <button @click="emit('confirm', 'out')" class="w-full p-4 rounded-lg bg-red-500 text-white text-xl font-bold hover:bg-red-600 transition-colors flex items-center justify-center space-x-2 space-x-reverse">
          <span>خروج</span>
          <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" /></svg>
        </button>
      </div>
    </div>
  </BaseModal>
</template>

<script setup>
import BaseModal from '@/components/layout/BaseModal.vue';

defineProps({ modelValue: Boolean });
const emit = defineEmits(['update:modelValue', 'confirm']);
</script>
