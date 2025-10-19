<template>
  <BaseModal :show="true" @close="$emit('close')">
    <template #title>{{ isEdit ? 'ویرایش کارمند' : 'افزودن کارمند' }}</template>
    <form @submit.prevent="submitForm" class="space-y-6 p-4">
      <div>
        <label for="number" class="block text-sm font-medium text-heading mb-2">شماره</label>
        <input v-model="form.number" type="text" id="number" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg" required>
      </div>
      <div>
        <label for="password" class="block text-sm font-medium text-heading mb-2">رمز عبور (برای تغییر وارد کنید)</label>
        <input v-model="form.password" type="password" id="password" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg">
      </div>
      <div class="pt-4 flex justify-end">
        <button type="button" @click="$emit('close')" class="ml-4 px-4 py-2 bg-gray-200 rounded-lg">انصراف</button>
        <button type="submit" class="px-4 py-2 bg-action text-white rounded-lg">ذخیره</button>
      </div>
    </form>
  </BaseModal>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { useToast } from 'vue-toastification';
import BaseModal from '@/components/layout/BaseModal.vue';

const props = defineProps({ staff: Object });
const emit = defineEmits(['close', 'save']);

const form = ref({ number: '', password: '' });
const toast = useToast();

const isEdit = computed(() => !!props.staff);

onMounted(() => {
  if (isEdit.value) {
    form.value.number = props.staff.number;
  }
});

const submitForm = async () => {
  const url = isEdit.value ? `/api/staff/${props.staff.id}/` : '/api/staff/';
  const method = isEdit.value ? 'patch' : 'post';
  
  const payload = {
    number: form.value.number,
  };
  if (form.value.password) {
    payload.password = form.value.password;
  }

  try {
    await axios[method](url, payload, { headers: { Authorization: `Bearer ${JSON.parse(localStorage.getItem('admin_token')).access}` } });
    toast.success('عملیات با موفقیت انجام شد');
    emit('save');
    emit('close');
  } catch (err) {
    const errorMsg = err.response?.data?.number?.[0] || 'ذخیره اطلاعات با خطا مواجه شد';
    toast.error(errorMsg);
  }
};
</script>
