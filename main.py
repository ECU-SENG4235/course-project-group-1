import os
import time
from pytube import YouTube, exceptions
from pytube.cli import on_progress
from database import create_database, insert_video_metadata, insert_audio_metadata
import ffmpeg

# Helper function to ensure download directories exist
def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to download video with specified resolution
def download_video(video_url, resolution='720p'):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    
    stream = yt.streams.filter(res=resolution, progressive=True).first()
    
    if not stream:
        print(f"No stream found for resolution {resolution}. Attempting to download highest resolution available.")
        stream = yt.streams.get_highest_resolution()

    if stream:
        parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        video_directory = os.path.join(parent_directory, "video_downloads")
        ensure_directory_exists(video_directory)
        
        stream.download(output_path=video_directory)
        print(f"Downloaded video: {stream.title}")

        video_metadata = (video_url, stream.title, yt.author, yt.length, stream.resolution)
        insert_video_metadata("video_metadata.db", video_metadata)
        print("Video metadata saved to the database.")
    else:
        print("Unable to download video. No suitable stream found.")

# Function to download audio with specified quality and format
def download_audio(video_url, channel='stereo', bit_depth='16-bit', format='mp3'):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    audio_streams = yt.streams.filter(only_audio=True)
    stream = audio_streams.first()
    
    ensure_directory_exists("audio_downloads")
    audio_file = stream.download(output_path="audio_downloads")
    base_audio_file = audio_file.replace(".mp4", "")
    audio_file_formatted = f"{base_audio_file}_{channel}_{bit_depth}.{format}"

    ffmpeg_params = {
        'ac': 1 if channel == 'mono' else 2,
        'acodec': 'pcm_s16le' if bit_depth == '16-bit' else 'pcm_s24le',
        'ar': '44100'
    }
    if format == 'mp3':
        ffmpeg_params['acodec'] = 'libmp3lame'
    
    ffmpeg.input(audio_file).output(audio_file_formatted, **ffmpeg_params).run(overwrite_output=True)
    os.remove(audio_file)
    print(f"Downloaded and converted audio: {audio_file_formatted}")

    audio_metadata = (video_url, yt.title, yt.author, yt.length, channel, bit_depth, format)
    insert_audio_metadata("video_metadata.db", audio_metadata)
    print("Audio metadata saved to the database.")

# Function to handle GUI interaction, simplified for direct call from GUI buttons
def handle_media_download(video_url, media_format, resolution='720p', channel='stereo', bit_depth='16-bit', format='mp3'):
    try:
        if media_format == 'audio':
            download_audio(video_url, channel, bit_depth, format)
        elif media_format == 'video':
            download_video(video_url, resolution)
        elif media_format == 'both':
            download_video(video_url, resolution)
            download_audio(video_url, channel, bit_depth, format)
        else:
            print("Invalid media format selection.")
    except exceptions.RegexMatchError:
        print("Invalid YouTube video URL. Please enter a valid URL.")

def main():
    create_database("video_metadata.db")

    while True:
        video_url = input("Enter the YouTube video URL (or type 'exit' to quit): ").strip()
        if video_url.lower() == 'exit':
            break

        media_format = input("Download as Only Audio, Only Video, or Both (audio/video/both)?: ").strip().lower()

        if media_format in ['audio', 'both']:
            channel = input("Select audio channel (Mono/Stereo): ").strip().lower()
            bit_depth = input("Select bit depth (16-bit/24-bit): ").strip().lower()
            format = input("Select file format (MP3/WAV): ").strip().lower()
            handle_media_download(video_url, media_format, channel=channel, bit_depth=bit_depth, format=format)

        if media_format in ['video', 'both']:
            resolution = input("Select video resolution (480p/720p/1080p): ").strip().lower()
            handle_media_download(video_url, media_format, resolution=resolution)

        if media_format not in ['audio', 'video', 'both']:
            print("Invalid choice. Please enter 'audio', 'video', or 'both'.")

        another_download = input("Do you want to download another file? (yes/no): ").strip().lower()
        if another_download != 'yes':
            break

if __name__ == "__main__":
    main()
