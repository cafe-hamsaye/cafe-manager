<template>
  <div class="max-w-md mx-auto text-center">
    <h2 class="text-2xl font-bold text-heading mb-4">اسکن کد QR</h2>
    
    <div v-if="!cameraReady && !error" class="p-8">
        <p class="text-body mb-6">برای اسکن کد، نیاز به دسترسی به دوربین شما داریم.</p>
        <button @click="initCamera" class="px-6 py-3 bg-action text-white rounded-lg">فعال‌سازی دوربین</button>
    </div>

    <div v-if="cameraReady" class="relative border-4 border-gray-300 rounded-lg overflow-hidden w-64 h-64 mx-auto">
      <qrcode-stream @decode="onDecode" @init="onInit" @error="onCameraError"></qrcode-stream>
      <div class="scanner-line"></div>
    </div>
    <p v-if="log" class="text-sm text-gray-500 mt-2">{{ log }}</p>
    <p v-if="error" class="text-red-500 mt-4">{{ error }}</p>

    <AttendanceActionModal v-model="showConfirmModal" @confirm="recordAttendance" />
  </div>
</template>

<style scoped>
.scanner-line {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: red;
  box-shadow: 0 0 10px red;
  animation: scan 2s linear infinite;
}

@keyframes scan {
  0% {
    top: 0;
  }
  100% {
    top: 100%;
  }
}
</style>

<script setup>
import { ref } from 'vue';
import { StreamBarcodeReader } from "vue-barcode-reader";
import axios from 'axios';
import { useToast } from 'vue-toastification';
import AttendanceActionModal from './AttendanceActionModal.vue';
import { AUTH_TOKEN_KEYS } from '@/config/constants';

const error = ref('');
const log = ref('');
const cameraReady = ref(false);
const showConfirmModal = ref(false);
const decodedToken = ref(null);
const toast = useToast();

const initCamera = async () => {
  error.value = '';
  log.value = 'در حال درخواست دسترسی به دوربین...';
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    stream.getTracks().forEach(track => track.stop());
    cameraReady.value = true;
    log.value = 'دوربین با موفقیت فعال شد. منتظر اسکن...';
  } catch (err) {
    if (err.name === 'NotAllowedError') {
      error.value = 'شما دسترسی به دوربین را مسدود کرده‌اید. لطفا از تنظیمات مرورگر آن را فعال کنید.';
    } else {
      error.value = `خطا در فعال‌سازی دوربین: ${err.name}`;
    }
    log.value = '';
  }
};

const onInit = async (promise) => {
  log.value = 'در حال آماده‌سازی اسکنر...';
  try {
    await promise;
    log.value = 'اسکنر آماده است. دوربین را به سمت کد QR بگیرید.';
  } catch (err) {
    if (err.name === 'NotAllowedError') {
      error.value = 'شما دسترسی به دوربین را مسدود کرده‌اید.';
    } else if (err.name === 'NotFoundError') {
      error.value = 'هیچ دوربینی در این دستگاه یافت نشد.';
    } else if (err.name === 'NotSupportedError') {
      error.value = 'دسترسی به دوربین در این مرورگر (در محیط ناامن) پشتیبانی نمی‌شود.';
    } else if (err.name === 'NotReadableError') {
      error.value = 'دوربین توسط یک برنامه دیگر در حال استفاده است.';
    } else if (err.name === 'OverconstrainedError') {
      error.value = 'دوربین نصب شده با کیفیت مورد نیاز سازگار نیست.';
    } else {
      error.value = `خطای ناشناخته دوربین: ${err.name}`;
    }
    log.value = '';
  }
};

const onDecode = (result) => {
  log.value = 'کد با موفقیت اسکن شد!';
  error.value = '';
  decodedToken.value = result;
  showConfirmModal.value = true;
};

const onCameraError = (err) => {
  error.value = `خطای دوربین: ${err.name}`;
  cameraReady.value = false;
  log.value = '';
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
    cameraReady.value = false;
  }
};
</script>
