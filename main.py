import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from pytube.cli import on_progress
import os

def download_video(video_url):
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path="video_downloads")
        result = messagebox.askyesno("Download Complete", f"Downloaded video: {stream.title}. Do you want to download another file?")
        if result:
            entry.delete(0, tk.END)  # Clear the entry field
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading video: {str(e)}")

def download_audio(video_url, quality='high'):
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        if quality == 'high':
            stream = yt.streams.filter(only_audio=True).first()
            quality_tag = 'high_q'
        elif quality == 'low':
            stream = yt.streams.filter(only_audio=True, abr='128kbps').first()
            quality_tag = 'low_q'
        else:
            messagebox.showwarning("Invalid Choice", "Invalid audio quality choice. Downloading in high quality.")
            stream = yt.streams.filter(only_audio=True).first()
            quality_tag = 'high_q'

        audio_file = stream.download(output_path="audio_downloads")
        audio_file_mp3 = audio_file.replace(".mp4", f"_{quality_tag}.mp3")

        if os.path.exists(audio_file_mp3):
            pass  # Do nothing
        else:
            os.rename(audio_file, audio_file_mp3)
        result = messagebox.askyesno("Download Complete", f"Downloaded and converted audio to MP3: {audio_file_mp3}. Do you want to download another file?")
        if result:
            entry.delete(0, tk.END)  # Clear the entry field
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading audio: {str(e)}")

def download():
    video_url = entry.get()
    choice = var.get()
    quality = var_quality.get()

    if choice == 'video':
        download_video(video_url)
    elif choice == 'audio':
        download_audio(video_url, quality)

def show_quality_selection():
    if var.get() == 'audio':
        quality_frame.pack()
    else:
        quality_frame.pack_forget()

root = tk.Tk()
root.title("YouTube Downloader")

# Entry Box
tk.Label(root, text="Enter YouTube video URL:").pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Radio Buttons for Choice (Audio/Video)
var = tk.StringVar()
var.set("video")
tk.Label(root, text="Select download type:").pack()
tk.Radiobutton(root, text="Video", variable=var, value="video", command=show_quality_selection).pack()
tk.Radiobutton(root, text="Audio", variable=var, value="audio", command=show_quality_selection).pack()

# Radio Buttons for Audio Quality
var_quality = tk.StringVar()
var_quality.set("high")
quality_frame = tk.Frame(root)
tk.Label(quality_frame, text="Select audio quality:").pack()
tk.Radiobutton(quality_frame, text="High", variable=var_quality, value="high").pack(side="left")
tk.Radiobutton(quality_frame, text="Low", variable=var_quality, value="low").pack(side="left")

# Download Button
download_button = tk.Button(root, text="Download", command=download)
download_button.pack(side="bottom")

root.mainloop()
