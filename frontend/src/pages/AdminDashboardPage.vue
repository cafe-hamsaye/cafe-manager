<template>
  <div class="container mx-auto py-10 px-4 sm:px-6 lg:px-8">
    <div v-if="!activeComponent">
      <h1 class="text-2xl font-bold text-heading mb-4">به پنل مدیریت خوش آمدید</h1>
      <p class="text-body">لطفا برای شروع، یک گزینه از منوی بالا انتخاب کنید.</p>
    </div>
    <component :is="activeComponent" v-else />
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useRoute } from 'vue-router';
import UsersTable from '@/components/admin/UsersTable.vue';
import MenuTable from '@/components/admin/MenuTable.vue';
import StaffTable from '@/components/admin/StaffTable.vue';

const route = useRoute();
const currentView = ref(route.query.view || null); // Default to null

const componentMap = {
  users: UsersTable,
  menu: MenuTable,
  staff: StaffTable,
};

const activeComponent = computed(() => componentMap[currentView.value]);

watch(() => route.query.view, (newView) => {
  currentView.value = newView || null;
});
</script>
