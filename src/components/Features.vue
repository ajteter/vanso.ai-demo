<template>
  <div class="content-stretch flex flex-col gap-[48px] items-center max-w-[1280px] mx-auto px-[16px] py-[96px] relative shrink-0 w-full z-10">
    <div class="content-stretch flex flex-col gap-[24px] items-center relative shrink-0 w-full">
      <div class="content-stretch flex flex-col items-center relative shrink-0 w-full">
        <div class="flex flex-col font-bold justify-center text-[36px] md:text-[48px] text-center text-white leading-[1.2]">
          <p class="whitespace-pre-wrap">
            <span>Built for the </span>
            <span class="bg-clip-text text-[transparent] font-bold" style="background-image: linear-gradient(175deg, #54E3D5 33%, #F5328A 91%)">
              AI Music Era
            </span>
          </p>
        </div>
      </div>
      <div class="content-stretch flex flex-col items-center max-w-[672px] relative shrink-0 w-full">
        <p class="font-normal justify-center text-[#a1a1aa] text-[16px] text-center whitespace-pre-wrap leading-[24px]">Seamlessly integrated tools designed for the next generation of creators.</p>
      </div>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 relative shrink-0 w-full">
      <!-- Card 1 -->
      <div class="backdrop-blur-[20px] bg-white/5 border border-white/10 content-stretch flex flex-col items-start justify-between min-h-[300px] overflow-hidden p-[32px] rounded-[24px] relative group hover:-translate-y-1 transition-transform">
        <div class="relative shrink-0 size-[48px] mb-6">
          <div class="h-[48px] relative rounded-[16px] shrink-0 w-full flex items-center justify-center shadow-lg" style="background-image: linear-gradient(134deg, #F5328A 19%, #ECA08B 58%, #54E3D5 91%);">
            <img alt="Reach icon" class="w-[20px] h-[20px]" src="/assets/icon-feature1.svg" />
          </div>
        </div>
        <div class="relative shrink-0 w-full flex flex-col gap-[12px] z-10">
          <h3 class="font-bold text-[20px] text-white leading-[28px]">Massive Mobile Reach</h3>
          <p class="font-normal leading-[24px] text-[#a1a1aa] text-[14px]">Deliver your tracks directly to 400 million+ users via mobile music apps worldwide.</p>
        </div>
        <div class="absolute bg-[rgba(92,225,255,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-[9999px] size-[128px] group-hover:bg-[rgba(92,225,255,0.2)] transition-colors"></div>
      </div>
      
      <!-- Card 2 -->
      <div class="backdrop-blur-[20px] bg-white/5 border border-white/10 content-stretch flex flex-col items-start justify-between min-h-[300px] overflow-hidden p-[32px] rounded-[24px] relative group hover:-translate-y-1 transition-transform">
        <div class="relative shrink-0 size-[48px] mb-6">
          <div class="h-[48px] relative rounded-[16px] shrink-0 w-full flex items-center justify-center shadow-lg" style="background-image: linear-gradient(135deg, #b84dff 47%, #F5328A 100%);">
            <img alt="Lightning icon" class="w-[16px] h-[20px]" src="/assets/icon-feature2.svg" />
          </div>
        </div>
        <div class="relative shrink-0 w-full flex flex-col gap-[12px] z-10">
          <h3 class="font-bold text-[20px] text-white leading-[28px]">Lightning Distribution</h3>
          <p class="font-normal leading-[24px] text-[#a1a1aa] text-[14px]">Powered by our seamless pipeline, your track could reach listeners in the very next minute.</p>
        </div>
        <div class="absolute bg-[rgba(184,77,255,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-[9999px] size-[128px] group-hover:bg-[rgba(184,77,255,0.2)] transition-colors"></div>
      </div>
      
      <!-- Card 3 -->
      <div class="backdrop-blur-[20px] bg-white/5 border border-white/10 content-stretch flex flex-col items-start justify-between min-h-[300px] overflow-hidden p-[32px] rounded-[24px] relative group hover:-translate-y-1 transition-transform">
        <div class="relative shrink-0 size-[48px] mb-6">
          <div class="h-[48px] relative rounded-[16px] shrink-0 w-full flex items-center justify-center shadow-lg" style="background-image: linear-gradient(135deg, #54E3D5 23%, #F5328A 100%);">
            <img alt="AIGC icon" class="w-[22px] h-[22px]" src="/assets/icon-feature3.svg" />
          </div>
        </div>
        <div class="relative shrink-0 w-full flex flex-col gap-[12px] z-10">
          <h3 class="font-bold text-[20px] text-white leading-[28px]">AIGC Welcomed</h3>
          <p class="font-normal leading-[24px] text-[#a1a1aa] text-[14px]">We fully embrace AI-generated music. Creativity has no boundaries, tools should never be limited.</p>
        </div>
        <div class="absolute bg-[rgba(255,102,196,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-[9999px] size-[128px] group-hover:bg-[rgba(255,102,196,0.2)] transition-colors"></div>
      </div>
      
      <!-- Card 4 -->
      <div class="backdrop-blur-[20px] bg-white/5 border border-white/10 content-stretch flex flex-col items-start justify-between min-h-[300px] overflow-hidden p-[32px] rounded-[24px] relative group hover:-translate-y-1 transition-transform">
        <div class="relative shrink-0 size-[48px] mb-6">
          <div class="h-[48px] relative rounded-[16px] shrink-0 w-full flex items-center justify-center shadow-lg" style="background-image: linear-gradient(135deg, #54E3D5 0%, #b84dff 100%);">
            <img alt="Smart icon" class="w-[19px] h-[20px]" src="/assets/icon-feature4.svg" />
          </div>
        </div>
        <div class="relative shrink-0 w-full flex flex-col gap-[12px] z-10">
          <h3 class="font-bold text-[20px] text-white leading-[28px]">Smart Algorithms</h3>
          <p class="font-normal leading-[24px] text-[#a1a1aa] text-[14px]">Advanced AI analyzes your music DNA to match your tracks with the perfect audience globally.</p>
        </div>
        <div class="absolute bg-[rgba(184,77,255,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-[9999px] size-[128px] group-hover:bg-[rgba(184,77,255,0.2)] transition-colors"></div>
      </div>
      
      <!-- Card 5 -->
      <div class="backdrop-blur-[20px] bg-white/5 border border-white/10 content-stretch flex flex-col items-start justify-between min-h-[300px] overflow-hidden p-[32px] rounded-[24px] relative group hover:-translate-y-1 transition-transform">
        <div class="relative shrink-0 size-[48px] mb-6">
          <div class="h-[48px] relative rounded-[16px] shrink-0 w-full flex items-center justify-center shadow-lg" style="background-image: linear-gradient(135deg, #ECA08B 43%, #54E3D5 100%);">
            <img alt="Data icon" class="w-[18px] h-[18px]" src="/assets/icon-feature5.svg" />
          </div>
        </div>
        <div class="relative shrink-0 w-full flex flex-col gap-[12px] z-10">
          <h3 class="font-bold text-[20px] text-white leading-[28px]">Transparent Data</h3>
          <p class="font-normal leading-[24px] text-[#a1a1aa] text-[14px]">Track plays, audience demographics, and revenue with our detailed and transparent dashboard.</p>
        </div>
        <div class="absolute bg-[rgba(92,225,255,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-[9999px] size-[128px] group-hover:bg-[rgba(92,225,255,0.2)] transition-colors"></div>
      </div>
      
      <!-- Card 6 -->
      <div class="backdrop-blur-[20px] bg-white/5 border border-white/10 content-stretch flex flex-col items-start justify-between min-h-[300px] overflow-hidden p-[32px] rounded-[24px] relative group hover:-translate-y-1 transition-transform">
        <div class="relative shrink-0 size-[48px] mb-6">
          <div class="h-[48px] relative rounded-[16px] shrink-0 w-full flex items-center justify-center shadow-lg" style="background-image: linear-gradient(135deg, #b84dff 0%, #54E3D5 100%);">
            <img alt="Open icon" class="w-[16px] h-[20px]" src="/assets/icon-workflow-arrow.svg" />
          </div>
        </div>
        <div class="relative shrink-0 w-full flex flex-col gap-[12px] z-10">
          <h3 class="font-bold text-[20px] text-white leading-[28px]">Open & Compliant</h3>
          <p class="font-normal leading-[24px] text-[#a1a1aa] text-[14px]">We champion the freedom to upload. You are welcome to share any content, as long as it is legally compliant.</p>
        </div>
        <div class="absolute bg-[rgba(255,102,196,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-[9999px] size-[128px] group-hover:bg-[rgba(255,102,196,0.2)] transition-colors"></div>
      </div>
      
    </div>
  </div>
</template>

<script setup>
</script>
