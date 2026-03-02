<script setup>
import { Globe, Menu } from 'lucide-vue-next';
import { ref } from 'vue';

const isMenuOpen = ref(false);
const isLangOpen = ref(false);
</script>

<template>
  <div class="fixed top-0 left-0 right-0 z-50 flex justify-center mt-6 px-4 pointer-events-none transition-all duration-300">
    <nav class="flex items-center justify-between w-full max-w-5xl px-6 py-3 bg-white/5 backdrop-blur-2xl border border-white/10 rounded-full pointer-events-auto">
      
      <!-- Left: Logo -->
      <div class="flex items-center gap-2 cursor-pointer">
        <span class="text-xl font-bold tracking-widest text-white">VANSO</span>
      </div>

      <!-- Center: Links (Desktop) -->
      <div class="hidden md:flex items-center gap-6">
        <a href="#features" class="text-sm font-medium text-zinc-400 hover:text-white transition-colors duration-300">Features</a>
        <a href="#how-it-works" class="text-sm font-medium text-zinc-400 hover:text-white transition-colors duration-300">How it works</a>
        <a href="#about" class="text-sm font-medium text-zinc-400 hover:text-white transition-colors duration-300">About us</a>
        <a href="#footer" class="text-sm font-medium text-zinc-400 hover:text-white transition-colors duration-300">Contact</a>
      </div>

      <!-- Right: Actions (Desktop & Mobile) -->
      <div class="flex items-center gap-4 md:gap-5">
        
        <!-- Language Switcher -->
        <div class="relative">
          <button @click="isLangOpen = !isLangOpen" class="flex items-center gap-1 text-sm text-zinc-400 hover:text-white transition-colors duration-200">
            <Globe class="w-4 h-4" />
            <span>EN ▾</span>
          </button>
          <div v-if="isLangOpen" class="absolute top-full right-0 mt-2 w-32 bg-[#0A0A0B] border border-white/10 rounded-xl overflow-hidden py-1 shadow-2xl z-50">
            <a href="#" class="block px-4 py-2 text-sm text-zinc-400 hover:text-white hover:bg-white/5">English</a>
            <a href="#" class="block px-4 py-2 text-sm text-zinc-400 hover:text-white hover:bg-white/5">Español</a>
            <a href="#" class="block px-4 py-2 text-sm text-zinc-400 hover:text-white hover:bg-white/5">Português</a>
            <a href="#" class="block px-4 py-2 text-sm text-zinc-400 hover:text-white hover:bg-white/5">Bahasa</a>
          </div>
        </div>

        <!-- Creator Login (Hidden on Mobile) -->
        <a href="#" class="hidden md:block text-sm text-zinc-400 hover:text-white transition-colors duration-200">
          Creator Login
        </a>

        <!-- Get App -->
        <button class="bg-white text-black rounded-full px-5 py-2 text-sm font-medium hover:scale-105 transition-transform duration-300 shadow-[0_0_15px_rgba(255,255,255,0.3)]">
          Get App
        </button>

        <!-- Mobile Menu Toggle -->
        <button @click="isMenuOpen = !isMenuOpen" class="md:hidden text-white hover:text-zinc-300">
          <Menu class="w-6 h-6" />
        </button>
      </div>

    </nav>

    <!-- Mobile Menu -->
    <div v-if="isMenuOpen" class="absolute top-16 left-4 right-4 bg-[#0A0A0B]/95 backdrop-blur-2xl border border-white/10 rounded-2xl p-6 flex flex-col gap-4 pointer-events-auto shadow-2xl md:hidden">
      <a href="#features" @click="isMenuOpen = false" class="text-base font-medium text-white hover:text-[#00F0FF] transition-colors">Features</a>
      <a href="#how-it-works" @click="isMenuOpen = false" class="text-base font-medium text-white hover:text-[#00F0FF] transition-colors">How it works</a>
      <a href="#about" @click="isMenuOpen = false" class="text-base font-medium text-white hover:text-[#00F0FF] transition-colors">About us</a>
      <a href="#footer" @click="isMenuOpen = false" class="text-base font-medium text-white hover:text-[#00F0FF] transition-colors">Contact</a>
      <div class="h-[1px] bg-white/10 w-full my-2"></div>
      <a href="#" class="text-base font-medium text-zinc-400 hover:text-white transition-colors">Creator Login</a>
    </div>
  </div>
</template>
