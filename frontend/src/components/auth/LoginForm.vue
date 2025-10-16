<template>
  <div class="w-full max-w-md p-4">
    <div class="bg-surface border border-border-subtle rounded-2xl shadow-xl p-8">
      <div class="text-center mb-10">
        <h1 class="text-2xl font-bold text-heading mb-2">خوش آمدید</h1>
        <p class="text-sm text-body">لطفا اطلاعات حساب خود را وارد نمایید</p>
      </div>
      
      <form @submit.prevent="handleSubmit" class="space-y-6">
        <div>
          <label for="phoneNumber-login" class="block text-sm font-medium text-heading mb-2">شماره تلفن</label>
          <input v-model="phoneNumber" type="tel" id="phoneNumber-login" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg focus:border-action focus:ring-2 focus:ring-action/20 outline-none transition-all duration-300 text-right" style="direction: ltr;" placeholder="09123456789" required>
        </div>
        
        <div>
          <label for="password-login" class="block text-sm font-medium text-heading mb-2">رمز عبور</label>
          <div class="relative">
            <input v-model="password" :type="passwordFieldType" id="password-login" class="w-full p-3 bg-input-bg border border-border-subtle rounded-lg focus:border-action focus:ring-2 focus:ring-action/20 outline-none transition-all duration-300" placeholder="••••••••" required>
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center cursor-pointer" @click="togglePasswordVisibility">
              <svg v-if="passwordFieldType === 'password'" class="h-5 w-5 text-body" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
              <svg v-else class="h-5 w-5 text-body" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>
            </div>
          </div>
        </div>
        
        <div class="pt-4">
          <button type="submit" class="w-full p-3 bg-action text-white rounded-lg hover:bg-action-hover transition-all duration-300 font-medium shadow-md hover:shadow-lg hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-action/50">
              ورود به سیستم
          </button>
        </div>

      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { AUTH_API } from '@/config/api';
import { useToast } from 'vue-toastification';

const phoneNumber = ref('');
const password = ref('');
const passwordFieldType = ref('password');

const toast = useToast();
const router = useRouter();

const togglePasswordVisibility = () => {
  passwordFieldType.value = passwordFieldType.value === 'password' ? 'text' : 'password';
};

const handleSubmit = async () => {
  try {
    const response = await fetch(AUTH_API.LOGIN, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        phone_number: phoneNumber.value,
        password: password.value,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      const errorMessage = data.detail || data[Object.keys(data)[0]][0] || 'Something went wrong';
      throw new Error(errorMessage);
    }

    toast.success(data.message);
    router.push('/dashboard');

  } catch (error) {
    console.error('Login error:', error);
    toast.error(error.message);
  }
};
</script>