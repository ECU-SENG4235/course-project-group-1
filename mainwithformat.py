import os
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube  # Importing the YouTube class from the pytube library
from pytube.cli import on_progress  # Importing the on_progress function from the pytube library
from pytube.exceptions import RegexMatchError  # Importing the RegexMatchError class from the pytube library
from database import create_database, insert_video_metadata, insert_audio_metadata  # Importing functions for database operations
from view_downloads import display_sections  # Importing function to display download sections
from moviepy.editor import VideoFileClip  # Importing VideoFileClip class from moviepy.editor library

# Function to download a video from a YouTube URL
def download_video(video_url, video_format='mp4'):
    yt = YouTube(video_url, on_progress_callback=on_progress)  # Create a YouTube object for the provided URL

    stream = yt.streams.get_highest_resolution()  # Get the highest resolution video stream

    # Check if a suitable stream is found
    if not stream:
        print("No streams found for the video.")
        return

    # Download the video to the specified output path
    video_file_path = stream.download(output_path="video_downloads")
    print(f"Downloaded video: {stream.title}")

    # Check if the video needs conversion (e.g., if it includes audio track and is not in the desired format)
    if stream.includes_audio_track and stream.mime_type != f'video/{video_format}':
        converted_video_path = video_file_path.replace(".mp4", f".{video_format}")
        video_clip = VideoFileClip(video_file_path)

        # Specify codec and parameters for video conversion
        codec = "libx264"  # Example codec
        parameters = ['-preset', 'fast', '-crf', '23']  # Example parameters

        # Convert the video and save it with the specified format
        video_clip.write_videofile(converted_video_path, codec=codec, ffmpeg_params=parameters)
        video_clip.close()
        os.remove(video_file_path)  # Remove the original video file after conversion
        print(f"Converted video to {video_format.upper()}: {converted_video_path}")
    else:
        converted_video_path = video_file_path

    # Insert video metadata into the database
    video_metadata = (video_url, stream.title, yt.author, yt.length, stream.resolution, video_format)
    insert_video_metadata("link2playback.db", video_metadata)
    print("Video metadata saved to the database.")

# Function to download audio from a YouTube URL
def download_audio(video_url, audio_format='mp3', quality='high'):
    yt = YouTube(video_url, on_progress_callback=on_progress)  # Create a YouTube object for the provided URL

    # Determine the appropriate audio stream based on the specified quality
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

    # Download the audio stream to the specified output path
    audio_file = stream.download(output_path="audio_downloads")

    # Rename the downloaded audio file with the appropriate quality tag and format extension
    filename, extension = os.path.splitext(audio_file)
    renamed_audio_file = f"{filename}_{quality_tag}.{audio_format}"
    os.rename(audio_file, renamed_audio_file)

    # Print a message indicating successful download and conversion of audio
    print(f"Downloaded and converted audio to {quality_tag} {audio_format.upper()}: {renamed_audio_file}")

    # Insert audio metadata into the database
    audio_metadata = (video_url, yt.title, yt.author, yt.length, quality, audio_format, stream.abr)
    insert_audio_metadata("link2playback.db", audio_metadata)
    print("Audio metadata saved to the database.")

# Main function to manage the downloading process
def main():
    create_database("link2playback.db")  # Create a database or connect to an existing one

    # Continue prompting the user to enter a YouTube video URL and choose the download type until they decide to stop
    while True:
        video_url = input("Enter the YouTube video URL: ")  # Prompt the user to enter a YouTube video URL
        
        try:
            YouTube(video_url)  # Validate the YouTube video URL
        except RegexMatchError:
            print("Invalid YouTube video URL. Please enter a valid URL.")
            continue

        choice = input("Download as Audio or Video (A/V)?: ").lower()  # Prompt the user to choose audio or video download
        
        # Depending on the user's choice, prompt for additional options and initiate the download process
        if choice == 'a':
            audio_format = input("Select audio format (MP3/MP4/WAV/OGG): ").lower()
            quality = input("Select audio quality (High/Low): ").lower()
            download_audio(video_url, audio_format, quality)
        elif choice == 'v':
            video_format = input("Select video format (MP4/MOV/AVI/WMV/WEBM/FLV): ").lower()
            download_video(video_url, video_format)
        else:
            print("Invalid choice. Please enter 'A' for audio or 'V' for video.")
        
        # Prompt the user if they want to download another file or exit the program
        another_download = input("Do you want to download another file? (yes/no): ").lower()
        if another_download != 'yes':
            break

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to start the downloading process
