<template>
  <base-modal :model-value="modelValue" @update:model-value="(val) => emit('update:modelValue', val)" :title="isEdit ? 'ویرایش آیتم منو' : 'افزودن آیتم جدید'">
    <form @submit.prevent="handleSubmit" class="space-y-6">
      <!-- Form fields -->
      <div>
        <label for="name" class="block text-sm font-medium text-heading mb-2">نام</label>
        <input v-model="form.name" type="text" id="name" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg focus:border-action focus:ring-2 focus:ring-action/20 outline-none transition-all duration-300" required>
      </div>
      <div>
        <label for="description" class="block text-sm font-medium text-heading mb-2">توضیحات</label>
        <textarea v-model="form.description" id="description" rows="3" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg focus:border-action focus:ring-2 focus:ring-action/20 outline-none transition-all duration-300" required></textarea>
      </div>
      <div>
        <label for="price" class="block text-sm font-medium text-heading mb-2">قیمت</label>
        <input v-model="form.price" type="number" id="price" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg focus:border-action focus:ring-2 focus:ring-action/20 outline-none transition-all duration-300" required>
      </div>
      <div>
        <label for="image_url" class="block text-sm font-medium text-heading mb-2">آدرس تصویر</label>
        <input v-model="form.image_url" type="text" id="image_url" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg focus:border-action focus:ring-2 focus:ring-action/20 outline-none transition-all duration-300" required>
      </div>
      <div class="pt-4 flex justify-end">
        <button type="submit" class="w-full p-3 bg-action text-white rounded-lg hover:bg-action-hover transition-all duration-300 font-medium shadow-md hover:shadow-lg hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-action/50">
          {{ isEdit ? 'به‌روزرسانی' : 'ایجاد' }}
        </button>
      </div>
    </form>
  </base-modal>
</template>

<script setup>
import { ref, watch } from 'vue';
import BaseModal from '../layout/BaseModal.vue';

const props = defineProps({
  modelValue: { type: Boolean, default: false },
  isEdit: { type: Boolean, default: false },
  item: { type: Object, default: () => ({}) },
});

const emit = defineEmits(['update:modelValue', 'submit']);

const form = ref({});

watch(() => props.item, (newItem) => {
  form.value = { ...(newItem || {}) };
}, { immediate: true, deep: true });

const handleSubmit = () => {
  emit('submit', form.value);
  emit('update:modelValue', false);
};
</script>
