import os
from pytube import YouTube
from pytube.cli import on_progress
from pytube.exceptions import RegexMatchError
from database import create_database, insert_video_metadata

# Function to download video
def download_video(video_url):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path="video_downloads")
    print(f"Downloaded video: {stream.title}")

    # Insert video metadata into the database
    video_metadata = (video_url, stream.title, yt.author, yt.length, stream.resolution)
    insert_video_metadata("video_metadata.db", video_metadata)
    print("Video metadata saved to the database.")

# Function to download audio
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

    if os.path.exists(audio_file_mp3):
        print(f"MP3 file already exists: {audio_file_mp3}")
    else:
        os.rename(audio_file, audio_file_mp3)
        print(f"Downloaded and converted audio to MP3: {audio_file_mp3}")

    # Insert video metadata into the database
    video_metadata = (video_url, yt.title, yt.author, yt.length, 'Audio')
    insert_video_metadata("video_metadata.db", video_metadata)
    print("Audio metadata saved to the database.")

def main():
    # Create the database if it doesn't exist
    create_database("video_metadata.db")

    while True:
        video_url = input("Enter the YouTube video URL: ")
        
        try:
            YouTube(video_url)
        except RegexMatchError:
            print("Invalid YouTube video URL. Please enter a valid URL.")
            continue

        choice = input("Download as Audio or Video (A/V)?: ").lower()
        
        if choice == 'a':
            quality = input("Select audio quality (High/Low): ").lower()
            download_audio(video_url, quality)
        elif choice == 'v':
            download_video(video_url)
        else:
            print("Invalid choice. Please enter 'A' for audio or 'V' for video.")
        
        another_download = input("Do you want to download another file? (yes/no): ").lower()
        if another_download != 'yes':
            break

if __name__ == "__main__":
    main()
