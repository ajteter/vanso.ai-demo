# 📋 Prompt 2: H5 Tracks List (单曲列表)

## 📌 Context & Vibe
Create a mobile-first "Tracks List" page for an AI music platform. 
**Style**: Premium Dark Mode (`#000000`), compact, high-performance feel.

---

## 🎨 Layout & UI Components

### 1. Navigation Shell
- Inherit the top navigation tabs from the overview page.
- Active tab: "单曲数据" (White, bold, gradient underline).
- Inactive tab: "账号总览" (Zinc-500).

### 2. Sort Selection Bar
- A full-width horizontal switcher with `bg-white/5` background and `border-vanso-border`.
- **Options**: "按播放量" (Active) and "按发布时间".
- **Styling**: Center-aligned text, `bg-white/10` for the active background, `min-h-[40px]` for touch usability.

### 3. Track List Items
- **Container**: A vertical stack of rounded-2xl cards (`bg-[#0A0A0B]`).
- **Row Content**:
  - **Left Section**: 44x44px rounded-xl thumbnail placeholder (with a vibrant brand-colored icon tint) + Track Title (Bold, `15px`) + Status/Date (`11px` Zinc).
  - **Right Section**: "播放量" label + Large metric number (Bold, `15px`).
- **Interactive States**:
  - On Touch (`active`): Use `scale-98` and a subtle `bg-white/6` highlight.
  - Titles should support truncation (`truncate`) for very long names.
- **Visual Flourish**: Small colored icons (Cyan, Peach, etc.) next to track titles to differentiate genres/styles.

---

## 📱 Mobile UX Requirements
- **Performance**: High scroll performance on H5.
- **Touch Target**: Every list item acts as a button to open the analytics drawer.
- **Vertical Rhythm**: Consistent padding (`p-4`) and gap (`gap-3`) between items.
