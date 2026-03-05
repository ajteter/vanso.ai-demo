import os
import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace '../components/' with '../v1_components/'
    new_content = content.replace('../components/', '../v1_components/')

    # In case there are './components/' in some files
    new_content = new_content.replace('./components/', './v1_components/')
    
    # Also replace router imports if needed (router might not be an issue)
    
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
    process_dir('v1_views')
    process_dir('v1_components')
