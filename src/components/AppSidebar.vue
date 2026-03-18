<script setup>
import { computed, ref, onMounted, onBeforeUnmount } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const props = defineProps({
  showProfilePanel: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(['toggle-profile']);

const currentPage = computed(() => route.name);

const showDropdown = ref(false);
const dropdownRef = ref(null);

function navigateTo(name) {
  router.push({ name });
}

function toggleDropdown() {
  showDropdown.value = !showDropdown.value;
}

function openProfile() {
  showDropdown.value = false;
  emit('toggle-profile');
}

function signOut() {
  showDropdown.value = false;
  router.push({ name: 'Landing' });
}

function handleClickOutside(e) {
  if (dropdownRef.value && !dropdownRef.value.contains(e.target)) {
    showDropdown.value = false;
  }
}

onMounted(() => document.addEventListener('click', handleClickOutside));
onBeforeUnmount(() => document.removeEventListener('click', handleClickOutside));
</script>

<template>
  <aside class="bg-vanso-card border-r border-white/10 flex flex-col h-full items-start justify-between overflow-visible p-[17px] shrink-0 w-65">
    <!-- Top section: Logo + Nav -->
    <div class="w-full">
      <div class="flex flex-col gap-10 items-center pt-[24px] w-full">
        <!-- Logo -->
        <div class="flex gap-2.5 items-center justify-center w-full cursor-pointer" @click="navigateTo('Dashboard')">
          <div class="relative rounded-full shrink-0 size-10">
            <img alt="Vanso Logo" class="absolute inset-0 object-cover pointer-events-none rounded-full size-full" src="/vanso-logo.webp" />
          </div>
          <div class="h-6 shrink-0 w-27">
            <img alt="Vanso" class="block max-w-none h-6 w-27" src="/assets/vanso-text.svg" />
          </div>
        </div>

        <!-- Navigation -->
        <nav class="flex flex-col gap-2 items-center w-full">
          <!-- Dashboard Link -->
          <button
            class="flex gap-3 items-center py-[10px] rounded-lg w-full transition-colors duration-300 cursor-pointer"
            :class="currentPage === 'Dashboard' 
              ? 'bg-white/10 border-l-2 border-vanso-magenta pl-[14px] pr-[12px]' 
              : 'px-3 hover:bg-white/5'"
            @click="navigateTo('Dashboard')"
          >
            <!-- Dashboard Icon (grid) -->
            <svg class="shrink-0 size-[18px]" :class="currentPage === 'Dashboard' ? 'text-white' : 'text-zinc-400'" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="1" y="1" width="6" height="6" rx="1.5" stroke="currentColor" stroke-width="1.5"/>
              <rect x="11" y="1" width="6" height="6" rx="1.5" stroke="currentColor" stroke-width="1.5"/>
              <rect x="1" y="11" width="6" height="6" rx="1.5" stroke="currentColor" stroke-width="1.5"/>
              <rect x="11" y="11" width="6" height="6" rx="1.5" stroke="currentColor" stroke-width="1.5"/>
            </svg>
            <span 
              class="font-['Inter',sans-serif] font-medium text-sm leading-[21px]"
              :class="currentPage === 'Dashboard' ? 'text-white' : 'text-zinc-400'"
            >Dashboard</span>
          </button>

          <!-- Statistics Link -->
          <button
            class="flex gap-3 items-center py-[10px] rounded-lg w-full transition-colors duration-300 cursor-pointer"
            :class="currentPage === 'Statistics'
              ? 'bg-white/10 border-l-2 border-vanso-magenta pl-[14px] pr-[12px]' 
              : 'px-3 hover:bg-white/5'"
            @click="navigateTo('Statistics')"
          >
            <!-- Statistics Icon (bar chart) -->
            <svg class="shrink-0 size-[18px]" :class="currentPage === 'Statistics' ? 'text-white' : 'text-zinc-400'" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="1" y="8" width="4" height="9" rx="1" stroke="currentColor" stroke-width="1.5"/>
              <rect x="7" y="4" width="4" height="13" rx="1" stroke="currentColor" stroke-width="1.5"/>
              <rect x="13" y="1" width="4" height="16" rx="1" stroke="currentColor" stroke-width="1.5"/>
            </svg>
            <span 
              class="font-['Inter',sans-serif] font-medium text-sm leading-[21px]"
              :class="currentPage === 'Statistics' ? 'text-white' : 'text-zinc-400'"
            >Statistics</span>
          </button>

          <!-- My Drops Link -->
          <button
            class="flex gap-3 items-center py-[10px] rounded-lg w-full transition-colors duration-300 cursor-pointer"
            :class="(currentPage === 'MyDrops' || currentPage === 'NewDrop')
              ? 'bg-white/10 border-l-2 border-vanso-magenta pl-[14px] pr-[12px]' 
              : 'px-3 hover:bg-white/5'"
            @click="navigateTo('MyDrops')"
          >
            <!-- My Drops Icon (music note) -->
            <svg class="shrink-0 size-[18px]" :class="(currentPage === 'MyDrops' || currentPage === 'NewDrop') ? 'text-white' : 'text-zinc-400'" viewBox="0 0 12 18" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M4 14V3.5L11 1.5V12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <circle cx="2.5" cy="14.5" r="2.5" stroke="currentColor" stroke-width="1.2"/>
              <circle cx="9.5" cy="12.5" r="2.5" stroke="currentColor" stroke-width="1.2"/>
            </svg>
            <span 
              class="font-['Inter',sans-serif] font-medium text-sm leading-[21px]"
              :class="(currentPage === 'MyDrops' || currentPage === 'NewDrop') ? 'text-white' : 'text-zinc-400'"
            >My Drops</span>
          </button>
        </nav>

      </div>
    </div>

    <!-- Bottom section: User profile -->
    <div class="w-full relative" ref="dropdownRef">
      <!-- Dropdown Menu (pops upward) -->
      <Transition name="dropdown">
        <div 
          v-if="showDropdown"
          class="absolute bottom-[68px] left-[12px] right-[12px] bg-zinc-950 border border-white/10 rounded-xl shadow-[0_-8px_30px_rgba(0,0,0,0.5)] overflow-hidden z-50"
        >
          <button
            class="flex gap-2.5 items-center w-full px-4 py-3 cursor-pointer transition-colors duration-300 hover:bg-white/5"
            @click="openProfile"
          >
            <!-- User icon -->
            <svg class="size-4 text-zinc-400" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="8" cy="5" r="3" stroke="currentColor" stroke-width="1.3"/>
              <path d="M2 14c0-2.761 2.686-5 6-5s6 2.239 6 5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
            </svg>
            <span class="font-medium text-sm text-white leading-[20px]">Profile</span>
          </button>
          <div class="h-px bg-white/10 mx-[12px]"></div>
          <button
            class="flex gap-2.5 items-center w-full px-4 py-3 cursor-pointer transition-colors duration-300 hover:bg-white/5"
            @click="signOut"
          >
            <!-- Sign out icon -->
            <svg class="size-4 text-red-500" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 14H3.333A1.333 1.333 0 0 1 2 12.667V3.333A1.333 1.333 0 0 1 3.333 2H6" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M10.667 11.333 14 8l-3.333-3.333M14 8H6" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span class="font-medium text-sm text-red-500 leading-[20px]">Sign Out</span>
          </button>
        </div>
      </Transition>

      <div class="border-t border-white/10 flex gap-3 items-center pb-[16px] pt-[17px] px-3 w-full">
        <!-- Avatar circle -->
        <div 
          class="relative rounded-full shrink-0 size-10 cursor-pointer bg-gradient-to-tr from-vanso-magenta to-vanso-cyan"
          @click="openProfile"
        >
          <div class="flex items-center justify-center size-full">
            <span class="font-['Inter',sans-serif] font-bold text-sm text-white text-center leading-[20px]">JD</span>
          </div>
        </div>
        <!-- Name -->
        <div class="shrink-0">
          <span class="font-['Inter',sans-serif] font-medium text-sm text-white leading-[20px]">John Doe</span>
        </div>
        <!-- Chevron (toggles dropdown) -->
        <svg 
          class="ml-auto shrink-0 w-[10px] h-[5px] text-zinc-400 cursor-pointer transition-transform duration-300"
          :class="showDropdown ? 'rotate-180' : ''"
          @click.stop="toggleDropdown" 
          viewBox="0 0 10 5" fill="none" xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M1 1L5 4L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.dropdown-enter-active, .dropdown-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.dropdown-enter-from, .dropdown-leave-to {
  opacity: 0;
  transform: translateY(8px);
}
</style>
