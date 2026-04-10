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

### 2.2 Android (Traditional XML)

因为项目使用的是传统 XML 系统，我们要动态绑定背景渐变色，同时赋予 `#` 号光晕阴影效果。

**1. `item_hashtag.xml` (视图布局)**
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/chipContainer"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:orientation="horizontal"
    android:gravity="center_vertical"
    android:paddingStart="8dp"
    android:paddingEnd="8dp"
    android:paddingTop="6dp"
    android:paddingBottom="6dp"
    android:clickable="true"
    android:focusable="true">

    <LinearLayout
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:gravity="center_vertical">

        <!-- 霓虹灯起辉符号 -->
        <TextView
            android:id="@+id/tvHash"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="#"
            android:textStyle="bold"
            android:textSize="14sp"
            android:shadowRadius="8"
            android:shadowColor="#000000"
            android:shadowDx="0"
            android:shadowDy="0" />

        <TextView
            android:id="@+id/tvHashtagText"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginStart="4dp"
            android:text="hashtag"
            android:textColor="#FFFFFF"
            android:textSize="14sp"
            android:textStyle="italic" />
    </LinearLayout>

    <ImageView
        android:id="@+id/ivPlayButton"
        android:layout_width="12dp"
        android:layout_height="12dp"
        android:layout_marginStart="10dp"
        android:src="@drawable/ic_play"
        app:tint="#A1A1AA" />
</LinearLayout>
```

**2. 动态绑定逻辑 (在 ViewHolder 中实现)**
```kotlin
import android.graphics.Color
import android.graphics.drawable.GradientDrawable
import android.util.TypedValue
import androidx.core.graphics.ColorUtils

fun bindHashtagView(view: View, text: String, accentColorString: String) {
    val chipContainer = view.findViewById<LinearLayout>(R.id.chipContainer)
    val tvHash = view.findViewById<TextView>(R.id.tvHash)
    val tvHashtagText = view.findViewById<TextView>(R.id.tvHashtagText)
    
    val accentColorInt = Color.parseColor(accentColorString)
    tvHashtagText.text = text
    tvHash.setTextColor(accentColorInt)
    
    // 设置 50% 深度的霓虹发光阴影 (Alpha: 0x80 = 128)
    val shadowColor = ColorUtils.setAlphaComponent(accentColorInt, 128)
    tvHash.setShadowLayer(8f, 0f, 0f, shadowColor)

    // 动态生成渐变背景 (左端15%霓虹色，右端2%白色)
    // 15% opacity ≈ 38, 2% opacity ≈ 5, 4% opacity ≈ 10
    val startColor = ColorUtils.setAlphaComponent(accentColorInt, 38)
    val endColor = Color.argb(5, 255, 255, 255)
    val borderStrokeColor = Color.argb(10, 255, 255, 255) 

    val dpToPx = { dp: Float -> TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, dp, view.resources.displayMetrics) }
    
    val bgDrawable = GradientDrawable(
        GradientDrawable.Orientation.LEFT_RIGHT,
        intArrayOf(startColor, endColor)
    ).apply {
        cornerRadius = dpToPx(4f)
        setStroke(dpToPx(1f).toInt(), borderStrokeColor)
    }

    chipContainer.background = bgDrawable

    // (可选附加) 监听按下状态的亮度变化或使用 StateListDrawable 切换样式
}
```

### 2.3 iOS (UIKit)

```swift
import UIKit

class HashtagChipControl: UIControl {
    
    private let textLabel = UILabel()
    private let hashLabel = UILabel()
    private let playIconView = UIImageView()
    private let gradientLayer = CAGradientLayer()
    
    var accentColor: UIColor = .cyan {
        didSet {
            updateColors()
        }
    }
    
    var text: String = "" {
        didSet {
            textLabel.text = text
        }
    }
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        setupUI()
    }
    
    override func layoutSubviews() {
        super.layoutSubviews()
        // Ensure gradient layer matches dynamic bounds
        gradientLayer.frame = bounds
        gradientLayer.cornerRadius = 4
    }
    
    override var isHighlighted: Bool {
        didSet {
            UIView.animate(withDuration: 0.2) {
                // Dim on press and brighten icon
                self.alpha = self.isHighlighted ? 0.8 : 1.0
                self.playIconView.tintColor = self.isHighlighted ? .white : UIColor(white: 0.63, alpha: 1.0)
            }
        }
    }
    
    private func setupUI() {
        layer.cornerRadius = 4
        layer.borderWidth = 1
        layer.borderColor = UIColor(white: 1.0, alpha: 0.04).cgColor
        
        // Setup Gradient
        gradientLayer.startPoint = CGPoint(x: 0, y: 0.5)
        gradientLayer.endPoint = CGPoint(x: 1, y: 0.5)
        layer.insertSublayer(gradientLayer, at: 0)
        
        // Hashtag Symbol
        hashLabel.text = "#"
        hashLabel.font = .systemFont(ofSize: 14, weight: .bold)
        
        // Texts
        textLabel.font = .italicSystemFont(ofSize: 14)
        textLabel.textColor = .white
        
        let textStack = UIStackView(arrangedSubviews: [hashLabel, textLabel])
        textStack.axis = .horizontal
        textStack.spacing = 4
        textStack.alignment = .center
        
        // Play Icon
        playIconView.image = UIImage(systemName: "play.fill")
        playIconView.tintColor = UIColor(white: 0.63, alpha: 1.0)
        playIconView.contentMode = .scaleAspectFit
        playIconView.translatesAutoresizingMaskIntoConstraints = false
        playIconView.widthAnchor.constraint(equalToConstant: 10).isActive = true
        playIconView.heightAnchor.constraint(equalToConstant: 10).isActive = true
        
        // Main Container Stack
        let mainStack = UIStackView(arrangedSubviews: [textStack, playIconView])
        mainStack.axis = .horizontal
        mainStack.spacing = 10
        mainStack.alignment = .center
        mainStack.isUserInteractionEnabled = false // Allow parent UIControl to handle taps
        
        addSubview(mainStack)
        mainStack.translatesAutoresizingMaskIntoConstraints = false
        
        // Layout Config (padding: 6px 8px)
        NSLayoutConstraint.activate([
            mainStack.leadingAnchor.constraint(equalTo: leadingAnchor, constant: 8),
            mainStack.trailingAnchor.constraint(equalTo: trailingAnchor, constant: -8),
            mainStack.topAnchor.constraint(equalTo: topAnchor, constant: 6),
            mainStack.bottomAnchor.constraint(equalTo: bottomAnchor, constant: -6)
        ])
        
        updateColors()
    }
    
    private func updateColors() {
        hashLabel.textColor = accentColor
        
        // Neon Glow Shadow for # (50% opacity, 8 Radius blur)
        hashLabel.layer.shadowColor = accentColor.cgColor
        hashLabel.layer.shadowRadius = 8
        hashLabel.layer.shadowOpacity = 0.5
        hashLabel.layer.shadowOffset = .zero
        
        // Horizontal Gradient (Left: 15% opacity neon, Right: 2% opacity white)
        let startColor = accentColor.withAlphaComponent(0.15).cgColor
        let endColor = UIColor(white: 1.0, alpha: 0.02).cgColor
        gradientLayer.colors = [startColor, endColor]
    }
}
```
