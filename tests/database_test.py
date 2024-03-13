import unittest
import sqlite3
import tempfile
import os

# Import functions from the file to be tested
from database import create_database, insert_video_metadata, fetch_all_videos

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
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='videos'")
        result = c.fetchone()
        self.assertIsNotNone(result)

    def test_insert_and_fetch(self):
        # Insert test data
        video_metadata = ('http://example.com/video1', 'Video 1', 'Author 1', 120, '1080p')
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

if __name__ == '__main__':
    unittest.main()
