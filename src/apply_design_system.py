import os
import re

REPLACEMENTS = {
    # Typography
    r'text-\[#a1a1aa\]': 'text-zinc-400',
    r'text-\[#71717a\]': 'text-zinc-500',
    r'text-\[#FFFFFF\]': 'text-white',
    r'bg-\[#000000\]': 'bg-black',
    r'#0A0A0B': 'vanso-card',
    
    # Glassmorphism
    r'bg-\[rgba\(255,255,255,0\.05\)\]': 'bg-white/5',
    r'bg-\[rgba\(255,255,255,0\.02\)\]': 'bg-white/5',
    r'bg-\[rgba\(255,255,255,0\.1\)\]': 'bg-white/10',
    r'border-\[rgba\(255,255,255,0\.1\)\]': 'border-white/10',
    
    # Backdrop
    r'backdrop-blur-\[12px\]': 'backdrop-blur-xl',
    r'backdrop-blur-\[6px\]': 'backdrop-blur-lg',
    r'backdrop-blur-\[2px\]': 'backdrop-blur-md',

    # Hover animations (UI-UX pro max)
    r'duration-150': 'duration-300',
    r'duration-200': 'duration-300',
    
    # Remove scale transforms on hover to prevent layout shift (unless specific)
    r'hover:-translate-y-2': 'hover:-translate-y-1',
}

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    new_content = content
    for old, new in REPLACEMENTS.items():
        new_content = re.sub(old, new, new_content)
    
    if content != new_content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")

def process_dir(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.vue'):
                process_file(os.path.join(root, file))

if __name__ == '__main__':
    process_dir('components')
    process_dir('views')
    process_file('App.vue')
