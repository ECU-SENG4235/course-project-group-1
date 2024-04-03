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
        audio_quality_label.grid(row=3, column=1, sticky="w")
        high_quality_button.grid(row=4, column=1, sticky="w")
        low_quality_button.grid(row=5, column=1, sticky="w")
        audio_format_label.grid(row=6, column=1, sticky="w")
        audio_format_menu.grid(row=7, column=1, sticky="w")
        video_format_label.grid_forget()
        video_format_menu.grid_forget()
    elif choice_var.get() == 'V':
        video_format_label.grid(row=3, column=1, sticky="w")
        video_format_menu.grid(row=4, column=1, sticky="w")
        audio_quality_label.grid_forget()
        high_quality_button.grid_forget()
        low_quality_button.grid_forget()
        audio_format_label.grid_forget()
        audio_format_menu.grid_forget()

def change_theme(theme):
    root.configure(bg=theme_colors[theme]['bg'])
    url_label.configure(fg=theme_colors[theme]['fg'])
    theme_label.configure(fg=theme_colors[theme]['fg'])
    nav_frame.configure(bg=theme_colors[theme]['nav_bg'])
    # Add more widget-specific styling if needed

def run():
    global root
    root = tk.Tk()
    root.title("Link2Playback")
    root.geometry("900x500")

    # Left Side Navigation Bar
    nav_frame = tk.Frame(root, width=300, height=500, bg="#202020")
    nav_frame.grid(row=0, column=0, rowspan=10, sticky="nswe")

    # Buttons in the Navigation Bar
    download_button = tk.Button(nav_frame, text="Download", command=download)
    download_button.pack(pady=10)
    view_downloads_metadata_button = tk.Button(nav_frame, text="View Download Metadata", command=view_download_metadata)
    view_downloads_metadata_button.pack(pady=10)
    view_downloaded_files_button = tk.Button(nav_frame, text="View Downloaded Files", command=download_files)
    view_downloaded_files_button.pack(pady=10)

    # Right Side Frame for URL, Format, and Quality Options
    options_frame = tk.Frame(root)
    options_frame.grid(row=0, column=1, padx=20)

    url_label = tk.Label(options_frame, text="YouTube URL:")
    url_label.grid(row=0, column=0, sticky="w", pady=(10, 0))
    global url_entry
    url_entry = tk.Entry(options_frame)
    url_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

    global choice_var
    choice_var = tk.StringVar()
    video_button = tk.Radiobutton(options_frame, text="Video", variable=choice_var, value='V', command=toggle_quality_options)
    audio_button = tk.Radiobutton(options_frame, text="Audio", variable=choice_var, value='A', command=toggle_quality_options)
    audio_button.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    video_button.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    # Quality Options
    global video_format_label, video_format_menu
    video_format_label = tk.Label(options_frame, text="Select Video Format:")
    video_format_var = tk.StringVar(value='mp4')
    video_format_menu = tk.OptionMenu(options_frame, video_format_var, 'mp4', 'mov', 'avi', 'wmv', 'webm', 'flv')

    global audio_format_label, audio_format_menu
    audio_format_label = tk.Label(options_frame, text="Select Audio Format:")
    audio_format_var = tk.StringVar(value='mp3')
    audio_format_menu = tk.OptionMenu(options_frame, audio_format_var, 'mp3', 'mp4', 'wav', 'ogg')

    global audio_quality_label, quality_var, high_quality_button, low_quality_button
    audio_quality_label = tk.Label(options_frame, text="Select Audio Quality:")
    quality_var = tk.StringVar(value='high')
    high_quality_button = tk.Radiobutton(options_frame, text="High Quality", variable=quality_var, value='high')
    low_quality_button = tk.Radiobutton(options_frame, text="Low Quality", variable=quality_var, value='low')

    # Theme Selection
    theme_label = tk.Label(root, text="Select Theme:")
    theme_label.grid(row=9, column=0, sticky="w", padx=20, pady=10)
    theme_var = tk.StringVar(value='light')
    themes = ['light', 'dark', 'green', 'blue', 'red']
    theme_radiobuttons = []
    for idx, theme in enumerate(themes):
        theme_radiobuttons.append(tk.Radiobutton(root, text=theme.capitalize(), variable=theme_var, value=theme, command=lambda theme=theme: change_theme(theme)))
        theme_radiobuttons[-1].grid(row=9, column=1+idx, sticky="w", padx=10, pady=10)

    toggle_quality_options()  # To initialize the quality options based on the default choice

    root.mainloop()

# Theme Colors
theme_colors = {
    'light': {'bg': 'white', 'fg': 'black', 'nav_bg': '#ccc'},
    'dark': {'bg': '#333', 'fg': 'white', 'nav_bg': '#666'},
    'green': {'bg': '#7FFF00', 'fg': 'black', 'nav_bg': '#00CC00'},
    'blue': {'bg': '#4682B4', 'fg': 'white', 'nav_bg': '#1E90FF'},
    'red': {'bg': '#FF6347', 'fg': 'white', 'nav_bg': '#FF4500'}
}

if __name__ == "__main__":
    run()
