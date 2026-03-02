<template>
  <!-- Header: y=100, height=872, full width 1280 -->
  <div class="content-stretch flex flex-col items-center relative shrink-0 w-full">
    <!-- Container: x=128, y=48, w=1024, h=776 -->
    <div class="flex flex-col gap-[64px] items-center max-w-[1024px] mx-auto py-[48px] relative w-full px-4 md:px-0">
      <!-- Heading 1: y=64 inside container, h=408 -->
      <div class="flex flex-col items-center relative shrink-0 w-full mt-[64px]">
        <!-- Line 1: "Turn Your AI Music" h=96 -->
        <div class="flex justify-center w-full">
          <span class="font-bold text-[48px] md:text-[96px] text-white tracking-[-2.4px] leading-[1] text-center">Turn Your AI Music</span>
        </div>
        <!-- Line 2: "Into Global Hits." h=96, gap=8px from line1 -->
        <div class="flex justify-center w-full mt-[8px]">
          <span class="font-bold text-[48px] md:text-[96px] text-white tracking-[-2.4px] leading-[1] text-center">Into Global Hits.</span>
        </div>
        <!-- Line 3: "Reach 400M+ Listeners." gradient, h=200 (2 lines), gap=8px -->
        <div class="flex justify-center w-full mt-[8px]">
          <span class="bg-clip-text font-bold text-[48px] md:text-[96px] text-[transparent] tracking-[-2.4px] leading-[1] text-center" style="background-image: linear-gradient(163deg, #F5328A 33%, #54E3D5 71%);">Reach 400M+ Listeners.</span>
        </div>
      </div>
      
      <!-- Buttons container: gap from heading = 536-408-64 = 64px already handled by parent gap -->
      <div class="flex flex-col md:flex-row gap-[16px] items-center justify-center relative shrink-0 w-full">
        <!-- Button 1: "Android App" w=204, h=56 -->
        <button class="relative overflow-hidden px-[32px] py-[16px] rounded-[9999px] shrink-0 hover:scale-105 transition-transform group h-[56px]">
          <div class="absolute inset-0 opacity-90 transition-opacity group-hover:opacity-100 rounded-[9999px]" style="background-image: linear-gradient(164deg, #F5328A 19%, #ECA08B 58%, #54E3D5 91%);"></div>
          <div class="flex gap-[8px] items-center justify-center relative z-10">
            <img alt="Android" class="size-[16px]" src="/assets/icon-android.svg" />
            <span class="font-bold text-[16px] text-white leading-[24px]">Android App</span>
          </div>
          <div class="absolute inset-0 rounded-[9999px] shadow-[0px_0px_0px_2px_rgba(255,255,255,0.2)] bg-transparent z-20 pointer-events-none"></div>
        </button>
        
        <!-- Button 2: "Upload Your Track" w=202, h=56 -->
        <button class="group relative overflow-hidden px-[32px] py-[16px] rounded-[9999px] shrink-0 hover:scale-105 transition-transform h-[56px]">
          <div class="absolute inset-0 opacity-50 rounded-[9999px] bg-gradient-to-r from-[#ff66c4] via-[#b84dff] to-[#5ce1ff] transition-opacity group-hover:opacity-100"></div>
          <div class="absolute inset-[1px] rounded-[9999px] bg-black z-10 transition-colors group-hover:bg-[#1a1a1a]"></div>
          <div class="flex items-center justify-center relative z-20">
            <span class="font-normal text-[16px] text-white leading-[24px]">Upload Your Track</span>
          </div>
        </button>
      </div>
      
      <!-- Subtitle: x=128(+128=256 from body), w=768, h=56 -->
      <div class="flex flex-col items-center max-w-[768px] px-4 md:px-0 relative shrink-0 w-full">
        <p class="font-normal leading-[28px] text-[#a1a1aa] text-[16px] md:text-[20px] text-center">Don't just generate—get heard. The only platform that puts your AI tracks directly onto millions mobile players.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
