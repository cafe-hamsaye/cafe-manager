<template>
  <base-modal :model-value="modelValue" @update:model-value="(val) => emit('update:modelValue', val)" :title="title">
    <p class="text-body mb-6">{{ message }}</p>
    <div class="flex justify-end space-x-4 space-x-reverse">
      <button @click="confirm" class="px-4 py-2 bg-action text-white rounded-lg hover:bg-action-hover transition-colors">{{ confirmText }}</button>
      <button @click="cancel" class="px-4 py-2 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition-colors">{{ cancelText }}</button>
    </div>
  </base-modal>
</template>

<script setup>
import BaseModal from './BaseModal.vue';

const props = defineProps({
  modelValue: { type: Boolean, default: false },
  title: { type: String, default: 'تایید' },
  message: { type: String, default: 'آیا مطمئن هستید؟' },
  confirmText: { type: String, default: 'بله' },
  cancelText: { type: String, default: 'خیر' },
});

const emit = defineEmits(['update:modelValue', 'confirm', 'cancel']);

const confirm = () => {
  emit('confirm');
  emit('update:modelValue', false);
};

const cancel = () => {
  emit('cancel');
  emit('update:modelValue', false);
};
</script>
