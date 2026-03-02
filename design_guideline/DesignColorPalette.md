# 🎨 Vanso Brand Design System & Color Palette (For AI Vibe Coding)

> **Instructions for AI:**
> Before generating any UI components for the "Vanso" landing page, carefully read and strictly apply the following design system, color palette, and visual principles. This is critical for achieving the "Sonic Aura" premium aesthetic.

## 1. Core Visual Vibe
*   **Aesthetic:** "Premium Dark Mode" meets "Fluid Cyberpunk". Think Apple Music mixed with Arc Browser.
*   **Rule of Restraint:** DO NOT use bright colors for large solid backgrounds. Bright brand colors are strictly reserved for text gradients, button gradients, subtle borders, and heavily blurred background glowing auras.
*   **Material:** Extensive use of "Glassmorphism" for cards and navbars. This mimics the semi-transparent white "V" in the Vanso logo.

## 2. Global Color Palette (Tailwind Configuration)
Treat these as the custom theme colors for the project:

### Backgrounds & Surfaces (The Canvas)
*   **Deep Void (Main Background):** `#000000` (Use `bg-black` or `bg-[#000000]`).
*   **Card Surface:** `#0A0A0B` or `rgba(255, 255, 255, 0.03)` (Use `bg-[#0A0A0B]` or `bg-white/5`).
*   **Borders:** `rgba(255, 255, 255, 0.1)` (Use `border-white/10` for subtle card outlines).

### Brand Accents (Extracted from Vanso Logo)
*   **Vanso Magenta:** `#F5328A` (Neon Pink - Left side of logo).
*   **Vanso Cyan:** `#54E3D5` (Aqua/Teal - Right side of logo).
*   **Vanso Peach:** `#ECA08B` (Warm Orange/Peach - Top right transition).

### Typography
*   **Primary Text (Headings/Important):** `#FFFFFF` (Pure White).
*   **Secondary Text (Paragraphs/Subtitles):** `#A1A1AA` (Zinc 400).
*   **Muted Text (Footers/Hints):** `#71717A` (Zinc 500).

## 3. Key UI Components & Effects (How to apply the colors)

When generating specific components, use these exact styling patterns:

### A. The "Sonic Aura" Background (For Hero Sections)
Create large, absolute-positioned, heavily blurred orbs in the background to simulate a glowing, fluid music vibe.
*   *Implementation idea:*
    `<div class="absolute top-10 left-10 w-[500px] h-[500px] bg-[#F5328A] rounded-full mix-blend-screen blur-[150px] opacity-20 animate-pulse"></div>`
    `<div class="absolute bottom-10 right-10 w-[500px] h-[500px] bg-[#54E3D5] rounded-full mix-blend-screen blur-[150px] opacity-20"></div>`

### B. Primary CTA Button (The Conversion Button)
Buttons like "Download App" must use a diagonal gradient combining the brand colors, just like the logo's background.
*   *Implementation idea:*
    `class="bg-gradient-to-br from-[#F5328A] via-[#ECA08B] to-[#54E3D5] text-white font-semibold rounded-full px-6 py-3 shadow-[0_0_20px_rgba(245,50,138,0.3)] hover:scale-105 transition-transform"`

### C. Highlight Text Gradient (For Big Headlines)
Use text clipping for keywords like "400M+ Listeners".
*   *Implementation idea:*
    `class="bg-clip-text text-transparent bg-gradient-to-r from-[#54E3D5] to-[#F5328A]"`

### D. Glassmorphism Cards (For Features/Bento Grid/Ticker)
Cards should look like translucent glass floating over the dark background.
*   *Implementation idea:*
    `class="bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 hover:bg-white/10 transition-colors"`

## 4. Typography Guidelines
*   **Font Family:** Use `Inter` or a similar clean, modern sans-serif.
*   **Headings:** Use high contrast. Very large font sizes (`text-5xl` to `text-8xl`), bold weights (`font-extrabold`), tight tracking (`tracking-tight`).
*   **Body:** Keep it readable, muted (`text-zinc-400`), with comfortable line height (`leading-relaxed`).

> **Final Check for AI:** Before outputting code, verify that the overall contrast is high (bright text on pure black), and the brand colors (`#F5328A` and `#54E3D5`) are used exclusively as glowing accents, gradients, or button fills, NEVER as flat background colors for large containers.