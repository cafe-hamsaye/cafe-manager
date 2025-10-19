<template>
  <BaseModal :show="show" @close="$emit('close')">
    <template #title>Scan QR Code</template>
    <div class="container">
      <div v-if="!showScanner">
        <button @click="showScanner = true; status = 'in'">Clock In</button>
        <button @click="showScanner = true; status = 'out'">Clock Out</button>
      </div>
      <div v-if="showScanner">
        <qrcode-stream @decode="onDecode"></qrcode-stream>
        <button @click="showScanner = false">Cancel</button>
      </div>
      <p v-if="message">{{ message }}</p>
    </div>
  </BaseModal>
</template>

<script>
import { QrcodeStream } from 'vue-qrcode-reader';
import axios from 'axios';
import { API_BASE_URL } from '@/config/api';
import { AUTH_TOKEN_KEYS } from '@/config/constants';
import BaseModal from '@/components/layout/BaseModal.vue';

export default {
  name: 'QRCodeScannerModal',
  components: {
    QrcodeStream,
    BaseModal,
  },
  props: {
    show: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      showScanner: false,
      status: '',
      message: '',
    };
  },
  methods: {
    async onDecode(decodedString) {
      this.showScanner = false;
      const tokenData = JSON.parse(localStorage.getItem(AUTH_TOKEN_KEYS.USER));
      if (!tokenData || !tokenData.access) {
        this.message = 'You are not logged in.';
        return;
      }

      try {
        await axios.post(
          `${API_BASE_URL}/attendance/scan/`,
          {
            token: decodedString,
            status: this.status,
          },
          {
            headers: {
              Authorization: `Bearer ${tokenData.access}`,
            },
          }
        );
        this.message = 'Attendance recorded successfully!';
      } catch (error) {
        console.error('Error recording attendance:', error);
        this.message = error.response?.data?.detail || 'Failed to record attendance. Please try again.';
      }
    },
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
button {
  margin: 1rem;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  cursor: pointer;
}
</style>
