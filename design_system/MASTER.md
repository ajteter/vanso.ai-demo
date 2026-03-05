# Vanso Brand Design System (Master)

## 1. Core Visual Vibe
- **Aesthetic**: Premium Dark Mode meets Fluid Cyberpunk. Think Apple Music mixed with Arc Browser.
- **Rule of Restraint**: DO NOT use bright colors for large solid backgrounds. Bright colors are strictly reserved for:
  - Text gradients
  - Button gradients
  - Subtle borders
  - Heavily blurred background glowing auras
- **Material**: Glassmorphism (`bg-white/5` with `backdrop-blur-xl`) mimics the semi-transparent white "V" in the logo.

## 2. Product Identity
- **Product Type**: AI Media & Audio Creation Platform
- **Industry**: AI / Music tech / SaaS

## 3. Global Color Palette (Tailwind)
**Backgrounds & Surfaces**
- Deep Void (Main Background): `#000000` (`bg-black`)
- Card Surface: `#0A0A0B` or `rgba(255, 255, 255, 0.03)` (`bg-white/5`)
- Borders: `rgba(255, 255, 255, 0.1)` (`border-white/10`)

**Brand Accents**
- Vanso Magenta: `#F5328A` (Neon Pink)
- Vanso Cyan: `#54E3D5` (Aqua/Teal)
- Vanso Peach: `#ECA08B` (Warm Orange/Peach)

**Typography Colors**
- Primary Text: `#FFFFFF` (Pure White)
- Secondary Text: `#A1A1AA` (Zinc 400)
- Muted Text: `#71717A` (Zinc 500)

## 4. UI/UX Pro Max Rules strictly applied
- **Accessibility**: 4.5:1 contrast ratio guaranteed by strictly pairing `#FFFFFF` or `#A1A1AA` against `#000000`. 
- **Touch Targets**: All action buttons min 44x44px padding structure.
- **Hover States**: No layout shifting (strictly avoiding `transform: scale` without bounds, mostly using `bg-white/10` or `brightness` changes). Hover on cards uses smooth `transition-colors duration-300`.
- **Transitions**: 150-300ms micro-interactions.
- **Icons**: Utilize SVG strictly (Lucide/Heroicons), sizing fixed `w-6 h-6`. No emojis for critical UI.

## 5. Components & Effects

### The "Sonic Aura" Background
A glowing background using extremely blurred `mix-blend-screen` standard divs.
```html
<!-- Example Aura -->
<div class="fixed top-10 left-10 w-[500px] h-[500px] bg-[#F5328A] rounded-full mix-blend-screen blur-[150px] opacity-20 animate-pulse"></div>
```

### Primary CTA
```html
<button class="bg-gradient-to-br from-[#F5328A] via-[#ECA08B] to-[#54E3D5] text-white font-semibold rounded-full px-8 py-4 shadow-[0_0_20px_rgba(245,50,138,0.3)] hover:scale-105 hover:shadow-[0_0_30px_rgba(245,50,138,0.5)] transition-all duration-300 cursor-pointer">
</button>
```

### Highlight Text Gradient
```html
<span class="bg-clip-text text-transparent bg-gradient-to-r from-[#54E3D5] to-[#F5328A]">Highlighted text</span>
```

### Glassmorphism Cards
```html
<div class="bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 hover:bg-white/10 transition-colors duration-300">
</div>
```

## 6. Typography
- **Family**: Inter
- **Headings**: `text-5xl` to `text-8xl`, `font-extrabold`, `tracking-tight`
- **Body**: `text-zinc-400`, `leading-relaxed`
