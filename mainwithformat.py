import os
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from pytube.cli import on_progress
from pytube.exceptions import RegexMatchError
from database import create_database, insert_video_metadata, insert_audio_metadata
from view_downloads import display_sections
from moviepy.editor import VideoFileClip

def download_video(video_url, video_format='mp4'):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()

    # Check if stream is available
    if not stream:
        print("No streams found for the video.")
        return

    video_file_path = stream.download(output_path="video_downloads")
    print(f"Downloaded video: {stream.title}")

    # Check if format needs conversion
    if stream.includes_audio_track and stream.mime_type != f'video/{video_format}':
        converted_video_path = video_file_path.replace(".mp4", f"_{video_format}.{video_format}")
        video_clip = VideoFileClip(video_file_path)

        # Specify codec and parameters
        codec = "libx264"  # Example codec
        parameters = ['-preset', 'fast', '-crf', '23']  # Example parameters

        video_clip.write_videofile(converted_video_path, codec=codec, ffmpeg_params=parameters)
        video_clip.close()
        os.remove(video_file_path)
        print(f"Converted video to {video_format.upper()}: {converted_video_path}")
    else:
        converted_video_path = video_file_path

    # Insert video metadata into the database 
    video_metadata = (video_url, stream.title, yt.author, yt.length, stream.resolution, video_format)
    insert_video_metadata("link2playback.db", video_metadata)
    print("Video metadata saved to the database.")

def download_audio(video_url, audio_format='mp3', quality='high'):
    yt = YouTube(video_url, on_progress_callback=on_progress)

    if quality == 'high':
        stream = yt.streams.filter(only_audio=True, abr='128kbps').first()
        quality_tag = 'HQ'
    elif quality == 'low':
        stream = yt.streams.filter(only_audio=True).first()
        quality_tag = 'LQ'
    else:
        print("Invalid audio quality choice. Downloading in high quality.")
        stream = yt.streams.filter(only_audio=True, abr='128kbps').first()
        quality_tag = 'HQ'

    audio_file = stream.download(output_path="audio_downloads")
    filename, extension = os.path.splitext(audio_file)
    renamed_audio_file = f"{filename}_{quality_tag}.{audio_format}"
    os.rename(audio_file, renamed_audio_file)

    print(f"Downloaded and converted audio to {quality_tag} {audio_format.upper()}: {renamed_audio_file}")
        
    # Insert audio metadata into the database including format
    audio_metadata = (video_url, yt.title, yt.author, yt.length, quality, audio_format, stream.abr)
    insert_audio_metadata("link2playback.db", audio_metadata)
    print("Audio metadata saved to the database.")


def main():
    create_database("link2playback.db")

    while True:
        video_url = input("Enter the YouTube video URL: ")
        
        try:
            YouTube(video_url)
        except RegexMatchError:
            print("Invalid YouTube video URL. Please enter a valid URL.")
            continue

        choice = input("Download as Audio or Video (A/V)?: ").lower()
        
        if choice == 'a':
            audio_format = input("Select audio format (MP3/MP4/WAV/OGG): ").lower()
            quality = input("Select audio quality (High/Low): ").lower()
            download_audio(video_url, audio_format, quality)
        elif choice == 'v':
            video_format = input("Select video format (MP4/MOV/AVI/WMV/WEBM/FLV): ").lower()
            download_video(video_url, video_format)
        else:
            print("Invalid choice. Please enter 'A' for audio or 'V' for video.")
        
        another_download = input("Do you want to download another file? (yes/no): ").lower()
        if another_download != 'yes':
            break

if __name__ == "__main__":
    main()
