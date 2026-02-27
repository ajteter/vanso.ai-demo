<script setup>
import { UploadCloud } from 'lucide-vue-next';
</script>

<template>
  <section class="relative min-h-[80vh] flex flex-col items-center justify-center text-center px-4 overflow-hidden pt-20">
    
    <!-- Background Aura -->
    <div class="absolute inset-0 z-0 flex items-center justify-center pointer-events-none opacity-30">
      <div class="absolute w-[60vw] h-[60vw] max-w-[800px] max-h-[800px] rounded-full blur-[120px] bg-[radial-gradient(circle,rgba(139,92,246,0.8)_0%,rgba(6,182,212,0.8)_100%)] animate-fluid"></div>
    </div>

    <div class="relative z-10 flex flex-col items-center w-full max-w-5xl mx-auto space-y-4">
      <!-- Headline -->
      <h1 class="text-5xl md:text-7xl lg:text-8xl w-full flex flex-col items-center font-extrabold tracking-tight drop-shadow-lg leading-[1.1]">
        <span class="text-white block w-full">Turn AI Music Into Global Hits.</span>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#88FFF3] via-[#FFB34F] to-[#FF0770] block w-full mt-2 lg:mt-4">
          Reach 400M+ Listeners.
        </span>
      </h1>

      <!-- Subheadline -->
      <p class="text-lg md:text-xl text-white/60 max-w-3xl px-4 pt-4 leading-relaxed font-normal">
        The bridge between your AI generations and pre-installed mobile music apps worldwide. Listen to viral drops, or upload yours to trend globally.
      </p>

      <!-- CTAs -->
      <div class="flex flex-col md:flex-row items-center justify-center gap-4 w-full px-8 md:px-0 pt-4">
        
        <!-- Primary (Consumer) -->
        <button class="w-full md:w-auto bg-gradient-to-r from-purple-500 to-cyan-500 text-white font-semibold rounded-full px-8 py-4 text-lg shadow-[0_0_30px_rgba(139,92,246,0.3)] hover:shadow-[0_0_40px_rgba(6,182,212,0.5)] hover:scale-105 transition-all duration-300">
          Download App
        </button>

        <!-- Secondary (Creator) -->
        <button class="w-full md:w-auto flex items-center justify-center gap-2 bg-white/5 border border-white/10 text-white rounded-full px-8 py-4 text-lg font-medium hover:bg-white/10 hover:border-white/20 transition-all duration-300 backdrop-blur-md">
          <UploadCloud class="w-5 h-5 opacity-70" />
          <span>Login to Upload</span>
        </button>

      </div>
    </div>

  </section>
</template>
