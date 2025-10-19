<template>
  <BaseModal :model-value="modelValue" @update:model-value="(val) => emit('update:modelValue', val)" :title="isEdit ? 'ویرایش آیتم' : 'افزودن آیتم'">
    <form @submit.prevent="submitForm" class="space-y-6">
      <div>
        <label for="name" class="block text-sm font-medium text-heading mb-2">نام</label>
        <input v-model="form.name" type="text" id="name" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg" required>
      </div>
      <div>
        <label for="description" class="block text-sm font-medium text-heading mb-2">توضیحات</label>
        <textarea v-model="form.description" id="description" rows="4" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg"></textarea>
      </div>
      <div>
        <label for="price" class="block text-sm font-medium text-heading mb-2">قیمت</label>
        <input v-model="form.price" type="number" id="price" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg" required>
      </div>
      <div>
        <label for="image" class="block text-sm font-medium text-heading mb-2">تصویر</label>
        <input @change="handleImageUpload" type="file" id="image" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg">
        <img v-if="imagePreview" :src="imagePreview" class="mt-4 w-32 h-32 object-cover rounded-lg"/>
      </div>
      <div class="pt-4 flex justify-end space-x-4 space-x-reverse">
        <button type="button" @click="emit('update:modelValue', false)" class="px-6 py-2.5 rounded-lg bg-gray-200 text-gray-800 hover:bg-gray-300 transition-colors">انصراف</button>
        <button type="submit" class="px-6 py-2.5 rounded-lg bg-action text-white hover:bg-action-hover transition-colors">ذخیره</button>
      </div>
    </form>
  </BaseModal>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import BaseModal from '@/components/layout/BaseModal.vue';

const props = defineProps({ 
  modelValue: Boolean,
  isEdit: Boolean,
  item: Object 
});
const emit = defineEmits(['update:modelValue', 'submit']);

const form = ref({});
const imagePreview = ref(null);

watch(() => props.modelValue, (newValue) => {
  if (newValue) {
    form.value = { ...props.item };
    imagePreview.value = props.item?.image || null;
  } else {
    form.value = {};
    imagePreview.value = null;
  }
});

const handleImageUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    form.value.image = file;
    imagePreview.value = URL.createObjectURL(file);
  }
};

const submitForm = () => {
  const formData = new FormData();
  for (const key in form.value) {
    if (form.value[key] !== null && form.value[key] !== undefined) {
      formData.append(key, form.value[key]);
    }
  }
  emit('submit', formData);
  emit('update:modelValue', false);
};
</script>