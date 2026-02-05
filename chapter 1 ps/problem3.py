import os

directory_path = '/New folder'

# List only files
files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

print(f"Files in directory '{directory_path}':")
for file in files:
    print(file)
