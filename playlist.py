import tkinter as tk
from database import fetch_all_videos, fetch_all_audio
import os
import subprocess

def list_files(folder):
    files = os.listdir(folder)
    return files

def open_file(event):
    widget = event.widget
    index = widget.curselection()[0]
    folder = "video_downloads" if widget == video_listbox else "audio_downloads"
    filename = widget.get(index)
    filepath = os.path.join(folder, filename)
    subprocess.Popen(['xdg-open', filepath])  # Linux specific, opens file with default application

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
    details_label = tk.Label(popup, text=title)
    details_label.pack()

    for key, value in metadata.items():
        detail_text = f"{key}: {value}"
        detail_label = tk.Label(popup, text=detail_text)
        detail_label.pack()

def open_file_metadata():
    all_videos = fetch_all_videos("link2playback.db") 
    videos = [video for video in all_videos if video[6] != "Audio"]
    audio = fetch_all_audio("link2playback.db")

    root = tk.Tk()
    root.title("Downloads")

    root.geometry("736x414")

    video_frame = tk.Frame(root)
    video_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)  # Adjust to fill both directions
    video_label = tk.Label(video_frame, text="Videos")
    video_label.pack()
    video_listbox = tk.Listbox(video_frame)
    for video in videos:
        video_listbox.insert(tk.END, video[2]) 
    video_listbox.pack(fill=tk.BOTH, expand=True)  
    video_scrollbar = tk.Scrollbar(video_frame, orient=tk.VERTICAL, command=video_listbox.yview)
    video_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    video_listbox.config(yscrollcommand=video_scrollbar.set)

    audio_frame = tk.Frame(root)
    audio_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)  # Adjust to fill both directions
    audio_label = tk.Label(audio_frame, text="Audio")
    audio_label.pack()
    audio_listbox = tk.Listbox(audio_frame)
    for audio_item in audio:
        audio_listbox.insert(tk.END, audio_item[2])
    audio_listbox.pack(fill=tk.BOTH, expand=True)
    audio_scrollbar = tk.Scrollbar(audio_frame, orient=tk.VERTICAL, command=audio_listbox.yview)
    audio_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    audio_listbox.config(yscrollcommand=audio_scrollbar.set)

    def on_select_video(event):
        if video_listbox.curselection():
            index = video_listbox.curselection()[0]  
            selected_video = videos[index]
            video_metadata = {
                "URL": selected_video[1],
                "Author": selected_video[3],
                "Duration (minutes)": selected_video[4]/60 ,
                "Resolution": selected_video[5],
                "Format": selected_video[6],
            }
            display_details(selected_video[2], video_metadata)

    def on_select_audio(event):
        if audio_listbox.curselection():
            index = audio_listbox.curselection()[0]  
            selected_audio = audio[index]
            audio_metadata = {
                "URL": selected_audio[1],
                "Author": selected_audio[3],
                "Duration (minutes)": selected_audio[4]/60,
                "Quality": selected_audio[5],
                "Bitrate": selected_audio[7],
                "Format": selected_audio[6],
            }
            display_details(selected_audio[2], audio_metadata)

    video_listbox.bind("<<ListboxSelect>>", on_select_video)
    audio_listbox.bind("<<ListboxSelect>>", on_select_audio)

    root.mainloop()

def open_file_list():
    # Hide metadata frame and show file list frame
    metadata_frame.pack_forget()
    list_frame.pack(fill=tk.BOTH, expand=True)
    display_sections()

def run_gui():
    # Initialize the main window
    root = tk.Tk()
    root.title("Downloads in File Folders")

    # Set initial window size
    root.geometry("800x500")

    # Frames
    global list_frame
    list_frame = tk.Frame(root)
    list_frame.pack(fill=tk.BOTH, expand=True)

    global metadata_frame
    metadata_frame = tk.Frame(root)
    metadata_frame.pack(fill=tk.BOTH, expand=True)

    # Navigation bar
    nav_bar = tk.Frame(root, bg="lightgray")
    nav_bar.pack(side=tk.TOP, fill=tk.X)

    #list_button = tk.Button(nav_bar, text="File List", command=open_file_list)
    #list_button.pack(side=tk.LEFT, padx=10, pady=5)
    metadata_button = tk.Button(nav_bar, text="Metadata", command=open_file_metadata)
    metadata_button.pack(side=tk.LEFT, padx=10, pady=5)

    # Video files section
    global video_listbox
    video_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, font=("Helvetica", 12))
    video_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    video_listbox.bind("<Double-Button-1>", open_file)

    # Audio files section
    global audio_listbox
    audio_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, font=("Helvetica", 12))
    audio_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    audio_listbox.bind("<Double-Button-1>", open_file)

    # Button to refresh the lists
    refresh_button = tk.Button(root, text="Refresh", command=display_sections)
    refresh_button.pack(pady=10)

    # Display initial file lists
    display_sections()

    # Metadata display
    #metadata_button = tk.Button(metadata_frame, text="Back to File List", command=open_file_list)
    metadata_button.pack(side=tk.TOP, padx=10, pady=5)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    run_gui()
