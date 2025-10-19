<template>
  <div class="max-w-md mx-auto text-center">
    <h2 class="text-2xl font-bold text-heading mb-4">اسکن کد QR</h2>
    <p class="text-body mb-6">دوربین را به سمت کد QR بگیرید.</p>
    
    <div v-if="error" class="p-4 mb-4 text-red-700 bg-red-100 rounded-lg">
      <p class="font-bold">خطا:</p>
      <p>{{ error }}</p>
    </div>

    <StreamBarcodeReader @decode="onDecode" @error="onError" @loaded="onLoaded"></StreamBarcodeReader>

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
import { StreamBarcodeReader } from "vue-barcode-reader";
import axios from 'axios';
import { useToast } from 'vue-toastification';
import ConfirmationModal from '@/components/layout/ConfirmationModal.vue';
import { AUTH_TOKEN_KEYS } from '@/config/constants';

const error = ref('');
const showConfirmModal = ref(false);
const decodedToken = ref(null);
const toast = useToast();

const onDecode = (result) => {
  console.log('Decoded:', result);
  if (result) {
    decodedToken.value = result;
    showConfirmModal.value = true;
  }
};

const onError = (err) => {
  error.value = `خطا در دوربین: ${err.message}. لطفاً دسترسی به دوربین را در مرورگر خود بررسی کنید.`;
  console.error(err);
};

const onLoaded = () => {
  console.log('Camera and scanner loaded successfully.');
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
