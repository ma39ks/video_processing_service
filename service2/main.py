from pytube import YouTube
from shared.utils import process_video, find_video_file

def download_youtube_video(video_url, output_path):
    yt = YouTube(video_url)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path)

def process_youtube_video(video_url):
    download_youtube_video(video_url, "/app/tmp")
    process_video(find_video_file("/app/tmp"))

if __name__ == "__main__":
    youtube_video_url = "https://www.youtube.com/watch?v=_hdvA9dj4Jo"
    process_youtube_video(youtube_video_url)
