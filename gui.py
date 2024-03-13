import tkinter as tk
from tkinter import messagebox
from main import download_video, download_audio
from view_downloads import display_sections

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

def view_downloads():
    display_sections()  # Call the function to display sections

def toggle_quality_options():
    if choice_var.get() == 'A':
        high_quality_button.pack()
        low_quality_button.pack()
    else:
        high_quality_button.pack_forget()
        low_quality_button.pack_forget()

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

# Radio buttons for quality
quality_var = tk.StringVar(value='high')
high_quality_button = tk.Radiobutton(root, text="High Quality", variable=quality_var, value='high')
low_quality_button = tk.Radiobutton(root, text="Low Quality", variable=quality_var, value='low')

# Download button
download_button = tk.Button(root, text="Download", command=download)

# Button to view downloads
view_downloads_button = tk.Button(root, text="View Downloads", command=view_downloads)

# Pack buttons to bottom
download_button.pack(side="bottom", pady=(5, 10))  # Added padding at the top and bottom
view_downloads_button.pack(side="bottom", pady=(5, 10))  # Added padding at the top and bottom

# Run the application
root.mainloop()
