<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const stats = [
  { label: 'Total Plays', value: '12 540', change: '12%', icon: 'play_circle' },
  { label: 'Likes & Saves', value: '843', icon: 'favorite' },
];

const recentDrops = [
  { title: 'Neon Nights', date: 'Oct 24, 2023', plays: '1 204', status: 'live', cover: 1 },
  { title: 'Deep Focus', date: 'Oct 12, 2023', plays: '3 400', status: 'live', cover: 2 },
  { title: 'Urban Jungle', date: 'Sep 30, 2023', plays: '890', status: 'processing', cover: 3 },
  { title: 'Lo-Fi Sunday', date: 'Sep 15, 2023', plays: '5 100', status: 'live', cover: 4 },
  { title: 'Bass Drops', date: 'Aug 22, 2023', plays: '2 300', status: 'draft', cover: 5 },
];

function getStatusStyles(status) {
  switch (status) {
    case 'live':
      return {
        bg: 'bg-[rgba(84,227,213,0.1)]',
        border: 'shadow-[inset_0px_0px_0px_1px_rgba(84,227,213,0.5)]',
        glow: 'shadow-[0px_0px_10px_0px_rgba(84,227,213,0.3)]',
        text: 'text-vanso-cyan',
        label: 'Live',
      };
    case 'processing':
      return {
        bg: 'bg-[rgba(253,186,116,0.1)]',
        border: 'shadow-[inset_0px_0px_0px_1px_rgba(253,186,116,0.5)]',
        glow: 'shadow-[0px_0px_10px_0px_rgba(253,186,116,0.3)]',
        text: 'text-orange-300',
        label: 'Process',
      };
    case 'draft':
      return {
        bg: 'bg-white/5',
        border: 'shadow-[inset_0px_0px_0px_1px_rgba(255,255,255,0.1)]',
        glow: '',
        text: 'text-zinc-400',
        label: 'Draft',
      };
    default:
      return {
        bg: '', border: '', glow: '', text: '', label: status,
      };
  }
}

function getCoverGradient(idx) {
  const gradients = [
    'linear-gradient(135deg, #f5328a 0%, #54e3d5 100%)',
    'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
    'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
    'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
  ];
  return gradients[(idx - 1) % gradients.length];
}
</script>

<template>
  <div class="flex flex-col gap-8 items-start max-w-320 p-10 w-full">
    <!-- Header -->
    <div class="flex items-center justify-between w-full">
      <h1 class="font-bold text-[30px] text-white tracking-[-0.75px] leading-[36px]">Dashboard</h1>
      <button 
        class="bg-gradient-to-br from-vanso-magenta via-vanso-peach to-vanso-cyan text-white font-semibold rounded-full px-6 py-[10px] shadow-[0_0_20px] shadow-vanso-magenta/30 hover:shadow-[0_0_30px_rgba(84,227,213,0.5)] transition-shadow duration-300 flex items-center justify-center gap-2"
        @click="router.push({ name: 'NewDrop' })"
      >
        <!-- Plus icon -->
        <svg class="shrink-0 size-3 text-white" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M6 1V11M1 6H11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <span class="font-bold text-sm text-white text-center leading-[20px]">New Drop</span>
      </button>
    </div>

    <!-- Stats Cards -->
    <div class="flex gap-6 items-start justify-center w-full">
      <!-- Total Plays Card -->
      <div class="bg-vanso-card border border-white/10 flex flex-1 flex-col items-start overflow-hidden p-[33px] rounded-2xl h-[142px] relative">
        <!-- Background play icon watermark -->
        <div class="absolute bottom-[8px] right-[24px] opacity-[0.04]">
          <svg class="size-25 text-white" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/>
          </svg>
        </div>
        <div class="flex flex-col gap-2 items-start w-full relative z-[1]">
          <span class="font-medium text-sm text-zinc-400 tracking-[0.7px] uppercase leading-[20px]">{{ stats[0].label }}</span>
          <div class="flex gap-3 items-end w-full">
            <span class="font-bold text-[48px] leading-[48px] tracking-[-1.2px] bg-clip-text text-transparent bg-gradient-to-r from-vanso-cyan to-vanso-magenta">{{ stats[0].value }}</span>
            <div class="bg-vanso-cyan/10 border border-vanso-cyan/20 flex items-center px-[9px] py-[5px] rounded-full">
              <svg class="shrink-0 w-[17px] h-2 text-vanso-cyan mr-[2px]" viewBox="0 0 17 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M1 7L5 3L8.5 5.5L16 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M12 1H16V5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span class="font-medium text-sm text-vanso-cyan leading-[20px]">{{ stats[0].change }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Likes & Saves Card -->
      <div class="bg-vanso-card border border-white/10 flex flex-1 flex-col items-start overflow-hidden p-[33px] rounded-2xl h-[142px] relative">
        <!-- Background heart icon watermark -->
        <div class="absolute bottom-[8px] right-[24px] opacity-[0.04]">
          <svg class="size-25 text-white" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
          </svg>
        </div>
        <div class="flex flex-col gap-2 items-start w-full relative z-[1]">
          <span class="font-medium text-sm text-zinc-400 tracking-[0.7px] uppercase leading-[20px]">{{ stats[1].label }}</span>
          <div class="flex gap-3 items-end w-full">
            <span class="font-bold text-[48px] leading-[48px] tracking-[-1.2px] bg-clip-text text-transparent bg-gradient-to-r from-vanso-cyan to-vanso-magenta">{{ stats[1].value }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Recent Drops Table -->
    <div class="bg-vanso-card border border-white/10 flex flex-col items-start overflow-hidden rounded-2xl shadow-[0px_25px_50px_-12px_rgba(0,0,0,0.5)] w-full">
      <!-- Table Header -->
      <div class="border-b border-white/10 w-full">
        <div class="flex items-center justify-between py-5 px-6">
          <h3 class="font-bold text-lg text-white tracking-[-0.45px] leading-[28px]">Recent Drops</h3>
          <button class="font-medium text-sm text-vanso-cyan text-center leading-[20px] cursor-pointer hover:underline" @click="router.push({ name: 'MyDrops' })">View All</button>
        </div>
      </div>

      <!-- Table Columns Header -->
      <div class="border-b border-white/10 flex items-start w-full">
        <div class="w-24 px-6 py-4">
          <span class="font-semibold text-[11px] text-zinc-400 tracking-[1.1px] uppercase">Cover</span>
        </div>
        <div class="flex-1 px-6 py-4">
          <span class="font-semibold text-[11px] text-zinc-400 tracking-[1.1px] uppercase">Track Title</span>
        </div>
        <div class="flex-1 px-6 py-4">
          <span class="font-semibold text-[11px] text-zinc-400 tracking-[1.1px] uppercase">Upload Date</span>
        </div>
        <div class="w-50 px-6 py-4 text-right">
          <span class="font-semibold text-[11px] text-zinc-400 tracking-[1.1px] uppercase">Play Count</span>
        </div>
        <div class="w-35 px-6 py-4 text-center">
          <span class="font-semibold text-[11px] text-zinc-400 tracking-[1.1px] uppercase">Status</span>
        </div>
      </div>

      <!-- Table Body -->
      <div class="flex flex-col items-start w-full">
        <div 
          v-for="(drop, i) in recentDrops" 
          :key="i"
          class="flex items-center w-full transition-colors duration-300 hover:bg-white/5"
          :class="i > 0 ? 'border-t border-white/10' : ''"
        >
          <!-- Cover -->
          <div class="w-24 px-6 py-4">
            <div 
              class="rounded-lg size-12 border border-white/10"
              :style="{ backgroundImage: getCoverGradient(drop.cover) }"
            ></div>
          </div>
          <!-- Title -->
          <div class="flex-1 px-6 py-[30px]">
            <span class="font-medium text-sm text-white leading-[20px]">{{ drop.title }}</span>
          </div>
          <!-- Date -->
          <div class="flex-1 px-6 py-[30px]">
            <span class="font-normal text-sm text-zinc-400 leading-[20px]">{{ drop.date }}</span>
          </div>
          <!-- Play Count -->
          <div class="w-50 px-6 py-[30px] text-right">
            <span class="font-medium text-sm text-white leading-[20px]">{{ drop.plays }}</span>
          </div>
          <!-- Status Badge -->
          <div class="w-35 px-6 py-[26px] flex items-center justify-center">
            <div 
              class="flex items-center justify-center px-3 py-1 rounded-full relative"
              :class="[getStatusStyles(drop.status).bg]"
            >
              <div 
                class="absolute inset-0 rounded-full pointer-events-none"
                :class="[getStatusStyles(drop.status).border]"
              ></div>
              <span 
                class="font-bold text-[10px] tracking-[0.25px] uppercase leading-[20px] text-center relative z-[1]"
                :class="[getStatusStyles(drop.status).text]"
              >{{ getStatusStyles(drop.status).label }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
