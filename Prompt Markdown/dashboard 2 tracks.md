# 🎨 Vanso Creator Studio - Single Track Analytics UI Prompt

---

## 📌 Component Structure: Single Track Analytics (单曲数据详情)

### 1. Header (Track Info)
- **Layout:** Flex row, vertically centered.
- **Cover Art:** A small square image (e.g., 64x64px) with rounded corners.
- **Text Info:** 
  - **Song Title:** Large, bold font (`text-xl font-bold text-white`).
  - **Subtitle:** "上传时间: 2026-03-01" (Upload Date, `text-sm text-[#A1A1AA]`).
- **Action:** A close "X" icon on the top right of the drawer.

### 2. Hero Metrics (核心战绩)
- **Layout:** A prominent, full-width card immediately below the header.
- **Content:** 
  - Label: "累计播放次数" (Total Plays). Centered or left-aligned, muted text.
  - Value: A massive, bold number (e.g., "12,540"). Use pure white.

### 3. Content Quality Diagnosis (内容质量诊断)
- **Layout:** A clean card containing a chart. (Note: Although initially planned as a 2-column grid, since there is only one metric here, center it nicely within the card).
- **Metric: "完播率" (Completion Rate).**
  - **Chart Type:** A **Circular Progress Bar (Gauge Chart / 环形进度条)**.
  - **Visuals:** The ring should be partially filled (e.g., 42%) using a bright Cyan color (`#38E4D7`). The track background of the ring should be dark gray (`bg-white/10`).
  - **Center Text:** Display the percentage "42%" in a large font exactly in the middle of the circle.

### 4. Interaction Details (互动明细)
- **Layout:** A section at the bottom. Title: "互动明细" (text-sm, muted). Below the title, create a horizontal flex-row (or a 3-column grid) of small stat blocks.
- **Blocks (Clean numeric display):**
  - Block 1: Icon 👍 + Label "点赞数" (Likes) + Value "320".
  - Block 2: Icon ⭐ + Label "收藏数" (Saves) + Value "150".
  - Block 3: Icon 💬 + Label "评论数" (Comments) + Value "24".

---

## 🛡️ Edge Cases & UI States (Crucial for Logic)
*(Please ensure the UI code can handle these states gracefully without breaking)*

1. **Pending/Computing State (数据延迟/计算中):**
   - If the track was just uploaded, complex metrics aren't ready.
   - **UI Behavior:** Instead of showing "0%", the Circular Progress Bar should be entirely gray. The center text should read "-" or "计算中" (Computing).

2. **Zero Plays State (播放量为 0 的新歌):**
   - If "Total Plays" == 0, Completion Rate calculations will fail (divide by zero).
   - **UI Behavior:** The Content Quality card should display a grayed-out empty state with a text overlay: "暂无足够播放数据" (Not enough play data yet). Do not show a 0% chart, as it creates a negative psychological impact.