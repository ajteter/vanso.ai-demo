# 📋 Prompt 3: H5 Analytics Drawer (单曲数据弹窗/抽屉)

## 📌 Context & Vibe
Create a high-end mobile "Bottom Sheet" (Drawer) component for track-specific analytics.
**Animation**: Smooth slide-up from bottom (`translateY(100% -> 0)`) with a backdrop blur overlay.

---

## 🏗️ Structure & Content

### 1. Header & Controls
- **Visuals**: A rounded-t-3xl panel with a thick background blur.
- **Drag Handle**: A subtle centering pill at the very top to indicate swipability.
- **Close Button**: A circular button (44px touch target) on the top right.
- **Identity**: Track cover art placeholder (rounded-xl) + Track Title (Title Case, Bold) + Upload Date.

### 2. Main Metrics (Hero Stats)
- **Grid**: A 2-column grid.
- **Card A (Plays)**: "累计播放次数" (Bold value, e.g., 12,540). Muted background.
- **Card B (Completion)**: "完播率". 
  - **Visual**: A central SVG progress ring (Cyan color circle, 3px stroke).
  - **Value**: Percentage text centered inside the ring (e.g., 42%).
- **Empty State**: Support a "暂无数据" view for tracks with zero plays.

### 3. Interaction Grid
- **Section Label**: "互动明细" with a thin horizontal separator line.
- **Layout**: A 3-column grid of interaction cards.
- **Card Items**:
  - [1] **点赞 (Likes)**: Icon (Heart/Thumb) + Bold Number. Accent: Magenta.
  - [2] **收藏 (Saves)**: Icon (Bookmark) + Bold Number. Accent: Peach.
  - [3] **评论 (Comments)**: Icon (Message) + Bold Number. Accent: Cyan.
- **Styling**: Cards have `bg-[#111113]` and `border-vanso-border`.

---

## 📱 Interactions & Technical Requirements
- **Overlay**: Dark backdrop (`bg-black/60`) with `backdrop-blur-sm`. Clicking the backdrop closes the drawer.
- **Scrolling**: The drawer body should be independently scrollable (`overflow-y-auto`) if content exceeds height.
- **Animations**: Use `cubic-bezier(0.16, 1, 0.3, 1)` for a "native-feeling" elastic entrance.
- **Styling**: Strictly dark mode `#0A0A0B`. Ensure high contrast for numbers.
