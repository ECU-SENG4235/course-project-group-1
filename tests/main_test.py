import unittest
import os
from main import download_video, download_audio

class TestDownload(unittest.TestCase):

    def test_download_video(self):
        # Test successful video download
        video_url = "https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship" 
        video_id = "SQL Explained in 100 Seconds"  # Assuming download_video saves the video file with the video_id as name
        download_video(video_url)
        # Check if video file exists and has a non-zero size
        self.assertTrue(os.path.exists(os.path.join("video_downloads", f"{video_id}.mp4")))
        self.assertTrue(os.path.getsize(os.path.join("video_downloads", f"{video_id}.mp4")) > 0)

    def test_download_audio_high_quality(self):
        # Test successful high quality audio download
        video_url = "https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship"
        audio_id = "SQL Explained in 100 Seconds"  # Assuming download_audio saves the audio file with the audio_id as name
        download_audio(video_url, 'high')
        # Check if audio file exists and has a non-zero size
        self.assertTrue(os.path.exists(os.path.join("audio_downloads", f"{audio_id}_high_q.mp3")))
        self.assertTrue(os.path.getsize(os.path.join("audio_downloads", f"{audio_id}_high_q.mp3")) > 0)

    def test_download_audio_low_quality(self):
        # Test successful low quality audio download
        video_url = "https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship"
        audio_id = "SQL Explained in 100 Seconds"  # Assuming download_audio saves the audio file with the audio_id as name
        download_audio(video_url, 'low')
        # Check if audio file exists and has a non-zero size
        self.assertTrue(os.path.exists(os.path.join("audio_downloads", f"{audio_id}_low_q.mp3")))
        self.assertTrue(os.path.getsize(os.path.join("audio_downloads", f"{audio_id}_low_q.mp3")) > 0)

if __name__ == '__main__':
    unittest.main()
