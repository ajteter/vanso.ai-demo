# 💻 Vanso.ai Landing Page - Coding Prompts (v4.0 Premium Edition)

**Project:** Vanso.ai Landing Page (Premium Consumer & Creator Network)
**Design Language: "Sonic Aura" (Premium Minimalist)**
*   **Style:** Apple-like minimalism meets premium music streaming (like Spotify/Apple Music). Extremely clean, no harsh borders, no glitch effects.
*   **Theme:** Deep Dark Mode. Background: Pure Black `#000000` or Very Dark Slate `#0A0A0A`. Text: `#FFFFFF` and `#A1A1AA` (Zinc 400).
*   **Accents:** Soft, glowing "Aura" or "Mesh" gradients in the background (blending Deep Violet, Cyan, and Soft Pink). It should feel like glowing soundwaves.
*   **Effects:** High-quality Glassmorphism (heavy backdrop blur, very subtle white borders at 10% opacity), soft glowing drop-shadows.

---

## 📝 Master Prompt (For One-Shot Generation)

```markdown
Create a premium, highly polished landing page for "Vanso.ai" using Vue 3 and Tailwind CSS. The vibe should be premium, immersive, and native (similar to Apple Music or Vercel), avoiding overly aggressive cyberpunk styles.

**Page Structure & Logic:**

1.  **Floating Navbar:** A sleek, pill-shaped glassmorphism navbar centered at the top.
    *   Left: Logo text "VANSO" (Clean sans-serif, bold, white).
    *   Right: Two actions. 1. A subtle text button "Creator Login". 2. A primary solid button "[ Get App ]" (White background, Black text, slightly rounded).

2.  **Hero Section (The Core):** Full viewport height, centered content.
    *   Background: A breathtaking, smooth "Aurora" mesh gradient (Purple/Cyan/Pink) heavily blurred behind a dark overlay, moving very slowly to simulate breathing soundwaves.
    *   Typography: Massive, elegant Headline. "Get Heard on 100M+ Devices."
    *   Sub-headline: "The AI Audio Network embedded in OPPO & Vivo. Listen to viral drops, or upload yours to trend globally."
    *   **Dual CTAs (Center aligned):**
        *   Primary Action: "[ Download App ]" (Large, glowing gradient background or high-contrast White button).
        *   Secondary Action: "[ Login to Upload ]" (Glassmorphism outline button with a small 'Upload' icon).

3.  **Live Ticker (Social Proof Marquee):** A smooth, infinite scrolling horizontal strip right below the Hero CTAs.
    *   Content: Minimalist glass cards showing real-time activity.
    *   Card Data: Small Avatar + "@username dropped" + "Song Title" + "🔥".

4.  **Creator Features (Bento Grid):** Replace the old waitlist with a feature showcase.
    *   A clean 3-column Bento Grid showing why creators should join.
    *   Card 1: "Smart Import" (Paste links, auto-fill metadata).
    *   Card 2: "Instant Distribution" (Push to OEM lock screens).
    *   Card 3: "Creator Studio" (Manage your AI assets).

5.  **Footer:** Clean, minimalist standard footer.
    *   Top part: "Ready to drop your first track?" -> "[ Go to Creator Studio ]" button.
    *   Bottom part: Logo, Copyright 2026, Social Links (X, TikTok), Legal links (grey text).

**Technical Constraints:**
*   Make it hyper-responsive. On mobile, stack the Dual CTAs (Download App first, Creator Login second).
*   Use standard Tailwind utility classes. Focus on `backdrop-blur-xl`, `bg-white/5`, and subtle typography hierarchy.
```

---

## 🧱 Component-Level Prompts

### Step 1: The Premium Navbar
```markdown
Create a `Navbar.vue` component.
- **Position:** Fixed top, centered, `z-50`, `mt-6`.
- **Shape:** A sleek capsule (rounded-full). `max-w-4xl`.
- **Style:** Premium glassmorphism (`bg-white/5`, `backdrop-blur-2xl`, `border border-white/10`).
- **Left:** "VANSO" text (font-bold, tracking-widest).
- **Right (Desktop):** 
  - Text link: "Creator Login" (hover:text-white text-zinc-400 transition).
  - Button: "Download App" (bg-white text-black rounded-full px-5 py-2 font-medium hover:scale-105 transition).
- **Right (Mobile):** Just show a simple "Get App" pill button.
```

### Step 2: The Hero Section with Aurora Background & Dual CTAs
```markdown
Create a `Hero.vue` component.
- **Layout:** `min-h-[80vh]`, flex-center, column.
- **Background Aura:** Create an absolute positioned div behind the content. Use CSS to create a radial gradient (Purple `#8B5CF6`, Cyan `#06B6D4`) with massive blur (`blur-[120px]`) and opacity around 30%. It should look like a soft glowing cloud.
- **Text:**
  - H1: "Get Heard on 100M+ Devices." (Text size `text-6xl md:text-8xl`, tracking-tight, font-extrabold).
  - P: "The AI Audio Network embedded in OPPO & Vivo. Listen to viral drops, or upload yours to trend globally." (text-zinc-400, max-w-2xl, text-lg md:text-xl).
- **Dual CTAs (Flex row on desktop, col on mobile):**
  - Button 1 (Consumer): "Download App". Use a vibrant gradient background (e.g., `bg-gradient-to-r from-purple-500 to-cyan-500`), white text, large padding, rounded-full.
  - Button 2 (Creator): "Login to Upload". Use glassmorphism (`bg-white/5 border border-white/10`), rounded-full, with an upload icon (`UploadCloud`).
```

### Step 3: The Smooth Live Ticker
```markdown
Create a `LiveTicker.vue` component.
- **Position:** Place it directly below the Hero section to show instant activity.
- **Animation:** Infinite linear CSS translation (`marquee` effect).
- **Card Design:** Very clean and small pill-shaped cards. `bg-white/5`, `backdrop-blur-md`, `rounded-full`, `px-4 py-2`, `border border-white/5`.
- **Content inside Card:** Flex row. 
  - Tiny circular avatar image.
  - Gray text: "@creator dropped"
  - White text: "Neon Nights"
  - Emoji: "🔥"
```

### Step 4: The Creator Bento Box (Replaces Waitlist)
```markdown
Create a `Features.vue` component.
- **Header:** "Why upload on Vanso?"
- **Grid Layout:** CSS Grid, 1 column mobile, 3 columns desktop. `gap-6`.
- **Bento Cards Design:** `bg-[#111111]`, `rounded-3xl`, `border border-white/5`, `p-8`, subtle hover effect (slight lift and border glow).
- **Cards:**
  - Card 1: Icon `Link`, Title "Smart Import", Text "Paste external generation links. We automatically fetch metadata, cover art, and tags."
  - Card 2: Icon `Smartphone`, Title "Direct to OEM", Text "Your tracks bypass traditional algorithms and go straight to system-level audio players."
  - Card 3: Icon `BarChart2`, Title "Creator Analytics", Text "Track real-time plays, saves, and trending metrics from the Web Studio."
```

### Step 5: The Call-to-Action Footer
```markdown
Create a `Footer.vue` component.
- **Top Section (The Final Push):**
  - Centered text: "Ready to launch your AI tracks?"
  - Button: "Go to Creator Studio" (Glassmorphism style).
- **Divider:** A subtle `border-t border-white/10 mt-12 pt-8`.
- **Bottom Section:** Flex between (row on desktop, col on mobile).
  - Left: VANSO Logo + "© 2026 Vansound AI".
  - Right: Row of Links (Privacy, Terms, DMCA) in text-zinc-500.
```