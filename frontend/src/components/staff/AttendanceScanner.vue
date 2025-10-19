<template>
  <div class="max-w-md mx-auto text-center">
    <h2 class="text-2xl font-bold text-heading mb-4">اسکن کد QR</h2>
    <p class="text-body mb-6">لطفا کد QR نمایش داده شده در پنل ادمین را اسکن کنید.</p>
    <div class="border-4 border-gray-300 rounded-lg overflow-hidden w-64 h-64 mx-auto">
      <qrcode-stream @decode="onDecode" @error="onError"></qrcode-stream>
    </div>
    <p v-if="error" class="text-red-500 mt-4">{{ error }}</p>

    <confirmation-modal 
      v-model="showConfirmModal"
      title="ثبت تردد"
      message="لطفا نوع تردد خود را مشخص کنید:"
      confirm-text="ورود"
      cancel-text="خروج"
      @confirm="recordAttendance('in')"
      @cancel="recordAttendance('out')"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { QrcodeStream } from 'vue-qrcode-reader';
import axios from 'axios';
import { useToast } from 'vue-toastification';
import ConfirmationModal from '@/components/layout/ConfirmationModal.vue';
import { AUTH_TOKEN_KEYS } from '@/config/constants';

const error = ref('');
const showConfirmModal = ref(false);
const decodedToken = ref(null);
const toast = useToast();

const onDecode = (result) => {
  error.value = '';
  decodedToken.value = result;
  showConfirmModal.value = true;
};

const onError = (err) => {
  error.value = `خطا در دسترسی به دوربین: ${err.name}`;
};

const recordAttendance = async (status) => {
  if (!decodedToken.value) return;

  try {
    const token = JSON.parse(localStorage.getItem(AUTH_TOKEN_KEYS.STAFF))?.access;
    await axios.post('/api/attendance/record/', 
      { token: decodedToken.value, status }, 
      { headers: { Authorization: `Bearer ${token}` } }
    );
    toast.success(`تردد شما به عنوان '${status === 'in' ? 'ورود' : 'خروج'}' با موفقیت ثبت شد.`);
  } catch (err) {
    toast.error(err.response?.data?.detail || 'ثبت تردد با خطا مواجه شد.');
  } finally {
    decodedToken.value = null;
    showConfirmModal.value = false;
  }
};
</script>
