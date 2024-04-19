import unittest
from unittest.mock import patch, Mock, MagicMock
import sys
import os
sys.path.append("..")  # Add the parent directory to the path
from main import download_video, download_audio, batch_download, main
from moviepy.editor import VideoFileClip

class TestDownload(unittest.TestCase):
    def setUp(self):
        self.video_mock = Mock()
        self.video_mock.length = 142  # Set the video duration to 142 seconds

    def tearDown(self):
        pass

    @patch('builtins.input', side_effect=['yes', 'https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'A', 'mp3', 'high'])
    @patch('main.batch_download', side_effect=None)
    def test_main_batch_download(self, mock_batch_download, mock_input):
        main()
        self.assertTrue(mock_input.called)

    @patch('builtins.input', side_effect=['https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'V', 'mp4'])
    @patch('main.download_video', side_effect=None)
    def test_main_single_download_video(self, mock_download_video, mock_input):
        main()
        self.assertTrue(mock_input.called)

    @patch('pytube.YouTube')
    @patch('main.insert_audio_metadata')
    def test_download_audio_high_quality(self, mock_insert_audio_metadata, mock_youtube):
        mock_youtube.return_value = self.video_mock
        download_audio("https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship", 'mp3', 'high')
        mock_insert_audio_metadata.assert_called_once_with("link2playback.db", ('https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'SQL Explained in 100 Seconds', 'Fireship', 142, 'high', 'mp3', '128kbps'))

    @patch('pytube.YouTube')
    @patch('main.insert_audio_metadata')
    def test_download_audio_low_quality(self, mock_insert_audio_metadata, mock_youtube):
        mock_youtube.return_value = self.video_mock
        download_audio("https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship", 'mp3', 'low')
        mock_insert_audio_metadata.assert_called_once_with("link2playback.db", ('https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'SQL Explained in 100 Seconds', 'Fireship', 142, 'low', 'mp3', '48kbps'))

    @patch('pytube.YouTube')
    @patch('main.insert_video_metadata')
    def test_download_video(self, mock_insert_video_metadata, mock_youtube):
        mock_youtube.return_value = self.video_mock
        download_video("https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship", 'mp4')
        mock_insert_video_metadata.assert_called_once_with("link2playback.db", ('https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'SQL Explained in 100 Seconds', 'Fireship', 142, '720p', 'mp4'))


    @patch('builtins.input', side_effect=['a', 'mp3', 'high'])
    @patch('main.download_audio')
    @patch('main.download_video')  # Add this line to patch download_video
    def test_batch_download_audio(self, mock_download_video, mock_download_audio, mock_input):
        urls = ['https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship',
                'https://www.youtube.com/watch?v=Y8Tko2YC5hA']
        download_type = 'a'
        format_choice = 'mp3'
        quality_choice = 'high'
        batch_download(urls, download_type, format_choice, quality_choice)
        
        # Verify that download_audio is called for both URLs
        mock_download_audio.assert_any_call(urls[0], format_choice, quality_choice)
        mock_download_audio.assert_any_call(urls[1], format_choice, quality_choice)
        
        # Verify that download_video is not called
        mock_download_video.assert_not_called()
        
    @patch('builtins.input', side_effect=['v', 'mp4'])
    @patch('main.download_video')
    @patch('main.download_audio')  # Add this line to patch download_audio
    def test_batch_download_video(self, mock_download_audio, mock_download_video, mock_input):
        urls = ['https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship',
                'https://www.youtube.com/watch?v=Y8Tko2YC5hA']
        download_type = 'v'
        format_choice = 'mp4'
        batch_download(urls, download_type, format_choice)
        
        # Verify that download_video is called for both URLs
        mock_download_video.assert_any_call(urls[0], format_choice)
        mock_download_video.assert_any_call(urls[1], format_choice)
        
        # Verify that download_audio is not called
        mock_download_audio.assert_not_called()

    @patch('pytube.YouTube')
    @patch('main.insert_video_metadata')
    @patch('moviepy.editor.VideoFileClip')
    def test_download_video_mov_format(self, mock_video_clip, mock_insert_video_metadata, mock_youtube):
        mock_youtube.return_value = self.video_mock
        download_video("https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship", 'mov')
        mock_insert_video_metadata.assert_called_once_with("link2playback.db", ('https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'SQL Explained in 100 Seconds', 'Fireship', 142, '720p', 'mov'))

    @patch('pytube.YouTube')
    @patch('main.insert_audio_metadata')
    def test_download_audio_wav_format(self, mock_insert_audio_metadata, mock_youtube):
        mock_youtube.return_value = self.video_mock
        download_audio("https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship", 'wav', 'high')
        mock_insert_audio_metadata.assert_called_once_with("link2playback.db", ('https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'SQL Explained in 100 Seconds', 'Fireship', 142, 'high', 'wav', '128kbps'))


    @patch('builtins.input', side_effect=['https://www.youtube.com/watch?v=zsjvFFKOm3c&ab_channel=Fireship', 'A', 'mp3', 'high'])
    @patch('main.download_audio', side_effect=None)
    def test_main_single_download_audio(self, mock_download_audio, mock_input):
        main()
        self.assertTrue(mock_input.called)

        
if __name__ == '__main__':
    unittest.main()
