import os
from pytubefix import YouTube
import moviepy.editor as mp
import pandas as pd

def download_video(url, output_directory, video_title):
    yt = YouTube(url)
    ys = yt.streams.filter(only_audio=False).first()
    video_output_path = os.path.join(output_directory, video_title+".mp4")
    ys.download(output_path=output_directory, filename=video_title+".mp4")
    return video_output_path

def video_to_mp3(video_path, mp3_path):
    audio_clip = mp.AudioFileClip(video_path)
    audio_clip.write_audiofile(mp3_path)

def process_video(video_title :str, video_url :str):
    output_directory = "downloads"
    videos_output_directory = os.path.join(output_directory, "videos")
    audios_output_directory = os.path.join(output_directory, "audios")
    os.makedirs(output_directory, exist_ok=True)
    os.makedirs(videos_output_directory, exist_ok=True)
    os.makedirs(audios_output_directory, exist_ok=True)
    video_output_path = download_video(video_url, videos_output_directory, video_title)
    mp3_output_path = os.path.join(audios_output_directory, video_title+".mp3")
    video_to_mp3(video_output_path, mp3_output_path)
    print(f"Video downloaded and converted to MP3: {mp3_output_path}")


if __name__ == "__main__":
    urls_file_path = "urls.xlsx"
    videos_data = pd.read_excel('urls.xlsx', index_col=0).loc[:, ["Video url"]]
    for index, serie in videos_data.iterrows():
        video_title = r"{}".format(index).replace("/", " ")
        video_url = serie.values[0]
        print("video_title : ", video_title)
        print("video_url : ", video_url)
        process_video(video_title, video_url)
        
    
    """
    youtube_url = "https://www.youtube.com/watch?v=vaSRCBj64vk"
    output_directory = "downloads"
    os.makedirs(output_directory, exist_ok=True)
    video_output_path = download_video(youtube_url, output_directory)
    mp3_output_path = os.path.join(output_directory, "audio.mp3")
    video_to_mp3(video_output_path, mp3_output_path)
    print(f"Video downloaded and converted to MP3: {mp3_output_path}")
    """