<template>
  <header class="bg-surface/80 backdrop-blur-lg sticky top-0 z-50 border-b border-border-subtle">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-20">
        <router-link to="/admin-panel" class="text-xl font-bold text-heading">
          پنل مدیریت
        </router-link>
        <nav>
          <UserProfileMenu />
        </nav>
      </div>
    </div>
  </header>
</template>

<script setup>
import UserProfileMenu from './UserProfileMenu.vue';
</script>
