<template>
  <div class="min-h-screen flex flex-col items-center justify-center py-10 px-4">
    <BackButton class="absolute top-8 left-8 z-10" />
    <div class="w-full max-w-md p-4">
      <div class="bg-surface border border-border-subtle rounded-2xl shadow-xl p-8">
        <div class="text-center mb-10">
          <h1 class="text-2xl font-bold text-heading mb-2">ورود کارکنان</h1>
          <p class="text-sm text-body">لطفا شماره و رمز عبور خود را وارد کنید</p>
        </div>
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <div>
            <label for="number-login" class="block text-sm font-medium text-heading mb-2">شماره</label>
            <input v-model="number" type="text" id="number-login" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg" required>
          </div>
          <div>
            <label for="password-login" class="block text-sm font-medium text-heading mb-2">رمز عبور</label>
            <input v-model="password" type="password" id="password-login" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg" required>
          </div>
          <div class="pt-4">
            <button type="submit" class="w-full p-3 bg-action text-white rounded-lg">ورود</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useToast } from 'vue-toastification';
import { AUTH_TOKEN_KEYS } from '@/config/constants';
import { STAFF_API } from '@/config/api';
import BackButton from '@/components/layout/BackButton.vue';

const number = ref('');
const password = ref('');
const toast = useToast();
const router = useRouter();

const handleSubmit = async () => {
  const payload = { number: number.value, password: password.value };
  console.log('Sending payload:', payload);
  try {
    const response = await axios.post(STAFF_API.LOGIN, payload);
    localStorage.setItem(AUTH_TOKEN_KEYS.STAFF, JSON.stringify(response.data));
    router.push('/staff-panel');
  } catch (err) {
    console.error('Staff login error:', err.response);
    toast.error(err.response?.data?.detail || 'Login failed');
  }
};
</script>
