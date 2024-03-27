import os
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from pytube.cli import on_progress
from pytube.exceptions import RegexMatchError
from mainwithformat import download_video, download_audio
from view_downloads import display_sections
from downloadlist import run_gui
from moviepy.editor import VideoFileClip

def download():
    video_url = url_entry.get()
    choice = choice_var.get()
    if choice == 'A':
        audio_format = audio_format_var.get()  # Get audio format if downloading audio
        audio_quality = quality_var.get()  # Get audio quality if downloading audio
        download_audio(video_url, audio_format, audio_quality)  # Pass audio quality to the download_audio function
    elif choice == 'V':
        video_format = video_format_var.get()  # Get video format if downloading video
        download_video(video_url, video_format)
    else:
        messagebox.showerror("Error", "Invalid choice. Please select either Audio or Video.")

def view_download_metadata():
    display_sections()  # Call the function to display sections

def download_files():
    run_gui()

def toggle_quality_options():
    if choice_var.get() == 'A':
        audio_quality_label.pack()
        high_quality_button.pack()
        low_quality_button.pack()
        audio_format_label.pack()  # Show audio format options when selecting audio
        audio_format_menu.pack()
        video_format_label.pack_forget()  # Hide video format options when selecting audio
        video_format_menu.pack_forget()
    elif choice_var.get() == 'V':
        video_format_label.pack()  # Show video format options when selecting video
        video_format_menu.pack()
        audio_quality_label.pack_forget()  # Hide audio quality options when selecting video
        high_quality_button.pack_forget()
        low_quality_button.pack_forget()
        audio_format_label.pack_forget()  # Hide audio format options when selecting video
        audio_format_menu.pack_forget()

# Initialize the main window
root = tk.Tk()
root.title("Link2Playback")

# Set initial window size
root.geometry("736x414")

# URL entry
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack(pady=(10, 0))  # Added padding on the y-axis, more space at the top
url_entry = tk.Entry(root)
url_entry.pack(pady=(0, 10))  # Added padding on the y-axis, more space at the bottom

# Radio buttons for choice
choice_var = tk.StringVar()
video_button = tk.Radiobutton(root, text="Video", variable=choice_var, value='V', command=toggle_quality_options)
audio_button = tk.Radiobutton(root, text="Audio", variable=choice_var, value='A', command=toggle_quality_options)

audio_button.pack(pady=5)  # Added padding between the buttons
video_button.pack(pady=5)  # Added padding between the buttons

# Label and menu for video format selection
video_format_label = tk.Label(root, text="Select Video Format:")
video_format_label.pack_forget()  # Initially hidden
video_format_var = tk.StringVar(value='mp4')
video_format_menu = tk.OptionMenu(root, video_format_var, 'mp4', 'mov', 'avi', 'wmv', 'webm', 'flv')
video_format_menu.pack_forget()  # Initially hidden

# Label and menu for audio format selection
audio_format_label = tk.Label(root, text="Select Audio Format:")
audio_format_label.pack_forget()  # Initially hidden
audio_format_var = tk.StringVar(value='mp3')
audio_format_menu = tk.OptionMenu(root, audio_format_var, 'mp3', 'mp4', 'wav', 'ogg')
audio_format_menu.pack_forget()  # Initially hidden

# Label and radio buttons for audio quality selection
audio_quality_label = tk.Label(root, text="Select Audio Quality:")
audio_quality_label.pack_forget()  # Initially hidden
quality_var = tk.StringVar(value='high')
high_quality_button = tk.Radiobutton(root, text="High Quality", variable=quality_var, value='high')
low_quality_button = tk.Radiobutton(root, text="Low Quality", variable=quality_var, value='low')
high_quality_button.pack_forget()  # Initially hidden
low_quality_button.pack_forget()  # Initially hidden

# Download button
download_button = tk.Button(root, text="Download", command=download)

# Button to view downloads
view_downloads_metadata_button = tk.Button(root, text="View Download Metadata", command=view_download_metadata)

# Button to view download files (from folders)
view_downloaded_files_button = tk.Button(root, text="View Downloaded Files", command=run_gui)

# Pack buttons to bottom
download_button.pack(side="bottom", pady=(5, 10))  # Added padding at the top and bottom
view_downloads_metadata_button.pack(side="bottom", pady=(5, 10))  # Added padding at the top and bottom
view_downloaded_files_button.pack(side="bottom", pady=(5, 10))  # Added padding at the top and bottom

# Run the application
root.mainloop()
