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
    
    <!-- BG blur spot 1: Magenta glow top-left — breathe delay 0s -->
    <div class="glow-orb glow-orb-1 absolute top-[-20px] left-[-164px] w-[640px] h-[512px] bg-[#f5328a] rounded-full blur-[120px] pointer-events-none z-0"></div>
    
    <!-- BG blur spot 2: Cyan glow top-right — breathe delay 2s -->
    <div class="glow-orb glow-orb-2 absolute top-[384px] right-[-189px] w-[640px] h-[512px] pointer-events-none z-0">
      <img alt="" class="block w-full h-full" src="/assets/bg-blur.svg" />
    </div>
    
    <!-- BG blur spot 3: Magenta glow bottom-left — breathe delay 4s -->
    <div class="glow-orb glow-orb-3 absolute top-[2547px] left-[-164px] w-[640px] h-[512px] bg-[#f5328a] rounded-full blur-[120px] pointer-events-none z-0"></div>
    
    <!-- BG blur spot 4: Cyan glow bottom-right — breathe delay 6s -->
    <div class="glow-orb glow-orb-4 absolute top-[2876px] right-[-189px] w-[640px] h-[512px] pointer-events-none z-0">
      <img alt="" class="block w-full h-full" src="/assets/bg-blur.svg" />
    </div>

    <Navbar />
    <Hero />
    <LiveTicker />
    <Features />
    <Workflow />
    <Footer />
  </div>
</template>

<style>
/* Staggered breathing animation for background glow spots */
@keyframes glowBreathe {
  0%, 100% {
    opacity: 0.12;
    transform: scale(1);
  }
  50% {
    opacity: 0.28;
    transform: scale(1.08);
  }
}

.glow-orb {
  will-change: opacity, transform;
}

.glow-orb-1 {
  animation: glowBreathe 8s ease-in-out 0s infinite;
}

.glow-orb-2 {
  animation: glowBreathe 8s ease-in-out 2s infinite;
}

.glow-orb-3 {
  animation: glowBreathe 8s ease-in-out 4s infinite;
}

.glow-orb-4 {
  animation: glowBreathe 8s ease-in-out 6s infinite;
}
</style>
