<script setup>
import { Smartphone, Zap, Sparkles, Brain, BarChart, ShieldCheck } from 'lucide-vue-next';
</script>

<template>
  <section id="features" class="py-24 px-4 w-full max-w-6xl mx-auto">
    <div class="mb-16 text-center">
      <h2 class="text-3xl md:text-5xl font-bold text-white tracking-tight">Built for the AI Music Era</h2>
    </div>

    <!-- 6-Card Bento Grid (3x2) -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      
      <!-- Card 1 -->
      <div class="group bg-[#0A0A0B] rounded-[2rem] border border-white/10 p-8 transition-all duration-300 hover:-translate-y-1 hover:border-white/20 hover:shadow-[0_0_40px_rgba(0,240,255,0.15)]">
        <div class="w-12 h-12 rounded-xl bg-white/5 flex items-center justify-center mb-6 border border-white/10 group-hover:bg-[#00F0FF]/10 group-hover:border-[#00F0FF]/30 transition-colors">
          <Smartphone class="w-6 h-6 text-white group-hover:text-[#00F0FF] transition-colors" />
        </div>
        <h3 class="text-xl font-semibold text-white mb-3 tracking-tight">Massive Mobile Reach</h3>
        <p class="text-zinc-400 leading-relaxed text-sm">
          Deliver your tracks directly to 400 million+ users via pre-installed mobile music apps worldwide.
        </p>
      </div>

      <!-- Card 2 -->
      <div class="group bg-[#0A0A0B] rounded-[2rem] border border-white/10 p-8 transition-all duration-300 hover:-translate-y-1 hover:border-white/20 hover:shadow-[0_0_40px_rgba(112,0,255,0.15)]">
        <div class="w-12 h-12 rounded-xl bg-white/5 flex items-center justify-center mb-6 border border-white/10 group-hover:bg-[#7000FF]/10 group-hover:border-[#7000FF]/30 transition-colors">
          <Zap class="w-6 h-6 text-white group-hover:text-[#7000FF] transition-colors" />
        </div>
        <h3 class="text-xl font-semibold text-white mb-3 tracking-tight">Lightning Distribution</h3>
        <p class="text-zinc-400 leading-relaxed text-sm">
          Powered by our seamless and frictionless pipeline, your track could reach global listeners in the very next minute.
        </p>
      </div>

      <!-- Card 3 -->
      <div class="group bg-[#0A0A0B] rounded-[2rem] border border-white/10 p-8 transition-all duration-300 hover:-translate-y-1 hover:border-white/20 hover:shadow-[0_0_40px_rgba(255,179,79,0.15)]">
        <div class="w-12 h-12 rounded-xl bg-white/5 flex items-center justify-center mb-6 border border-white/10 group-hover:bg-[#FFB34F]/10 group-hover:border-[#FFB34F]/30 transition-colors">
          <Sparkles class="w-6 h-6 text-white group-hover:text-[#FFB34F] transition-colors" />
        </div>
        <h3 class="text-xl font-semibold text-white mb-3 tracking-tight">AIGC Welcomed</h3>
        <p class="text-zinc-400 leading-relaxed text-sm">
          We fully embrace AI-generated music. Creativity has no boundaries, and your tools should never be a limitation.
        </p>
      </div>

      <!-- Card 4 -->
      <div class="group bg-[#0A0A0B] rounded-[2rem] border border-white/10 p-8 transition-all duration-300 hover:-translate-y-1 hover:border-white/20 hover:shadow-[0_0_40px_rgba(112,0,255,0.15)]">
        <div class="w-12 h-12 rounded-xl bg-white/5 flex items-center justify-center mb-6 border border-white/10 group-hover:bg-[#7000FF]/10 group-hover:border-[#7000FF]/30 transition-colors">
          <Brain class="w-6 h-6 text-white group-hover:text-[#7000FF] transition-colors" />
        </div>
        <h3 class="text-xl font-semibold text-white mb-3 tracking-tight">Smart Algorithms</h3>
        <p class="text-zinc-400 leading-relaxed text-sm">
          Advanced AI analyzes your music DNA to match your tracks with the perfect audience globally.
        </p>
      </div>

      <!-- Card 5 -->
      <div class="group bg-[#0A0A0B] rounded-[2rem] border border-white/10 p-8 transition-all duration-300 hover:-translate-y-1 hover:border-white/20 hover:shadow-[0_0_40px_rgba(0,240,255,0.15)]">
        <div class="w-12 h-12 rounded-xl bg-white/5 flex items-center justify-center mb-6 border border-white/10 group-hover:bg-[#00F0FF]/10 group-hover:border-[#00F0FF]/30 transition-colors">
          <BarChart class="w-6 h-6 text-white group-hover:text-[#00F0FF] transition-colors" />
        </div>
        <h3 class="text-xl font-semibold text-white mb-3 tracking-tight">Transparent Data</h3>
        <p class="text-zinc-400 leading-relaxed text-sm">
          Track plays, audience demographics, and revenue with our detailed and transparent dashboard.
        </p>
      </div>

      <!-- Card 6 -->
      <div class="group bg-[#0A0A0B] rounded-[2rem] border border-white/10 p-8 transition-all duration-300 hover:-translate-y-1 hover:border-white/20 hover:shadow-[0_0_40px_rgba(255,255,255,0.15)]">
        <div class="w-12 h-12 rounded-xl bg-white/5 flex items-center justify-center mb-6 border border-white/10 group-hover:bg-white/10 group-hover:border-white/30 transition-colors">
          <ShieldCheck class="w-6 h-6 text-white group-hover:text-white transition-colors" />
        </div>
        <h3 class="text-xl font-semibold text-white mb-3 tracking-tight">Open & Compliant</h3>
        <p class="text-zinc-400 leading-relaxed text-sm">
          We champion the freedom to upload. You are welcome to share any content, as long as it is legally compliant.
        </p>
      </div>

    </div>
  </section>
</template>
