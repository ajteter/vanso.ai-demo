<template>
  <div class="content-stretch flex h-20 items-start justify-center px-4 relative shrink-0 w-full z-50 pt-4">
    <div class="backdrop-blur-[12px] bg-white/5 border border-white/10 content-stretch flex h-full items-center justify-between max-w-288 pl-[24px] pr-[24px] py-3 relative rounded-[9999px] shrink-0 w-full md:w-288">
      <div class="relative shrink-0 flex items-center gap-2.5 cursor-pointer hover:opacity-80 transition-opacity">
        <img alt="Vanso Logo" class="rounded-[100px] size-10 pointer-events-none object-cover" src="/assets/vanso-logo.png" />
        <div class="h-6 relative shrink-0 w-27">
          <img alt="Vanso" class="absolute h-full object-contain" src="/assets/vanso-text.svg" />
        </div>
      </div>
      <div class="relative shrink-0 flex gap-4 items-center">
        <div class="flex gap-1 items-center relative shrink-0 cursor-pointer hover:text-white transition-colors">
          <img alt="Globe" class="size-[15px] opacity-60" src="/assets/icon-container.svg" />
          <span class="font-normal text-zinc-400 text-sm">EN</span>
          <img alt="Arrow down" class="w-[7px] h-1 opacity-60" src="/assets/icon-container1.svg" />
        </div>
        <button class="font-normal text-zinc-400 text-sm whitespace-nowrap hover:text-white transition-colors leading-[20px] cursor-pointer" @click="$emit('open-login')">
          Sign in
        </button>
        <button class="bg-gradient-to-br from-vanso-magenta via-vanso-peach to-vanso-cyan text-white font-semibold rounded-full px-6 py-[10px] shadow-[0_0_20px] shadow-vanso-magenta/30 hover:scale-105 hover:shadow-[0_0_30px_rgba(84,227,213,0.5)] transition-all duration-300 flex items-center justify-center shrink-0">
          <span class="font-bold text-sm text-white leading-[20px]">Get App</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineEmits(['open-login']);
</script>
