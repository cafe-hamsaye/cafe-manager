<template>
  <header class="bg-surface/80 backdrop-blur-lg sticky top-0 z-50 border-b border-border-subtle">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-20">
        <!-- Right Section: Title & Menu -->
        <div class="flex items-center space-x-8 space-x-reverse">
          <router-link to="/" class="text-xl font-bold text-heading">
            کافه همسایه
          </router-link>
          <div class="border-l border-border-subtle h-6"></div>
          <router-link to="/menu" class="text-sm font-medium text-body hover:text-heading transition-colors">
            منو
          </router-link>
        </div>

        <!-- Left Section: Auth Button -->
        <nav>
          <router-link to="/auth" class="px-5 py-2.5 bg-action text-white text-sm font-medium rounded-lg hover:bg-action-hover transition-all duration-300 shadow-sm hover:shadow-md hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-action/50">
            ورود / ثبت نام
          </router-link>
        </nav>
      </div>
    </div>
  </header>
</template>

<script setup>
// No script needed, all styling is done via Tailwind classes.
</script>
