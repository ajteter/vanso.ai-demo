<template>
  <div class="backdrop-blur-[2px] content-stretch flex flex-col items-start overflow-hidden py-[24px] relative shrink-0 w-full mt-12 mb-8 select-none">
    
    <!-- Top row / Marquee 1 -->
    <div class="h-[184px] relative shrink-0 w-[200%] flex animate-marquee">
      <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex h-full items-start relative w-1/2 justify-around">
        <div class="content-stretch flex gap-[24px] items-start px-[12px] relative self-stretch shrink-0 w-full">
          <!-- Card Repeat -->
          <div v-for="i in 5" :key="'card-'+i" class="backdrop-blur-[20px] bg-white/5 border border-white/10 content-stretch flex flex-col gap-[12px] h-[184px] items-start justify-center min-w-[300px] px-[16px] py-[8px] relative rounded-[20px] shrink-0 hover:bg-white/10 transition-colors">
            <div class="relative shrink-0 w-[168.17px]">
              <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[12px] items-center px-[12px] relative w-full">
                <div class="bg-cover bg-center border border-[rgba(255,255,255,0.2)] border-solid rounded-[9999px] shrink-0 size-[32px]" style="background-image: url('/assets/img-border.png')"></div>
                <div class="content-stretch flex flex-[1_0_0] flex-col items-start min-h-px min-w-px relative">
                  <div class="flex flex-col font-normal h-[16px] justify-center leading-[0] relative shrink-0 text-[#a1a1aa] text-[12px] w-[136.17px]">
                    <p class="whitespace-pre-wrap">
                      <span class="leading-[16px]">@neon_drifter </span>
                      <span class="leading-[16px] text-[#eca08b]">dropped</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <div class="backdrop-blur-[12px] bg-black/40 border border-[rgba(255,255,255,0.05)] border-solid relative rounded-[16px] shrink-0 w-[300px]">
              <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex flex-col gap-[16px] items-center justify-center overflow-clip p-[16px] relative rounded-[inherit] w-full">
                <div class="relative shrink-0 w-full">
                  <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[16px] items-start relative w-full">
                    <div class="bg-[rgba(255,255,255,0)] content-stretch flex flex-col items-start justify-center overflow-clip relative rounded-[12px] shadow-[0px_10px_15px_-3px_rgba(0,0,0,0.5),0px_4px_6px_-4px_rgba(0,0,0,0.5)] shrink-0 size-[80px]">
                      <div class="flex-[1_0_0] min-h-px min-w-px relative w-full">
                        <div class="absolute inset-0 overflow-hidden pointer-events-none">
                          <img alt="" class="absolute left-0 max-w-none size-full top-0 object-cover" src="/assets/album-art.png" />
                        </div>
                      </div>
                    </div>
                    <div class="content-stretch flex flex-[1_0_0] flex-col items-start justify-center min-h-px min-w-px pt-[4px] relative self-stretch">
                      <div class="content-stretch flex flex-col items-start overflow-clip pr-[64px] relative shrink-0 w-full">
                        <div class="flex flex-col font-bold justify-center leading-[0] not-italic relative shrink-0 text-[16px] text-white whitespace-nowrap">
                          <p class="leading-[20px]">Midnight City Remix</p>
                        </div>
                      </div>
                      <div class="content-stretch flex flex-col items-start pt-[4px] relative shrink-0 w-full">
                        <div class="h-[12px] shrink-0 w-full"></div>
                      </div>
                      <div class="content-stretch flex flex-col items-start relative shrink-0 w-full">
                        <div class="content-stretch flex items-center relative shrink-0 w-full">
                          <div class="content-stretch flex gap-[16px] items-center relative shrink-0 w-[191.5px]">
                            <div class="content-stretch flex gap-[6px] items-center relative shrink-0">
                              <div class="relative shrink-0 size-[15px]">
                                <img alt="" class="absolute block max-w-none size-full" src="/assets/icon-container3.svg" />
                              </div>
                              <div class="content-stretch flex flex-col items-start relative shrink-0">
                                <div class="flex flex-col font-medium justify-center leading-[0] not-italic relative shrink-0 text-[14px] text-white whitespace-nowrap">
                                  <p class="leading-[20px]">8.1k</p>
                                </div>
                              </div>
                            </div>
                            <div class="content-stretch flex gap-[6px] items-center relative shrink-0">
                              <div class="h-[13.762px] relative shrink-0 w-[15px]">
                                <img alt="" class="absolute block max-w-none size-full" src="/assets/icon-container4.svg" />
                              </div>
                              <div class="content-stretch flex flex-col items-start relative shrink-0">
                                <div class="flex flex-col font-medium h-[20px] justify-center leading-[0] not-italic relative shrink-0 text-[14px] text-white w-[26.59px]">
                                  <p class="leading-[20px] whitespace-pre-wrap">1.9k</p>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex h-full items-start relative w-1/2 justify-around">
        <div class="content-stretch flex gap-[24px] items-start px-[12px] relative self-stretch shrink-0 w-full">
          <!-- Card Repeat for infinite duplicate -->
          <div v-for="i in 5" :key="'card-dup-'+i" class="backdrop-blur-[20px] bg-white/5 border border-white/10 content-stretch flex flex-col gap-[12px] h-[184px] items-start justify-center min-w-[300px] px-[16px] py-[8px] relative rounded-[20px] shrink-0">
            <div class="relative shrink-0 w-[168.17px]">
              <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[12px] items-center px-[12px] relative w-full">
                <div class="bg-cover bg-center border border-[rgba(255,255,255,0.2)] border-solid rounded-[9999px] shrink-0 size-[32px]" style="background-image: url('/assets/img-border.png')"></div>
                <div class="content-stretch flex flex-[1_0_0] flex-col items-start min-h-px min-w-px relative">
                  <div class="flex flex-col font-normal h-[16px] justify-center leading-[0] relative shrink-0 text-[#a1a1aa] text-[12px]">
                    <p class="whitespace-pre-wrap">
                      <span class="leading-[16px]">@neon_drifter </span>
                      <span class="leading-[16px] text-[#eca08b]">dropped</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <div class="backdrop-blur-[12px] bg-black/40 border border-[rgba(255,255,255,0.05)] border-solid relative rounded-[16px] shrink-0 w-[300px]">
              <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex flex-col gap-[16px] items-center justify-center overflow-clip p-[16px] relative rounded-[inherit] w-full">
                <div class="relative shrink-0 w-full">
                  <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[16px] items-start relative w-full">
                    <div class="bg-[rgba(255,255,255,0)] content-stretch flex flex-col items-start justify-center overflow-clip relative rounded-[12px] shadow-xl shrink-0 size-[80px]">
                      <div class="absolute inset-0 overflow-hidden pointer-events-none">
                        <img alt="" class="absolute left-0 max-w-none size-full top-0 object-cover" src="/assets/album-art.png" />
                      </div>
                    </div>
                    <div class="content-stretch flex flex-[1_0_0] flex-col items-start justify-center min-h-px min-w-px pt-[4px] relative self-stretch">
                      <div class="content-stretch flex flex-col items-start overflow-clip relative shrink-0 w-full">
                        <p class="font-bold text-[16px] text-white leading-[20px]">Midnight City Remix</p>
                      </div>
                      <div class="h-[12px] shrink-0 w-full"></div>
                      <div class="content-stretch flex items-center relative shrink-0 w-full">
                        <div class="content-stretch flex gap-[16px] items-center relative shrink-0">
                          <div class="content-stretch flex gap-[6px] items-center relative shrink-0">
                            <div class="relative shrink-0 size-[15px]"><img alt="" class="absolute block max-w-none size-full" src="/assets/icon-container3.svg" /></div>
                            <div class="font-medium text-[14px] text-white"><p class="leading-[20px]">8.1k</p></div>
                          </div>
                          <div class="content-stretch flex gap-[6px] items-center relative shrink-0">
                            <div class="h-[13.762px] relative shrink-0 w-[15px]"><img alt="" class="absolute block max-w-none size-full" src="/assets/icon-container4.svg" /></div>
                            <div class="font-medium text-[14px] text-white"><p class="leading-[20px]">1.9k</p></div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom row / Marquee 2 (Skeletons) -->
    <div class="h-[52px] mt-6 relative shrink-0 w-[200%] flex animate-marquee-reverse opacity-70">
      <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex h-full items-start relative w-1/2 justify-around">
        <div class="content-stretch flex gap-[24px] items-start px-[12px] relative self-stretch shrink-0 w-full">
          <div class="backdrop-blur-[20px] bg-[rgba(255,255,255,0.03)] border border-[rgba(255,255,255,0.1)] border-solid content-stretch flex gap-[12px] h-full items-center min-w-[300px] pl-[17px] pr-[80.59px] py-[9px] relative rounded-[9999px] shrink-0" >
            <div class="rounded-[9999px] shrink-0 size-[32px] bg-gradient-to-tr from-[#b84dff] to-[#ff66c4]"></div>
            <div class="relative shrink-0 w-[158.41px]">
              <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex flex-col items-start relative w-full gap-2">
                <div class="h-[12px] rounded bg-white/10 shrink-0 w-full"></div>
                <div class="h-[12px] rounded bg-white/20 shrink-0 w-1/2"></div>
              </div>
            </div>
          </div>
          <div class="backdrop-blur-[20px] bg-[rgba(255,255,255,0.03)] border border-[rgba(255,255,255,0.1)] border-solid content-stretch flex gap-[12px] h-full items-center min-w-[300px] pl-[17px] pr-[80.59px] py-[9px] relative rounded-[9999px] shrink-0" >
            <div class="rounded-[9999px] shrink-0 size-[32px] bg-gradient-to-tr from-[#ff66c4] to-[#b84dff]"></div>
            <div class="relative shrink-0 w-[158.41px]">
              <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex flex-col items-start relative w-full gap-2">
                <div class="h-[12px] bg-white/10 rounded shrink-0 w-full"></div>
                <div class="h-[12px] bg-white/20 rounded shrink-0 w-2/3"></div>
              </div>
            </div>
          </div>
          <div class="backdrop-blur-[20px] bg-[rgba(255,255,255,0.03)] border border-[rgba(255,255,255,0.1)] border-solid content-stretch flex gap-[12px] h-full items-center min-w-[300px] pl-[17px] pr-[80.59px] py-[9px] relative rounded-[9999px] shrink-0" >
            <div class="rounded-[9999px] shrink-0 size-[32px] bg-gradient-to-tr from-[#5ce1ff] to-[#b84dff]"></div>
            <div class="relative shrink-0 w-[158.41px]">
              <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex flex-col items-start relative w-full gap-2">
                <div class="h-[12px] rounded bg-white/10 shrink-0 w-full"></div>
                <div class="h-[12px] rounded bg-white/20 shrink-0 w-1/3"></div>
              </div>
            </div>
          </div>
          <div class="backdrop-blur-[20px] bg-[rgba(255,255,255,0.03)] border border-[rgba(255,255,255,0.1)] border-solid content-stretch flex gap-[12px] h-full items-center min-w-[300px] pl-[17px] pr-[80.59px] py-[9px] relative rounded-[9999px] shrink-0" >
            <div class="rounded-[9999px] shrink-0 size-[32px] bg-gradient-to-tr from-[#ff66c4] to-[#5ce1ff]"></div>
            <div class="relative shrink-0 w-[158.41px]">
              <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex flex-col items-start relative w-full gap-2">
                <div class="h-[12px] rounded bg-white/10 shrink-0 w-full"></div>
                <div class="h-[12px] rounded bg-white/20 shrink-0 w-3/4"></div>
              </div>
            </div>
          </div>
          <div class="backdrop-blur-[20px] bg-[rgba(255,255,255,0.03)] border border-[rgba(255,255,255,0.1)] border-solid content-stretch flex gap-[12px] h-full items-center min-w-[300px] pl-[17px] pr-[80.59px] py-[9px] relative rounded-[9999px] shrink-0" >
            <div class="rounded-[9999px] shrink-0 size-[32px] bg-gradient-to-tr from-[#5ce1ff] to-[#54e3d5]"></div>
            <div class="relative shrink-0 w-[158.41px]">
              <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex flex-col items-start relative w-full gap-2">
                <div class="h-[12px] rounded bg-white/10 shrink-0 w-full"></div>
                <div class="h-[12px] rounded bg-white/20 shrink-0 w-1/4"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Duplicate for second half of marquee -->
      <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex h-full items-start relative w-1/2 justify-around">
        <div class="content-stretch flex gap-[24px] items-start px-[12px] relative self-stretch shrink-0 w-full">
          <!-- Duplicated skeletons... -->
          <div v-for="color in ['from-[#b84dff] to-[#ff66c4]', 'from-[#ff66c4] to-[#b84dff]', 'from-[#5ce1ff] to-[#b84dff]', 'from-[#ff66c4] to-[#5ce1ff]', 'from-[#5ce1ff] to-[#54e3d5]']" :key="'skel-dup-'+color" class="backdrop-blur-[20px] bg-[rgba(255,255,255,0.03)] border border-[rgba(255,255,255,0.1)] border-solid content-stretch flex gap-[12px] h-full items-center min-w-[300px] pl-[17px] pr-[80.59px] py-[9px] relative rounded-[9999px] shrink-0">
            <div :class="['rounded-[9999px] shrink-0 size-[32px] bg-gradient-to-tr', color]"></div>
            <div class="relative shrink-0 w-[158.41px]">
              <div class="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex flex-col items-start relative w-full gap-2">
                <div class="h-[12px] rounded bg-white/10 shrink-0 w-full"></div>
                <div class="h-[12px] rounded bg-white/20 shrink-0 w-1/2"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.animate-marquee {
  animation: marquee 30s linear infinite;
}
.animate-marquee-reverse {
  animation: marquee 20s linear infinite reverse;
}
@keyframes marquee {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-50%); }
}
</style>
