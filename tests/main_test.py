import unittest
from unittest.mock import patch, Mock
import sys
sys.path.append("..")  # Add the parent directory to the path
from main import download_video, download_audio, main

class TestDownload(unittest.TestCase):
    @patch('builtins.input', side_effect=['yes', 'https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'A', 'mp3', 'high'])
    @patch('main.batch_download', side_effect=None)
    def test_main_batch_download(self, mock_batch_download, mock_input):
        main()
        self.assertTrue(mock_input.called)

    @patch('builtins.input', side_effect=['https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'A', 'mp3', 'high'])
    @patch('main.download_audio', side_effect=None)
    def test_main_single_download(self, mock_download_audio, mock_input):
        main()
        self.assertTrue(mock_input.called)

    @patch('pytube.YouTube')
    @patch('main.insert_audio_metadata')
    def test_download_audio_high_quality(self, mock_insert_audio_metadata, mock_youtube):
        video_mock = Mock()
        video_mock.length = 142  # Set the video duration to 142 seconds
        mock_youtube.return_value = video_mock
        download_audio("https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship", 'mp3', 'high')
        mock_insert_audio_metadata.assert_called_once_with("link2playback.db", ('https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'SQL Explained in 100 Seconds', 'Fireship', 142, 'high', 'mp3', '128kbps'))

    @patch('pytube.YouTube')
    @patch('main.insert_audio_metadata')
    def test_download_audio_low_quality(self, mock_insert_audio_metadata, mock_youtube):
        video_mock = Mock()
        video_mock.length = 142  # Set the video duration to 142 seconds
        mock_youtube.return_value = video_mock
        download_audio("https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship", 'mp3', 'low')
        mock_insert_audio_metadata.assert_called_once_with("link2playback.db", ('https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'SQL Explained in 100 Seconds', 'Fireship', 142, 'low', 'mp3', '48kbps'))

    @patch('pytube.YouTube')
    @patch('main.insert_video_metadata')
    def test_download_video(self, mock_insert_video_metadata, mock_youtube):
        video_mock = Mock()
        video_mock.length = 142  # Set the video duration to 142 seconds
        mock_youtube.return_value = video_mock
        download_video("https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship", 'mp4')
        mock_insert_video_metadata.assert_called_once_with("link2playback.db", ('https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'SQL Explained in 100 Seconds', 'Fireship', 142, '720p', 'mp4'))

if __name__ == '__main__':
    unittest.main()
