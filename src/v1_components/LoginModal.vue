<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();
const emit = defineEmits(['close']);

function signInWithGoogle() {
  emit('close');
  router.push({ name: 'Dashboard' });
}
</script>

<template>
  <Teleport to="body">
    <!-- Overlay -->
    <Transition name="login-overlay">
      <div 
        class="fixed inset-0 bg-black/70 backdrop-blur-[6px] z-[300] flex items-center justify-center"
        @click.self="$emit('close')"
      >
        <!-- Modal Card -->
        <Transition name="login-modal">
          <div class="bg-[#111111] border border-white/10 rounded-[24px] shadow-[0_30px_60px_rgba(0,0,0,0.6)] w-[420px] max-w-[90vw] p-[40px] flex flex-col items-center gap-[28px] relative">
            
            <!-- Close Button -->
            <button 
              class="absolute top-[16px] right-[16px] size-[32px] flex items-center justify-center rounded-full cursor-pointer transition-colors duration-200 hover:bg-white/5"
              @click="$emit('close')"
            >
              <svg class="size-[12px] text-[#a1a1aa]" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M1 1L11 11M1 11L11 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
              </svg>
            </button>

            <!-- Vanso Logo -->
            <div class="size-[64px] rounded-full overflow-hidden shadow-[0_0_30px_rgba(245,50,138,0.2)]">
              <img alt="Vanso Logo" class="size-full object-cover" src="/vanso-logo.webp" />
            </div>

            <!-- Title -->
            <h2 class="font-bold text-[24px] text-white text-center tracking-[-0.5px] leading-[32px]">Continue to Vanso</h2>

            <!-- Sign in with Google Button -->
            <button 
              class="flex items-center justify-center gap-[12px] w-full bg-white hover:bg-gray-100 rounded-full py-[14px] px-[24px] transition-colors duration-200 cursor-pointer shadow-[0_2px_8px_rgba(0,0,0,0.15)]"
              @click="signInWithGoogle"
            >
              <!-- Google Icon -->
              <svg class="size-[20px] shrink-0" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 0 1-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z" fill="#4285F4"/>
                <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
                <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
              </svg>
              <span class="font-semibold text-[15px] text-[#1f1f1f] leading-[20px]">Sign in with Google</span>
            </button>

            <!-- Privacy Notice -->
            <p class="text-[12px] text-[#71717a] text-center leading-[18px] max-w-[300px]">
              By continuing, you accept our 
              <a href="#" class="text-[#a1a1aa] underline hover:text-white transition-colors">Privacy Policy</a> 
              and 
              <a href="#" class="text-[#a1a1aa] underline hover:text-white transition-colors">Terms of Use</a>
            </p>
          </div>
        </Transition>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.login-overlay-enter-active, .login-overlay-leave-active { transition: opacity 0.3s ease; }
.login-overlay-enter-from, .login-overlay-leave-to { opacity: 0; }
.login-modal-enter-active { transition: opacity 0.3s ease, transform 0.3s ease; }
.login-modal-leave-active { transition: opacity 0.2s ease, transform 0.2s ease; }
.login-modal-enter-from { opacity: 0; transform: scale(0.92) translateY(10px); }
.login-modal-leave-to { opacity: 0; transform: scale(0.95); }
</style>
