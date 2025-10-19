<template>
  <div class="container mx-auto py-10 px-4 sm:px-6 lg:px-8 flex flex-col items-center">
    <div class="w-full max-w-lg text-center bg-surface p-8 rounded-2xl shadow-xl">
      <h1 class="text-3xl font-bold text-heading mb-4">کد QR حضور و غیاب</h1>
      <p class="text-body mb-8">این کد را برای ثبت تردد در اختیار کارکنان قرار دهید.</p>
      
      <div v-if="token" class="relative inline-block p-4 bg-white rounded-lg shadow-inner">
        <qrcode-vue :value="token" :size="300" level="H" />
      </div>
      <div v-else class="w-[316px] h-[316px] mx-auto">
        <Skeletor width="100%" height="100%" />
      </div>

      <div class="mt-8">
        <p class="text-lg text-body">کد جدید تا <span class="font-bold text-action text-2xl">{{ countdown }}</span> ثانیه دیگر</p>
        <div class="w-full bg-gray-200 rounded-full h-2.5 mt-2">
          <div class="bg-action h-2.5 rounded-full transition-all duration-1000 ease-linear" :style="{ width: countdownWidth + '%' }"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import QrcodeVue from 'qrcode.vue';
import axios from 'axios';
import { API_BASE_URL, ATTENDANCE_API } from '@/config/api';

export default {
  name: 'AttendanceQRCodePage',
  components: {
    QrcodeVue,
  },
  setup() {
    const REFRESH_INTERVAL = 10; // seconds
    const token = ref(null);
    const countdown = ref(REFRESH_INTERVAL);
    let apiIntervalId = null;
    let countdownIntervalId = null;

    const countdownWidth = computed(() => (countdown.value / REFRESH_INTERVAL) * 100);

    const fetchQRCode = async () => {
      try {
        const tokenData = JSON.parse(localStorage.getItem('admin_token'));
        const response = await axios.get(ATTENDANCE_API.QR_CODE, {
          headers: { Authorization: `Bearer ${tokenData.access}` },
        });
        token.value = response.data.token;
        countdown.value = REFRESH_INTERVAL;
      } catch (error) {
        console.error('Error fetching QR code:', error);
      }
    };

    const startCountdown = () => {
      countdownIntervalId = setInterval(() => {
        if (countdown.value > 0) {
          countdown.value--;
        } else {
          countdown.value = REFRESH_INTERVAL;
        }
      }, 1000);
    };

    onMounted(() => {
      fetchQRCode();
      startCountdown();
      apiIntervalId = setInterval(fetchQRCode, REFRESH_INTERVAL * 1000);
    });

    onBeforeUnmount(() => {
      clearInterval(apiIntervalId);
      clearInterval(countdownIntervalId);
    });

    return { token, countdown, countdownWidth };
  },
};
</script>
