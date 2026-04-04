import os
import shutil

# Change this path if needed
source_folder = os.path.expanduser("~/Documents")

file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Archives": [".zip", ".rar"]
}

print(f"Organizing files in {source_folder}...\n")

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.endswith(tuple(extensions)):
                folder_path = os.path.join(source_folder, folder)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"Moved: {file} → {folder}")
