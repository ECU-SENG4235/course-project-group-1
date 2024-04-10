import os
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Toplevel

# Import the relevant functions from main.py
from main import download_audio, download_video

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\kenda\Documents\course-project-group-1\guiPage2\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_guiPage2():
    window = Toplevel()
    window.geometry("1108x506")
    window.configure(bg="#FFFFFF")

    photo_images = []  # Prevents Python garbage collector from breaking assets during quality page opening

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=506,
        width=1108,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Define the functions for button clicks

    # Function for clicking "MP4" button
    def mp4_clicked():
        download_video("mp4")  # Link to relevant function in main.py

    # Function for clicking "Low Quality" button
    def low_quality_clicked():
        download_audio("low")  # Link to relevant function in main.py

    # Function for clicking "Video" button
    def video_clicked():
        download_video("video")  # Link to relevant function in main.py

    # Function for clicking "Audio" button
    def audio_clicked():
        download_audio("audio")  # Link to relevant function in main.py

    # Function for clicking "Both (A&V)" button
    def both_clicked():
        download_audio("both")  # Link to relevant function in main.py

    # Function for clicking "Hi Quality" button
    def hi_quality_clicked():
        download_audio("hi_quality")  # Link to relevant function in main.py

    # Function for clicking "MP3" button
    def mp3_clicked():
        download_audio("mp3")  # Link to relevant function in main.py

    # Function for clicking "WAV" button
    def wav_clicked():
        download_audio("wav")  # Link to relevant function in main.py

    # Function for clicking "WVM" button
    def wvm_clicked():
        download_video("wvm")  # Link to relevant function in main.py

    # Function for clicking "MOV" button
    def mov_clicked():
        download_video("mov")  # Link to relevant function in main.py

    # Function for clicking "WEBM" button
    def webm_clicked():
        download_video("webm")  # Link to relevant function in main.py

    # Create PhotoImage objects for buttons
    image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
    button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
    button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
    button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
    button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
    button_image_12 = PhotoImage(file=relative_to_assets("button_12.png"))
    button_image_13 = PhotoImage(file=relative_to_assets("button_13.png"))

    # Create buttons and link them to relevant functions
    canvas.create_image(554.0, 253.0, image=image_1)
    canvas.create_text(659.0, 127.0, anchor="nw", text="MP4", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))
    canvas.create_text(435.0, 169.0, anchor="nw", text="Low Quality", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))
    canvas.create_text(173.0, 91.0, anchor="nw", text="Format", fill="#000000", font=("KronaOne Regular", 20 * -1))
    canvas.create_text(233.0, 127.0, anchor="nw", text="Video", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))
    canvas.create_text(220.0, 171.0, anchor="nw", text="Audio", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))
    canvas.create_text(220.0, 216.0, anchor="nw", text="Both (A&V)", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))
    canvas.create_text(435.0, 124.0, anchor="nw", text="Hi Quality", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))
    canvas.create_text(404.0, 262.0, anchor="nw", text="Audio Format", fill="#000000", font=("KronaOne Regular", 20 * -1))
    canvas.create_text(645.0, 92.0, anchor="nw", text="Video Format", fill="#000000", font=("KronaOne Regular", 20 * -1))
    canvas.create_text(645.0, 262.0, anchor="nw", text="", fill="#000000", font=("KronaOne Regular", 20 * -1))
    canvas.create_text(659.0, 220.0, anchor="nw", text="AVI", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))
    canvas.create_text(435.0, 299.0, anchor="nw", text="MP3", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))
    canvas.create_text(168.0, 24.0, anchor="nw", text="Media Quality", fill="#000000", font=("K2D Regular", 40 * -1))
    canvas.create_text(435.0, 348.0, anchor="nw", text="WAV", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))
    canvas.create_text(659.0, 299.0, anchor="nw", text="WVM", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))
    canvas.create_text(659.0, 174.0, anchor="nw", text="MOV", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))
    canvas.create_text(659.0, 346.0, anchor="nw", text="WEBM", fill="#000000", font=("JetBrainsMonoRoman Regular", 20 * -1))

    # Download Button (Which just returns you to gui.py within guiPage1)
    button_1 = Button(window, image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("Download clicked"), relief="flat")
    button_1.place(x=842.0, y=227.0, width=135.0, height=72.0)

    # 480p video quality button
    button_2 = Button(window, image=button_image_2, borderwidth=0, highlightthickness=0, command=video_clicked, relief="flat")
    button_2.place(x=190.0, y=123.0, width=30.0, height=31.0)

    # 720p button
    button_3 = Button(window, image=button_image_3, borderwidth=0, highlightthickness=0, command=video_clicked, relief="flat")
    button_3.place(x=190.0, y=167.0, width=30.0, height=31.0)

    # 1080p button clicked
    button_4 = Button(window, image=button_image_4, borderwidth=0, highlightthickness=0, command=video_clicked, relief="flat")
    button_4.place(x=190.0, y=213.0, width=30.0, height=31.0)

    # Mono button clicked
    button_5 = Button(window, image=button_image_5, borderwidth=0, highlightthickness=0, command=audio_clicked, relief="flat")
    button_5.place(x=405.0, y=121.0, width=30.0, height=31.0)

    # Stereo button
    button_6 = Button(window, image=button_image_6, borderwidth=0, highlightthickness=0, command=audio_clicked, relief="flat")
    button_6.place(x=405.0, y=168.0, width=30.0, height=31.0)

    # 16 bit button
    button_7 = Button(window, image=button_image_7, borderwidth=0, highlightthickness=0, command=bit_16_clicked, relief="flat")
    button_7.place(x=405.0, y=296.0, width=30.0, height=31.0)

    # 24 bit button
    button_8 = Button(window, image=button_image_8, borderwidth=0, highlightthickness=0, command=bit_24_clicked, relief="flat")
    button_8.place(x=405.0, y=345.0, width=30.0, height=31.0)

    # WAV File format button
    button_9 = Button(window, image=button_image_9, borderwidth=0, highlightthickness=0, command=wav_clicked, relief="flat")
    button_9.place(x=629.0, y=296.0, width=30.0, height=31.0)

    # Video as Download choice
    button_10 = Button(window, image=button_image_10, borderwidth=0, highlightthickness=0, command=mp4_clicked, relief="flat")
    button_10.place(x=629.0, y=124.0, width=30.0, height=31.0)

    # MP3 File Format
    button_11 = Button(window, image=button_image_11, borderwidth=0, highlightthickness=0, command=mp3_clicked, relief="flat")
    button_11.place(x=629.0, y=343.0, width=30.0, height=31.0)

    # Download Only Audio
    button_12 = Button(window, image=button_image_12, borderwidth=0, highlightthickness=0, command=audio_only_clicked, relief="flat")
    button_12.place(x=629.0, y=171.0, width=30.0, height=31.0)

    # Download both audio and video
    button_13 = Button(window, image=button_image_13, borderwidth=0, highlightthickness=0, command=both_clicked, relief="flat")
    button_13.place(x=629.0, y=217.0, width=30.0, height=31.0)

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    open_guiPage2()
