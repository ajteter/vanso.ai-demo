# Trending Hashtags - Style Optimization Guide (v4 - Internal Structure Fix)

## 1. Rationale (设计重构思路)

### 1.1 Balanced Vibrant Neon Accents (平衡版霓虹点缀方案)
The 9 initial pastel colors have been translated to "Vibrant Neon" variants. They provide a lively, energetic pop against the dark mode background without being overly washed out or too dim.

**Vibrant Neon Palette Mapping**:
| Original Pastel | Vibrant Neon Equivalent | Hex Code |
| :--- | :--- | :--- |
| `#F6E4C4` | Neon Amber | `#FBBF24` |
| `#F0D9DA` | Neon Rose | `#FB7185` |
| `#D1E4D1` | Neon Green | `#4ADE80` |
| `#F3FBF1` | Neon Mint | `#6EE7B7` |
| `#C8D9EB` | Neon Blue | `#60A5FA` |
| `#B7B9F4` | Neon Violet | `#A78BFA` |
| `#FEC8D8` | Neon Pink | `#F472B6` |
| `#FFFFC3` | Neon Yellow | `#FDE047` |
| `#D2F6FC` | Neon Cyan | `#22D3EE` |

### 1.2 Layout Alignment inside Hashtag Element (内部间距与播放图标适配)
Per your latest structural rule:
- `padding: 6px 8px; border-radius: 4px;`
- Crucially, `gap: 10px;` is meant to position the right-side Play Button away from the hashtag text block. 
- The `#` prefix and the tag body text now have a minimalist tight gap (e.g. `4px` or `2px`).

---

## 2. Implementation Code (各端实现代码)

### 2.1 Web (Vue 3 + Tailwind CSS)

```vue
<template>
  <button 
    class="flex items-center justify-between gap-[10px] px-[8px] py-[6px] rounded backdrop-blur-md border border-white/5 hover:brightness-125 active:scale-95 transition-all duration-300 cursor-pointer shrink-0 group"
    :style="{ background: `linear-gradient(90deg, ${accentColor}26 0%, rgba(255,255,255,0.02) 100%)` }"
    @click="$emit('click', text)"
  >
    <!-- Left Section: Icon & Text -->
    <div class="flex items-center gap-[4px]">
      <span 
        class="font-bold text-sm transition-transform group-hover:scale-105" 
        :style="{ color: accentColor, textShadow: `0 0 8px ${accentColor}80` }"
      >#</span>
      <span class="text-sm font-medium text-white italic">{{ text }}</span>
    </div>

    <!-- Right Section: Play Button -->
    <svg class="w-3.5 h-3.5 text-zinc-400 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24">
       <path d="M8 5v14l11-7z" />
    </svg>
  </button>
</template>

<script setup>
defineProps({
  text: String,
  accentColor: String // Hex color from Vibrant Neon Palette
});
defineEmits(['click']);
</script>
```

### 2.2 Android (Jetpack Compose)

```kotlin
import androidx.compose.animation.animateColorAsState
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.interaction.collectIsPressedAsState
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material3.Icon
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

val VibrantNeonPalette = listOf(
    Color(0xFFFBBF24), Color(0xFFFB7185), Color(0xFF4ADE80),
    Color(0xFF6EE7B7), Color(0xFF60A5FA), Color(0xFFA78BFA),
    Color(0xFFF472B6), Color(0xFFFDE047), Color(0xFF22D3EE)
)

@Composable
fun HashtagChip(
    text: String,
    accentColor: Color = VibrantNeonPalette.random(),
    onClick: () -> Unit
) {
    val interactionSource = remember { MutableInteractionSource() }
    val isPressed by interactionSource.collectIsPressedAsState()
    
    val baseColor = if (isPressed) Color.White else accentColor
    val iconColor by animateColorAsState(if (isPressed) Color.White else Color(0xFFA1A1AA))

    Surface(
        color = Color.Transparent,
        shape = RoundedCornerShape(4.dp),
        border = BorderStroke(1.dp, Color.White.copy(0.04f)),
        modifier = Modifier
            .background(
                Brush.horizontalGradient(
                    colors = listOf(baseColor.copy(alpha = 0.15f), Color.White.copy(alpha = 0.02f))
                ),
                shape = RoundedCornerShape(4.dp)
            )
            .clickable(interactionSource, indication = null, onClick = onClick)
    ) {
        Row(
            modifier = Modifier.padding(horizontal = 8.dp, vertical = 6.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(10.dp)
        ) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(text = "#", color = accentColor, fontWeight = FontWeight.Bold, fontSize = 14.sp)
                Spacer(modifier = Modifier.width(4.dp))
                Text(
                    text = text,
                    color = Color.White,
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Medium,
                    fontStyle = FontStyle.Italic
                )
            }
            Icon(
                imageVector = Icons.Filled.PlayArrow,
                contentDescription = "Play",
                tint = iconColor,
                modifier = Modifier.size(12.dp)
            )
        }
    }
}
```

### 2.3 iOS (SwiftUI)

```swift
import SwiftUI

struct HashtagChip: View {
    let text: String
    let accentHex: String
    let action: () -> Void
    
    @State private var isHovered = false
    
    var body: some View {
        Button(action: action) {
            var parsedColor = Color.white
            if accentHex.hasPrefix("#") {
                parsedColor = Color(hex: accentHex)
            }

            return HStack(spacing: 10) {
                HStack(spacing: 4) {
                    Text("#")
                        .font(.system(size: 14, weight: .bold))
                        .foregroundColor(parsedColor)
                        .shadow(color: parsedColor.opacity(0.5), radius: 4, x: 0, y: 0)
                    
                    Text(text)
                        .font(.system(size: 14, weight: .medium))
                        .foregroundColor(.white)
                        .italic()
                }

                Image(systemName: "play.fill")
                    .resizable()
                    .frame(width: 10, height: 10)
                    .foregroundColor(isHovered ? .white : Color(white: 0.63))
            }
            .padding(.horizontal, 8)
            .padding(.vertical, 6)    
            .background(
                RoundedRectangle(cornerRadius: 4)
                    .fill(LinearGradient(
                        gradient: Gradient(colors: [parsedColor.opacity(0.15), Color.white.opacity(0.02)]),
                        startPoint: .leading,
                        endPoint: .trailing
                    ))
            )
            .background(
                RoundedRectangle(cornerRadius: 4) 
                    .stroke(Color.white.opacity(isHovered ? 0.08 : 0.04), lineWidth: 1)
            )
        }
        .buttonStyle(PlainButtonStyle())
        .onHover { hovering in
            withAnimation(.easeInOut(duration: 0.2)) {
                isHovered = hovering
            }
        }
    }
}
```
