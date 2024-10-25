import os
import shutil

# Define the source and destination folders
source_dir = r"G:\real data"
destination_dir = r"G:\New folder\ddeep Fake AI\new_videos"

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Define the video file extensions you want to look for
video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']

# Walk through the source directory and its subdirectories
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # Check if the file has a video extension
        if any(file.lower().endswith(ext) for ext in video_extensions):
            # Construct full file path
            file_path = os.path.join(root, file)
            # Copy the file to the destination directory
            shutil.copy(file_path, destination_dir)
            print(f"Copied: {file_path}")

print("Video files have been copied to the destination folder.")

# this particular code is used to get the video file from dataset

    
# import torch
# print(torch.cuda.is_available())
