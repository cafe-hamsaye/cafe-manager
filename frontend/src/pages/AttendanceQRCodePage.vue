<template>
  <div class="container">
    <h1>Attendance QR Code</h1>
    <div v-if="token">
      <qrcode-vue :value="token" :size="300" level="H" />
    </div>
    <div v-else>
      <p>Loading QR code...</p>
    </div>
  </div>
</template>

<script>
import QrcodeVue from 'qrcode.vue';
import authFetch from '@/utils/authFetch';
import { API_BASE_URL } from '@/config/api';

export default {
  name: 'AttendanceQRCodePage',
  components: {
    QrcodeVue,
  },
  data() {
    return {
      token: null,
      intervalId: null,
    };
  },
  methods: {
    async fetchQRCode() {
      try {
        const response = await authFetch(`${API_BASE_URL}/attendance/qr-code/`);
        const data = await response.json();
        this.token = data.token;
      } catch (error) {
        console.error('Error fetching QR code:', error);
      }
    },
  },
  mounted() {
    this.fetchQRCode();
    this.intervalId = setInterval(this.fetchQRCode, 300000);
  },
  beforeUnmount() {
    clearInterval(this.intervalId);
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
}
</style>
