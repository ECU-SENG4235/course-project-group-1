import unittest
import os
from main import download_video, download_audio, main
from unittest.mock import patch, call

class TestDownload(unittest.TestCase):

    def setUp(self):
        # Create necessary directories for testing
        os.makedirs("video_downloads", exist_ok=True)
        os.makedirs("audio_downloads", exist_ok=True)
        self.downloaded_files = set()  # Keep track of downloaded files

    def tearDown(self):
        # Remove downloaded files after each test
        for file in self.downloaded_files:
            os.remove(file)
        self.downloaded_files.clear()

    @patch('main.insert_video_metadata')
    def test_download_video(self, mock_insert_video_metadata):
        video_url = "https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship" 
        video_id = "SQL Explained in 100 Seconds"
        download_video(video_url)
        video_file_path = os.path.join("video_downloads", f"{video_id}.mp4")
        self.assertTrue(os.path.exists(video_file_path))
        self.assertTrue(os.path.getsize(video_file_path) > 0)
        mock_insert_video_metadata.assert_called_once()
        self.downloaded_files.add(video_file_path)  # Add downloaded file to the set

    @patch('main.insert_audio_metadata')
    def test_download_audio_high_quality(self, mock_insert_audio_metadata):
        video_url = "https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship"
        audio_id = "SQL Explained in 100 Seconds"
        download_audio(video_url, 'high')
        audio_file_path = os.path.join("audio_downloads", f"{audio_id}_high_q.mp3")
        self.assertTrue(os.path.exists(audio_file_path))
        self.assertTrue(os.path.getsize(audio_file_path) > 0)
        mock_insert_audio_metadata.assert_called_once()
        self.downloaded_files.add(audio_file_path)  # Add downloaded file to the set

    @patch('main.insert_audio_metadata')
    def test_download_audio_low_quality(self, mock_insert_audio_metadata):
        video_url = "https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship"
        audio_id = "SQL Explained in 100 Seconds"
        download_audio(video_url, 'low')
        audio_file_path = os.path.join("audio_downloads", f"{audio_id}_low_q.mp3")
        self.assertTrue(os.path.exists(audio_file_path))
        self.assertTrue(os.path.getsize(audio_file_path) > 0)
        mock_insert_audio_metadata.assert_called_once()
        self.downloaded_files.add(audio_file_path)  # Add downloaded file to the set

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
