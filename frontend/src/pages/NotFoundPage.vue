<template>
  <div class="min-h-screen flex flex-col items-center justify-center text-center px-4 bg-bg-main">
    <h1 class="text-9xl font-bold text-action">404</h1>
    <h2 class="text-3xl font-semibold text-heading mt-4 mb-2">صفحه یافت نشد</h2>
    <p class="text-body mb-8">متاسفانه صفحه‌ای که به دنبال آن بودید وجود ندارد.</p>
    <router-link 
      to="/" 
      class="px-6 py-3 bg-action text-white text-sm font-medium rounded-lg hover:bg-action-hover transition-all duration-300 shadow-md hover:shadow-lg hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-action/50"
    >
      بازگشت به صفحه اصلی
    </router-link>
  </div>
</template>

<script setup>
// No script logic needed for this simple page.
</script>
