import unittest
import sqlite3
import tempfile
import os

# Import functions from the file to be tested
from database import create_database, insert_video_metadata, insert_audio_metadata, fetch_all_videos, fetch_all_audio

class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        create_database(self.db_path)

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_create_database(self):
        # Check if the database file exists
        self.assertTrue(os.path.exists(self.db_path))

        # Connect to the database and check if the table exists
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='video_metadata'")
        result = c.fetchone()
        self.assertIsNotNone(result)

        # Check if the audio_metadata table exists
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='audio_metadata'")
        result = c.fetchone()
        self.assertIsNotNone(result)

    def test_insert_and_fetch_videos(self):
        # Insert test data
        video_metadata = ('http://example.com/video1', 'Video 1', 'Author 1', 120, '1080p', 'mp4')
        insert_video_metadata(self.db_path, video_metadata)

        # Fetch the inserted data
        videos = fetch_all_videos(self.db_path)

        # Check if the fetched data matches the inserted data
        self.assertEqual(len(videos), 1)
        self.assertEqual(videos[0][1], 'http://example.com/video1')
        self.assertEqual(videos[0][2], 'Video 1')
        self.assertEqual(videos[0][3], 'Author 1')
        self.assertEqual(videos[0][4], 120)
        self.assertEqual(videos[0][5], '1080p')
        self.assertEqual(videos[0][6], 'mp4')

        # Check if downloaded_at is not None
        self.assertIsNotNone(videos[0][7])

    def test_insert_and_fetch_audio(self):
        # Insert test data
        audio_metadata = ('http://example.com/audio1', 'Audio 1', 'Author 1', 120, 'high', 128, 'mp3')
        insert_audio_metadata(self.db_path, audio_metadata)

        # Fetch the inserted data
        audio = fetch_all_audio(self.db_path)

        # Check if the fetched data matches the inserted data
        self.assertEqual(len(audio), 1)
        self.assertEqual(audio[0][1], 'http://example.com/audio1')
        self.assertEqual(audio[0][2], 'Audio 1')
        self.assertEqual(audio[0][3], 'Author 1')
        self.assertEqual(audio[0][4], 120)
        self.assertEqual(audio[0][5], 'high')
        self.assertEqual(audio[0][6], 128)
        self.assertEqual(audio[0][7], 'mp3')

        # Check if downloaded_at is not None
        self.assertIsNotNone(audio[0][8])

if __name__ == '__main__':
    unittest.main()
