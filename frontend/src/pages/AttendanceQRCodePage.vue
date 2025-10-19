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
import axios from 'axios';
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
        const tokenData = JSON.parse(localStorage.getItem('admin_token'));
        const response = await axios.get(`${API_BASE_URL}/attendance/qr-code/`, {
          headers: { Authorization: `Bearer ${tokenData.access}` },
        });
        this.token = response.data.token;
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
