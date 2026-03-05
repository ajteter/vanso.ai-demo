import os
import re

REPLACEMENTS = {
    # 1. Hex to Theme Tokens (vanso colors)
    r'text-\[#F5328A\]|text-\[#f5328a\]': 'text-vanso-magenta',
    r'text-\[#54E3D5\]|text-\[#54e3d5\]': 'text-vanso-cyan',
    r'text-\[#ECA08B\]|text-\[#eca08b\]': 'text-vanso-peach',
    r'text-\[#eb493d\]|text-\[#EB493D\]': 'text-red-500',
    
    r'bg-\[#F5328A\]|bg-\[#f5328a\]': 'bg-vanso-magenta',
    r'bg-\[#54E3D5\]|bg-\[#54e3d5\]': 'bg-vanso-cyan',
    r'bg-\[#ECA08B\]|bg-\[#eca08b\]': 'bg-vanso-peach',
    r'bg-\[#eb493d\]|bg-\[#EB493D\]': 'bg-red-500',
    
    r'from-\[#F5328A\]|from-\[#f5328a\]': 'from-vanso-magenta',
    r'from-\[#54E3D5\]|from-\[#54e3d5\]': 'from-vanso-cyan',
    r'from-\[#ECA08B\]|from-\[#eca08b\]': 'from-vanso-peach',
    
    r'via-\[#F5328A\]|via-\[#f5328a\]': 'via-vanso-magenta',
    r'via-\[#54E3D5\]|via-\[#54e3d5\]': 'via-vanso-cyan',
    r'via-\[#ECA08B\]|via-\[#eca08b\]': 'via-vanso-peach',
    
    r'to-\[#F5328A\]|to-\[#f5328a\]': 'to-vanso-magenta',
    r'to-\[#54E3D5\]|to-\[#54e3d5\]': 'to-vanso-cyan',
    r'to-\[#ECA08B\]|to-\[#eca08b\]': 'to-vanso-peach',
    
    r'border-\[#F5328A\]|border-\[#f5328a\]': 'border-vanso-magenta',
    r'border-\[#54E3D5\]|border-\[#54e3d5\]': 'border-vanso-cyan',
    r'border-\[#ECA08B\]|border-\[#eca08b\]': 'border-vanso-peach',
    r'border-\[#eb493d\]|border-\[#EB493D\]': 'border-red-500',
    
    # Shadows
    r'shadow-\[0_0_20px_rgba\(245,50,138,0\.3\)\]|shadow-\[0px_0px_20px_0px_rgba\(245,50,138,0\.3\)\]': 'shadow-[0_0_20px] shadow-vanso-magenta/30',
    r'shadow-\[0_0_30px_rgba\(245,50,138,0\.5\)\]|shadow-\[0_0_35px_rgba\(84,227,213,0\.6\)\]': 'shadow-[0_0_30px] shadow-vanso-magenta/50',
    r'shadow-\[0_0_25px_0px_rgba\(245,50,138,0\.4\)\]|shadow-\[0px_0px_25px_0px_rgba\(245,50,138,0\.4\)\]': 'shadow-[0_0_25px] shadow-vanso-magenta/40',
    r'shadow-\[0_0_15px_rgba\(235,73,61,0\.3\)\]': 'shadow-[0_0_15px] shadow-red-500/30',
    r'shadow-\[0px_0px_15px_0px_rgba\(84,227,213,0\.5\)\]|shadow-\[0_0_15px_0px_rgba\(84,227,213,0\.5\)\]': 'shadow-[0_0_15px] shadow-vanso-cyan/50',
    r'shadow-\[0px_0px_25px_0px_rgba\(245,50,138,0\.4\)\]': 'shadow-[0_0_25px] shadow-vanso-magenta/40',

    # 2. Zinc and Gray Replacements (Clean up system colors)
    r'text-\[#a1a1aa\]|text-\[#A1A1AA\]': 'text-zinc-400',
    r'text-\[#71717A\]|text-\[#71717a\]': 'text-zinc-500',
    r'text-\[#52525b\]|text-\[#52525B\]': 'text-zinc-600',
    r'text-\[#1f1f1f\]|text-\[#1F1F1F\]': 'text-zinc-950',
    
    r'bg-\[#1a1a1a\]|bg-\[#1A1A1A\]|bg-\[#111111\]|bg-\[#0e0e0e\]|bg-\[#0E0E0E\]|bg-\[#050505\]': 'bg-zinc-950',
    
    r'hover:bg-\[#d43b2f\]': 'hover:bg-red-600',
    r'text-\[#fdba74\]': 'text-orange-300',

    # 3. Typography & Arbitrary Spacing
    r'text-\[12px\] leading-\[16px\]': 'text-xs',
    r'text-\[14px\] leading-\[20px\]': 'text-sm',
    r'text-\[16px\] leading-\[24px\]': 'text-base',
    r'text-\[18px\] leading-\[28px\]': 'text-lg',
    
    r'text-\[12px\]': 'text-xs',
    r'text-\[14px\]': 'text-sm',
    r'text-\[16px\]': 'text-base',
    r'text-\[18px\]': 'text-lg',
    
    # Flex Gap
    r'gap-\[4px\]': 'gap-1',
    r'gap-\[6px\]': 'gap-1.5',
    r'gap-\[8px\]': 'gap-2',
    r'gap-\[10px\]': 'gap-2.5',
    r'gap-\[12px\]': 'gap-3',
    r'gap-\[16px\]': 'gap-4',
    r'gap-\[20px\]': 'gap-5',
    r'gap-\[24px\]': 'gap-6',
    r'gap-\[32px\]': 'gap-8',
    
    # Margin
    r'mb-\[4px\]': 'mb-1', r'mt-\[4px\]': 'mt-1', r'ml-\[4px\]': 'ml-1', r'mr-\[4px\]': 'mr-1',
    r'mb-\[8px\]': 'mb-2', r'mt-\[8px\]': 'mt-2', r'ml-\[8px\]': 'ml-2', r'mr-\[8px\]': 'mr-2',
    r'mb-\[12px\]': 'mb-3', r'mt-\[12px\]': 'mt-3', r'ml-\[12px\]': 'ml-3', r'mr-\[12px\]': 'mr-3',
    r'mb-\[16px\]': 'mb-4', r'mt-\[16px\]': 'mt-4', r'ml-\[16px\]': 'ml-4', r'mr-\[16px\]': 'mr-4',
    r'mb-\[20px\]': 'mb-5', r'mt-\[20px\]': 'mt-5', r'ml-\[20px\]': 'ml-5', r'mr-\[20px\]': 'mr-5',
    r'mb-\[24px\]': 'mb-6', r'mt-\[24px\]': 'mt-6', r'ml-\[24px\]': 'ml-6', r'mr-\[24px\]': 'mr-6',
    r'mb-\[32px\]': 'mb-8', r'mt-\[32px\]': 'mt-8', r'ml-\[32px\]': 'ml-8', r'mr-\[32px\]': 'mr-8',

    # Padding
    r'p-\[4px\]': 'p-1', r'px-\[4px\]': 'px-1', r'py-\[4px\]': 'py-1',
    r'p-\[8px\]': 'p-2', r'px-\[8px\]': 'px-2', r'py-\[8px\]': 'py-2',
    r'p-\[12px\]': 'p-3', r'px-\[12px\]': 'px-3', r'py-\[12px\]': 'py-3',
    r'p-\[16px\]': 'p-4', r'px-\[16px\]': 'px-4', r'py-\[16px\]': 'py-4',
    r'p-\[20px\]': 'p-5', r'px-\[20px\]': 'px-5', r'py-\[20px\]': 'py-5',
    r'p-\[24px\]': 'p-6', r'px-\[24px\]': 'px-6', r'py-\[24px\]': 'py-6',
    r'p-\[32px\]': 'p-8', r'px-\[32px\]': 'px-8', r'py-\[32px\]': 'py-8',
    r'p-\[40px\]': 'p-10', r'px-\[40px\]': 'px-10', r'py-\[40px\]': 'py-10',
    
    # Rounding
    r'rounded-\[8px\]': 'rounded-lg',
    r'rounded-\[12px\]': 'rounded-xl',
    r'rounded-\[16px\]': 'rounded-2xl',
    r'rounded-\[24px\]': 'rounded-3xl',
}

# Regex for w-[Xpx], h-[Xpx], size-[Xpx] where X is divisible by 4 (to rem scale)
def sizing_replacer(match):
    prop = match.group(1) # w, h, or size
    val = int(match.group(2))
    if val % 4 == 0:
        return f"{prop}-{val//4}"
    return match.group(0)

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    new_content = content
    # Process dictionary replacements
    for old, new in REPLACEMENTS.items():
        new_content = re.sub(old, new, new_content)
    
    # Process dynamically sizing
    new_content = re.sub(r'(w|h|size)-\[([0-9]+)px\]', sizing_replacer, new_content)
    
    if content != new_content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")

def process_dir(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.vue') or file.endswith('.html'):
                process_file(os.path.join(root, file))

if __name__ == '__main__':
    process_dir('src/components')
    process_dir('src/views')
    process_dir('src/v1_components')
    process_dir('src/v1_views')
    process_file('src/App.vue')
    
    # Process the HTML previews
    if os.path.exists('design_system/design_system_preview.html'):
        process_file('design_system/design_system_preview.html')
