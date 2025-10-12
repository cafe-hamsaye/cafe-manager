<template>
  <div class="w-full max-w-md mx-4">
    <div class="bg-white rounded-xl shadow-lg overflow-hidden border border-[color:var(--c-light-cream)]">
      <div class="p-6 sm:p-8">
        <h1 class="text-2xl font-bold text-center text-[color:var(--c-dark-brown)] mb-1">ایجاد حساب کاربری</h1>
        <p class="text-sm text-center text-[color:var(--c-medium-brown)] mb-8">برای استفاده از امکانات، ثبت‌نام کنید</p>
        
        <form @submit.prevent="handleSubmit" class="space-y-6">
          
          <div class="flex space-x-4 space-x-reverse">
            <div class="w-1/2">
              <label for="firstName-signup" class="block text-sm font-medium text-[color:var(--c-dark-brown)] mb-1">نام</label>
              <input v-model="firstName" type="text" id="firstName-signup" class="input-focus bg-[color:var(--c-light-cream)] border border-[color:var(--c-medium-brown)] text-[color:var(--c-dark-brown)] text-sm sm:text-base rounded-lg focus:ring-2 focus:ring-[color:var(--c-medium-brown)] focus:border-[color:var(--c-medium-brown)] block w-full p-2 sm:p-3" placeholder="نام" required>
            </div>
            <div class="w-1/2">
              <label for="lastName-signup" class="block text-sm font-medium text-[color:var(--c-dark-brown)] mb-1">نام خانوادگی</label>
              <input v-model="lastName" type="text" id="lastName-signup" class="input-focus bg-[color:var(--c-light-cream)] border border-[color:var(--c-medium-brown)] text-[color:var(--c-dark-brown)] text-sm sm:text-base rounded-lg focus:ring-2 focus:ring-[color:var(--c-medium-brown)] focus:border-[color:var(--c-medium-brown)] block w-full p-2 sm:p-3" placeholder="نام خانوادگی" required>
            </div>
          </div>

          <div>
            <label for="phoneNumber-signup" class="block text-sm font-medium text-[color:var(--c-dark-brown)] mb-1">شماره تلفن</label>
            <input v-model="phoneNumber" type="tel" id="phoneNumber-signup" class="input-focus bg-[color:var(--c-light-cream)] border border-[color:var(--c-medium-brown)] text-[color:var(--c-dark-brown)] text-sm sm:text-base rounded-lg focus:ring-2 focus:ring-[color:var(--c-medium-brown)] focus:border-[color:var(--c-medium-brown)] block w-full p-2 sm:p-3" placeholder="09123456789" required>
          </div>

          <div>
            <label for="password-signup" class="block text-sm font-medium text-[color:var(--c-dark-brown)] mb-1">رمز عبور</label>
            <div class="relative">
              <input v-model="password" :type="passwordFieldType" id="password-signup" class="input-focus bg-[color:var(--c-light-cream)] border border-[color:var(--c-medium-brown)] text-[color:var(--c-dark-brown)] text-sm sm:text-base rounded-lg focus:ring-2 focus:ring-[color:var(--c-medium-brown)] focus:border-[color:var(--c-medium-brown)] block w-full p-2 sm:p-3 pr-10" placeholder="••••••••" required>
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center cursor-pointer" @click="togglePasswordVisibility">
                <svg v-if="passwordFieldType === 'password'" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-eye text-[color:var(--c-medium-brown)]"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-eye-off text-[color:var(--c-medium-brown)]"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>
              </div>
            </div>
          </div>

          <div>
            <label for="confirm-password-signup" class="block text-sm font-medium text-[color:var(--c-dark-brown)] mb-1">تکرار رمز عبور</label>
            <div class="relative">
              <input v-model="confirmPassword" :type="confirmPasswordFieldType" id="confirm-password-signup" class="input-focus bg-[color:var(--c-light-cream)] border border-[color:var(--c-medium-brown)] text-[color:var(--c-dark-brown)] text-sm sm:text-base rounded-lg focus:ring-2 focus:ring-[color:var(--c-medium-brown)] focus:border-[color:var(--c-medium-brown)] block w-full p-2 sm:p-3 pr-10" placeholder="••••••••" required>
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center cursor-pointer" @click="toggleConfirmPasswordVisibility">
                <svg v-if="confirmPasswordFieldType === 'password'" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-eye text-[color:var(--c-medium-brown)]"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-eye-off text-[color:var(--c-medium-brown)]"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>
              </div>
            </div>
          </div>
          
          <button type="submit" class="btn-hover w-full text-white bg-[color:var(--c-medium-brown)] hover:bg-[color:var(--c-dark-brown)] focus:ring-4 focus:ring-[color:var(--c-medium-brown)] font-medium rounded-lg text-sm px-5 py-2.5 text-center">
              ثبت نام
          </button>

        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { AUTH_API } from '@/config/api';
import { useToast } from 'vue-toastification';

const firstName = ref('');
const lastName = ref('');
const phoneNumber = ref('');
const password = ref('');
const confirmPassword = ref('');
const passwordFieldType = ref('password');
const confirmPasswordFieldType = ref('password');

const toast = useToast();

const togglePasswordVisibility = () => {
  passwordFieldType.value = passwordFieldType.value === 'password' ? 'text' : 'password';
};

const toggleConfirmPasswordVisibility = () => {
  confirmPasswordFieldType.value = confirmPasswordFieldType.value === 'password' ? 'text' : 'password';
};

const handleSubmit = async () => {
  if (password.value !== confirmPassword.value) {
    toast.error('رمزهای عبور یکسان نیستند!');
    return;
  }

  try {
    const response = await fetch(AUTH_API.REGISTER, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        first_name: firstName.value,
        last_name: lastName.value,
        phone_number: phoneNumber.value,
        password: password.value,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || 'Something went wrong');
    }

    toast.success('ثبت نام با موفقیت انجام شد!');

  } catch (error) {
    console.error('Signup error:', error);
    toast.error(error.message);
  }
};
</script>

<style scoped>
/* Styles are copied from LoginForm.vue for consistency */
.input-focus {
    transition: all 0.3s ease;
    outline: none !important;
}

.input-focus:focus {
    border-color: #34d399;
    box-shadow: 0 0 0 3px rgba(52, 211, 153, 0.2);
}

.btn-hover {
    transition: all 0.3s ease, transform 0.2s ease;
}

.btn-hover:hover {
    background-color: #059669;
    transform: scale(1.03);
}

#phoneNumber-signup {
  direction: ltr;
  text-align: right;
}
</style>