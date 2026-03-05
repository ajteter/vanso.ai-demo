<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const title = ref('');
const language = ref('English');
const description = ref('');
const lyrics = ref('');
const coverFile = ref(null);
const audioFile = ref(null);
const audioFileName = ref('');
const isDragging = ref(false);
const confirmed = ref(false);

function handleFileDrop(e) {
  isDragging.value = false;
  const files = e.dataTransfer?.files;
  if (files && files.length > 0) {
    audioFile.value = files[0];
    audioFileName.value = files[0].name;
  }
}

function handleFileSelect(e) {
  const files = e.target?.files;
  if (files && files.length > 0) {
    audioFile.value = files[0];
    audioFileName.value = files[0].name;
  }
}

function handleCoverSelect(e) {
  const files = e.target?.files;
  if (files && files.length > 0) {
    coverFile.value = files[0];
  }
}

function goBack() {
  router.back();
}
</script>

<template>
  <div class="flex flex-col gap-8 items-start max-w-250 pb-[128px] pt-[40px] px-8 w-full">
    <!-- Header -->
    <div class="flex items-start justify-between w-full">
      <h1 class="font-bold text-[30px] text-white tracking-[-0.75px] leading-[36px] drop-shadow-[0_2px_2px_rgba(0,0,0,0.06)]">New Drop</h1>
      <!-- Close Button -->
      <button 
        class="backdrop-blur-[6px] bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] flex items-center justify-center rounded-full size-10 cursor-pointer transition-colors duration-200 hover:bg-[rgba(255,255,255,0.1)]"
        @click="goBack"
      >
        <svg class="size-[14px] text-zinc-400" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M1 1L13 13M1 13L13 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
      </button>
    </div>

    <!-- Upload Dropzone -->
    <!-- Empty state -->
    <div 
      v-if="!audioFileName"
      class="backdrop-blur-[6px] border-2 border-dashed flex flex-col h-26 items-center justify-center rounded-xl w-full cursor-pointer transition-all duration-200"
      :class="isDragging 
        ? 'bg-[rgba(84,227,213,0.08)] border-vanso-cyan' 
        : 'bg-[rgba(255,255,255,0.05)] border-[rgba(255,255,255,0.1)] hover:border-[rgba(255,255,255,0.2)]'"
      @dragover.prevent="isDragging = true"
      @dragleave="isDragging = false"
      @drop.prevent="handleFileDrop"
      @click="$refs.audioInput.click()"
    >
      <input ref="audioInput" type="file" accept="audio/*" class="hidden" @change="handleFileSelect" />
      <div class="flex gap-4 items-center justify-center px-4">
        <!-- Cloud upload icon -->
        <div class="bg-[rgba(84,227,213,0.1)] rounded-full p-3">
          <svg class="size-6 text-vanso-cyan" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 16V8M12 8L9 11M12 8L15 11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M20 16.7428C21.2215 15.734 22 14.2079 22 12.5C22 9.46243 19.5376 7 16.5 7C16.2815 7 16.0771 6.886 15.9661 6.69788C14.6621 4.48016 12.2544 3 9.5 3C5.35786 3 2 6.35786 2 10.5C2 12.5661 2.83545 14.4371 4.18695 15.7935" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <span class="font-semibold text-lg text-white text-center tracking-[0.45px]">Click to upload or drag and drop</span>
      </div>
    </div>
    <!-- Uploaded state -->
    <div 
      v-else
      class="backdrop-blur-[6px] bg-[rgba(84,227,213,0.03)] border border-[rgba(84,227,213,0.3)] flex items-center rounded-xl w-full px-6 py-5"
    >
      <input ref="audioInput" type="file" accept="audio/*" class="hidden" @change="handleFileSelect" />
      <div class="flex items-center gap-4 flex-1">
        <!-- Checkmark icon -->
        <div class="bg-[rgba(84,227,213,0.15)] rounded-full size-10 flex items-center justify-center shrink-0">
          <svg class="size-5 text-vanso-cyan" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M5 10L8.5 13.5L15 6.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="flex flex-col">
          <span class="font-semibold text-base text-white leading-[22px]">{{ audioFileName }}</span>
          <span class="font-normal text-[13px] text-vanso-cyan leading-[18px]">Upload Complete • 45.2 MB</span>
        </div>
      </div>
      <!-- Delete/trash button -->
      <button 
        class="size-9 flex items-center justify-center rounded-lg cursor-pointer transition-colors duration-200 hover:bg-[rgba(239,68,68,0.1)]"
        @click.stop="audioFileName = ''; audioFile = null"
      >
        <svg class="size-[18px] text-zinc-400" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M2.25 4.5h13.5M6 4.5V3a1.5 1.5 0 0 1 1.5-1.5h3A1.5 1.5 0 0 1 12 3v1.5m2.25 0v10.5a1.5 1.5 0 0 1-1.5 1.5h-7.5a1.5 1.5 0 0 1-1.5-1.5V4.5h10.5z" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
    </div>

    <!-- Form Fields -->
    <div class="flex flex-col gap-8 items-start pb-[16px] w-full">
      <!-- Title + Language row -->
      <div class="flex gap-6 items-start w-full">
        <!-- Title -->
        <div class="flex-1 flex flex-col gap-2">
          <label class="font-medium text-sm text-zinc-400 leading-[20px]">Title</label>
          <div class="backdrop-blur-[2px] bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] rounded-lg overflow-hidden shadow-[inset_0px_2px_4px_1px_rgba(0,0,0,0.05)]">
            <input 
              v-model="title"
              type="text" 
              placeholder="e.g. Midnight City"
              class="bg-transparent w-full px-[17px] py-[15px] text-base text-white placeholder-[#a1a1aa] outline-none font-normal"
            />
          </div>
        </div>
        <!-- Language -->
        <div class="flex-1 flex flex-col gap-2">
          <label class="font-medium text-sm text-zinc-400 leading-[20px]">Language</label>
          <div class="relative backdrop-blur-[2px] bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] rounded-lg overflow-hidden shadow-[inset_0px_2px_4px_0px_rgba(0,0,0,0.05)]">
            <select 
              v-model="language"
              class="bg-transparent w-full px-[17px] py-[13px] text-base text-white outline-none appearance-none cursor-pointer font-normal h-[50px]"
            >
              <option value="English" class="bg-zinc-950">English</option>
              <option value="Spanish" class="bg-zinc-950">Spanish</option>
              <option value="French" class="bg-zinc-950">French</option>
              <option value="Chinese" class="bg-zinc-950">Chinese</option>
              <option value="Japanese" class="bg-zinc-950">Japanese</option>
              <option value="Korean" class="bg-zinc-950">Korean</option>
            </select>
            <!-- Dropdown arrow -->
            <svg class="absolute right-[12px] top-1/2 -translate-y-1/2 size-6 text-zinc-400 pointer-events-none" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 9L12 15L18 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Cover Art + Description row -->
      <div class="flex gap-8 items-start w-full">
        <!-- Cover Art -->
        <div class="flex flex-col gap-2 w-50 shrink-0">
          <label class="font-medium text-sm text-zinc-400 leading-[20px]">Cover Art</label>
          <div 
            class="backdrop-blur-[2px] bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] rounded-lg overflow-hidden size-50 flex flex-col items-center justify-center cursor-pointer transition-colors duration-200 hover:bg-[rgba(255,255,255,0.08)] shadow-[inset_0px_2px_4px_1px_rgba(0,0,0,0.05)] relative"
            @click="$refs.coverInput.click()"
          >
            <input ref="coverInput" type="file" accept="image/*" class="hidden" @change="handleCoverSelect" />
            <!-- Upload Image icon -->
            <svg class="size-[22px] text-zinc-400 mb-2" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="3" y="3" width="18" height="18" rx="3" stroke="currentColor" stroke-width="1.5"/>
              <circle cx="8.5" cy="8.5" r="1.5" stroke="currentColor" stroke-width="1.5"/>
              <path d="M3 16L8 11L13 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M13 14L16 11L21 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span class="text-xs text-zinc-400 text-center leading-[16px]">Upload Image<br>3000x3000px</span>
          </div>
        </div>
        <!-- Description -->
        <div class="flex-1 flex flex-col gap-2 self-stretch">
          <label class="font-medium text-sm text-zinc-400 leading-[20px]">Description</label>
          <div class="backdrop-blur-[2px] bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] rounded-lg overflow-hidden flex-1 min-h-50 shadow-[inset_0px_2px_4px_1px_rgba(0,0,0,0.05)]">
            <textarea 
              v-model="description"
              placeholder="Tell your fans about this track..."
              class="bg-transparent w-full h-full px-[17px] py-[13px] text-base text-white placeholder-[#a1a1aa] outline-none resize-none font-normal leading-[24px]"
            ></textarea>
          </div>
        </div>
      </div>

      <!-- Lyrics -->
      <div class="flex flex-col gap-2 w-full">
        <div class="flex items-center justify-between w-full">
          <label class="font-medium text-sm text-zinc-400 leading-[20px]">Lyrics</label>
          <button class="flex gap-1 items-center px-2 py-1 rounded-[4px] cursor-pointer hover:bg-[rgba(84,227,213,0.05)]">
            <!-- Upload icon -->
            <svg class="size-[13px] text-vanso-cyan" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6.5 10V2M6.5 2L3.5 5M6.5 2L9.5 5" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M2 9V10.5C2 11.0523 2.44772 11.5 3 11.5H10C10.5523 11.5 11 11.0523 11 10.5V9" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span class="font-semibold text-xs text-vanso-cyan text-center leading-[16px]">Upload .txt / .lrc</span>
          </button>
        </div>
        <div class="backdrop-blur-[2px] bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] rounded-lg overflow-hidden shadow-[inset_0px_2px_4px_1px_rgba(0,0,0,0.05)]">
          <textarea 
            v-model="lyrics"
            placeholder="Paste lyrics here..."
            class="bg-transparent w-full px-[17px] py-[13px] text-sm text-white placeholder-[#a1a1aa] outline-none resize-none font-['Liberation_Mono',monospace] leading-[20px] min-h-[150px]"
          ></textarea>
        </div>
      </div>
    </div>

    <!-- Action Buttons -->
    <div class="border-t border-[rgba(255,255,255,0.1)] flex items-center justify-between pt-[25px] w-full">
      <!-- Checkbox Confirmation -->
      <label class="flex items-start gap-2.5 cursor-pointer max-w-150 shrink">
        <div class="relative flex items-center mt-[2px]">
          <input 
            v-model="confirmed" 
            type="checkbox" 
            class="peer appearance-none size-4 border border-[rgba(255,255,255,0.2)] bg-[rgba(255,255,255,0.05)] rounded-[4px] checked:bg-vanso-cyan checked:border-vanso-cyan cursor-pointer transition-colors"
          />
          <svg class="absolute w-[10px] h-[10px] left-[3px] top-[3px] text-black opacity-0 peer-checked:opacity-100 pointer-events-none" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M2 7L5.5 10.5L12 3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <span class="text-[13px] text-zinc-400 leading-[18px]">
          By uploading, you confirm that this content comply with our 
          <a href="https://h5.vansound.com/#/communityrule.html" target="_blank" class="text-vanso-cyan hover:underline hover:text-white transition-colors" @click.stop>Community Guidelines</a> 
          and you don't infringe anyone else's rights.
        </span>
      </label>

      <!-- Buttons -->
      <div class="flex gap-4 items-center shrink-0">
        <button class="border border-transparent rounded-full px-[25px] py-[13px] cursor-pointer transition-colors duration-200 hover:bg-[rgba(255,255,255,0.05)]">
          <span class="font-medium text-sm text-zinc-400 text-center leading-[20px]">Save Draft</span>
        </button>
        <button 
          :disabled="!confirmed"
          class="bg-gradient-to-br from-vanso-magenta via-vanso-peach to-vanso-cyan text-white font-semibold rounded-full px-10 py-3 shadow-[0_0_25px] shadow-vanso-magenta/40 disabled:opacity-50 disabled:cursor-not-allowed hover:shadow-[0_0_30px] shadow-vanso-magenta/50 transition-all duration-300 cursor-pointer"
        >
          <span class="font-bold text-sm text-center tracking-[0.35px] leading-[20px]">Post Drop</span>
        </button>
      </div>
    </div>
  </div>
</template>
