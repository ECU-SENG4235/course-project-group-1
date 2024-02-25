import unittest
import os
import shutil
from unittest.mock import patch
from main import download_video, download_audio

class TestDownload(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = os.path.join(os.getcwd(), "temp_test_files")
        os.makedirs(self.temp_dir, exist_ok=True)

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.temp_dir)

    @patch("main.messagebox.askyesno", return_value=True)  # Mock askyesno to always return True
    @patch("main.entry.get", return_value="https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship")  # Mock entry.get to return a URL
    def test_download_video(self, mock_entry_get, mock_askyesno):
        # Test successful video download
        download_video("https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship")
        # Check if video file exists and has a non-zero size
        video_files = [f for f in os.listdir("video_downloads") if f.endswith(".mp4")]
        self.assertTrue(len(video_files) == 1)
        video_file_path = os.path.join("video_downloads", video_files[0])
        self.assertTrue(os.path.exists(video_file_path))
        self.assertTrue(os.path.getsize(video_file_path) > 0)

    @patch("main.messagebox.askyesno", return_value=True)  # Mock askyesno to always return True
    @patch("main.entry.get", return_value="https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship")  # Mock entry.get to return a URL
    def test_download_audio_high_quality(self, mock_entry_get, mock_askyesno):
        # Test successful high quality audio download
        download_audio("https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship")
        # Check if audio file exists and has a non-zero size
        audio_files = [f for f in os.listdir("audio_downloads") if f.endswith("_high_q.mp3")]
        self.assertTrue(len(audio_files) == 1)
        audio_file_path = os.path.join("audio_downloads", audio_files[0])
        self.assertTrue(os.path.exists(audio_file_path))
        self.assertTrue(os.path.getsize(audio_file_path) > 0)

    @patch("main.messagebox.askyesno", return_value=True)  # Mock askyesno to always return True
    @patch("main.entry.get", return_value="https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship")  # Mock entry.get to return a URL
    def test_download_audio_low_quality(self, mock_entry_get, mock_askyesno):
        # Test successful low quality audio download
        download_audio("https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship", quality='low')
        # Check if audio file exists and has a non-zero size
        audio_files = [f for f in os.listdir("audio_downloads") if f.endswith("_low_q.mp3")]
        self.assertTrue(len(audio_files) == 1)
        audio_file_path = os.path.join("audio_downloads", audio_files[0])
        self.assertTrue(os.path.exists(audio_file_path))
        self.assertTrue(os.path.getsize(audio_file_path) > 0)

if __name__ == '__main__':
    unittest.main()
