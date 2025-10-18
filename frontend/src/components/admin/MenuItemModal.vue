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
        <label for="image" class="block text-sm font-medium text-heading mb-2">تصویر</label>
        <input @change="handleImageUpload" type="file" id="image" class="w-full p-2 bg-input-bg border border-border-subtle rounded-lg file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-action file:text-white hover:file:bg-action-hover"/>
        <img v-if="imagePreview" :src="imagePreview" class="mt-4 w-32 h-32 object-cover rounded-lg"/>
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
const imagePreview = ref(null);
const imageFile = ref(null);

watch(() => props.item, (newItem) => {
  form.value = { ...(newItem || {}) };
  if (newItem && newItem.image) {
    imagePreview.value = newItem.image;
  } else {
    imagePreview.value = null;
  }
  imageFile.value = null;
}, { immediate: true, deep: true });

const handleImageUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    imageFile.value = file;
    const reader = new FileReader();
    reader.onload = (e) => {
      imagePreview.value = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};

const handleSubmit = () => {
  const formData = new FormData();
  Object.keys(form.value).forEach(key => {
    if (key !== 'image') { // Don't append the old image URL
      formData.append(key, form.value[key]);
    }
  });
  if (imageFile.value) {
    formData.append('image', imageFile.value);
  }
  
  emit('submit', formData);
  emit('update:modelValue', false);
};
</script>
