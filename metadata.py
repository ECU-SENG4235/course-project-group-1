# This code will possibly extract metadata from YouTube videos

from pytube import YouTube
import requests
from io import BytesIO
from PIL import Image

def get_video_metadata(video_url):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Accessing metadata
        print("Video Title:", yt.title)
        print("Channel Name:", yt.author)
        print("Video Duration:", yt.length, "seconds")
        print("Video Views:", yt.views)
        print("Video Description:", yt.description)

        # Get thumbnail URL
        thumbnail_url = yt.thumbnail_url

        # Download and display the thumbnail
        response = requests.get(thumbnail_url)
        img = Image.open(BytesIO(response.content))
        img.show()

        # Get available streams
        streams = yt.streams.filter(file_extension='mp4', only_video=True).all()
        if streams:
            # Print available video resolutions
            print("Available Resolutions:")
            for stream in streams:
                print(stream.resolution)

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    # Replace 'VIDEO_URL' with the URL of the YouTube video
    video_url = "VIDEO_URL"
    get_video_metadata(video_url)
