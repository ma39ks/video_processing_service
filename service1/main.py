from shared.utils import process_video

def process_local_video(file_path):
    process_video(file_path)

if __name__ == "__main__":
    video_file_path = "/app/local_video.mp4"
    process_local_video(video_file_path)
