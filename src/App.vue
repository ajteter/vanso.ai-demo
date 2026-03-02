<script setup>
import Navbar from './components/Navbar.vue';
import Hero from './components/Hero.vue';
import LiveTicker from './components/LiveTicker.vue';
import Features from './components/Features.vue';
import Workflow from './components/Workflow.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <div class="bg-black content-stretch flex flex-col items-start relative size-full overflow-x-hidden min-h-screen text-white font-['Plus_Jakarta_Sans',sans-serif]">
    
    <!-- Sonic Aura Background Glow Spots (4 blurred orbs as per Figma & DesignColorPalette) -->
    <!-- Spot 1: Top-left Magenta -->
    <div class="absolute top-[-100px] left-[-200px] w-[600px] h-[600px] bg-[#F5328A] rounded-full mix-blend-screen blur-[150px] opacity-20 pointer-events-none z-0"></div>
    <!-- Spot 2: Top-right Cyan -->
    <div class="absolute top-[100px] right-[-150px] w-[500px] h-[500px] bg-[#54E3D5] rounded-full mix-blend-screen blur-[150px] opacity-15 pointer-events-none z-0"></div>
    <!-- Spot 3: Middle-left Cyan/Teal (near features) -->
    <div class="absolute top-[1400px] left-[-250px] w-[600px] h-[600px] bg-[#54E3D5] rounded-full mix-blend-screen blur-[180px] opacity-15 pointer-events-none z-0"></div>
    <!-- Spot 4: Bottom-right Magenta (near workflow/slogan) -->
    <div class="absolute top-[2400px] right-[-200px] w-[500px] h-[500px] bg-[#F5328A] rounded-full mix-blend-screen blur-[150px] opacity-20 pointer-events-none z-0"></div>

    <Navbar />
    <Hero />
    <LiveTicker />
    <Features />
    <Workflow />
    <Footer />
  </div>
</template>
