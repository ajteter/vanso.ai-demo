<template>
  <!-- feature: y=1204, w=1280, h=960 -->
  <div class="flex flex-col items-center py-[96px] relative shrink-0 w-full z-10">
    <!-- Heading area: x=16, y=96, w=1248, h=96 -->
    <div class="flex flex-col gap-[24px] items-center max-w-[1248px] mx-auto px-4 relative shrink-0 w-full">
      <!-- "Built for the AI Music Era" h=48 -->
      <div class="flex justify-center w-full">
        <h2 class="font-bold text-[32px] md:text-[48px] text-center text-white leading-[48px]">
          <span>Built for the </span>
          <span class="bg-clip-text text-[transparent]" style="background-image: linear-gradient(175deg, #54E3D5 33%, #F5328A 91%)">AI Music Era</span>
        </h2>
      </div>
      <!-- Subtitle: w=672, h=24, centered -->
      <p class="font-normal text-[#a1a1aa] text-[16px] text-center leading-[24px] max-w-[672px]">Seamlessly integrated tools designed for the next generation of creators.</p>
    </div>
    
    <!-- Cards grid: x=16, y=240, w=1248, h=624 — 3 cols, 24px gap, each card 400x300 -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-[24px] max-w-[1248px] mx-auto mt-[48px] px-4 relative shrink-0 w-full">
      <!-- Card 1: 400x300 -->
      <div class="bg-white/5 backdrop-blur-2xl border border-white/10 flex flex-col items-start overflow-hidden relative rounded-3xl group hover:bg-white/10 hover:-translate-y-2 hover:shadow-[0_0_40px_rgba(255,255,255,0.05)] hover:border-white/20 transition-all duration-300 h-[300px]">
        <div class="p-[33px] flex flex-col justify-between h-full w-full">
          <div class="size-[48px] rounded-[16px] flex items-center justify-center shadow-lg" style="background-image: linear-gradient(134deg, #F5328A 19%, #ECA08B 58%, #54E3D5 91%);">
            <img alt="" class="w-[15px] h-[22px]" src="/assets/icon-feature1.svg" />
          </div>
          <div class="flex flex-col gap-[11px] w-full max-w-[334px]">
            <h3 class="font-bold text-[20px] text-white leading-[28px]">Massive Mobile Reach</h3>
            <p class="font-normal text-[#a1a1aa] text-[14px] leading-[23px]">Deliver your tracks directly to 400 million+ users via mobile music apps worldwide.</p>
          </div>
        </div>
        <div class="absolute bg-[rgba(92,225,255,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-full size-[128px] group-hover:bg-[rgba(92,225,255,0.2)] transition-colors"></div>
      </div>
      
      <!-- Card 2: 400x300 -->
      <div class="bg-white/5 backdrop-blur-2xl border border-white/10 flex flex-col items-start overflow-hidden relative rounded-3xl group hover:bg-white/10 hover:-translate-y-2 hover:shadow-[0_0_40px_rgba(255,255,255,0.05)] hover:border-white/20 transition-all duration-300 h-[300px]">
        <div class="p-[33px] flex flex-col justify-between h-full w-full">
          <div class="size-[48px] rounded-[16px] flex items-center justify-center shadow-lg" style="background-image: linear-gradient(135deg, #b84dff 47%, #F5328A 100%);">
            <img alt="" class="w-[16px] h-[20px]" src="/assets/icon-feature2.svg" />
          </div>
          <div class="flex flex-col gap-[11px] w-full max-w-[334px]">
            <h3 class="font-bold text-[20px] text-white leading-[28px]">Lightning Distribution</h3>
            <p class="font-normal text-[#a1a1aa] text-[14px] leading-[23px]">Powered by our seamless pipeline, your track could reach listeners in the very next minute.</p>
          </div>
        </div>
        <div class="absolute bg-[rgba(184,77,255,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-full size-[128px] group-hover:bg-[rgba(184,77,255,0.2)] transition-colors"></div>
      </div>
      
      <!-- Card 3: 400x300 -->
      <div class="bg-white/5 backdrop-blur-2xl border border-white/10 flex flex-col items-start overflow-hidden relative rounded-3xl group hover:bg-white/10 hover:-translate-y-2 hover:shadow-[0_0_40px_rgba(255,255,255,0.05)] hover:border-white/20 transition-all duration-300 h-[300px]">
        <div class="p-[33px] flex flex-col justify-between h-full w-full">
          <div class="size-[48px] rounded-[16px] flex items-center justify-center shadow-lg" style="background-image: linear-gradient(135deg, #54E3D5 23%, #F5328A 100%);">
            <img alt="" class="w-[22px] h-[22px]" src="/assets/icon-feature3.svg" />
          </div>
          <div class="flex flex-col gap-[11px] w-full max-w-[334px]">
            <h3 class="font-bold text-[20px] text-white leading-[28px]">AIGC Welcomed</h3>
            <p class="font-normal text-[#a1a1aa] text-[14px] leading-[23px]">We fully embrace AI-generated music. Creativity has no boundaries, tools should never be limited.</p>
          </div>
        </div>
        <div class="absolute bg-[rgba(255,102,196,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-full size-[128px] group-hover:bg-[rgba(255,102,196,0.2)] transition-colors"></div>
      </div>
      
      <!-- Card 4: 400x300 -->
      <div class="bg-white/5 backdrop-blur-2xl border border-white/10 flex flex-col items-start overflow-hidden relative rounded-3xl group hover:bg-white/10 hover:-translate-y-2 hover:shadow-[0_0_40px_rgba(255,255,255,0.05)] hover:border-white/20 transition-all duration-300 h-[300px]">
        <div class="p-[33px] flex flex-col justify-between h-full w-full">
          <div class="size-[48px] rounded-[16px] flex items-center justify-center shadow-lg" style="background-image: linear-gradient(135deg, #54E3D5 0%, #b84dff 100%);">
            <img alt="" class="w-[19px] h-[20px]" src="/assets/icon-feature4.svg" />
          </div>
          <div class="flex flex-col gap-[11px] w-full max-w-[334px]">
            <h3 class="font-bold text-[20px] text-white leading-[28px]">Smart Algorithms</h3>
            <p class="font-normal text-[#a1a1aa] text-[14px] leading-[23px]">Advanced AI analyzes your music DNA to match your tracks with the perfect audience globally.</p>
          </div>
        </div>
        <div class="absolute bg-[rgba(184,77,255,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-full size-[128px] group-hover:bg-[rgba(184,77,255,0.2)] transition-colors"></div>
      </div>
      
      <!-- Card 5: 400x300 -->
      <div class="bg-white/5 backdrop-blur-2xl border border-white/10 flex flex-col items-start overflow-hidden relative rounded-3xl group hover:bg-white/10 hover:-translate-y-2 hover:shadow-[0_0_40px_rgba(255,255,255,0.05)] hover:border-white/20 transition-all duration-300 h-[300px]">
        <div class="p-[33px] flex flex-col justify-between h-full w-full">
          <div class="size-[48px] rounded-[16px] flex items-center justify-center shadow-lg" style="background-image: linear-gradient(135deg, #ECA08B 43%, #54E3D5 100%);">
            <img alt="" class="w-[18px] h-[18px]" src="/assets/icon-feature5.svg" />
          </div>
          <div class="flex flex-col gap-[11px] w-full max-w-[334px]">
            <h3 class="font-bold text-[20px] text-white leading-[28px]">Transparent Data</h3>
            <p class="font-normal text-[#a1a1aa] text-[14px] leading-[23px]">Track plays, audience demographics, and revenue with our detailed and transparent dashboard.</p>
          </div>
        </div>
        <div class="absolute bg-[rgba(92,225,255,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-full size-[128px] group-hover:bg-[rgba(92,225,255,0.2)] transition-colors"></div>
      </div>
      
      <!-- Card 6: 400x300 -->
      <div class="bg-white/5 backdrop-blur-2xl border border-white/10 flex flex-col items-start overflow-hidden relative rounded-3xl group hover:bg-white/10 hover:-translate-y-2 hover:shadow-[0_0_40px_rgba(255,255,255,0.05)] hover:border-white/20 transition-all duration-300 h-[300px]">
        <div class="p-[33px] flex flex-col justify-between h-full w-full">
          <div class="size-[48px] rounded-[16px] flex items-center justify-center shadow-lg" style="background-image: linear-gradient(135deg, #b84dff 0%, #54E3D5 100%);">
            <img alt="" class="w-[16px] h-[20px]" src="/assets/icon-workflow-arrow.svg" />
          </div>
          <div class="flex flex-col gap-[11px] w-full max-w-[334px]">
            <h3 class="font-bold text-[20px] text-white leading-[28px]">Open & Compliant</h3>
            <p class="font-normal text-[#a1a1aa] text-[14px] leading-[23px]">We champion the freedom to upload. You are welcome to share any content, as long as it is legally compliant.</p>
          </div>
        </div>
        <div class="absolute bg-[rgba(255,102,196,0.1)] blur-[32px] bottom-[-40px] right-[-40px] rounded-full size-[128px] group-hover:bg-[rgba(255,102,196,0.2)] transition-colors"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
