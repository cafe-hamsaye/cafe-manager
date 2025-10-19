<template>
  <div>
    <StaffHeader @open-scanner="showScanner = true" />
    <main class="p-8">
      <div v-if="!showScanner">
        <h1 class="text-2xl font-bold">داشبورد کارکنان</h1>
        <p>خوش آمدید!</p>
      </div>
      <AttendanceScanner v-else />
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import StaffHeader from '@/components/layout/StaffHeader.vue';
import AttendanceScanner from '@/components/staff/AttendanceScanner.vue';

const showScanner = ref(false);
</script>
