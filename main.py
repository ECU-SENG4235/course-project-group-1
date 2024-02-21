import os
from pytube import YouTube
from pytube.cli import on_progress

import os

def download_video(video_url):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path="video_downloads")
    print(f"Downloaded video: {stream.title}")

def download_audio(video_url, quality='high'):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    if quality == 'high':
        stream = yt.streams.filter(only_audio=True).first()
        quality_tag = 'high_q'
    elif quality == 'low':
        stream = yt.streams.filter(only_audio=True, abr='128kbps').first()
        quality_tag = 'low_q'
    else:
        print("Invalid audio quality choice. Downloading in high quality.")
        stream = yt.streams.filter(only_audio=True).first()
        quality_tag = 'high_q'

    audio_file = stream.download(output_path="audio_downloads")
    audio_file_mp3 = audio_file.replace(".mp4", f"_{quality_tag}.mp3")

    # Check if the destination file already exists
    if os.path.exists(audio_file_mp3):
        print(f"MP3 file already exists: {audio_file_mp3}")
    else:
        os.rename(audio_file, audio_file_mp3)
        print(f"Downloaded and converted audio to MP3: {audio_file_mp3}")

def main():
    # Prompt user for YouTube video URL
    video_url = input("Enter the YouTube video URL: ")
    
    # Prompt user to choose between audio and video download
    choice = input("Download as Audio or Video (A/V)?: ").lower()
    
    if choice == 'a':  # If user chooses to download audio
        # Prompt user to select audio quality
        quality = input("Select audio quality (High/Low): ").lower()
        # Call download_audio function with specified quality
        download_audio(video_url, quality)
    elif choice == 'v':  # If user chooses to download video
        # Call download_video function
        download_video(video_url)
    else:
        print("Invalid choice. Please enter 'A' for audio or 'V' for video.")

# Entry point of the program
if __name__ == "__main__":
    main()
