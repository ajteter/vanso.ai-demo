<script setup>
// Mock data for the ticker
const items = Array.from({ length: 8 }, (_, i) => ({
  id: i,
  user: `@creator${i + 1}`,
  song: ['Neon Nights', 'Sonic Boom', 'Aura Pulse', 'Midnight Run', 'Cyber Stream', 'Neural Wave', 'Synth Drop', 'Bass Line'][i % 8],
  avatar: `https://api.dicebear.com/7.x/avataaars/svg?seed=vanso${i}`,
}));
</script>

<template>
  <div class="w-full overflow-hidden py-4 border-y border-white/5 bg-transparent relative z-20">
    <div class="flex animate-scroll hover:[animation-play-state:paused] w-max">
      <!-- Doubled for seamless loop -->
      <div v-for="n in 2" :key="n" class="flex gap-4 px-2">
        <div v-for="item in items" :key="item.id + '_' + n" 
             class="bg-white/5 backdrop-blur-md rounded-full px-5 py-2.5 border border-white/5 flex items-center gap-3 shrink-0 cursor-pointer hover:bg-white/10 hover:border-white/10 transition-colors">
          <img :src="item.avatar" alt="Avatar" class="w-7 h-7 rounded-full" />
          <div class="flex items-center gap-2 text-[15px]">
            <span class="text-white/60 font-medium">{{ item.user }} dropped <span class="text-white">"{{ item.song }}"</span></span>
            <span class="text-white/40 text-xs ml-1">🚀 Trending now</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.animate-scroll {
  animation: scroll 30s linear infinite;
}
</style>
