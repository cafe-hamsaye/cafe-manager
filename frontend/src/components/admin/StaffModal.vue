<template>
  <BaseModal :model-value="modelValue" @update:model-value="(val) => emit('update:modelValue', val)" :title="isEdit ? 'ویرایش کارمند' : 'افزودن کارمند'">
    <form @submit.prevent="submitForm" class="space-y-6">
      <div>
        <label for="number" class="block text-sm font-medium text-heading mb-2">شماره</label>
        <input v-model="form.number" type="text" id="number" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg" required>
      </div>
      <div>
        <label for="password" class="block text-sm font-medium text-heading mb-2">رمز عبور <span v-if="isEdit" class="text-xs text-gray-500">(برای تغییر وارد کنید)</span></label>
        <input v-model="form.password" type="password" id="password" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg" :required="!isEdit">
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
import axios from 'axios';
import { useToast } from 'vue-toastification';
import { STAFF_API } from '@/config/api';
import BaseModal from '@/components/layout/BaseModal.vue';

const props = defineProps({ 
  modelValue: Boolean,
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

watch(() => props.modelValue, (newValue) => {
  if (newValue) {
    if (isEdit.value) {
      form.value.number = props.staff.number;
      form.value.password = '';
    } else {
      form.value.number = '';
      form.value.password = '';
    }
  }
});

const submitForm = async () => {
  const url = isEdit.value ? STAFF_API.UPDATE(props.staff.id) : STAFF_API.CREATE;
  const method = isEdit.value ? 'patch' : 'post';
  
  const payload = {};
  if (form.value.number) payload.number = form.value.number;
  if (form.value.password) payload.password = form.value.password;

  if (!isEdit.value && !payload.password) {
      toast.error("رمز عبور برای کارمند جدید الزامی است.");
      return;
  }

  try {
    await axios[method](url, payload, { headers: getAuthHeaders() });
    toast.success('عملیات با موفقیت انجام شد');
    emit('save');
    emit('update:modelValue', false);
  } catch (err) {
    const errorMsg = err.response?.data?.number?.[0] || 'ذخیره اطلاعات با خطا مواجه شد';
    toast.error(errorMsg);
  }
};
</script>
