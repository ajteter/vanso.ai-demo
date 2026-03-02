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
    
    <!-- Top bg blur spot -->
    <div class="absolute flex inset-[-20px_-1px_2666px_1px] items-center justify-center pointer-events-none z-[-1]">
      <div class="flex-none h-[992px] rotate-180 w-[1280px]">
        <div class="opacity-80 overflow-clip relative size-full">
          <div class="absolute bg-[#f5328a] blur-[75px] h-[512px] left-[-164px] opacity-25 rounded-[9999px] top-[55px] w-[640px]" />
          <div class="absolute bottom-[96px] h-[512px] right-[-189px] w-[640px]">
            <div class="absolute inset-[-29.3%_-23.44%]">
              <img alt="" class="block max-w-none size-full" src="/assets/bg-blur.svg" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom bg blur spot -->
    <div class="absolute flex inset-[1500px_0_1146px_0] items-center justify-center pointer-events-none z-[-1]">
      <div class="-scale-y-100 flex-none h-[992px] w-[1280px]">
        <div class="overflow-clip relative size-full">
          <div class="absolute bg-[#f5328a] blur-[75px] h-[512px] left-[-164px] opacity-25 rounded-[9999px] top-[55px] w-[640px]" />
          <div class="absolute bottom-[96px] h-[512px] right-[-189px] w-[640px]">
            <div class="absolute inset-[-29.3%_-23.44%]">
              <img alt="" class="block max-w-none size-full" src="/assets/bg-blur.svg" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <Navbar />
    <Hero />
    <LiveTicker />
    <Features />
    <Workflow />
    <!-- Slogan section has been moved inside Workflow.vue for simplicity, or we can add it here -->
    
    <Footer />
  </div>
</template>
