<script setup>
import { ref } from 'vue';
import { ArrowRight, Loader2, CheckCircle2 } from 'lucide-vue-next';
import confetti from 'canvas-confetti';

const state = ref('idle'); // idle, loading, success
const email = ref('');

const submit = () => {
  if (!email.value) return;
  state.value = 'loading';
  
  setTimeout(() => {
    state.value = 'success';
    confetti({
      particleCount: 150,
      spread: 70,
      origin: { y: 0.6 },
      colors: ['#CCFF00', '#B026FF', '#ffffff']
    });
  }, 2000);
};
</script>

<template>
  <div class="w-full max-w-3xl mx-auto py-32 px-4 min-h-[500px] flex items-center justify-center relative">
    
    <!-- Background Glow -->
    <div class="absolute inset-0 bg-neon-purple/5 blur-[100px] rounded-full pointer-events-none"></div>

    <!-- Idle State -->
    <transition name="fade" mode="out-in">
      <div v-if="state === 'idle'" key="idle" class="w-full relative z-10">
        <label class="block text-neon-green font-mono text-sm mb-4 tracking-widest pl-1 text-glow">JOIN THE REVOLUTION</label>
        <form @submit.prevent="submit" class="relative group">
          <input 
            v-model="email"
            type="email" 
            placeholder="Enter your email..." 
            class="w-full bg-transparent border-b-2 border-white/20 text-4xl md:text-6xl font-light py-6 text-white placeholder:text-white/20 focus:outline-none focus:border-neon-green transition-all focus:shadow-[0_10px_20px_-10px_rgba(204,255,0,0.2)]"
            required
          />
          <button type="submit" class="absolute right-0 top-1/2 -translate-y-1/2 text-white/50 hover:text-neon-green hover:scale-110 transition-all disabled:opacity-50">
            <ArrowRight class="w-12 h-12 md:w-20 md:h-20" />
          </button>
        </form>
      </div>

      <!-- Loading State -->
      <div v-else-if="state === 'loading'" key="loading" class="flex flex-col items-center gap-8 relative z-10">
        <div class="relative">
          <div class="w-20 h-20 border-4 border-neon-purple/30 border-t-neon-green rounded-full animate-spin"></div>
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="w-10 h-10 bg-white/10 rounded-full animate-pulse"></div>
          </div>
        </div>
        <p class="text-white/50 animate-pulse font-mono tracking-widest text-lg">CONNECTING_NEURAL_NET...</p>
      </div>

      <!-- Success State -->
      <div v-else key="success" class="flex flex-col items-center w-full relative z-10">
        <div class="glass-panel w-full max-w-md p-8 md:p-12 rounded-3xl border-l-[6px] border-l-neon-green relative overflow-hidden group shadow-[0_0_50px_rgba(204,255,0,0.1)] hover:shadow-[0_0_80px_rgba(204,255,0,0.2)] transition-shadow">
          <!-- Background Decoration -->
          <div class="absolute -right-10 -top-10 w-40 h-40 bg-neon-green/20 blur-3xl rounded-full"></div>
          
          <div class="flex justify-between items-start mb-10">
            <div>
              <h3 class="text-neon-green font-black text-3xl tracking-tighter shadow-neon">YOU ARE IN</h3>
              <p class="text-white/60 text-sm mt-1 tracking-wider">WELCOME TO THE FUTURE</p>
            </div>
            <CheckCircle2 class="text-neon-green w-10 h-10" />
          </div>
          
          <div class="border-t-2 border-dashed border-white/10 my-8 relative">
            <div class="absolute -left-14 -top-3 w-6 h-6 bg-[#050505] rounded-full"></div>
            <div class="absolute -right-14 -top-3 w-6 h-6 bg-[#050505] rounded-full"></div>
          </div>
          
          <div class="flex justify-between items-end">
            <div>
              <p class="text-white/40 text-xs font-mono mb-1">QUEUE ID</p>
              <p class="text-white font-mono text-2xl tracking-[0.2em]">#8492</p>
            </div>
            <div class="text-right">
              <p class="text-white/40 text-xs font-mono mb-1">STATUS</p>
              <span class="bg-neon-green/10 border border-neon-green/30 text-neon-green text-xs font-bold px-3 py-1.5 rounded-full">CONFIRMED</span>
            </div>
          </div>
          
          <!-- Access Code -->
           <div class="mt-8 pt-4 border-t border-white/5 flex justify-center opacity-50">
             <div class="h-8 w-48 bg-white/10 rounded flex gap-1 items-center justify-center overflow-hidden">
               <div v-for="i in 20" :key="i" class="w-1 h-4 bg-white/40"></div>
             </div>
           </div>
        </div>
        
        <button class="mt-12 text-white/60 hover:text-white hover:underline decoration-neon-purple underline-offset-8 transition-all text-sm tracking-wide">
          Download App to Skip Queue ->
        </button>
      </div>
    </transition>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(20px);
}
</style>
