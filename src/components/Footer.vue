<template>
  <footer class="bg-black border-t border-white/5 content-stretch flex flex-col items-center overflow-hidden pb-[32px] pt-[33px] relative shrink-0 w-full z-10">
    <div class="max-w-[1280px] relative shrink-0 w-full mx-auto">
      <div class="content-stretch flex flex-col items-center md:items-start max-w-[inherit] px-[24px] relative w-full">
        <div class="border-t border-white/5 content-stretch flex flex-col md:flex-row gap-[48px] items-start justify-between pt-[49px] relative shrink-0 w-full">
          <!-- Logo & Socials -->
          <div class="relative shrink-0 w-full md:w-[272px]">
            <div class="flex flex-col gap-[16px] items-center md:items-start pb-[4px] relative w-full">
              <div class="flex gap-[8px] items-center relative shrink-0 justify-center md:justify-start">
                <div class="flex gap-[10px] items-center justify-center relative shrink-0">
                  <div class="relative rounded-[100px] shrink-0 size-[40px]">
                    <img alt="Vanso" class="absolute inset-0 max-w-none object-cover pointer-events-none rounded-[100px] size-full" src="/assets/vanso-logo.png" />
                  </div>
                  <div class="h-[24px] relative shrink-0 w-[108px]">
                    <img alt="Vanso" class="absolute h-[24px] left-0 top-0 w-[108px] object-contain" src="/assets/vanso-footer-text.svg" />
                  </div>
                </div>
              </div>
              <!-- Social icons: Discord, TikTok, Instagram, X -->
              <div class="flex gap-[12px] items-center relative shrink-0 w-full justify-center md:justify-start mt-4">
                <!-- Discord -->
                <a href="#" class="bg-white/5 backdrop-blur-xl border border-white/10 flex items-center justify-center rounded-full size-[40px] hover:bg-white/20 hover:shadow-[0_0_15px_rgba(255,255,255,0.05)] transition-all duration-300" aria-label="Discord">
                  <svg class="size-[18px] text-[#a1a1aa]" fill="currentColor" viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.095 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.095 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
                </a>
                <!-- TikTok -->
                <a href="#" class="bg-white/5 backdrop-blur-xl border border-white/10 flex items-center justify-center rounded-full size-[40px] hover:bg-white/20 hover:shadow-[0_0_15px_rgba(255,255,255,0.05)] transition-all duration-300" aria-label="TikTok">
                  <svg class="size-[18px] text-[#a1a1aa]" fill="currentColor" viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.5 2.89 2.89 0 0 1-2.89-2.89 2.89 2.89 0 0 1 2.89-2.89c.28 0 .54.04.79.1v-3.5a6.37 6.37 0 0 0-.79-.05A6.34 6.34 0 0 0 3.15 15.2a6.34 6.34 0 0 0 6.34 6.34 6.34 6.34 0 0 0 6.34-6.34V9.37a8.16 8.16 0 0 0 4.76 1.53V7.35a4.82 4.82 0 0 1-1-.66z"/></svg>
                </a>
                <!-- Instagram -->
                <a href="#" class="bg-white/5 backdrop-blur-xl border border-white/10 flex items-center justify-center rounded-full size-[40px] hover:bg-white/20 hover:shadow-[0_0_15px_rgba(255,255,255,0.05)] transition-all duration-300" aria-label="Instagram">
                  <svg class="size-[18px] text-[#a1a1aa]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
                </a>
                <!-- X (Twitter) -->
                <a href="#" class="bg-white/5 backdrop-blur-xl border border-white/10 flex items-center justify-center rounded-full size-[40px] hover:bg-white/20 hover:shadow-[0_0_15px_rgba(255,255,255,0.05)] transition-all duration-300" aria-label="X">
                  <svg class="size-[16px] text-[#a1a1aa]" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                </a>
              </div>
            </div>
          </div>
          
          <!-- Contact info -->
          <div class="relative shrink-0 w-full md:w-[272px] text-center md:text-left">
            <div class="flex flex-col gap-[16px] items-center md:items-start relative w-full">
              <h4 class="font-bold text-[16px] text-white leading-[24px]">Contact</h4>
              <div class="flex flex-col gap-[8px] items-center md:items-start relative shrink-0 w-full">
                <p class="font-normal text-[#a1a1aa] text-[14px] leading-[20px]">service@vansound.com</p>
                <div class="font-normal text-[#a1a1aa] text-[14px] leading-[20px] mt-2">
                  <p class="mb-0">Business Inquiries: </p>
                  <p>office2025@vansound.com</p>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Legal Links -->
          <div class="relative shrink-0 w-full md:w-[592px] text-center md:text-right">
            <div class="flex flex-col gap-[36px] items-center md:items-end relative w-full">
              <div class="flex flex-col items-center md:items-end pb-[16px] relative shrink-0">
                <div class="flex flex-wrap justify-center md:justify-end gap-[12px] md:gap-[24px] items-center relative shrink-0">
                  <a href="#" class="font-normal text-[#71717a] text-[14px] hover:text-white transition-colors">Privacy Policy</a>
                  <a href="#" class="font-normal text-[#71717a] text-[14px] hover:text-white transition-colors">User Agreement</a>
                  <a href="#" class="font-normal text-[#71717a] text-[14px] hover:text-white transition-colors">Community Guidelines</a>
                  <a href="#" class="font-normal text-[#71717a] text-[14px] hover:text-white transition-colors">Copyright Policy</a>
                </div>
              </div>
              <p class="font-normal text-[#52525b] text-[12px] leading-[16px]">© 2026 Vanso. All rights reserved.</p>
            </div>
          </div>
          
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>
