<template>
  <div class="flex flex-col items-center relative shrink-0 w-full z-10">
    
    <!-- introduction: y=2164, w=1280, h=452 -->
    <div class="flex flex-col items-center py-[48px] relative shrink-0 w-full max-w-[1280px] mx-auto">
      <!-- Heading: x=16, y=0, w=1248, h=72 -->
      <div class="flex flex-col gap-[8px] items-center max-w-[1248px] mx-auto px-4 relative shrink-0 w-full">
        <!-- "From Creation to 400M+ Users" h=40, text-[32px] -->
        <h2 class="font-bold text-[28px] md:text-[32px] text-center text-white leading-[40px]">
          <span>From Creation to </span>
          <span class="bg-clip-text text-[transparent] font-bold" style="background-image: linear-gradient(176deg, #F5328A 43%, #54E3D5 77%)">400M+ Users</span>
        </h2>
        <p class="font-normal text-[#71717a] text-[16px] text-center leading-[24px]">The fastest pipeline in the industry.</p>
      </div>
      
      <!-- Steps container: x=16, y=136, w=1248, h=220 -->
      <div class="flex flex-col md:flex-row items-start justify-between max-w-[1248px] mx-auto mt-[64px] px-4 relative shrink-0 w-full gap-8 md:gap-0">
        <!-- Horizontal divider line: y=48 within this container, spanning ~80% -->
        <div class="hidden md:block absolute h-[2px] left-[10%] right-[10%] top-[48px] bg-[rgba(255,255,255,0.08)]"></div>
        
        <!-- Step 1: w=416, h=200 -->
        <div class="flex-1 flex flex-col items-center text-center relative min-w-0">
          <!-- Circle: 96x96, centered -->
          <div class="bg-white/5 backdrop-blur-xl border border-white/10 flex items-center justify-center rounded-full size-[96px] z-10 mb-[24px] shadow-lg">
            <img alt="Upload" class="w-[27.5px] h-[20px]" src="/assets/icon-workflow-1.svg" />
          </div>
          <!-- Title: h=28 -->
          <h3 class="font-bold text-[20px] text-white leading-[28px] mb-[12px]">1. Upload AIGC & Originals</h3>
          <!-- Desc: w=338, h=60 -->
          <p class="font-normal text-[14px] text-[#a1a1aa] leading-[20px] max-w-[338px]">Designed for the AI era. Whether created with AI music generator or your DAW, simply upload your tracks.</p>
        </div>
        
        <!-- Step 2: w=416, h=220 -->
        <div class="flex-1 flex flex-col items-center text-center relative min-w-0">
          <div class="bg-white/5 backdrop-blur-xl border border-white/10 flex items-center justify-center rounded-full size-[96px] z-10 mb-[24px] shadow-lg">
            <img alt="Deploy" class="w-[25px] h-[25px]" src="/assets/icon-workflow-2.svg" />
          </div>
          <h3 class="font-bold text-[20px] text-white leading-[28px] mb-[12px]">2. Rapid Deployment</h3>
          <p class="font-normal text-[14px] text-[#a1a1aa] leading-[20px] max-w-[340px]">No tedious waiting. Our streamlined distribution pipeline processes your files instantly for immediate release.</p>
        </div>
        
        <!-- Step 3: w=416, h=200 -->
        <div class="flex-1 flex flex-col items-center text-center relative min-w-0">
          <div class="bg-white/5 backdrop-blur-xl border border-white/10 flex items-center justify-center rounded-full size-[96px] z-10 mb-[24px] shadow-lg">
            <img alt="Global" class="size-[25px]" src="/assets/icon-workflow-3.svg" />
          </div>
          <h3 class="font-bold text-[20px] text-white leading-[28px] mb-[12px]">3. Reach 400M+ Users</h3>
          <p class="font-normal text-[14px] text-[#a1a1aa] leading-[20px] max-w-[348px]">Your music goes live to over 400 million mobile listeners worldwide.</p>
        </div>
      </div>
    </div>

    <!-- slogan: y=2616, w=1280, h=800 -->
    <div class="flex items-center justify-center relative shrink-0 w-full h-[800px] overflow-hidden">
      <!-- light2.png: x=240, y=0, w=800, h=800 centered -->
      <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
        <img alt="" class="block object-contain w-[800px] h-[800px] opacity-40" src="/assets/light2.png" />
      </div>
      <!-- Text container: y=248, h=304 -->
      <div class="relative z-10 flex flex-col items-center w-full max-w-[1280px] px-4">
        <!-- "Music the World": h=72, text-[60px] -->
        <h2 class="bg-clip-text bg-gradient-to-b from-white to-[#52525b] font-bold text-[48px] md:text-[60px] text-[transparent] text-center leading-[72px] mb-[72px]">Music the World</h2>
        <!-- Body text: x=145, w=990, h=112 -->
        <p class="font-normal text-[#a1a1aa] text-[16px] md:text-[20px] text-center leading-[28px] max-w-[990px] mx-auto">Vanso is dedicated to democratizing music distribution. We believe in a future where every creator—whether using instruments or algorithms—has a stage. We bridge the gap between creators and the massive potential of mobile ecosystem listeners, building native experiences that make music discovery feel effortless for hundreds of millions of users.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
