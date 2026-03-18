<script setup>
import { ref, computed } from 'vue';

// --- State ---
const activePage = ref('overview');
const activeFilter = ref('7d');
const activeSort = ref('plays');

const cardDefs = [
  { id: 1, title: '播放总数', value: '12,450', color: '#FFFFFF' },
  { id: 2, title: '互动总量', value: '843',    color: '#ECA08B' },
  { id: 3, title: '新增粉丝', value: '120',    color: '#F5328A' },
  { id: 4, title: '主页访问', value: '3,200',  color: '#54E3D5' },
];
const activeCard = ref(cardDefs[0]);

const chartTitle = computed(() => activeCard.value.title);
const chartColor = computed(() => activeCard.value.color);

const tracks = [
  { id: 1, title: 'Cyberpunk City',                                  date: '2026-03-01', plays: '12,540', completion: '42%', isDraft: false, iconColor: 'text-vanso-cyan/60' },
  { id: 2, title: 'Neon Lights Extended Version With Very Long Title', date: '2026-02-24', plays: '8,320',  completion: '58%', isDraft: false, iconColor: 'text-vanso-peach/60' },
  { id: 3, title: 'Silent Echoes (Draft)',                            date: '刚刚上传',    plays: '0',      completion: '-',   isDraft: true,  iconColor: 'text-zinc-700' },
];

// --- Drawer ---
const drawerOpen   = ref(false);
const drawerData   = ref({ title: '', plays: '0', completion: '0%', isZero: true, likes: 0, saves: 0, comments: 0 });
const drawerChartPercent = computed(() => parseInt(drawerData.value.completion) || 0);

function openDrawer(track) {
  drawerData.value.title      = track.title;
  drawerData.value.plays      = track.plays;
  drawerData.value.completion = track.completion;
  drawerData.value.isZero     = track.plays === '0';
  if (!drawerData.value.isZero) {
    drawerData.value.likes    = Math.floor(Math.random() * 500) + 50;
    drawerData.value.saves    = Math.floor(Math.random() * 200) + 10;
    drawerData.value.comments = Math.floor(Math.random() * 50)  + 1;
  } else {
    drawerData.value.likes = drawerData.value.saves = drawerData.value.comments = 0;
  }
  drawerOpen.value = true;
  document.body.style.overflow = 'hidden';
}

function closeDrawer() {
  drawerOpen.value = false;
  document.body.style.overflow = '';
}
</script>

<template>
  <!-- Page wrapper: matches other Studio pages padding/max-width -->
  <div class="flex flex-col gap-8 items-start max-w-320 p-10 w-full">

    <!-- ── Page Header ── -->
    <div class="flex items-center justify-between w-full">
      <h1 class="font-bold text-[30px] text-white tracking-[-0.75px] leading-[36px]">Statistics</h1>

      <!-- Tab Toggle -->
      <div class="flex items-center gap-8">
        <button
          class="stat-tab text-sm font-medium pb-4 transition-colors"
          :class="activePage === 'overview' ? 'active' : 'text-zinc-500 hover:text-white'"
          @click="activePage = 'overview'"
        >数据总览</button>
        <button
          class="stat-tab text-sm font-medium pb-4 transition-colors"
          :class="activePage === 'tracks' ? 'active' : 'text-zinc-500 hover:text-white'"
          @click="activePage = 'tracks'"
        >单曲数据</button>
      </div>
    </div>

    <!-- ════════════════════ PAGE 1: OVERVIEW ════════════════════ -->
    <div v-show="activePage === 'overview'" class="stat-page flex-col gap-8 w-full active">

      <!-- Filter pills -->
      <div class="bg-white/5 border border-white/10 p-1 rounded-lg flex self-start">
        <button
          v-for="f in [{ id:'7d', label:'近 7 日' }, { id:'30d', label:'近 30 日' }]"
          :key="f.id"
          class="px-6 py-1.5 rounded-md font-medium text-sm whitespace-nowrap cursor-pointer transition-all"
          :class="activeFilter === f.id ? 'text-white bg-white/10' : 'text-zinc-500 hover:text-white'"
          @click="activeFilter = f.id"
        >{{ f.label }}</button>
      </div>

      <!-- Summary Cards -->
      <div class="grid grid-cols-4 gap-5 w-full">
        <div
          v-for="card in cardDefs"
          :key="card.id"
          class="metric-card bg-vanso-card rounded-2xl p-6 flex flex-col gap-2 cursor-pointer border border-white/10 transition-all duration-200"
          :class="activeCard.id === card.id ? 'card-active' : 'hover:bg-white/5'"
          :style="{ '--card-color': activeCard.id === card.id ? card.color : 'rgba(255,255,255,0.1)' }"
          @click="activeCard = card"
        >
          <span class="text-zinc-500 font-medium text-sm tracking-wide truncate">{{ card.title }}</span>
          <div class="text-3xl font-bold text-white mt-1 truncate tracking-tight">{{ card.value }}</div>
        </div>
      </div>

      <!-- Trend Chart -->
      <div
        class="bg-vanso-card border border-white/10 rounded-3xl p-8 w-full flex flex-col gap-6 relative"
        :style="{ '--chart-color': chartColor }"
      >
        <h3 class="font-bold text-lg text-white">{{ chartTitle }}</h3>
        <div class="w-full h-72 relative mt-2">
          <svg class="w-full h-full overflow-visible" preserveAspectRatio="none" viewBox="0 0 1000 240">
            <defs>
              <linearGradient id="cg" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%"   stop-color="var(--chart-color)" stop-opacity="0.15"/>
                <stop offset="100%" stop-color="var(--chart-color)" stop-opacity="0"/>
              </linearGradient>
            </defs>
            <path d="M0,40 L1000,40 M0,100 L1000,100 M0,160 L1000,160 M0,220 L1000,220"
                  stroke="rgba(255,255,255,0.04)" stroke-width="1" fill="none" stroke-dasharray="4 6"/>
            <g class="transition-all duration-500">
              <path d="M0,240 L0,180 C100,150 200,200 300,140 C400,90 500,150 600,80 C700,50 800,110 900,40 C950,20 1000,60 1000,60 L1000,240 Z"
                    fill="url(#cg)"/>
              <path d="M0,180 C100,150 200,200 300,140 C400,90 500,150 600,80 C700,50 800,110 900,40 C950,20 1000,60 1000,60"
                    fill="none" stroke="var(--chart-color)" stroke-width="3" stroke-linecap="round"/>
            </g>
          </svg>

          <!-- Tooltip dot -->
          <div class="absolute top-[25%] left-[80%] -translate-x-1/2 -translate-y-[130%]
                      bg-zinc-900/95 backdrop-blur-md border border-white/10 text-white
                      px-4 py-2.5 rounded-xl shadow-xl pointer-events-none flex flex-col items-center z-10 min-w-[80px]">
            <span class="text-zinc-400 mb-1 text-xs text-center">03-06</span>
            <span class="font-bold text-[var(--chart-color)] text-sm text-center">3,200</span>
            <div class="absolute bottom-[-5px] left-1/2 -translate-x-1/2 w-2 h-2
                        bg-zinc-900/95 border-r border-b border-white/10 rotate-45"/>
          </div>
          <div class="absolute top-[25%] left-[80%] w-3.5 h-3.5 rounded-full -translate-x-1/2 -translate-y-1/2 z-10 transition-colors"
               :style="{ background: chartColor, boxShadow: `0 0 12px ${chartColor}` }"/>

          <!-- X-Axis labels -->
          <div class="absolute bottom-[-28px] left-0 w-full flex justify-between text-zinc-500 text-xs font-medium">
            <span v-for="d in ['03-01','03-02','03-03','03-04','03-05','03-06','03-07']" :key="d">{{ d }}</span>
          </div>
        </div>
      </div>

      <!-- Engagement Breakdown -->
      <div class="grid grid-cols-2 gap-5 w-full mt-2">
        <div class="bg-vanso-card border border-white/10 rounded-3xl p-8 flex flex-col gap-6">
          <h3 class="font-bold text-lg text-white">互动构成</h3>
          <div class="flex items-center gap-12 px-2">
            <!-- Donut -->
            <div class="relative w-28 h-28 shrink-0">
              <svg class="w-full h-full -rotate-90" viewBox="0 0 36 36">
                <circle cx="18" cy="18" r="15.9" fill="transparent" stroke="rgba(255,255,255,0.05)" stroke-width="4"/>
                <circle cx="18" cy="18" r="15.9" fill="transparent" stroke="#54E3D5" stroke-width="4" stroke-dasharray="10 90" stroke-linecap="round"/>
                <circle cx="18" cy="18" r="15.9" fill="transparent" stroke="#ECA08B" stroke-width="4" stroke-dasharray="30 70" stroke-dashoffset="-10" stroke-linecap="round"/>
                <circle cx="18" cy="18" r="15.9" fill="transparent" stroke="#F5328A" stroke-width="4" stroke-dasharray="60 40" stroke-dashoffset="-40" stroke-linecap="round"/>
              </svg>
            </div>
            <!-- Legend -->
            <div class="flex flex-col gap-4 flex-1">
              <div v-for="item in [
                { label:'点赞', pct:'60%', color:'text-vanso-peach' },
                { label:'收藏', pct:'30%', color:'text-vanso-magenta' },
                { label:'评论', pct:'10%', color:'text-vanso-cyan' },
              ]" :key="item.label" class="flex items-center gap-3">
                <span class="w-2 h-2 rounded-full shrink-0" :class="item.color.replace('text-','bg-')"/>
                <span class="text-zinc-400 text-sm flex-1">{{ item.label }}</span>
                <span class="text-white text-sm font-semibold">{{ item.pct }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ════════════════════ PAGE 2: TRACKS ════════════════════ -->
    <div v-show="activePage === 'tracks'" class="stat-page flex-col gap-5 w-full active">

      <!-- Sort bar -->
      <div class="flex items-center w-full">
        <div class="bg-white/5 border border-white/10 p-1 rounded-lg flex">
          <button
            v-for="s in [{ id:'plays', label:'按播放量' }, { id:'date', label:'按发布时间' }]"
            :key="s.id"
            class="px-5 py-1.5 rounded-md font-medium text-sm whitespace-nowrap cursor-pointer transition-all"
            :class="activeSort === s.id ? 'text-white bg-white/10' : 'text-zinc-500 hover:text-white'"
            @click="activeSort = s.id"
          >{{ s.label }}</button>
        </div>
      </div>

      <!-- Track list -->
      <div class="flex flex-col gap-3 w-full">
        <div
          v-for="track in tracks"
          :key="track.id"
          class="track-item bg-vanso-card border border-white/10 rounded-2xl p-5 flex items-center justify-between
                 transition-all cursor-pointer group hover:bg-white/5"
          @click="openDrawer(track)"
        >
          <div class="flex items-center gap-4 min-w-0 pr-4 max-w-[60%]">
            <div class="w-12 h-12 rounded-xl flex items-center justify-center shrink-0 border"
                 :class="track.isDraft ? 'bg-zinc-900 border-zinc-800/50' : 'bg-zinc-800/60 border-white/10'">
              <svg class="w-5 h-5" :class="track.iconColor" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>
              </svg>
            </div>
            <div class="flex flex-col gap-0.5 min-w-0">
              <span class="font-semibold text-sm transition-colors truncate" :class="track.isDraft ? 'text-zinc-400' : 'text-white'">{{ track.title }}</span>
              <span class="text-xs truncate" :class="track.isDraft ? 'text-zinc-600' : 'text-zinc-500'">{{ track.date }}</span>
            </div>
          </div>
          <div class="flex items-center gap-12 shrink-0">
            <div class="flex flex-col text-right">
              <span class="text-xs text-zinc-500 mb-0.5">播放量</span>
              <span class="font-bold text-sm" :class="track.isDraft ? 'text-zinc-500' : 'text-white'">{{ track.plays }}</span>
            </div>
            <div class="flex flex-col text-right w-12">
              <span class="text-xs text-zinc-500 mb-0.5">完播率</span>
              <span class="font-bold text-sm" :class="track.isDraft ? 'text-zinc-600' : 'text-white'">{{ track.completion }}</span>
            </div>
            <svg class="w-5 h-5 text-zinc-600 group-hover:text-white transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5l7 7-7 7"/>
            </svg>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ════════ Track Detail Drawer (slides from right) ════════ -->
  <div
    class="fixed inset-0 z-50 flex justify-end"
    :style="{ pointerEvents: drawerOpen ? 'auto' : 'none', opacity: drawerOpen ? 1 : 0, transition: 'opacity 0.3s ease' }"
  >
    <!-- Backdrop -->
    <div class="absolute inset-0 bg-black/60 backdrop-blur-sm cursor-pointer" @click="closeDrawer"/>
    <!-- Panel -->
    <div
      class="relative w-[480px] max-w-full h-full bg-vanso-card border-l border-white/10 shadow-2xl flex flex-col"
      :style="{ transform: drawerOpen ? 'translateX(0)' : 'translateX(100%)', transition: 'transform 0.3s cubic-bezier(0.16,1,0.3,1)' }"
    >
      <!-- Close -->
      <button class="absolute top-5 right-5 p-2 rounded-full hover:bg-white/10 text-zinc-500 hover:text-white transition-colors cursor-pointer z-10" @click="closeDrawer">
        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>

      <div class="p-7 overflow-y-auto flex-1 flex flex-col gap-7 custom-scrollbar">
        <!-- Track Info -->
        <div class="flex items-center gap-4 mt-2">
          <div class="w-16 h-16 rounded-xl bg-zinc-800/60 border border-white/10 flex items-center justify-center shrink-0">
            <svg class="w-7 h-7 text-vanso-cyan/50" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/>
            </svg>
          </div>
          <div class="flex flex-col gap-1 pr-10 min-w-0">
            <h2 class="text-lg font-bold text-white leading-snug line-clamp-2 break-words">{{ drawerData.title }}</h2>
            <p class="text-xs text-zinc-500">上传时间: 2026-03-01</p>
          </div>
        </div>

        <!-- Hero metrics -->
        <div class="grid grid-cols-2 gap-3 h-32">
          <div class="bg-zinc-950/60 border border-white/10 rounded-2xl p-5 flex flex-col justify-between relative overflow-hidden">
            <span class="text-zinc-500 text-xs font-medium">累计播放次数</span>
            <span class="text-2xl font-bold text-white tracking-tight truncate">{{ drawerData.plays }}</span>
          </div>
          <div class="bg-zinc-950/60 border border-white/10 rounded-2xl p-5 flex flex-col items-end justify-end relative overflow-hidden">
            <span class="text-zinc-500 text-xs font-medium absolute top-5 left-5">完播率</span>
            <!-- Donut ring -->
            <div v-show="!drawerData.isZero" class="relative w-16 h-16 flex items-center justify-center">
              <svg class="w-full h-full -rotate-90 absolute inset-0" viewBox="0 0 36 36">
                <circle cx="18" cy="18" r="16" fill="transparent" stroke="rgba(255,255,255,0.05)" stroke-width="3"/>
                <circle cx="18" cy="18" r="16" fill="transparent" stroke="#FFFFFF" stroke-width="3"
                        :stroke-dasharray="`${drawerChartPercent} 100`" stroke-linecap="round"
                        class="transition-all duration-700 ease-out"/>
              </svg>
              <span class="text-sm font-bold text-white z-10">{{ drawerData.completion }}</span>
            </div>
            <div v-show="drawerData.isZero" class="absolute inset-0 flex items-center justify-center">
              <span class="text-xs text-zinc-600">暂无数据</span>
            </div>
          </div>
        </div>

        <!-- Interaction Details -->
        <div class="flex flex-col gap-3">
          <div class="flex items-center gap-3">
            <span class="text-xs font-medium text-zinc-500 shrink-0">互动明细</span>
            <div class="h-px flex-1 bg-white/10"/>
          </div>
          <div class="grid grid-cols-3 gap-3">
            <div v-for="stat in [
              { label:'点赞',  val: drawerData.likes,    color:'text-vanso-peach/70',   icon:'M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5' },
              { label:'收藏',  val: drawerData.saves,    color:'text-vanso-magenta/70', icon:'M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z' },
              { label:'评论',  val: drawerData.comments, color:'text-vanso-cyan/70',    icon:'M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z' },
            ]" :key="stat.label"
               class="bg-zinc-950/60 border border-white/10 rounded-xl p-4 flex flex-col items-center gap-2">
              <svg class="w-5 h-5" :class="stat.color" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" :d="stat.icon"/>
              </svg>
              <div class="flex flex-col items-center gap-0.5 w-full">
                <span class="text-xl font-bold text-white truncate w-full text-center">{{ stat.val }}</span>
                <span class="text-xs text-zinc-600 text-center">{{ stat.label }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Page tab indicator */
.stat-tab {
  position: relative;
  color: #71717A;
}
.stat-tab.active {
  color: #FFFFFF;
  font-weight: 700;
}
.stat-tab.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: #FFFFFF;
  border-radius: 2px;
}

/* Metric card glow on active */
.metric-card.card-active {
  border-color: var(--card-color);
  box-shadow: 0 0 16px -4px var(--card-color);
}

/* Smooth page fade */
.stat-page {
  display: none;
  animation: fadeIn 0.3s ease-out forwards;
}
.stat-page.active {
  display: flex;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Track row press */
.track-item:active {
  transform: scale(0.99);
}

/* Drawer custom scrollbar */
.custom-scrollbar::-webkit-scrollbar { width: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
.custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #555; }
</style>
