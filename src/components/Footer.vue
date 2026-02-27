<script setup>
import { Github, Twitter, Mail } from 'lucide-vue-next';
</script>

<template>
  <!-- Full-width World Map Banner -->
  <section class="w-full relative py-20 bg-black overflow-hidden flex flex-col items-center justify-center">
    <!-- Image with gradient masks for seamless blending -->
    <div class="absolute inset-0 z-0">
      <img src="https://vansound.com/assets/world-image.webp" alt="Map" class="w-full h-full object-cover opacity-50" />
      <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-black"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-black via-transparent to-black"></div>
    </div>
    
    <div class="relative z-10 flex flex-col items-center text-center max-w-3xl px-4 mt-10">
      <h2 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white tracking-tight mb-4 drop-shadow-md">
        Every Creator Deserves a Stage.
      </h2>
      <p class="text-lg text-white/50 mb-10 max-w-xl">
        We bridge the gap between creators and the massive potential of mobile ecosystem listeners.
      </p>
      <button class="bg-white text-black px-8 py-4 rounded-full font-bold text-lg hover:scale-105 transition-transform duration-300 shadow-[0_0_30px_rgba(255,255,255,0.2)]">
        Launch Creator Studio
      </button>
    </div>
  </section>

  <footer class="w-full border-t border-white/5 bg-black py-16 px-6">
    <div class="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-start md:items-center gap-10">
      
      <div class="flex flex-col gap-4">
        <span class="text-2xl font-bold tracking-widest text-white">VANSO</span>
        <p class="text-sm text-zinc-500 max-w-xs">Connecting AI generations with global mobile audiences.</p>
        <div class="flex gap-4 mt-2">
          <a href="#" class="text-zinc-500 hover:text-white transition-colors">
            <Twitter class="w-5 h-5" />
          </a>
          <a href="#" class="text-zinc-500 hover:text-white transition-colors">
            <Github class="w-5 h-5" />
          </a>
          <a href="mailto:service@vansound.com" class="text-zinc-500 hover:text-white transition-colors">
            <Mail class="w-5 h-5" />
          </a>
        </div>
      </div>

      <!-- Legal Links based on Vansound -->
      <div class="flex flex-col sm:flex-row gap-6 sm:gap-12 w-full md:w-auto">
        <div class="flex flex-col gap-3">
          <h4 class="text-white font-medium mb-1">Company</h4>
          <a href="#" class="text-zinc-400 hover:text-white text-sm transition-colors">About Us</a>
          <a href="#" class="text-zinc-400 hover:text-white text-sm transition-colors">Contact</a>
        </div>
        <div class="flex flex-col gap-3">
          <h4 class="text-white font-medium mb-1">Legal</h4>
          <a href="#" class="text-zinc-400 hover:text-white text-sm transition-colors">Privacy Policy</a>
          <a href="#" class="text-zinc-400 hover:text-white text-sm transition-colors">User Agreement</a>
          <a href="#" class="text-zinc-400 hover:text-white text-sm transition-colors">Copyright Policy</a>
        </div>
      </div>
    </div>

    <div class="max-w-6xl mx-auto mt-16 pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-4">
      <p class="text-sm text-zinc-600">© 2026 Vanso. All rights reserved.</p>
    </div>
  </footer>
</template>
