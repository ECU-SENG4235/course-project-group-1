import tkinter as tk
from tkinter import ttk, messagebox, colorchooser, scrolledtext
from main import download_video, download_audio, batch_download
import subprocess
from ttkbootstrap import Style

def download():
    if mode_var.get() == "Single":
        video_url = url_entry.get()
        process_single_download(video_url)
    elif mode_var.get() == "Batch":
        video_urls_text = url_text.get("1.0", tk.END)  # Get the text from the widget
        process_batch_download(video_urls_text)  # Pass the text to the function


def process_single_download(video_url):
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

def process_batch_download(video_urls_text):
    video_urls = video_urls_text.split(',')
    video_urls = [url.strip() for url in video_urls if url.strip()]  # Filter out empty URLs
    if not video_urls:
        messagebox.showerror("Error", "No URLs provided for batch download.")
        return

    choice = choice_var.get()
    if choice == 'A':
        audio_format = audio_format_var.get()
        audio_quality = quality_var.get()
        batch_download(video_urls, 'a', audio_format, audio_quality)
    elif choice == 'V':
        video_format = video_format_var.get()
        batch_download(video_urls, 'v', video_format)
    else:
        messagebox.showerror("Error", "Invalid choice. Please select either Audio or Video.")


def toggle_download_mode():
    if mode_var.get() == "Single":
        url_entry.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")  # Reduced top padding
        url_text.grid_forget()
    else:
        url_entry.grid_forget()
        url_text.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew", columnspan=2)  # Reduced top padding

def run_playlist_script():
    subprocess.Popen(["python", "playlist.py"])

def change_color():
    color = colorchooser.askcolor(title="Choose color")
    if color[1]:  # Check if a color was chosen
        root.configure(bg=color[1])  # Change window background color
        nav_frame.configure(bg=color[1])  # Change navigation bar background color

def run():
    global root
    root = tk.Tk()
    root.title("Link2Playback")
    root.geometry("900x250")

    # Apply ttkbootstrap style with a different theme
    style = Style(theme='solar')

    # Left Side Navigation Bar
    global nav_frame
    nav_frame = tk.Frame(root)
    nav_frame.grid(row=0, column=0, sticky="nswe")
    nav_frame.grid_columnconfigure(0, weight=1)  # Make the navigation bar expandable horizontally

    # Buttons in the Navigation Bar
    download_button = ttk.Button(nav_frame, text="Download", command=download, style='success.Outline.TButton')
    download_button.pack(pady=10)

    playlist_button = ttk.Button(nav_frame, text="Playlist", command=run_playlist_script, style='primary.Outline.TButton')
    playlist_button.pack(pady=10)

    # Create a button to change color
    color_button = ttk.Button(nav_frame, text="Change Color", command=change_color, style='warning.Outline.TButton')
    color_button.pack(side="bottom", pady=10, padx=10)

    # Right Side Frame for URL, Format, and Quality Options
    options_frame = tk.Frame(root)
    options_frame.grid(row=0, column=1, padx=20, sticky="nswe")
    options_frame.grid_rowconfigure(0, weight=1)  # Make the options frame expandable vertically

    global mode_var
    mode_var = tk.StringVar(value="Single")
    single_mode_button = tk.Radiobutton(options_frame, text="Single URL", variable=mode_var, value='Single', command=toggle_download_mode)
    batch_mode_button = tk.Radiobutton(options_frame, text="Batch URLs", variable=mode_var, value='Batch', command=toggle_download_mode)
    single_mode_button.grid(row=0, column=0, sticky="w", padx=10, pady=(5, 2))  # Reduced bottom padding
    batch_mode_button.grid(row=0, column=1, sticky="w", padx=10, pady=(5, 2))  # Reduced bottom padding

    url_label = tk.Label(options_frame, text="YouTube URL:")
    url_label.grid(row=1, column=0, sticky="w", pady=(10, 0))
    global url_entry
    url_entry = tk.Entry(options_frame)
    url_entry.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="ew")

    global url_text
    url_text = scrolledtext.ScrolledText(options_frame, height=4)
    toggle_download_mode()

    global choice_var, video_format_var, audio_format_var, quality_var
    choice_var = tk.StringVar(value='V')
    video_button = tk.Radiobutton(options_frame, text="Video", variable=choice_var, value='V')
    audio_button = tk.Radiobutton(options_frame, text="Audio", variable=choice_var, value='A')
    video_button.grid(row=3, column=0, sticky="w", padx=10, pady=(2, 2))  # Reduced top and bottom padding

    video_format_label = tk.Label(options_frame, text="Select Video Format:")
    video_format_var = tk.StringVar(value='mp4')
    video_format_menu = tk.OptionMenu(options_frame, video_format_var, 'mp4', 'mov', 'avi', 'wmv', 'webm', 'flv')
    video_format_label.grid(row=4, column=0, sticky="w", padx=10, pady=(2, 2))  # Reduced top and bottom padding
    video_format_menu.grid(row=4, column=1, sticky="w", padx=10, pady=(2, 2))  # Reduced top and bottom padding

    audio_button.grid(row=5, column=0, sticky="w", padx=10, pady=(2, 2))  # Reduced top and bottom padding

    audio_format_label = tk.Label(options_frame, text="Select Audio Format:")
    audio_format_var = tk.StringVar(value='mp3')
    audio_format_menu = tk.OptionMenu(options_frame, audio_format_var, 'mp3', 'mp4', 'wav', 'ogg')
    audio_format_label.grid(row=6, column=0, sticky="w", padx=10, pady=(2, 2))  # Reduced top and bottom padding
    audio_format_menu.grid(row=6, column=1, sticky="w", padx=10, pady=(2, 2))  # Reduced top and bottom padding

    audio_quality_label = tk.Label(options_frame, text="Select Audio Quality:")
    quality_var = tk.StringVar(value='High')
    high_quality_button = tk.Radiobutton(options_frame, text="High", variable=quality_var, value='High')
    low_quality_button = tk.Radiobutton(options_frame, text="Low", variable=quality_var, value='Low')
    audio_quality_label.grid(row=7, column=0, sticky="w", padx=10, pady=(2, 5))  # Reduced top padding
    high_quality_button.grid(row=7, column=1, sticky="w", padx=10, pady=(2, 2))  # Reduced top and bottom padding
    low_quality_button.grid(row=7, column=2, sticky="w", padx=10, pady=(2, 5))  # Reduced top padding

    # Configure row and column weights to make the navigation bar and options frame expandable
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    run()          