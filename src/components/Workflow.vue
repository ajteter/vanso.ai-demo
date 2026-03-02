<template>
  <div class="content-stretch flex flex-col items-center py-[48px] relative shrink-0 w-full z-10 overflow-hidden">
    <!-- Workflow Steps -->
    <div class="content-stretch flex flex-col gap-[64px] items-center max-w-[1280px] px-[16px] relative shrink-0 w-full mb-32">
      <div class="content-stretch flex flex-col gap-[8px] items-center relative shrink-0 w-full">
        <div class="flex flex-col font-bold h-[40px] md:h-[60px] justify-center leading-[1.2] shrink-0 text-[36px] md:text-[48px] text-center text-white">
          <p class="whitespace-pre-wrap">
            <span>From Creation to </span>
            <span class="bg-clip-text text-[transparent] font-bold" style="background-image: linear-gradient(176deg, #F5328A 43%, #54E3D5 77%)">
              400M+ Users
            </span>
          </p>
        </div>
        <div class="flex flex-col font-normal justify-center leading-[24px] shrink-0 text-[#71717a] text-[16px] text-center mt-2">
          <p class="whitespace-pre-wrap">The fastest pipeline in the industry.</p>
        </div>
      </div>
      
      <div class="content-stretch flex flex-col md:flex-row items-start justify-between relative shrink-0 w-full gap-12 md:gap-0 mt-[48px]">
        <!-- Connecting Line for Desktop -->
        <div class="hidden md:block absolute h-[2px] left-[10%] right-[10%] top-[48px] bg-gradient-to-r from-[rgba(92,225,255,0.2)] via-[rgba(184,77,255,0.2)] to-[rgba(255,102,196,0.2)]"></div>
        
        <!-- Step 1 -->
        <div class="flex-[1_0_0] min-h-[200px] relative w-full flex flex-col items-center text-center">
          <div class="md:absolute md:-translate-x-1/2 left-1/2 top-0 bg-[#18181b] border border-[rgba(255,255,255,0.1)] border-solid flex items-center justify-center p-[1px] rounded-[9999px] size-[96px] z-10 mb-6 md:mb-0">
            <div class="h-[20px] w-[27.5px] relative">
              <img alt="Step 1" class="absolute inset-0 size-full" src="/assets/icon-workflow-1.svg" />
            </div>
          </div>
          <div class="md:absolute left-0 right-0 top-[120px] flex flex-col items-center">
            <h3 class="font-bold text-[20px] text-white leading-[28px] mb-2">1. Upload AIGC & Originals</h3>
            <p class="font-normal text-[14px] text-[#a1a1aa] leading-[20px] max-w-[338px] px-4">Designed for the AI era. Whether created with AI music generator or your DAW, simply upload your tracks.</p>
          </div>
        </div>
        
        <!-- Step 2 -->
        <div class="flex-[1_0_0] min-h-[200px] relative w-full flex flex-col items-center text-center">
          <div class="md:absolute md:-translate-x-1/2 left-1/2 top-0 bg-[#18181b] border border-[rgba(255,255,255,0.1)] border-solid flex items-center justify-center p-[1px] rounded-[9999px] size-[96px] z-10 mb-6 md:mb-0">
            <div class="h-[25px] w-[25px] relative">
              <img alt="Step 2" class="absolute inset-0 size-full" src="/assets/icon-workflow-2.svg" />
            </div>
          </div>
          <div class="md:absolute left-0 right-0 top-[120px] flex flex-col items-center">
            <h3 class="font-bold text-[20px] text-white leading-[28px] mb-2">2. Rapid Deployment</h3>
            <p class="font-normal text-[14px] text-[#a1a1aa] leading-[20px] max-w-[340px] px-4">No tedious waiting. Our streamlined distribution pipeline processes your files instantly for immediate release.</p>
          </div>
        </div>
        
        <!-- Step 3 -->
        <div class="flex-[1_0_0] min-h-[200px] relative w-full flex flex-col items-center text-center">
          <div class="md:absolute md:-translate-x-1/2 left-1/2 top-0 bg-[#18181b] border border-[rgba(255,255,255,0.1)] border-solid flex items-center justify-center p-[1px] rounded-[9999px] size-[96px] z-10 mb-6 md:mb-0">
            <div class="size-[25px] relative">
              <img alt="Step 3" class="absolute inset-0 size-full" src="/assets/icon-workflow-3.svg" />
            </div>
          </div>
          <div class="md:absolute left-0 right-0 top-[120px] flex flex-col items-center">
            <h3 class="font-bold text-[20px] text-white leading-[28px] mb-2">3. Reach 400M+ Users</h3>
            <p class="font-normal text-[14px] text-[#a1a1aa] leading-[20px] max-w-[348px] px-4">Your music goes live to over 400 million mobile listeners worldwide.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Slogan Section -->
    <div class="content-stretch flex gap-[32px] min-h-[800px] items-center justify-center py-[32px] relative shrink-0 w-full mt-24">
      <div class="absolute inset-0 flex items-center justify-center pointer-events-none opacity-40">
        <img alt="" class="block object-contain size-full max-w-[800px] max-h-[800px]" src="/assets/light2.png" />
      </div>
      <div class="relative shrink-0 w-full max-w-[1280px] z-10 px-4 md:px-0">
        <div class="content-stretch flex flex-col items-center w-full">
          <div class="bg-clip-text bg-gradient-to-b flex flex-col font-bold from-white justify-center leading-[1.2] text-[48px] md:text-[72px] text-[transparent] text-center to-[#52525b] mb-12">
            <p class="whitespace-pre-wrap">Music the World</p>
          </div>
          <div class="flex flex-col font-normal justify-center leading-[28px] text-[#a1a1aa] text-[16px] md:text-[20px] text-center max-w-[990px] mx-auto whitespace-pre-wrap">
            <p>Vanso is dedicated to democratizing music distribution. We believe in a future where every creator—whether using instruments or algorithms—has a stage.</p>
            <p>&nbsp;</p>
            <p>We bridge the gap between creators and the massive potential of mobile ecosystem listeners, building native experiences that make music discovery feel effortless for hundreds of millions of users.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
