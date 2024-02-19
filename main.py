from pytube import YouTube
from pytube.cli import on_progress

def download_video(video_url):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print(f"Downloaded video: {stream.title}")

def download_audio(video_url, quality='high'):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    if quality == 'high':
        stream = yt.streams.filter(only_audio=True).first()
    else:  # Assuming 'low' quality is requested
        stream = yt.streams.filter(only_audio=True).last()
    stream.download()
    print(f"Downloaded audio: {stream.title}")

def main():
    video_url = input("Enter the YouTube video URL: ")
    choice = input("Download as Audio or Video (A/V)?: ").lower()
    if choice == 'a':
        quality = input("Select audio quality (High/Low): ").lower()
        download_audio(video_url, quality)
    elif choice == 'v':
        download_video(video_url)
    else:
        print("Invalid choice. Please enter 'A' for audio or 'V' for video.")

if __name__ == "__main__":
    main()
