<script setup>
import { Users, Zap, Layers, BarChart } from 'lucide-vue-next';
</script>

<template>
  <section class="py-24 px-4 w-full max-w-5xl mx-auto">
    
    <!-- 4-Card Bento Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      
      <!-- Card 1: The Audience -->
      <div class="group bg-[#0A0A0B] rounded-[2rem] border border-white/5 p-10 transition-all duration-300 hover:-translate-y-1 hover:border-white/10 hover:shadow-[0_0_40px_rgba(255,255,255,0.03)]">
        <div class="w-14 h-14 rounded-2xl bg-white/5 flex items-center justify-center mb-8 border border-white/10 group-hover:bg-white/10 transition-colors">
          <Users class="w-7 h-7 text-white" />
        </div>
        <div class="text-[11px] font-bold tracking-widest text-[#88FFF3] uppercase mb-2">The Audience</div>
        <h3 class="text-2xl font-semibold text-white mb-4">Massive Built-in Reach</h3>
        <p class="text-white/50 leading-relaxed text-[17px]">
          Deliver your tracks directly to over 400 million users via pre-installed mobile music apps. No algorithms to fight, just real listeners.
        </p>
      </div>

      <!-- Card 2: The Speed -->
      <div class="group bg-[#0A0A0B] rounded-[2rem] border border-white/5 p-10 transition-all duration-300 hover:-translate-y-1 hover:border-white/10 hover:shadow-[0_0_40px_rgba(255,255,255,0.03)]">
        <div class="w-14 h-14 rounded-2xl bg-white/5 flex items-center justify-center mb-8 border border-white/10 group-hover:bg-white/10 transition-colors">
          <Zap class="w-7 h-7 text-white" />
        </div>
        <div class="text-[11px] font-bold tracking-widest text-[#FFB34F] uppercase mb-2">The Speed</div>
        <h3 class="text-2xl font-semibold text-white mb-4">Lightning Distribution</h3>
        <p class="text-white/50 leading-relaxed text-[17px]">
          No tedious waiting. Our frictionless pipeline processes your files instantly. Go live globally in the very next minute.
        </p>
      </div>

      <!-- Card 3: The Content -->
      <div class="group bg-[#0A0A0B] rounded-[2rem] border border-white/5 p-10 transition-all duration-300 hover:-translate-y-1 hover:border-white/10 hover:shadow-[0_0_40px_rgba(255,255,255,0.03)]">
        <div class="w-14 h-14 rounded-2xl bg-white/5 flex items-center justify-center mb-8 border border-white/10 group-hover:bg-white/10 transition-colors">
          <Layers class="w-7 h-7 text-white" />
        </div>
        <div class="text-[11px] font-bold tracking-widest text-[#FF0770] uppercase mb-2">The Content</div>
        <h3 class="text-2xl font-semibold text-white mb-4">AIGC Fully Welcomed</h3>
        <p class="text-white/50 leading-relaxed text-[17px]">
          We embrace all creators. Import from your favorite external generation tools and let our smart AI match your music DNA.
        </p>
      </div>

      <!-- Card 4: The Data -->
      <div class="group bg-[#0A0A0B] rounded-[2rem] border border-white/5 p-10 transition-all duration-300 hover:-translate-y-1 hover:border-white/10 hover:shadow-[0_0_40px_rgba(255,255,255,0.03)]">
        <div class="w-14 h-14 rounded-2xl bg-white/5 flex items-center justify-center mb-8 border border-white/10 group-hover:bg-white/10 transition-colors">
          <BarChart class="w-7 h-7 text-white" />
        </div>
        <div class="text-[11px] font-bold tracking-widest text-zinc-400 uppercase mb-2">The Data</div>
        <h3 class="text-2xl font-semibold text-white mb-4">Transparent Studio</h3>
        <p class="text-white/50 leading-relaxed text-[17px]">
          Track plays, audience demographics, and trending metrics in real-time through your dedicated creator dashboard.
        </p>
      </div>

    </div>
  </section>
</template>
