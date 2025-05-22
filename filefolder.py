import os
import shutil

# source_dir = r"c:\Users\divyavani.palli\Downloads"
# destination_dirs = {
#      "Images": [".jpg", ".jpeg", ".png", ".gif"],
#     "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
#     "Music": [".mp3", ".wav"],
#     "Videos": [".mp4", ".avi", ".mkv"],
#     "Archives": [".zip", ".rar", ".tar.gz"],
#     "Executables": [".exe", ".msi"]
# }
# def organize_files():
#     for file in os.listdir(source_dir):
#         file_path = os.path.join(source_dir, file)

#         # Skip directories, only move files
#         if os.path.isfile(file_path):
#             file_ext = os.path.splitext(file)[1]  # Get file extension

#             # Find the matching folder
#             for folder, extensions in destination_dirs.items():
#                 if file_ext in extensions:
#                     destination_path = os.path.join(source_dir, folder)

#                     # Create folder if it doesn't exist
#                     if not os.path.exists(destination_path):
#                         os.makedirs(destination_path)

#                     # Move the file
#                     shutil.move(file_path, os.path.join(destination_path, file))
#                     print(f"Moved {file} to {folder}")

# if __name__ == "__main__":
#     organize_files()

source_dir = r"c:\Users\divyavani.palli\Downloads"
destination_dirs = {
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Documents": ['.pdf', ".docx", ".xlsx", ".txt"],
    "Archived" : [".zip", '.rar', "tar.gz"],
    "Executables" : [".exe", '.msi'],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".mkv"]

}


def organize_files():
    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)

        # Skip directories, only move files
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1]  # Get file extension

            # Find the matching folder
            for folder, extensions in destination_dirs.items():
                if file_ext in extensions:
                    destination_path = os.path.join(source_dir, folder)

                    # Create folder if it doesn't exist
                    if not os.path.exists(destination_path):
                        os.makedirs(destination_path)

                    # Move the file
                    shutil.move(file_path, os.path.join(destination_path, file))
                    print(f"Moved {file} to {folder}")
                        
if __name__=="__main__":
    organize_files()
                    