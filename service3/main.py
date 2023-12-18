import os
import shutil
from torrentool.api import Torrent
from shared.utils import process_video, find_video_file

def download_torrent(torrent_file_path, output_path):
    with Torrent.from_file_path(torrent_file_path) as torrent:
        for file in torrent.files:
            file.download(path=output_path)

def process_torrent_video(torrent_file_path):
    temp_folder = "/app/temp_torrent_download"
    os.makedirs(temp_folder, exist_ok=True)
    download_torrent(torrent_file_path, temp_folder)
    video_file_path = find_video_file(temp_folder)
    if video_file_path:
        process_video(video_file_path)
    else:
        print("Не удалось найти видеофайл в торренте.")

    shutil.rmtree(temp_folder)

if __name__ == "__main__":
    torrent_file_path = "/app/Сцена в раундхейском саду (Первый фильм в истории!) Roundhay Garden Scene (Louis Aime Augustin Le Prince) [1888, Немое кино] [rutracker-626766].torrent"
    process_torrent_video(torrent_file_path)
