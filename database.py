import sqlite3

# Function to create the database and table
def create_database(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS videos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 url TEXT NOT NULL,
                 title TEXT,
                 author TEXT,
                 duration INTEGER,
                 resolution TEXT,
                 downloaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS audio_metadata
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                audio_url TEXT NOT NULL,
                title TEXT,
                author TEXT,
                duration INTEGER,
                quality TEXT,
                bitrate INTEGER,
                downloaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

    conn.commit()
    conn.close()

# Function to insert video metadata into the database
def insert_video_metadata(db_file, video_metadata):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''INSERT INTO videos (url, title, author, duration, resolution)
                 VALUES (?, ?, ?, ?, ?)''', video_metadata)
    conn.commit()
    conn.close()

def insert_audio_metadata(db_file, audio_metadata):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''INSERT INTO audio_metadata (audio_url, title, author, duration, quality, bitrate)
                 VALUES (?, ?, ?, ?, ?, ?)''', audio_metadata)
    conn.commit()
    conn.close()

def fetch_all_videos(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT * FROM videos")
    rows = c.fetchall()
    conn.close()
    return rows

def fetch_all_audio(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT * FROM audio_metadata")
    rows = c.fetchall()
    conn.close()
    return rows

