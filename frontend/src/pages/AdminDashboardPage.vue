<template>
  <div class="container mx-auto py-10 px-4 sm:px-6 lg:px-8">
    <component :is="activeComponent" />
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useRoute } from 'vue-router';
import UsersTable from '@/components/admin/UsersTable.vue';
import MenuTable from '@/components/admin/MenuTable.vue';

const route = useRoute();
const currentView = ref(route.query.view || 'users'); // Default to 'users'

const componentMap = {
  users: UsersTable,
  menu: MenuTable,
};

const activeComponent = computed(() => componentMap[currentView.value] || UsersTable);

watch(() => route.query.view, (newView) => {
  currentView.value = newView || 'users';
});
</script>
