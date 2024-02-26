import tkinter as tk
from tkinter import messagebox
from main import download_video, download_audio

def download():
    video_url = url_entry.get()
    choice = choice_var.get()
    quality = quality_var.get()
    if choice == 'A':
        download_audio(video_url, quality)
    elif choice == 'V':
        download_video(video_url)
    else:
        messagebox.showerror("Error", "Invalid choice. Please select either Audio or Video.")

# Initialize the main window
root = tk.Tk()
root.title("YouTube Downloader")

# Set initial window size
root.geometry("736x414")

# URL entry
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

# Radio buttons for choice
choice_var = tk.StringVar()
video_button = tk.Radiobutton(root, text="Video", variable=choice_var, value='V')
audio_button = tk.Radiobutton(root, text="Audio", variable=choice_var, value='A')

audio_button.pack()
video_button.pack()

# Radio buttons for quality
quality_var = tk.StringVar(value='high')
high_quality_button = tk.Radiobutton(root, text="High Quality", variable=quality_var, value='high')
low_quality_button = tk.Radiobutton(root, text="Low Quality", variable=quality_var, value='low')
high_quality_button.pack()
low_quality_button.pack()

# Download button
download_button = tk.Button(root, text="Download", command=download)
download_button.pack()

# Close button with round edges (example styling, adjust as needed)
#close_button = tk.Button(root, text="X", command=root.destroy)
#close_button.pack()

# Run the application
root.mainloop()
