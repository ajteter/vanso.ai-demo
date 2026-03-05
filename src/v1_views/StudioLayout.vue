<script setup>
import { ref } from 'vue';
import AppSidebar from '../v1_components/AppSidebar.vue';
import ProfilePanel from '../v1_components/ProfilePanel.vue';

const showProfilePanel = ref(false);

function toggleProfile() {
  showProfilePanel.value = !showProfilePanel.value;
}

function closeProfile() {
  showProfilePanel.value = false;
}
</script>

<template>
  <div class="bg-black flex flex-col items-start relative size-full min-h-screen text-white font-['Inter',sans-serif]">
    <!-- BG blur spots -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute bg-[#f5328a] blur-[75px] h-[512px] left-[-128px] opacity-20 rounded-full top-[-205px] w-[640px]"></div>
      <div class="absolute bg-[#54e3d5] blur-[75px] bottom-[-205px] h-[512px] opacity-20 right-[-128px] rounded-full w-[640px]"></div>
    </div>

    <!-- Main container -->
    <div class="flex h-screen items-start relative w-full">
      <!-- Sidebar -->
      <AppSidebar @toggle-profile="toggleProfile" />

      <!-- Main content -->
      <main class="flex flex-1 flex-col h-full items-start min-h-0 min-w-0 overflow-y-auto overflow-x-hidden relative">
        <RouterView />
      </main>
    </div>

    <!-- Profile Settings Panel (slide-over drawer) -->
    <Transition name="profile-panel">
      <ProfilePanel v-if="showProfilePanel" @close="closeProfile" />
    </Transition>

    <!-- Overlay for profile panel -->
    <Transition name="profile-overlay">
      <div 
        v-if="showProfilePanel" 
        class="fixed inset-0 z-40 backdrop-blur-[12px] bg-[rgba(0,0,0,0.3)]"
        @click="closeProfile"
      ></div>
    </Transition>
  </div>
</template>

<style scoped>
/* Profile panel slide-in from right */
.profile-panel-enter-active,
.profile-panel-leave-active {
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.profile-panel-enter-from,
.profile-panel-leave-to {
  transform: translateX(100%);
}

/* Overlay fade */
.profile-overlay-enter-active,
.profile-overlay-leave-active {
  transition: opacity 0.3s ease;
}
.profile-overlay-enter-from,
.profile-overlay-leave-to {
  opacity: 0;
}
</style>
