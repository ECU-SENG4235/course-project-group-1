import tkinter as tk
from tkinter import messagebox
from mainwithformat import download_video, download_audio
from view_downloads import display_sections
from downloadlist import run_gui

def download():
    video_url = url_entry.get()
    choice = choice_var.get()
    if choice == 'A':
        audio_format = audio_format_var.get()  
        audio_quality = quality_var.get()  
        download_audio(video_url, audio_format, audio_quality)  
    elif choice == 'V':
        video_format = video_format_var.get()  
        download_video(video_url, video_format)
    else:
        messagebox.showerror("Error", "Invalid choice. Please select either Audio or Video.")

def view_download_metadata():
    display_sections()  

def download_files():
    run_gui()

def toggle_quality_options():
    if choice_var.get() == 'A':
        audio_quality_label.pack()
        high_quality_button.pack()
        low_quality_button.pack()
        audio_format_label.pack()  
        audio_format_menu.pack()
        video_format_label.pack_forget()  
        video_format_menu.pack_forget()
    elif choice_var.get() == 'V':
        video_format_label.pack()  
        video_format_menu.pack()
        audio_quality_label.pack_forget()  
        high_quality_button.pack_forget()
        low_quality_button.pack_forget()
        audio_format_label.pack_forget()  
        audio_format_menu.pack_forget()

def run():
    root = tk.Tk()
    root.title("Link2Playback")
    root.geometry("736x414")

    url_label = tk.Label(root, text="YouTube URL:")
    url_label.pack(pady=(10, 0))  
    global url_entry
    url_entry = tk.Entry(root)
    url_entry.pack(pady=(0, 10))  

    global choice_var
    choice_var = tk.StringVar()
    video_button = tk.Radiobutton(root, text="Video", variable=choice_var, value='V', command=toggle_quality_options)
    audio_button = tk.Radiobutton(root, text="Audio", variable=choice_var, value='A', command=toggle_quality_options)

    audio_button.pack(pady=5)  
    video_button.pack(pady=5)  

    global video_format_label, video_format_menu
    video_format_label = tk.Label(root, text="Select Video Format:")
    video_format_label.pack_forget()  
    global video_format_var
    video_format_var = tk.StringVar(value='mp4')
    video_format_menu = tk.OptionMenu(root, video_format_var, 'mp4', 'mov', 'avi', 'wmv', 'webm', 'flv')
    video_format_menu.pack_forget()  

    global audio_format_label, audio_format_menu
    audio_format_label = tk.Label(root, text="Select Audio Format:")
    audio_format_label.pack_forget()  
    global audio_format_var
    audio_format_var = tk.StringVar(value='mp3')
    audio_format_menu = tk.OptionMenu(root, audio_format_var, 'mp3', 'mp4', 'wav', 'ogg')
    audio_format_menu.pack_forget()  

    global audio_quality_label, quality_var, high_quality_button, low_quality_button
    audio_quality_label = tk.Label(root, text="Select Audio Quality:")
    audio_quality_label.pack_forget()  
    quality_var = tk.StringVar(value='high')
    high_quality_button = tk.Radiobutton(root, text="High Quality", variable=quality_var, value='high')
    low_quality_button = tk.Radiobutton(root, text="Low Quality", variable=quality_var, value='low')
    high_quality_button.pack_forget()  
    low_quality_button.pack_forget()  

    download_button = tk.Button(root, text="Download", command=download)
    view_downloads_metadata_button = tk.Button(root, text="View Download Metadata", command=view_download_metadata)
    view_downloaded_files_button = tk.Button(root, text="View Downloaded Files", command=download_files)

    download_button.pack(side="bottom", pady=(5, 10))  
    view_downloads_metadata_button.pack(side="bottom", pady=(5, 10))  
    view_downloaded_files_button.pack(side="bottom", pady=(5, 10))  

    root.mainloop()

if __name__ == "__main__":
    run()
