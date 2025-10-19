<template>
  <BaseModal :model-value="modelValue" @update:model-value="(val) => emit('update:modelValue', val)" :title="title">
    <p class="text-body mb-8">{{ message }}</p>
    <div class="flex justify-end space-x-4 space-x-reverse">
      <button @click="emit('update:modelValue', false)" class="px-6 py-2.5 rounded-lg bg-gray-200 text-gray-800 hover:bg-gray-300 transition-colors">
        انصراف
      </button>
      <button @click="handleConfirm" class="px-6 py-2.5 rounded-lg bg-red-600 text-white hover:bg-red-700 transition-colors">
        تایید و حذف
      </button>
    </div>
  </BaseModal>
</template>

<script setup>
import BaseModal from './BaseModal.vue';

const props = defineProps({
  modelValue: { type: Boolean, default: false },
  title: { type: String, required: true },
  message: { type: String, required: true },
});

const emit = defineEmits(['update:modelValue', 'confirm']);

const handleConfirm = () => {
  emit('confirm');
  emit('update:modelValue', false);
};
</script>