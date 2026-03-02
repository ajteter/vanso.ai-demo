<template>
  <div class="content-stretch flex h-[100px] items-start justify-center px-[16px] relative shrink-0 w-full z-50 mt-4">
    <div class="backdrop-blur-[12px] bg-white/5 border border-white/10 content-stretch flex h-full items-center justify-between max-w-[1152px] pl-[24px] pr-[23.99px] py-[12px] relative rounded-[9999px] shrink-0 w-full md:w-[1152px]">
      <div class="relative shrink-0 flex items-center gap-[10px] cursor-pointer hover:opacity-80 transition-opacity">
        <img alt="Vanso Logo" class="rounded-[100px] size-[40px] pointer-events-none object-cover" src="/assets/vanso-logo.png" />
        <div class="h-[24px] relative shrink-0 w-[108px]">
          <img alt="Vanso" class="absolute h-full object-contain" src="/assets/vanso-text.svg" />
        </div>
      </div>
      <div class="relative shrink-0">
        <div class="content-stretch flex gap-[16px] items-center relative">
          <div class="content-stretch flex gap-[4px] items-center relative shrink-0 cursor-pointer hover:text-white transition-colors">
            <img alt="Globe" class="size-[15px]" src="/assets/icon-container.svg" />
            <div class="flex flex-col font-normal h-[20px] justify-center text-[#a1a1aa] text-[14px]">
              <p class="leading-[20px]">EN</p>
            </div>
            <img alt="Arrow down" class="w-[6.667px]" src="/assets/icon-container1.svg" />
          </div>
          <a href="#" class="font-normal justify-center text-[#a1a1aa] text-[14px] whitespace-nowrap hover:text-white transition-colors">
            Sign in
          </a>
          <button class="content-stretch flex items-center justify-center px-[20px] py-[10px] relative rounded-[9999px] shadow-[0px_0px_15px_0px_rgba(255,102,196,0.3)] shrink-0 hover:scale-105 transition-transform" style="background-image: linear-gradient(156deg, #F5328A 19%, #ECA08B 57%, #54E3D5 91%);">
            <span class="font-bold h-[20px] justify-center text-[14px] text-white">Get App</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
