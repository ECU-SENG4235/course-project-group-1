import unittest
import os
from main import download_video, download_audio, main
from unittest.mock import patch, call

class TestDownload(unittest.TestCase):

    def setUp(self):
        # Create necessary directories for testing
        os.makedirs("video_downloads", exist_ok=True)
        os.makedirs("audio_downloads", exist_ok=True)

    def tearDown(self):
        # Remove downloaded files after each test
        for file in os.listdir("video_downloads"):
            os.remove(os.path.join("video_downloads", file))
        for file in os.listdir("audio_downloads"):
            os.remove(os.path.join("audio_downloads", file))

    @patch('main.insert_video_metadata')
    def test_download_video(self, mock_insert_video_metadata):
        # Test successful video download
        video_url = "https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship" 
        video_id = "SQL Explained in 100 Seconds"  # Assuming download_video saves the video file with the video_id as name
        download_video(video_url)
        # Check if video file exists and has a non-zero size
        self.assertTrue(os.path.exists(os.path.join("video_downloads", f"{video_id}.mp4")))
        self.assertTrue(os.path.getsize(os.path.join("video_downloads", f"{video_id}.mp4")) > 0)
        # Assert that insert_video_metadata was called
        mock_insert_video_metadata.assert_called_once()

    @patch('main.insert_audio_metadata')
    def test_download_audio_high_quality(self, mock_insert_audio_metadata):
        # Test successful high quality audio download
        video_url = "https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship"
        audio_id = "SQL Explained in 100 Seconds"  # Assuming download_audio saves the audio file with the audio_id as name
        download_audio(video_url, 'high')
        # Check if audio file exists and has a non-zero size
        self.assertTrue(os.path.exists(os.path.join("audio_downloads", f"{audio_id}_high_q.mp3")))
        self.assertTrue(os.path.getsize(os.path.join("audio_downloads", f"{audio_id}_high_q.mp3")) > 0)
        # Assert that insert_audio_metadata was called
        mock_insert_audio_metadata.assert_called_once()

    @patch('main.insert_audio_metadata')
    def test_download_audio_low_quality(self, mock_insert_audio_metadata):
        # Test successful low quality audio download
        video_url = "https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship"
        audio_id = "SQL Explained in 100 Seconds"  # Assuming download_audio saves the audio file with the audio_id as name
        download_audio(video_url, 'low')
        # Check if audio file exists and has a non-zero size
        self.assertTrue(os.path.exists(os.path.join("audio_downloads", f"{audio_id}_low_q.mp3")))
        self.assertTrue(os.path.getsize(os.path.join("audio_downloads", f"{audio_id}_low_q.mp3")) > 0)
        # Assert that insert_audio_metadata was called
        mock_insert_audio_metadata.assert_called_once()

    @patch('main.insert_video_metadata')
    def test_invalid_video_url(self, mock_insert_video_metadata):
        # Test download with invalid video URL
        invalid_video_url = "https://www.youtube.com/watch_invalid_url"
        with self.assertRaises(Exception):  # Assuming an appropriate exception is raised
            download_video(invalid_video_url)
        # Assert that insert_video_metadata was not called
        mock_insert_video_metadata.assert_not_called()

    @patch('main.insert_audio_metadata')
    def test_invalid_audio_quality(self, mock_insert_audio_metadata):
        # Test download with invalid audio quality choice
        video_url = "https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship"
        invalid_quality = 'invalid_quality'
        download_audio(video_url, invalid_quality)
        # Check if audio file exists and has a non-zero size with high quality tag
        self.assertTrue(os.path.exists(os.path.join("audio_downloads", f"SQL Explained in 100 Seconds_high_q.mp3")))
        self.assertTrue(os.path.getsize(os.path.join("audio_downloads", f"SQL Explained in 100 Seconds_high_q.mp3")) > 0)
        # Assert that insert_audio_metadata was called
        mock_insert_audio_metadata.assert_called_once()

    @patch('main.insert_video_metadata')
    @patch('builtins.input', side_effect=['https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'V', 'no'])
    def test_invalid_user_choice(self, mock_input, mock_insert_video_metadata):
        # Test invalid user choice in main program
        main()  # Run the main program
        # Check if invalid choice prompt is displayed and then user is prompted again for a valid choice
        self.assertEqual(mock_input.call_args_list, [call("Enter the YouTube video URL: "),
                                                    call("Download as Audio or Video (A/V)?: "),
                                                    call("Do you want to download another file? (yes/no): ")])
        # Assert that insert_video_metadata was called once
        mock_insert_video_metadata.assert_called_once()

if __name__ == '__main__':
    unittest.main()
