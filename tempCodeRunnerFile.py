from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Radiobutton, ttk, messagebox, scrolledtext
from tkinter import StringVar
from pathlib import Path
from main import download_video, download_audio, batch_download
import subprocess

# Set the asset path
ASSETS_PATH = Path(__file__).parent / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path

# GUI setup
window = Tk()
window.title("Link2Playback")
window.geometry("728x407")  # Adjusted size to be about 50% smaller
window.configure(bg="#FFFFFF")

# Now we can safely create StringVar instances
mode_var = StringVar(value="Single")
choice_var = StringVar(value='V')  # Default choice set to Video
video_format_var = StringVar(value='mp4')
audio_format_var = StringVar(value='mp3')
quality_var = StringVar(value='High')

# Function to process the downloads
def download():
    mode = mode_var.get()
    choice = choice_var.get()
    if mode == "Single":
        video_url = url_entry.get()
        if choice == 'A':
            download_audio(video_url, audio_format_var.get(), quality_var.get())
        elif choice == 'V':
            download_video(video_url, video_format_var.get())
    elif mode == "Batch":
        video_urls_text = url_text.get("1.0", "end-1c")
        process_batch_download(video_urls_text)

def process_batch_download(video_urls_text):
    video_urls = [url.strip() for url in video_urls_text.split(',') if url.strip()]
    if not video_urls:
        messagebox.showerror("Error", "No URLs provided for batch download.")
        return
    if choice_var.get() == 'A':
        batch_download(video_urls, 'a', audio_format_var.get(), quality_var.get())
    elif choice_var.get() == 'V':
        batch_download(video_urls, 'v', video_format_var.get())

# Toggle between Single and Batch URL modes
def toggle_download_mode():
    if mode_var.get() == "Single":
        url_entry.place(x=185.0, y=63.0, width=439.0, height=124.0)
        url_text.place_forget()
    else:
        url_text.place(x=185.0, y=63.0, width=439.0, height=124.0)
        url_entry.place_forget()

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=407,
    width=728,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Image as background
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(364.0, 203.5, image=image_image_1)

# Buttons and Entry widgets
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
playlist_button = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen(["python", "playlist.py"]), relief="flat")
playlist_button.place(x=22.5, y=143.0, width=131.0, height=45.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
download_button = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=download, relief="flat")
download_button.place(x=22.5, y=63.0, width=131.0, height=45.0)

# Radio buttons for mode and type selection
single_mode_button = Radiobutton(window, text="Single URL", variable=mode_var, value='Single', command=toggle_download_mode)
single_mode_button.place(x=194.0, y=204.0, width=60.0, height=12.5)
video_mode_button = Radiobutton(window, text="Video Only", variable=choice_var, value='V')
video_mode_button.place(x=194.0, y=219.0, width=60.0, height=12.5)

batch_mode_button = Radiobutton(window, text="Batch URLs", variable=mode_var, value='Batch', command=toggle_download_mode)
batch_mode_button.place(x=435.5, y=204.0, width=60.0, height=12.5)
audio_mode_button = Radiobutton(window, text="Audio Only", variable=choice_var, value='A')
audio_mode_button.place(x=435.5, y=219.0, width=60.0, height=12.5)

# Entry for Single URL and Text for Batch URLs
url_entry = Entry(window, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
url_text = scrolledtext.ScrolledText(window, height=2)
toggle_download_mode()  # Initially set to single URL mode

# Dropdowns for formats
video_format_menu = ttk.OptionMenu(window, video_format_var, 'mp4', 'mp4', 'mov', 'avi', 'wmv', 'webm', 'flv')
video_format_menu.place(x=305.5, y=279.0, width=65.5, height=17.0)

audio_format_menu = ttk.OptionMenu(window, audio_format_var, 'mp3', 'mp3', 'mp4', 'wav', 'ogg')
audio_format_menu.place(x=544.0, y=281.0, width=65.5, height=17.0)

# Radio buttons for Audio Quality
high_quality_button = Radiobutton(window, text="High", variable=quality_var, value='High')
high_quality_button.place(x=550.0, y=317.5, width=25.0, height=12.5)
low_quality_button = Radiobutton(window, text="Low", variable=quality_var, value='Low')
low_quality_button.place(x=550.0, y=343.0, width=25.0, height=12.5)

window.resizable(False, False)
window.mainloop()
