<script setup>
import { Twitter, Navigation, MessageCircle, Mail } from 'lucide-vue-next';
</script>

<template>
  <!-- Full-width World Map Banner -->
  <section id="about" class="w-full relative py-20 bg-black overflow-hidden flex flex-col items-center justify-center">
    <!-- Image with gradient masks for seamless blending -->
    <div class="absolute inset-0 z-0">
      <img src="https://vansound.com/assets/world-image.webp" alt="Map" class="w-full h-full object-cover opacity-50" />
      <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-black"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-black via-transparent to-black"></div>
    </div>
    
    <div class="relative z-10 flex flex-col items-center text-center max-w-4xl px-4 mt-10">
      <h2 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white tracking-tight mb-8 drop-shadow-md">
        Music the World
      </h2>
      <p class="text-lg md:text-xl text-white/60 mb-10 max-w-4xl leading-relaxed">
        Vanso is dedicated to democratizing music distribution. We believe in a future where every creator—whether using instruments or algorithms—has a stage. We bridge the gap between creators and the massive potential of mobile ecosystem listeners, building native experiences that make music discovery feel effortless for hundreds of millions of users.
      </p>
      <button class="bg-white text-black px-10 py-4 rounded-full font-bold text-lg hover:scale-105 transition-transform duration-300 shadow-[0_0_30px_rgba(255,255,255,0.2)]">
        Launch Creator Studio
      </button>
    </div>
  </section>

  <footer id="footer" class="w-full border-t border-white/5 bg-black py-12 px-6">
    <div class="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-start md:items-center gap-10">
      
      <!-- Brand & Socials -->
      <div class="flex flex-col gap-4">
        <span class="text-2xl font-bold tracking-widest text-white">VANSO</span>
        <div class="flex gap-4 mt-2">
          <a href="#" class="text-zinc-500 hover:text-white transition-colors" aria-label="X (Twitter)">
            <Twitter class="w-5 h-5" />
          </a>
          <a href="#" class="text-zinc-500 hover:text-white transition-colors" aria-label="TikTok">
            <Navigation class="w-5 h-5" />
          </a>
          <a href="#" class="text-zinc-500 hover:text-white transition-colors" aria-label="Discord">
            <MessageCircle class="w-5 h-5" />
          </a>
        </div>
      </div>

      <!-- Contact Info -->
      <div class="flex flex-col gap-2 text-sm text-zinc-400">
        <p>Email: <a href="mailto:service@vansound.com" class="hover:text-white transition-colors">service@vansound.com</a></p>
        <p>Business Inquiries: <a href="mailto:office2025@vansound.com" class="hover:text-white transition-colors">office2025@vansound.com</a></p>
      </div>
      
    </div>

    <div class="max-w-6xl mx-auto mt-12 pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6">
      <!-- Legal Links (Horizontal Row) -->
      <div class="flex flex-wrap justify-center md:justify-start gap-6 text-sm">
        <a href="#" class="text-zinc-500 hover:text-white transition-colors">Privacy Policy</a>
        <a href="#" class="text-zinc-500 hover:text-white transition-colors">User Agreement</a>
        <a href="#" class="text-zinc-500 hover:text-white transition-colors">Community Guidelines</a>
        <a href="#" class="text-zinc-500 hover:text-white transition-colors">Copyright Policy</a>
      </div>

      <p class="text-sm text-zinc-600">© 2026 Vanso. All rights reserved.</p>
    </div>
  </footer>
</template>
