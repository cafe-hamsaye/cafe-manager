<template>
  <div id="app-wrapper" class="flex flex-col min-h-screen bg-bg-main text-body">
    <!-- Headers -->
    <DashboardHeader v-if="isUserDashboard" />
    <AdminHeader v-else-if="isAdminPanel" />
    <Header v-else-if="showGenericHeader" />

    <main class="flex-grow">
      <router-view />
    </main>

    <!-- Footer -->
    <Footer v-if="showGenericHeader" />
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';

// Layout Components
import Header from './components/layout/Header.vue';
import DashboardHeader from './components/layout/DashboardHeader.vue';
import AdminHeader from './components/layout/AdminHeader.vue';
import Footer from './components/layout/Footer.vue';

const route = useRoute();

// Computed properties to determine which layout to show
const isAuthPage = computed(() => route.path === '/auth' || route.path === '/admin');
const isUserDashboard = computed(() => route.path.startsWith('/dashboard'));
const isAdminPanel = computed(() => route.path.startsWith('/admin-panel'));

// Show generic header and footer on pages that are not special auth/dashboard/admin pages
const showGenericHeader = computed(() => !isAuthPage.value && !isUserDashboard.value && !isAdminPanel.value);

</script>
