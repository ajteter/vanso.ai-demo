<template>
  <div class="backdrop-blur-[2px] content-stretch flex flex-col items-start overflow-hidden py-6 relative shrink-0 w-full select-none">
    
    <!-- Single row marquee with cards -->
    <div class="h-46 relative shrink-0 w-[200%] flex animate-marquee">
      <div class="content-stretch flex h-full items-start relative w-1/2">
        <div class="content-stretch flex gap-6 items-start px-3 relative self-stretch shrink-0 w-full">
          <div v-for="card in cards" :key="'card-'+card.id" class="backdrop-blur-[20px] bg-white/5 border border-white/10 content-stretch flex flex-col gap-3 h-46 items-start justify-center min-w-75 px-4 py-2 relative rounded-[20px] shrink-0 hover:bg-white/10 transition-colors">
            <div class="relative shrink-0 w-42">
              <div class="flex gap-3 items-center px-3 relative w-full">
                <div class="bg-cover bg-center border border-white/20 rounded-full shrink-0 size-8" style="background-image: url('/assets/img-border.png')"></div>
                <div class="flex flex-col items-start relative">
                  <div class="flex font-normal h-4 items-center text-zinc-400 text-xs">
                    <span class="leading-[16px]">{{ card.user }} </span>
                    <span class="leading-[16px] text-vanso-peach ml-1">dropped</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="backdrop-blur-[12px] bg-black/40 border border-white/5 relative rounded-2xl shrink-0 w-75">
              <div class="flex flex-col gap-4 items-center justify-center overflow-clip p-4 rounded-[inherit] w-full">
                <div class="relative shrink-0 w-full">
                  <div class="flex gap-4 items-start relative w-full">
                    <div class="overflow-clip relative rounded-xl shadow-[0px_10px_15px_-3px_rgba(0,0,0,0.5)] shrink-0 size-20">
                      <img alt="Album Art" class="absolute inset-0 size-full object-cover" src="/assets/album-art.png" />
                    </div>
                    <div class="flex flex-1 flex-col items-start justify-center pt-[4px] self-stretch min-w-0">
                      <p class="font-bold text-base text-white leading-[20px] truncate w-full">{{ card.title }}</p>
                      <div class="h-3 shrink-0 w-full"></div>
                      <div class="flex items-center w-full">
                        <div class="flex gap-4 items-center">
                          <div class="flex gap-1.5 items-center">
                            <img alt="" class="size-[15px]" src="/assets/icon-container3.svg" />
                            <span class="font-medium text-sm text-white leading-[20px]">{{ card.plays }}</span>
                          </div>
                          <div class="flex gap-1.5 items-center">
                            <img alt="" class="w-[15px] h-[14px]" src="/assets/icon-container4.svg" />
                            <span class="font-medium text-sm text-white leading-[20px]">{{ card.likes }}</span>
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
      <!-- Duplicate for seamless loop -->
      <div class="content-stretch flex h-full items-start relative w-1/2">
        <div class="content-stretch flex gap-6 items-start px-3 relative self-stretch shrink-0 w-full">
          <div v-for="card in cards" :key="'card-dup-'+card.id" class="backdrop-blur-[20px] bg-white/5 border border-white/10 content-stretch flex flex-col gap-3 h-46 items-start justify-center min-w-75 px-4 py-2 relative rounded-[20px] shrink-0">
            <div class="relative shrink-0 w-42">
              <div class="flex gap-3 items-center px-3 relative w-full">
                <div class="bg-cover bg-center border border-white/20 rounded-full shrink-0 size-8" style="background-image: url('/assets/img-border.png')"></div>
                <div class="flex flex-col items-start relative">
                  <div class="flex font-normal h-4 items-center text-zinc-400 text-xs">
                    <span class="leading-[16px]">{{ card.user }} </span>
                    <span class="leading-[16px] text-vanso-peach ml-1">dropped</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="backdrop-blur-[12px] bg-black/40 border border-white/5 relative rounded-2xl shrink-0 w-75">
              <div class="flex flex-col gap-4 items-center justify-center overflow-clip p-4 rounded-[inherit] w-full">
                <div class="relative shrink-0 w-full">
                  <div class="flex gap-4 items-start relative w-full">
                    <div class="overflow-clip relative rounded-xl shadow-[0px_10px_15px_-3px_rgba(0,0,0,0.5)] shrink-0 size-20">
                      <img alt="Album Art" class="absolute inset-0 size-full object-cover" src="/assets/album-art.png" />
                    </div>
                    <div class="flex flex-1 flex-col items-start justify-center pt-[4px] self-stretch min-w-0">
                      <p class="font-bold text-base text-white leading-[20px] truncate w-full">{{ card.title }}</p>
                      <div class="h-3 shrink-0 w-full"></div>
                      <div class="flex items-center w-full">
                        <div class="flex gap-4 items-center">
                          <div class="flex gap-1.5 items-center">
                            <img alt="" class="size-[15px]" src="/assets/icon-container3.svg" />
                            <span class="font-medium text-sm text-white leading-[20px]">{{ card.plays }}</span>
                          </div>
                          <div class="flex gap-1.5 items-center">
                            <img alt="" class="w-[15px] h-[14px]" src="/assets/icon-container4.svg" />
                            <span class="font-medium text-sm text-white leading-[20px]">{{ card.likes }}</span>
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
</template>

<script setup>
const cards = [
  { id: 1, user: '@neon_drifter', title: 'Midnight City Remix', plays: '8.1k', likes: '1.9k' },
  { id: 2, user: '@synthwave_kid', title: 'Neon Dreams', plays: '12.3k', likes: '3.2k' },
  { id: 3, user: '@bass_prophet', title: 'Deep Ocean Wave', plays: '5.7k', likes: '1.1k' },
  { id: 4, user: '@aurora_beats', title: 'Crystal Cavern', plays: '9.4k', likes: '2.5k' },
  { id: 5, user: '@cosmic_dj', title: 'Starlight Express', plays: '15.2k', likes: '4.8k' },
];
</script>

<style scoped>
.animate-marquee {
  animation: marquee 30s linear infinite;
}
@keyframes marquee {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-50%); }
}
</style>
