import os
from pytube import YouTube
from pytube.cli import on_progress
from pytube.exceptions import RegexMatchError
from database import create_database, insert_video_metadata, insert_audio_metadata

# Function to download video
from moviepy.editor import VideoFileClip

# Function to download video
from moviepy.editor import VideoFileClip

# Function to download video
def download_video(video_url, video_format='mp4'):
    yt = YouTube(video_url, on_progress_callback=on_progress)

    # Attempt to get the highest resolution stream
    stream = yt.streams.get_highest_resolution()
    if not stream:
        print("No streams found for the video.")
        return

    # Download the video
    video_file_path = stream.download(output_path="video_downloads")
    print(f"Downloaded video: {stream.title}")

    # Check if the format matches the requested one
    if stream.includes_audio_track and stream.mime_type != f'video/{video_format}':
        # Convert the video to the specified format using moviepy
        converted_video_path = video_file_path.replace(".mp4", f"_{video_format}.{video_format}")
        video_clip = VideoFileClip(video_file_path)

        # Specify codec and parameters
        codec = "libx264"  # Example codec
        parameters = ['-preset', 'fast', '-crf', '23']  # Example parameters

        # Write the video file with specified codec and parameters
        video_clip.write_videofile(converted_video_path, codec=codec, ffmpeg_params=parameters)
        video_clip.close()
        os.remove(video_file_path)
        print(f"Converted video to {video_format.upper()}: {converted_video_path}")
    else:
        converted_video_path = video_file_path

    # Insert video metadata into the database
    video_metadata = (video_url, stream.title, yt.author, yt.length, stream.resolution)
    insert_video_metadata("video_metadata.db", video_metadata)
    print("Video metadata saved to the database.")



def download_audio(video_url, audio_format='mp3'):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    stream = yt.streams.filter(only_audio=True).first()
    audio_file = stream.download(output_path="audio_downloads")
    
    if audio_format != 'mp4':
        audio_file_wav = audio_file.replace(".mp4", f".{audio_format}")
        os.rename(audio_file, audio_file_wav)
        print(f"Downloaded and converted audio to {audio_format.upper()}: {audio_file_wav}")
    else:
        os.rename(audio_file, audio_file.replace(".mp4", "_mp4." + audio_format)) # Renaming to avoid conflict
        
    # Insert audio metadata into the database
    audio_metadata = (video_url, yt.title, yt.author, yt.length, audio_format, stream.abr)
    insert_audio_metadata("video_metadata.db", audio_metadata)
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
            audio_format = input("Select audio format (MP3/MP4/WAV/OGG): ").lower()
            download_audio(video_url, audio_format)
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
