<template>
  <div class="max-w-md mx-auto text-center">
    <h2 class="text-2xl font-bold text-heading mb-4">اسکن کد QR</h2>
    
    <div v-if="!cameraReady && !error" class="p-8">
        <p class="text-body mb-6">برای اسکن کد، نیاز به دسترسی به دوربین شما داریم.</p>
        <button @click="initCamera" class="px-6 py-3 bg-action text-white rounded-lg">فعال‌سازی دوربین</button>
    </div>

    <div v-if="cameraReady" class="border-4 border-gray-300 rounded-lg overflow-hidden w-64 h-64 mx-auto">
      <qrcode-stream @decode="onDecode" @error="onCameraError"></qrcode-stream>
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
const cameraReady = ref(false);
const showConfirmModal = ref(false);
const decodedToken = ref(null);
const toast = useToast();

const initCamera = async () => {
  error.value = '';
  try {
    // Explicitly request camera permissions
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    // Stop the tracks immediately, we only needed to trigger the permission prompt
    stream.getTracks().forEach(track => track.stop());
    cameraReady.value = true;
  } catch (err) {
    if (err.name === 'NotAllowedError') {
      error.value = 'شما دسترسی به دوربین را مسدود کرده‌اید. لطفا از تنظیمات مرورگر آن را فعال کنید.';
    } else {
      error.value = `خطا در فعال‌سازی دوربین: ${err.name}`;
    }
  }
};

const onDecode = (result) => {
  error.value = '';
  decodedToken.value = result;
  showConfirmModal.value = true;
};

const onCameraError = (err) => {
  error.value = `خطا در دوربین: ${err.name}`;
  cameraReady.value = false; // Reset camera state on error
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
    cameraReady.value = false; // Reset to show the button again
  }
};
</script>