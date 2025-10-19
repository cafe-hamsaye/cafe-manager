<template>
  <BaseModal :model-value="modelValue" @close="close">
    <template #title>{{ isEdit ? 'ویرایش کارمند' : 'افزودن کارمند' }}</template>
    <form @submit.prevent="submitForm" class="space-y-6 p-4">
      <div>
        <label for="number" class="block text-sm font-medium text-heading mb-2">شماره</label>
        <input v-model="form.number" type="text" id="number" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg" required>
      </div>
      <div>
        <label for="password" class="block text-sm font-medium text-heading mb-2">رمز عبور <span v-if="isEdit">(برای تغییر وارد کنید)</span></label>
        <input v-model="form.password" type="password" id="password" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg" :required="!isEdit">
      </div>
      <div class="pt-4 flex justify-end">
        <button type="button" @click="close" class="ml-4 px-4 py-2 bg-gray-200 rounded-lg">انصراف</button>
        <button type="submit" class="px-4 py-2 bg-action text-white rounded-lg">ذخیره</button>
      </div>
    </form>
  </BaseModal>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import axios from 'axios';
import { useToast } from 'vue-toastification';
import { STAFF_API } from '@/config/api';
import BaseModal from '@/components/layout/BaseModal.vue';

const props = defineProps({
  modelValue: Boolean, // for v-model
  staff: Object
});
const emit = defineEmits(['update:modelValue', 'save']);

const form = ref({ number: '', password: '' });
const toast = useToast();

const isEdit = computed(() => !!props.staff);

const getAuthHeaders = () => {
  const token = JSON.parse(localStorage.getItem('admin_token'))?.access;
  return { Authorization: `Bearer ${token}` };
};

// Watch for prop changes to reset form when modal is reused
watch(() => props.staff, (newStaff) => {
  if (newStaff) {
    form.value.number = newStaff.number;
    form.value.password = ''; // Always clear password field
  } else {
    form.value.number = '';
    form.value.password = '';
  }
});

const close = () => {
  emit('update:modelValue', false);
};

const submitForm = async () => {
  const url = isEdit.value ? STAFF_API.UPDATE(props.staff.id) : STAFF_API.CREATE;
  const method = isEdit.value ? 'patch' : 'post';
  
  const payload = {};
  if (form.value.number) payload.number = form.value.number;
  if (form.value.password) payload.password = form.value.password;

  if (!isEdit.value && (!payload.number || !payload.password)) {
      toast.error("شماره و رمز عبور برای کارمند جدید الزامی است.");
      return;
  }

  try {
    await axios[method](url, payload, { headers: getAuthHeaders() });
    toast.success('عملیات با موفقیت انجام شد');
    emit('save');
    close();
  } catch (err) {
    const errorMsg = err.response?.data?.number?.[0] || 'ذخیره اطلاعات با خطا مواجه شد';
    toast.error(errorMsg);
  }
};
</script>
