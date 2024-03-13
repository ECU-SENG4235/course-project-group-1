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

# Initialize the main window
root = tk.Tk()
root.title("Link2Playback")

#rounded edges
def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)



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

# Button to view downloads
view_downloads_button = tk.Button(root, text="View Downloads", command=view_downloads)
view_downloads_button.pack()


# Run the application
root.mainloop()
