# 📋 Prompt 1: H5 Account Overview (账号总览)

## 📌 Context & Vibe
Create a mobile-first "Account Overview" dashboard for an AI music platform. 
**Design System**: "Sonic Aura" (Pure Black `#000000` background, Glassmorphism, and vibrant fluid gradients).
**Target**: Mobile H5 / App WebView.

---

## 🎨 Design Tokens (Foundation)
- **Background**: `#000000`
- **Surface**: Card background `#0A0A0B` with `border: rgba(255,255,255,0.08)`.
- **Main Accent Gradient**: `linear-gradient(134deg, #F5328A 19.26%, #ECA08B 57.57%, #54E3D5 91.14%)`.
- **Accents**: Cyan `#54E3D5`, Magenta `#F5328A`, Peach `#ECA08B`.
- **Typography**: Inter (White for primary, Zinc-500 for secondary).
- **Mobile UX**: 44px touch targets. Items should have `active:scale(0.97)` feedback.

---

## 🏗️ Layout Structure

### 1. Navigation Tabs
- Simple text buttons at the top: "账号总览" and "单曲数据".
- **Active State**: Font color `#FFFFFF`, bold, plus a 2px bottom indicator line using the **Main Accent Gradient**.
- **Inactive State**: Color `#71717A`.

### 2. Global Time Filter
- A rounded pill-shaped container with `bg-white/5` background.
- Options: "近 7 日" (Active) and "近 30 日".
- Active option has a subtle `bg-white/10` background and white text.

### 3. Metric Cards (2x2 Grid)
- **Grid**: Use `grid-cols-2`.
- **Items**: 
  - [1] 播放总数 (12,450)
  - [2] 互动总量 (843)
  - [3] 新增粉丝 (120)
  - [4] 主页访问 (3,200)
- **Card UI**: 16px padding, rounded-2xl.
- **Selection State**: Clicking a card makes it "active". The active card shows a top border line using the **Main Accent Gradient** and a subtle `bg-white/3`.

### 4. Trend Chart Area
- Title: "播放总数" (Dynamic based on selected card).
- **Chart**: A smooth SVG Area Chart.
- **Visuals**: Line color should match its metric (default Cyan `#54E3D5`). Area fill is a vertical gradient from the metric color to transparent.
- **Details**: Dashed horizontal grid lines only. 
- **Tooltip**: A floating glass-morphic box showing data for the latest point (e.g., "03-06: 3,200"). Add a glowing dot at the data point.

### 5. Interaction Breakdown (Donut)
- Large card titled "互动构成".
- **Chart**: A donut ring showing:
  - 点赞 (Likes): 60% (Magenta)
  - 收藏 (Saves): 30% (Peach)
  - 评论 (Comments): 10% (Cyan)
- **Legend**: Neatly aligned list to the right with colored circular bullet points.
