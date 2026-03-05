<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const showEditDrawer = ref(false);
const editingDrop = ref(null);
const showDeleteConfirm = ref(false);
const deletingIndex = ref(null);

const drops = ref([
  { title: 'Midnight City Remix', plays: '8.1k', likes: '1.9k', date: 'Oct 24, 2023', cover: 1 },
  { title: 'Neon Nights (Original)', plays: '8.1k', likes: '1.9k', date: 'Oct 20, 2023', cover: 2 },
  { title: 'Summer Vibes', plays: '5.6k', likes: '1.2k', date: 'Oct 15, 2023', cover: 3 },
  { title: 'Cyberpunk Dreams', plays: '3.2k', likes: '800', date: 'Oct 10, 2023', cover: 4 },
  { title: 'Lofi Beats Vol. 1', plays: '1.5k', likes: '300', date: 'Oct 05, 2023', cover: 5 },
]);

function getCoverGradient(idx) {
  const gradients = [
    'linear-gradient(135deg, #f5328a 0%, #54e3d5 100%)',
    'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
    'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
    'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
  ];
  return gradients[(idx - 1) % gradients.length];
}

function openEditDrawer(drop) {
  editingDrop.value = { ...drop, description: drop.description || '' };
  showEditDrawer.value = true;
}

function closeEditDrawer() {
  showEditDrawer.value = false;
  editingDrop.value = null;
}

function requestDelete(index) {
  deletingIndex.value = index;
  showDeleteConfirm.value = true;
}

function cancelDelete() {
  showDeleteConfirm.value = false;
  deletingIndex.value = null;
}

function confirmDelete() {
  if (deletingIndex.value !== null) {
    drops.value.splice(deletingIndex.value, 1);
  }
  showDeleteConfirm.value = false;
  deletingIndex.value = null;
}
</script>

<template>
  <div class="flex flex-col gap-8 items-start max-w-320 p-10 w-full">
    <!-- Header -->
    <div class="flex items-center justify-between w-full">
      <h1 class="font-bold text-[30px] text-white tracking-[-0.75px] leading-[36px] italic">My Drops</h1>
      <button 
        class="bg-gradient-to-br from-vanso-magenta via-vanso-peach to-vanso-cyan text-white font-semibold rounded-full px-6 py-[10px] shadow-[0_0_20px] shadow-vanso-magenta/30 hover:shadow-[0_0_30px_rgba(84,227,213,0.5)] transition-shadow duration-300 flex items-center justify-center gap-2 cursor-pointer"
        @click="router.push({ name: 'NewDrop' })"
      >
        <svg class="shrink-0 size-3 text-white" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M6 1V11M1 6H11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <span class="font-bold text-sm text-white text-center leading-[20px]">New Drop</span>
      </button>
    </div>

    <!-- Drops Table -->
    <div class="bg-vanso-card border border-white/10 flex flex-col items-start overflow-hidden rounded-2xl shadow-[0px_25px_50px_-12px_rgba(0,0,0,0.5)] w-full">
      <!-- Table Header -->
      <div class="border-b border-white/10 flex items-center w-full">
        <div class="flex-1 px-6 py-4">
          <span class="font-semibold text-[11px] text-zinc-400 tracking-[1.1px] uppercase">Song Info</span>
        </div>
        <div class="w-50 px-6 py-4">
          <span class="font-semibold text-[11px] text-zinc-400 tracking-[1.1px] uppercase">Metrics</span>
        </div>
        <div class="w-40 px-6 py-4">
          <span class="font-semibold text-[11px] text-zinc-400 tracking-[1.1px] uppercase">Updated</span>
        </div>
        <div class="w-30 px-6 py-4 text-center">
          <span class="font-semibold text-[11px] text-zinc-400 tracking-[1.1px] uppercase">Actions</span>
        </div>
      </div>

      <!-- Table Body -->
      <div class="flex flex-col items-start w-full">
        <div 
          v-for="(drop, i) in drops" 
          :key="i"
          class="flex items-center w-full transition-colors duration-150 hover:bg-[rgba(255,255,255,0.02)]"
          :class="i > 0 ? 'border-t border-[rgba(255,255,255,0.05)]' : ''"
        >
          <!-- Song Info (cover + title) -->
          <div class="flex-1 px-6 py-4 flex items-center gap-4">
            <div 
              class="rounded-lg size-12 border border-[rgba(255,255,255,0.1)] shrink-0"
              :style="{ backgroundImage: getCoverGradient(drop.cover) }"
            ></div>
            <span class="font-medium text-sm text-white leading-[20px]">{{ drop.title }}</span>
          </div>
          <!-- Metrics (plays + likes) -->
          <div class="w-50 px-6 py-4 flex items-center gap-4">
            <div class="flex items-center gap-1">
              <svg class="size-4 text-vanso-cyan" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M8 1.333A6.667 6.667 0 1 0 14.667 8 6.667 6.667 0 0 0 8 1.333zm-1.333 9.334V5.333L10 8l-3.333 2.667z"/>
              </svg>
              <span class="font-normal text-[13px] text-zinc-400 leading-[20px]">{{ drop.plays }}</span>
            </div>
            <div class="flex items-center gap-1">
              <svg class="size-[14px] text-vanso-magenta" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M8 14.25l-1.025-.933C3.1 9.85 1 7.95 1 5.625 1 3.725 2.525 2.2 4.425 2.2c1.088 0 2.138.506 2.825 1.306A3.91 3.91 0 0 1 10.075 2.2C11.975 2.2 13.5 3.725 13.5 5.625c0 2.325-2.1 4.225-5.975 7.7L8 14.25z"/>
              </svg>
              <span class="font-normal text-[13px] text-zinc-400 leading-[20px]">{{ drop.likes }}</span>
            </div>
          </div>
          <!-- Updated date -->
          <div class="w-40 px-6 py-4">
            <span class="font-normal text-[13px] text-zinc-400 leading-[20px]">{{ drop.date }}</span>
          </div>
          <!-- Actions (edit + delete) -->
          <div class="w-30 px-6 py-4 flex items-center justify-center gap-3">
            <button 
              class="flex items-center justify-center rounded-[6px] size-8 cursor-pointer transition-colors duration-200 hover:bg-[rgba(255,255,255,0.05)]"
              @click="openEditDrawer(drop)"
            >
              <svg class="size-4 text-zinc-400" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M11.333 2A1.886 1.886 0 0 1 14 4.667L5.333 13.333H2V10l8.667-8.667.666.667z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
            <button 
              class="flex items-center justify-center rounded-[6px] size-8 cursor-pointer transition-colors duration-200 hover:bg-[rgba(239,68,68,0.1)]"
              @click="requestDelete(i)"
            >
              <svg class="size-4 text-red-500" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2 4h12M5.333 4V2.667a1.333 1.333 0 0 1 1.334-1.334h2.666a1.333 1.333 0 0 1 1.334 1.334V4m2 0v9.333a1.333 1.333 0 0 1-1.334 1.334H4.667a1.333 1.333 0 0 1-1.334-1.334V4h9.334z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Load More Button -->
    <div class="flex justify-center w-full">
      <button class="flex gap-2 items-center px-6 py-[10px] rounded-full bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] cursor-pointer transition-colors duration-200 hover:bg-[rgba(255,255,255,0.08)]">
        <span class="font-medium text-sm text-white text-center leading-[20px]">Load More</span>
        <svg class="size-3 text-zinc-400" viewBox="0 0 12 8" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M1 1.5L6 6.5L11 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
    </div>
  </div>

  <!-- Edit Details Drawer -->
  <Teleport to="body">
    <!-- Overlay -->
    <Transition name="overlay">
      <div 
        v-if="showEditDrawer"
        class="fixed inset-0 bg-black/40 z-[100]"
        @click="closeEditDrawer"
      ></div>
    </Transition>
    <!-- Drawer -->
    <Transition name="drawer">
      <div 
        v-if="showEditDrawer && editingDrop"
        class="fixed right-0 top-0 bottom-0 z-[101] backdrop-blur-[12px] bg-zinc-950 border-l border-[rgba(255,255,255,0.1)] flex flex-col w-125 max-w-[100vw]"
      >
        <!-- Header -->
        <div class="border-b border-[rgba(255,255,255,0.1)] w-full shrink-0">
          <div class="flex items-center justify-between py-6 px-8">
            <div class="flex gap-3 items-center">
              <svg class="size-[18px] text-white" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M13 2.5a2.121 2.121 0 0 1 3 3L5.5 16H2v-3.5L12.5 2l.5.5z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <h2 class="font-bold text-[20px] text-white tracking-[-0.5px] leading-[28px]">Edit Details</h2>
            </div>
            <button 
              class="bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] rounded-full size-9 flex items-center justify-center cursor-pointer transition-colors duration-200 hover:bg-[rgba(255,255,255,0.1)]"
              @click="closeEditDrawer"
            >
              <svg class="size-[10px] text-zinc-400" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M1 1L9 9M1 9L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
              </svg>
            </button>
          </div>
        </div>

        <!-- Content (scrollable) -->
        <div class="flex-1 overflow-y-auto">
          <div class="flex flex-col gap-6 items-start p-8">
            <!-- Cover Art -->
            <div class="flex flex-col gap-3 items-center w-full">
              <div 
                class="rounded-xl w-50 h-50 border border-[rgba(255,255,255,0.1)] shadow-[0px_10px_30px_rgba(0,0,0,0.3)]"
                :style="{ backgroundImage: getCoverGradient(editingDrop.cover), backgroundSize: 'cover' }"
              ></div>
              <span class="font-medium text-sm text-vanso-cyan text-center leading-[20px] cursor-pointer hover:underline">Change Image</span>
            </div>

            <!-- Audio Filename (locked) -->
            <div class="bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] rounded-xl flex items-center gap-3 p-4 w-full">
              <div class="size-10 rounded-lg bg-[rgba(255,255,255,0.05)] flex items-center justify-center shrink-0">
                <svg class="size-5 text-zinc-400" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M11 1H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7l-6-6z" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M11 1v6h6" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <div class="flex flex-col flex-1 min-w-0">
                <span class="font-semibold text-[11px] text-zinc-400 tracking-[0.5px] uppercase leading-[16px]">Audio Filename</span>
                <span class="font-medium text-sm text-white leading-[20px] truncate">song_final.mp3</span>
              </div>
              <svg class="size-4 text-red-500 shrink-0" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="3" y="7" width="10" height="8" rx="2" stroke="currentColor" stroke-width="1.3"/>
                <path d="M5 7V5a3 3 0 0 1 6 0v2" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
              </svg>
            </div>

            <!-- Title -->
            <div class="flex flex-col gap-2 w-full">
              <label class="font-medium text-sm text-zinc-400 leading-[20px]">Title</label>
              <div class="bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] rounded-lg overflow-hidden">
                <input 
                  v-model="editingDrop.title"
                  type="text" 
                  class="bg-transparent w-full px-[17px] py-[13px] text-sm text-white outline-none font-normal"
                />
              </div>
            </div>

            <!-- Language -->
            <div class="flex flex-col gap-2 w-full">
              <label class="font-medium text-sm text-zinc-400 leading-[20px]">Language</label>
              <div class="relative bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] rounded-lg overflow-hidden h-11">
                <select class="bg-transparent w-full h-full px-[17px] text-sm text-white outline-none appearance-none cursor-pointer font-normal">
                  <option value="English" class="bg-zinc-950">English</option>
                  <option value="Spanish" class="bg-zinc-950">Spanish</option>
                  <option value="French" class="bg-zinc-950">French</option>
                  <option value="Chinese" class="bg-zinc-950">Chinese</option>
                  <option value="Japanese" class="bg-zinc-950">Japanese</option>
                  <option value="Korean" class="bg-zinc-950">Korean</option>
                </select>
                <svg class="absolute right-[12px] top-1/2 -translate-y-1/2 size-[10px] text-zinc-400 pointer-events-none" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
            </div>

            <!-- Lyrics -->
            <div class="flex flex-col gap-2 w-full">
              <div class="flex items-center justify-between w-full">
                <label class="font-medium text-sm text-zinc-400 leading-[20px]">Lyrics</label>
                <button class="flex gap-1 items-center px-2 py-1 rounded-[4px] cursor-pointer hover:bg-[rgba(84,227,213,0.05)]">
                  <svg class="size-[13px] text-vanso-cyan" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M6.5 10V2M6.5 2L3.5 5M6.5 2L9.5 5" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M2 9V10.5C2 11.0523 2.44772 11.5 3 11.5H10C10.5523 11.5 11 11.0523 11 10.5V9" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <span class="font-semibold text-xs text-vanso-cyan text-center leading-[16px]">Upload .txt/.lrc</span>
                </button>
              </div>
              <div class="bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] rounded-lg overflow-hidden">
                <textarea 
                  placeholder="Enter or paste lyrics here..."
                  class="bg-transparent w-full px-[17px] py-[13px] text-sm text-white placeholder-[#a1a1aa] outline-none resize-none font-normal leading-[20px] min-h-[150px]"
                ></textarea>
              </div>
            </div>

            <!-- Description -->
            <div class="flex flex-col gap-2 w-full">
              <label class="font-medium text-sm text-zinc-400 leading-[20px]">Description</label>
              <div class="bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.1)] rounded-lg overflow-hidden">
                <textarea 
                  v-model="editingDrop.description"
                  placeholder="Tell your fans about this track..."
                  class="bg-transparent w-full px-[17px] py-[13px] text-sm text-white placeholder-[#a1a1aa] outline-none resize-none font-normal leading-[20px] min-h-30"
                ></textarea>
              </div>
            </div>
          </div>
        </div>

        <!-- Footer Actions -->
        <div class="backdrop-blur-[6px] bg-[rgba(0,0,0,0.2)] border-t border-[rgba(255,255,255,0.1)] shrink-0 w-full">
          <div class="flex gap-4 items-center justify-center py-6 px-8">
            <button 
              class="border border-[rgba(255,255,255,0.1)] rounded-full flex-[1] py-[13px] cursor-pointer transition-colors duration-200 hover:bg-[rgba(255,255,255,0.05)]"
              @click="closeEditDrawer"
            >
              <span class="font-medium text-sm text-white text-center leading-[20px] block">Cancel</span>
            </button>
            <button 
              class="rounded-full flex-[2] py-3 bg-gradient-to-br from-vanso-magenta via-vanso-peach to-vanso-cyan text-white shadow-[0px_0px_20px_0px_rgba(245,50,138,0.4)] hover:shadow-[0_0_30px_rgba(84,227,213,0.5)] transition-shadow duration-300 cursor-pointer"
            >
              <span class="font-bold text-sm text-center leading-[20px] block">Save Changes</span>
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>

  <!-- Delete Confirmation Modal -->
  <Teleport to="body">
    <Transition name="overlay">
      <div 
        v-if="showDeleteConfirm"
        class="fixed inset-0 bg-black/60 backdrop-blur-[4px] z-[200] flex items-center justify-center"
        @click.self="cancelDelete"
      >
        <Transition name="modal-pop">
          <div 
            v-if="showDeleteConfirm"
            class="bg-zinc-950 border border-white/10 rounded-[20px] shadow-[0_25px_60px_rgba(0,0,0,0.6)] w-100 max-w-[90vw] p-8 flex flex-col items-center gap-5"
          >
            <!-- Warning Icon -->
            <div class="size-14 rounded-full bg-[rgba(235,73,61,0.1)] flex items-center justify-center">
              <svg class="size-7 text-red-500" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 9V13M12 17H12.01" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <!-- Title -->
            <h3 class="font-bold text-[20px] text-white text-center leading-[28px]">Delete Drop?</h3>
            <!-- Description -->
            <p class="text-sm text-zinc-400 text-center leading-[22px]">
              This action cannot be undone. The track and all associated data will be permanently removed.
            </p>
            <!-- Actions -->
            <div class="flex gap-3 w-full mt-1">
              <button
                class="flex-1 border border-white/10 rounded-full py-3 cursor-pointer transition-colors duration-200 hover:bg-white/5"
                @click="cancelDelete"
              >
                <span class="font-medium text-sm text-white text-center leading-[20px] block">Cancel</span>
              </button>
              <button
                class="flex-1 bg-red-500 rounded-full py-3 cursor-pointer transition-all duration-200 hover:bg-red-600 shadow-[0_0_15px] shadow-red-500/30"
                @click="confirmDelete"
              >
                <span class="font-bold text-sm text-white text-center leading-[20px] block">Delete</span>
              </button>
            </div>
          </div>
        </Transition>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.overlay-enter-active, .overlay-leave-active { transition: opacity 0.3s ease; }
.overlay-enter-from, .overlay-leave-to { opacity: 0; }
.drawer-enter-active, .drawer-leave-active { transition: transform 0.3s ease; }
.drawer-enter-from, .drawer-leave-to { transform: translateX(100%); }
.modal-pop-enter-active { transition: opacity 0.2s ease, transform 0.2s ease; }
.modal-pop-leave-active { transition: opacity 0.15s ease, transform 0.15s ease; }
.modal-pop-enter-from { opacity: 0; transform: scale(0.95); }
.modal-pop-leave-to { opacity: 0; transform: scale(0.95); }
</style>
