<template>
  <div class="min-h-screen flex items-center justify-center py-10 px-4 relative">
    <BackButton class="absolute top-8 left-8 z-10" />
    <AdminLoginForm />
  </div>
</template>

<script setup>
import AdminLoginForm from '@/components/auth/AdminLoginForm.vue';
import BackButton from '@/components/layout/BackButton.vue';
</script>