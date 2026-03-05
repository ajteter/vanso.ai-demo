<script setup>
import { ref } from 'vue';

const emit = defineEmits(['close']);

const username = ref('vanso_creator');
const description = ref('Digital artist creating 3D assets for VR environments.');
const country = ref('United States');
</script>

<template>
  <div class="fixed right-0 top-0 bottom-0 z-50 backdrop-blur-xl bg-zinc-950 border-l border-white/10 flex flex-col w-140 max-w-[100vw]">
    <!-- Header -->
    <div class="border-b border-white/10 w-full shrink-0">
      <div class="flex items-center justify-between py-6 px-8">
        <div class="flex gap-3 items-center">
          <!-- Settings icon -->
          <svg class="size-[18px] text-white" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13 2.5a2.121 2.121 0 0 1 3 3L5.5 16H2v-3.5L12.5 2l.5.5z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <h2 class="font-bold text-[20px] text-white tracking-[-0.5px] leading-[28px]">Edit Profile</h2>
        </div>
        <!-- Close button -->
        <button 
          class="bg-white/5 border border-white/10 rounded-full size-9 flex items-center justify-center cursor-pointer transition-colors duration-300 hover:bg-white/10"
          @click="$emit('close')"
        >
          <svg class="size-[10px] text-zinc-400" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M1 1L9 9M1 9L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
        </button>
      </div>
    </div>

    <!-- Content (scrollable) -->
    <div class="flex-1 overflow-y-auto">
      <div class="flex flex-col gap-8 items-start p-8">
        <!-- Avatar Section -->
        <div class="flex flex-col gap-4 items-center justify-center w-full">
          <!-- Avatar with border -->
          <div class="relative">
            <div class="bg-transparent border-2 border-vanso-cyan rounded-full shadow-[0_0_15px] shadow-vanso-cyan/50 size-24 overflow-hidden flex items-center justify-center">
              <div 
                class="size-22 rounded-full flex items-center justify-center bg-gradient-to-br from-vanso-magenta to-vanso-cyan"
              >
                <span class="font-bold text-[32px] text-white">JD</span>
              </div>
            </div>
            <!-- Camera badge -->
            <div class="absolute bottom-0 right-0 bg-vanso-cyan border-2 border-black rounded-full p-2 cursor-pointer">
              <svg class="size-3 text-black" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M10.5 9.5C10.5 10.0523 10.0523 10.5 9.5 10.5H2.5C1.94772 10.5 1.5 10.0523 1.5 9.5V4.5C1.5 3.94772 1.94772 3.5 2.5 3.5H4L4.5 2H7.5L8 3.5H9.5C10.0523 3.5 10.5 3.94772 10.5 4.5V9.5Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                <circle cx="6" cy="6.8" r="2" stroke="currentColor" stroke-width="1.2"/>
              </svg>
            </div>
          </div>
          <span class="font-medium text-sm text-vanso-cyan text-center leading-[20px] cursor-pointer hover:underline">Change Photo</span>
        </div>

        <!-- Form Fields -->
        <div class="flex flex-col gap-6 items-start w-full">
          <!-- Username -->
          <div class="flex flex-col gap-2 w-full">
            <label class="font-medium text-sm text-zinc-400 leading-[20px]">Username</label>
            <div class="relative">
              <div class="bg-white/5 border border-white/10 rounded-lg overflow-hidden flex items-center h-11">
                <span class="text-zinc-500 text-base pl-[12px] font-normal">@</span>
                <input 
                  v-model="username"
                  type="text" 
                  class="bg-transparent flex-1 pl-[4px] pr-[17px] py-[13px] text-sm text-white outline-none font-normal"
                />
              </div>
            </div>
            <div class="flex items-center justify-end w-full">
              <span class="text-xs text-zinc-400 text-right leading-[16px]">Max 30 characters</span>
            </div>
          </div>

          <!-- Description -->
          <div class="flex flex-col gap-2 w-full">
            <label class="font-medium text-sm text-zinc-400 leading-[20px]">Description</label>
            <div class="bg-white/5 border border-white/10 rounded-lg overflow-hidden">
              <textarea 
                v-model="description"
                class="bg-transparent w-full px-[13px] py-[13px] text-sm text-white outline-none resize-none font-normal leading-[20px] min-h-25"
              ></textarea>
            </div>
            <div class="flex items-center justify-end w-full">
              <span class="text-xs text-zinc-400 text-right leading-[16px]">Max 150 characters</span>
            </div>
          </div>

          <!-- Country/Region -->
          <div class="flex flex-col gap-2 w-full">
            <label class="font-medium text-sm text-zinc-400 leading-[20px]">Country/Region</label>
            <div class="relative bg-white/5 border border-white/10 rounded-lg overflow-hidden h-11">
              <select 
                v-model="country"
                class="bg-transparent w-full h-full px-3 text-sm text-white outline-none appearance-none cursor-pointer font-normal"
              >
                <option value="United States" class="bg-zinc-950">United States</option>
                <option value="United Kingdom" class="bg-zinc-950">United Kingdom</option>
                <option value="Canada" class="bg-zinc-950">Canada</option>
                <option value="Germany" class="bg-zinc-950">Germany</option>
                <option value="France" class="bg-zinc-950">France</option>
                <option value="Japan" class="bg-zinc-950">Japan</option>
                <option value="China" class="bg-zinc-950">China</option>
                <option value="South Korea" class="bg-zinc-950">South Korea</option>
              </select>
              <!-- Chevron -->
              <svg class="absolute right-[12px] top-1/2 -translate-y-1/2 size-[10px] text-zinc-400 pointer-events-none" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>
        </div>

        <!-- Danger Zone -->
        <div class="pt-[16px] w-full">
          <div class="bg-[rgba(239,68,68,0.05)] border border-[rgba(239,68,68,0.2)] rounded-xl flex flex-col gap-4 items-start p-[21px]">
            <div class="flex gap-2 items-center">
              <!-- Warning icon -->
              <svg class="size-[18px] text-red-500" viewBox="0 0 18 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 1L17 15H1L9 1Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                <line x1="9" y1="6" x2="9" y2="10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                <circle cx="9" cy="12.5" r="0.8" fill="currentColor"/>
              </svg>
              <span class="font-bold text-sm text-red-500 tracking-[0.7px] uppercase leading-[20px]">Danger Zone</span>
            </div>
            <div class="flex items-center justify-between w-full">
              <div class="flex flex-col gap-1">
                <span class="font-medium text-sm text-[rgba(255,255,255,0.9)] leading-[20px]">Delete Account</span>
                <span class="text-xs text-zinc-400 leading-[16px]">Permanently delete your account and all data.</span>
              </div>
              <button class="border border-[rgba(235,73,61,0.5)] rounded-lg px-[17px] py-[9px] cursor-pointer transition-colors duration-300 hover:bg-[rgba(235,73,61,0.1)]">
                <span class="font-medium text-sm text-red-500 text-center leading-[20px]">Delete Account</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Actions -->
    <div class="backdrop-blur-lg bg-[rgba(0,0,0,0.2)] border-t border-white/10 shrink-0 w-full">
      <div class="flex gap-4 items-center justify-center py-6 px-8">
        <button 
          class="border border-white/10 rounded-full flex-[1] py-[13px] cursor-pointer transition-colors duration-300 hover:bg-white/5"
          @click="$emit('close')"
        >
          <span class="font-medium text-sm text-white text-center leading-[20px] block">Cancel</span>
        </button>
        <button 
          class="bg-gradient-to-br from-vanso-magenta via-vanso-peach to-vanso-cyan text-white font-semibold rounded-full flex-[2] py-3 shadow-[0_0_20px_rgba(245,50,138,0.4)] hover:shadow-[0_0_30px_rgba(84,227,213,0.5)] transition-shadow duration-300 cursor-pointer"
        >
          <span class="font-bold text-sm text-center leading-[20px] block">Save Changes</span>
        </button>
      </div>
    </div>
  </div>
</template>
