import os
import tkinter as tk
import subprocess

def list_files(folder):
    files = os.listdir(folder)
    return files

def display_sections():
    video_files = list_files("video_downloads")
    audio_files = list_files("audio_downloads")

    video_list.delete(0, tk.END)
    for file in video_files:
        video_list.insert(tk.END, file)

    audio_list.delete(0, tk.END)
    for file in audio_files:
        audio_list.insert(tk.END, file)

def open_file(event):
    widget = event.widget
    index = widget.curselection()[0]
    folder = "video_downloads" if widget == video_list else "audio_downloads"
    filename = widget.get(index)
    filepath = os.path.join(folder, filename)
    subprocess.Popen(['xdg-open', filepath])  # Linux specific, opens file with default application

def run_gui():
    # Initialize the main window
    root = tk.Tk()
    root.title("Downloads in File Folders")

    # Set initial window size
    root.geometry("1800x400")

    # Video files section
    video_frame = tk.Frame(root, bd=1, relief=tk.SUNKEN)
    video_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    video_label = tk.Label(video_frame, text="Video Files", font=("Helvetica", 16))
    video_label.pack(pady=(0, 10))

    global video_list
    video_list = tk.Listbox(video_frame, selectmode=tk.SINGLE, font=("Helvetica", 12))
    video_list.pack(fill=tk.BOTH, expand=True)
    video_list.bind("<Double-Button-1>", open_file)

    # Audio files section
    audio_frame = tk.Frame(root, bd=1, relief=tk.SUNKEN)
    audio_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    audio_label = tk.Label(audio_frame, text="Audio Files", font=("Helvetica", 16))
    audio_label.pack(pady=(0, 10))

    global audio_list
    audio_list = tk.Listbox(audio_frame, selectmode=tk.SINGLE, font=("Helvetica", 12))
    audio_list.pack(fill=tk.BOTH, expand=True)
    audio_list.bind("<Double-Button-1>", open_file)

    # Button to refresh the lists
    refresh_button = tk.Button(root, text="Refresh", command=display_sections)
    refresh_button.pack(pady=10)

    # Display initial file lists
    display_sections()

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    run_gui()
