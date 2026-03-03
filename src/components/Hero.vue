<template>
  <!-- Header: Full height hero section -->
  <div class="content-stretch flex flex-col items-center relative shrink-0 w-full overflow-hidden min-h-[800px] justify-center">
    
    <!-- Sonic Aura Background Simulation (Fluid Cyberpunk) -->
    <div class="absolute top-[-10%] left-[-10%] w-[600px] h-[600px] bg-vanso-magenta rounded-full mix-blend-screen blur-[150px] opacity-20 pointer-events-none animate-pulse"></div>
    <div class="absolute bottom-[-10%] right-[-10%] w-[600px] h-[600px] bg-vanso-cyan rounded-full mix-blend-screen blur-[150px] opacity-20 pointer-events-none"></div>

    <!-- Container -->
    <div class="flex flex-col items-center max-w-[1024px] mx-auto pt-[48px] pb-[48px] relative w-full px-4 md:px-0 z-10">
      
      <!-- Heading 1 -->
      <div class="flex flex-col items-center relative shrink-0 w-full mt-[16px]">
        <!-- Line 1: "Turn Your AI Music" -->
        <div class="flex justify-center w-full">
          <span class="font-extrabold text-[48px] md:text-[80px] text-white tracking-tight leading-[1.1] text-center">Turn Your AI Music</span>
        </div>
        <!-- Line 2: "Into Global Hits." -->
        <div class="flex justify-center w-full mt-[4px]">
          <span class="font-extrabold text-[48px] md:text-[80px] text-white tracking-tight leading-[1.1] text-center">Into Global Hits.</span>
        </div>
        <!-- Line 3: "Reach 400M+ Listeners." gradient -->
        <div class="flex justify-center w-full mt-[16px]">
          <span class="bg-clip-text text-transparent bg-gradient-to-r from-[#54E3D5] to-[#F5328A] font-extrabold text-[48px] md:text-[80px] tracking-tight leading-[1.1] text-center">
            Reach 400M+<br class="hidden md:inline"> Listeners.
          </span>
        </div>
      </div>
      
      <!-- Buttons container -->
      <div class="flex flex-col md:flex-row gap-[16px] items-center justify-center relative shrink-0 w-full mt-[48px]">
        <!-- Button 1: "Download App" -->
        <button class="bg-gradient-to-br from-vanso-magenta via-vanso-peach to-vanso-cyan text-white font-semibold rounded-full px-[32px] py-[16px] shadow-[0_0_25px_rgba(245,50,138,0.4)] hover:scale-105 hover:shadow-[0_0_35px_rgba(84,227,213,0.5)] transition-all duration-300 text-lg flex gap-[8px] items-center justify-center">
          <img alt="Android" class="size-[20px]" src="/assets/icon-android.svg" style="filter: brightness(0) invert(1);" />
          <span>Download App</span>
        </button>
        
        <!-- Button 2: "Login to Upload" -->
        <button class="bg-white/5 backdrop-blur-xl border border-white/10 text-white font-semibold rounded-full px-[32px] py-[16px] hover:bg-white/10 hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(255,255,255,0.05)] transition-all duration-300 text-lg flex items-center justify-center cursor-pointer" @click="$emit('open-login')">
          <span>Login to Upload</span>
        </button>
      </div>
      
      <!-- Subtitle -->
      <div class="flex flex-col items-center max-w-[768px] px-4 md:px-0 relative shrink-0 w-full mt-[48px]">
        <p class="font-normal leading-relaxed text-zinc-400 text-[18px] md:text-[18px] text-center">
          Don't just generate—get heard.<br>The only platform that puts your AI tracks directly onto millions mobile players.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
defineEmits(['open-login']);
</script>
