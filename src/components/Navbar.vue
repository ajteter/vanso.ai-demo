<script setup>
// No script logic needed for now
</script>

<template>
  <div class="fixed top-0 left-0 right-0 z-50 flex justify-center mt-6 px-4 pointer-events-none">
    <nav class="flex items-center justify-between w-full max-w-4xl px-6 py-3 bg-white/5 backdrop-blur-2xl border border-white/10 rounded-full pointer-events-auto">
      
      <!-- Left: Logo -->
      <div class="flex items-center gap-2 cursor-pointer">
        <span class="text-xl font-bold tracking-widest text-white">VANSO</span>
      </div>

      <!-- Right: Actions (Desktop & Mobile) -->
      <div class="flex items-center gap-4 md:gap-6">
        <a href="#" class="hidden md:block text-sm text-zinc-400 hover:text-white transition-colors duration-200">
          Creator Login
        </a>
        <button class="bg-white text-black rounded-full px-5 py-2 text-sm font-medium hover:scale-105 transition-transform duration-200 shadow-[0_0_15px_rgba(255,255,255,0.3)]">
          Get App
        </button>
      </div>

    </nav>
  </div>
</template>

<style scoped>
@keyframes glitch-1 {
  0% { transform: translate(0); }
  20% { transform: translate(-2px, 2px); }
  40% { transform: translate(-2px, -2px); }
  60% { transform: translate(2px, 2px); }
  80% { transform: translate(2px, -2px); }
  100% { transform: translate(0); }
}
@keyframes glitch-2 {
  0% { transform: translate(0); }
  20% { transform: translate(2px, -2px); }
  40% { transform: translate(2px, 2px); }
  60% { transform: translate(-2px, 2px); }
  80% { transform: translate(-2px, -2px); }
  100% { transform: translate(0); }
}

.animate-glitch-1 {
  animation: glitch-1 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) both infinite;
}
.animate-glitch-2 {
  animation: glitch-2 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) both infinite;
  animation-delay: 0.1s;
}
</style>
