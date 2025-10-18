<template>
  <vue-final-modal
    :model-value="modelValue"
    @update:model-value="(val) => emit('update:modelValue', val)"
    :teleport-to="teleportTo"
    :hide-overlay="hideOverlay"
    :show-close="showClose"
    :esc-to-close="escToClose"
    :click-to-close="clickToClose"
    :prevent-click="preventClick"
    :focus-trap="focusTrap"
    :lock-scroll="lockScroll"
    :swipe-to-close="swipeToClose"
    :transition="{...defaultTransition, ...transition}"
    :overlay-transition="{...defaultOverlayTransition, ...overlayTransition}"
    content-class="vfm-content"
    overlay-class="vfm-overlay"
  >
    <div class="bg-surface border border-border-subtle rounded-2xl shadow-xl p-8 w-full max-w-md mx-auto max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between mb-6">
        <h3 class="text-xl font-bold text-heading">{{ title }}</h3>
        <button @click="emit('update:modelValue', false)" class="text-body hover:text-heading transition-colors">
          <svg class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      </div>
      <div>
        <slot />
      </div>
    </div>
  </vue-final-modal>
</template>

<script setup>
import { VueFinalModal } from 'vue-final-modal';

const props = defineProps({
  modelValue: { type: Boolean, default: false },
  title: { type: String, default: '' },
  teleportTo: { type: String, default: 'body' },
  hideOverlay: { type: Boolean, default: false },
  showClose: { type: Boolean, default: true },
  escToClose: { type: Boolean, default: true },
  clickToClose: { type: Boolean, default: true },
  preventClick: { type: Boolean, default: false },
  focusTrap: { type: Boolean, default: true },
  lockScroll: { type: Boolean, default: true },
  swipeToClose: { type: String, default: 'none' },
  transition: { type: Object, default: () => ({}) },
  overlayTransition: { type: Object, default: () => ({}) },
});

const emit = defineEmits(['update:modelValue']);

const defaultTransition = {
  'enter-active-class': 'transition duration-300 ease-out',
  'enter-from-class': 'transform scale-95 opacity-0',
  'enter-to-class': 'transform scale-100 opacity-100',
  'leave-active-class': 'transition duration-200 ease-in',
  'leave-from-class': 'transform scale-100 opacity-100',
  'leave-to-class': 'transform scale-95 opacity-0',
};

const defaultOverlayTransition = {
  'enter-active-class': 'transition duration-300 ease-out',
  'enter-from-class': 'opacity-0',
  'enter-to-class': 'opacity-100',
  'leave-active-class': 'transition duration-200 ease-in',
  'leave-from-class': 'opacity-100',
  'leave-to-class': 'opacity-0',
};
</script>

<style>
.vfm-overlay {
  @apply bg-black bg-opacity-50;
}
</style>
