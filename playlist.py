import tkinter as tk
import os
from ttkbootstrap import Style
from tkinter import ttk
from database import fetch_all_videos, fetch_all_audio, initialize_database
from metadata import get_video_metadata
from pathlib import Path

def list_files(folder):
    files = os.listdir(folder)
    return files

def open_file(event):
    widget = event.widget
    index = widget.curselection()[0]
    folder = "video_downloads" if widget == video_listbox else "audio_downloads"
    filename = widget.get(index)
    filepath = os.path.join(folder, filename)
    os.startfile(filepath)  # Open file with default application

def play_selected_file():
    if video_listbox.curselection():
        open_file_video()
    elif audio_listbox.curselection():
        open_file_audio()

def open_file_video():
    if video_listbox.curselection():
        index = video_listbox.curselection()[0]
        folder = "video_downloads"
        filename = video_listbox.get(index)
        filepath = os.path.join(folder, filename)
        os.startfile(filepath)  # Open video file with default application

def open_file_audio():
    if audio_listbox.curselection():
        index = audio_listbox.curselection()[0]
        folder = "audio_downloads"
        filename = audio_listbox.get(index)
        filepath = os.path.join(folder, filename)
        os.startfile(filepath)  # Open audio file with default application

def display_sections():
    video_files = list_files("video_downloads")
    audio_files = list_files("audio_downloads")

    video_listbox.delete(0, tk.END)
    for file in video_files:
        video_listbox.insert(tk.END, file)

    audio_listbox.delete(0, tk.END)
    for file in audio_files:
        audio_listbox.insert(tk.END, file)

def display_details(title, metadata):
    popup = tk.Toplevel()
    popup.title("Details")
    details_label = tk.Label(popup, text=title, font=("Nunito", 14, "bold"), bg="gray", fg="white")
    details_label.pack()

    for key, value in metadata.items():
        detail_text = f"{key}: {value}"
        detail_label = tk.Label(popup, text=detail_text, font=("Nunito", 12), bg="gray", fg="white")
        detail_label.pack()

def open_file_metadata():
    all_videos = fetch_all_videos("link2playback.db") 
    videos = [video for video in all_videos if video[6] != "Audio"]
    audio = fetch_all_audio("link2playback.db")

    root = tk.Tk()
    root.title("Link2Playback - Metadata")
    root.geometry("800x500")

    icon_path = Path(__file__).parent / "frame0" / "icon.ico"
    root.iconbitmap(icon_path)  # Set window icon

    video_frame = tk.Frame(root)
    video_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
    video_label = tk.Label(video_frame, text="Videos", font=("Nunito", 14, "bold"))
    video_label.pack()
    global video_listbox
    video_listbox = tk.Listbox(video_frame, font=("Nunito", 12))
    video_listbox.pack(fill=tk.BOTH, expand=True)
    video_scrollbar = tk.Scrollbar(video_frame, orient=tk.VERTICAL, command=video_listbox.yview)
    video_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    video_listbox.config(yscrollcommand=video_scrollbar.set)

    for video in videos:
        video_listbox.insert(tk.END, video[2])

    audio_frame = tk.Frame(root)
    audio_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
    audio_label = tk.Label(audio_frame, text="Audio", font=("Nunito", 14, "bold"))
    audio_label.pack()
    global audio_listbox
    audio_listbox = tk.Listbox(audio_frame, font=("Nunito", 12))
    audio_listbox.pack(fill=tk.BOTH, expand=True)
    audio_scrollbar = tk.Scrollbar(audio_frame, orient=tk.VERTICAL, command=audio_listbox.yview)
    audio_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    audio_listbox.config(yscrollcommand=audio_scrollbar.set)

    for audio_item in audio:
        audio_listbox.insert(tk.END, audio_item[2])

    def on_select_video(event):
        index = video_listbox.curselection()[0]
        selected_video = videos[index]
        video_metadata = {
            "URL": selected_video[1],
            "Author": selected_video[3],
            "Duration (minutes)": selected_video[4] / 60,
            "Resolution": selected_video[5],
            "Format": selected_video[6],
        }
        display_details(selected_video[2], video_metadata)

    def on_select_audio(event):
        index = audio_listbox.curselection()[0]
        selected_audio = audio[index]
        audio_metadata = {
            "URL": selected_audio[1],
            "Author": selected_audio[3],
            "Duration (minutes)": selected_audio[4] / 60,
            "Quality": selected_audio[5],
            "Bitrate": selected_audio[7],
            "Format": selected_audio[6],
        }
        display_details(selected_audio[2], audio_metadata)

    video_listbox.bind("<<ListboxSelect>>", on_select_video)
    audio_listbox.bind("<<ListboxSelect>>", on_select_audio)

    root.mainloop()


def open_file_list():
    # No changes needed in this function
    pass

def search_files(keyword):
    # No changes needed in this function
    pass

def sort_files_alphabetically():
    # No changes needed in this function
    pass

def run_gui():
    db_file = "link2playback.db"
    initialize_database(db_file)  # Ensure DB is initialized
    root = tk.Tk()
    root.title("Link2Playback - Playlist")
    root.geometry("800x500")
    icon_path = Path(__file__).parent / "frame0" / "icon.ico"
    root.iconbitmap(icon_path)
    root.configure(bg="lightgray")

    style = Style(theme='simplex')
    style.configure('TButton', background='#FF0000', foreground='white', font=('Nunito', 12, 'bold'))
    style.configure('TLabel', background='#D9D9D9', foreground='white', font=('Nunito', 12, 'bold'))

    search_frame = tk.Frame(root, bg="lightgray")
    search_frame.pack(side=tk.TOP, fill=tk.X)

    search_entry = tk.Entry(search_frame, width=50, font=("Nunito", 12))
    search_entry.pack(side=tk.LEFT, padx=10, pady=5)

    search_button = tk.Button(search_frame, text="Search", command=lambda: search_files(search_entry.get()), font=("Nunito", 12), bg="red", fg="white")
    search_button.pack(side=tk.LEFT, padx=5, pady=5)

    sort_button = tk.Button(search_frame, text="Sort Alphabetically", command=sort_files_alphabetically, font=("Nunito", 12), bg="red", fg="white")
    sort_button.pack(side=tk.RIGHT, padx=5, pady=5)

    refresh_button = tk.Button(search_frame, text="Refresh", command=display_sections, font=("Nunito", 12), bg="red", fg="white")
    refresh_button.pack(side=tk.RIGHT, padx=5, pady=5)

    # Frames
    list_frame = tk.Frame(root)
    list_frame.pack(fill=tk.BOTH, expand=True)

    metadata_frame = tk.Frame(root)
    metadata_frame.pack(fill=tk.BOTH, expand=True)

    # Navigation bar
    nav_bar = tk.Frame(root, bg="lightgray")
    nav_bar.pack(side=tk.TOP, fill=tk.X)

    metadata_button = tk.Button(nav_bar, text="Metadata", command=open_file_metadata, font=("Nunito", 12), bg="red", fg="white")
    metadata_button.pack(side=tk.LEFT, padx=10, pady=5)

    # Video files section
    global video_listbox
    video_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, font=("Nunito", 12), bg="gray", fg="white")
    video_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    video_listbox.bind("<Double-Button-1>", open_file)

    # Audio files section
    global audio_listbox
    audio_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, font=("Nunito", 12), bg="gray", fg="white")
    audio_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    audio_listbox.bind("<Double-Button-1>", open_file)

    # Play button
    play_button = tk.Button(root, text="Play", command=play_selected_file, font=("Nunito", 12), bg="red", fg="white")
    play_button.pack(pady=10)

    # Display initial file lists
    display_sections()

    # Metadata display
    metadata_button.pack(side=tk.TOP, padx=10, pady=5)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    run_gui()
