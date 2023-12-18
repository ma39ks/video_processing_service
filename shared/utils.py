import subprocess
import os

def process_video(input_file):
    command = ["ffmpeg", "-y", "-i", input_file, "-f", "null", "-"]
    subprocess.run(command)

def find_video_file(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith((".mp4", ".avi", ".mkv", ".mov")):
                return os.path.join(root, file)
    return None
