<script setup>
import Navbar from './components/Navbar.vue';
import Hero from './components/Hero.vue';
import LiveTicker from './components/LiveTicker.vue';
import Features from './components/Features.vue';
import Workflow from './components/Workflow.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <div class="bg-black flex flex-col items-start relative size-full overflow-x-hidden min-h-screen text-white font-['Plus_Jakarta_Sans',sans-serif]">
    
    <!-- BG blur spot 1 (top area, y=~-20, x=~-164): Magenta glow, matches Figma "BG blur spot" at y=-20 -->
    <div class="absolute top-[-20px] left-[-164px] w-[640px] h-[512px] bg-[#f5328a] rounded-full blur-[75px] opacity-25 pointer-events-none z-0"></div>
    
    <!-- BG blur spot 2 (top-right, y=~384): Cyan/teal glow from bg-blur.svg position -->
    <div class="absolute top-[384px] right-[-189px] w-[640px] h-[512px] pointer-events-none z-0">
      <img alt="" class="block w-full h-full opacity-80" src="/assets/bg-blur.svg" />
    </div>
    
    <!-- BG blur spot 3 (bottom area, y=~2492+55=2547): Magenta glow -->
    <div class="absolute top-[2547px] left-[-164px] w-[640px] h-[512px] bg-[#f5328a] rounded-full blur-[75px] opacity-25 pointer-events-none z-0"></div>
    
    <!-- BG blur spot 4 (bottom-right, y=~2492+384=2876): Cyan glow -->
    <div class="absolute top-[2876px] right-[-189px] w-[640px] h-[512px] pointer-events-none z-0">
      <img alt="" class="block w-full h-full opacity-80" src="/assets/bg-blur.svg" />
    </div>

    <Navbar />
    <Hero />
    <LiveTicker />
    <Features />
    <Workflow />
    <Footer />
  </div>
</template>
