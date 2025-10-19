<template>
  <div class="max-w-md mx-auto text-center">
    <h2 class="text-2xl font-bold text-heading mb-4">اسکن کد QR</h2>
    
    <div v-if="!cameraReady && !error" class="p-8">
        <p class="text-body mb-6">برای اسکن کد، نیاز به دسترسی به دوربین شما داریم.</p>
        <button @click="initCamera" class="px-6 py-3 bg-action text-white rounded-lg">فعال‌سازی دوربین</button>
    </div>

    <div v-if="cameraReady" class="relative border-4 border-gray-300 rounded-lg overflow-hidden w-64 h-64 mx-auto">
      <StreamBarcodeReader v-if="scannerReady" @decode="onDecode" @loaded="onLoaded" @error="onCameraError"></StreamBarcodeReader>
      <div v-if="scannerReady" class="scanner-line"></div>
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
import { ref, nextTick } from 'vue';
import { StreamBarcodeReader } from "vue-barcode-reader";
import axios from 'axios';
import { useToast } from 'vue-toastification';
import AttendanceActionModal from './AttendanceActionModal.vue';
import { ATTENDANCE_API } from '@/config/api';

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
    await axios.post(ATTENDANCE_API.RECORD, 
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
