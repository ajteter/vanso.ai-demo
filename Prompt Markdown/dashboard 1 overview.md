# 🎨 Vanso Creator Studio - Data Center UI Prompt

---

## 📌 Page: Account Overview (账号总览)

**Layout:** A full-width dashboard container.

### 1. Header & Global Filters
- **Title:** "Data Overview" (数据总览) aligned to the left.
- **Filter Toggle:** Right-aligned segmented control pill. Options: `[ Last 7 Days ]` (Active, highlighted) and `[ Last 30 Days ]`.

### 2. The Big 4 Summary Cards (Interactive Top Row)
*Layout: A 4-column grid. These cards act as tabs to control the main chart below.*

- **Card Style (Default):** Dark gray background (`#1E1E1E`), padding, subtle border. Cursor pointer to indicate clickability.
- **Card Style (Active/Selected):** The first card should appear selected. Add a subtle blue glow or a top border accent (`border-t-2 border-[#247CFF]`), and slightly lighter background (`bg-[#262626]`).
- **Card 1 (Active):** 
  - Label: "Total Plays" (播放总数). 
  - Value: "12,450" (Massive typography). 
- **Card 2:** Label: "Total Engagements" (互动总量). Value: "843".
- **Card 3:** Label: "New Followers" (新增粉丝). Value: "120".
- **Card 4:** Label: "Profile Visits" (主页访问). Value: "3,200".

### 3. The Main Trend Chart (Center Section)
*Layout: A large, full-width card immediately below the Big 4 cards.*

- **Header:** Title reads "Total Plays Trend" (dynamically matching the selected active card above).
- **Chart Type:** A smooth **Area Chart (折线面积图)**. 
- **Visuals:** The line should be a vibrant Electric Blue. The area under the line should be a smooth vertical gradient from Electric Blue (top) fading into transparent dark gray (bottom).
- **Axes:** X-axis shows dates (e.g., Mar 01 - Mar 07). Y-axis shows numbers. Hide the vertical grid lines, keep only faint horizontal grid lines.
- **Interaction Hint:** Show a tooltip hovering over a data peak (e.g., "Mar 05: 3,200 Plays").

### 4. Bottom Analytics Dashboard
- **Engagement Breakdown (互动构成)**
  - **Chart Type:** A minimalist **Donut Chart (环形图)**.
  - **Data Slices:** 
    - 60% "Likes" (点赞) - Use Pink/Magenta color.
    - 30% "Saves" (收藏) - Use Orange color.
    - 10% "Comments" (评论) - Use Cyan color.
  - **Legend:** Place the legend neatly to the right of the donut chart, showing the color dot, label, and percentage.

---

### 💡 AI Generation Notes
- Ensure there is clear visual hierarchy. The numbers in the top cards should be the largest text on the page.
- The connection between the "Top Cards" and the "Main Trend Chart" must be visually obvious (e.g., the active card's accent color matches the chart's line color).