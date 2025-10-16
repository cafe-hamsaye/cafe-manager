<template>
  <header class="bg-surface/80 backdrop-blur-lg sticky top-0 z-50 border-b border-border-subtle">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-20">
        <!-- Right Section: Title & Menu -->
        <div class="flex items-center space-x-8 space-x-reverse">
          <router-link to="/admin-panel" class="text-xl font-bold text-heading">
            پنل مدیریت
          </router-link>
          <div class="border-l border-border-subtle h-6"></div>
          <router-link to="/admin-panel/users" class="text-sm font-medium text-body hover:text-heading transition-colors">
            مدیریت کاربران
          </router-link>
          <!-- Add other admin menu items here -->
        </div>

        <!-- Left Section: Profile -->
        <div>
          <UserProfileMenu />
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import UserProfileMenu from './UserProfileMenu.vue';
</script>