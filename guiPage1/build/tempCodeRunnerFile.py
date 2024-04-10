import os
import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))  # Adding parent directory to sys path
from main import handle_gui_interaction

# Import guiPage2's tkinter code here
from guiPage2.build.gui import open_guiPage2

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\kenda\Documents\course-project-group-1\guiPage1\build\assets\frame0") 

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def search_button_clicked():
    video_url = entry_2.get()
    handle_gui_interaction(video_url, 'v')

def quality_button_clicked():
    video_url = entry_2.get()
    quality = 'high'  # You can add functionality to select quality in the GUI
    handle_gui_interaction(video_url, 'a', quality)
    
    # Open guiPage2 when quality button is clicked
    open_guiPage2()

def download_button_clicked():
    video_url = entry_2.get()
    handle_gui_interaction(video_url, 'v')

window = Tk()

window.geometry("1108x506")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 506,
    width = 1108,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    554.0,
    253.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    551.5,
    304.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#EDECEC",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=201.0,
    y=243.0,
    width=701.0,
    height=121.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    524.5,
    202.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=231.0,
    y=175.0,
    width=587.0,
    height=53.0
)

canvas.create_text(
    415.0,
    16.0,
    anchor="nw",
    text="Link2Playback",
    fill="#000000",
    font=("K2D Regular", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=search_button_clicked,  # Command linked to search_button_clicked function
    relief="flat"
)
button_1.place(
    x=842.0,
    y=175.0,
    width=145.0,
    height=68.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=quality_button_clicked,  # Command linked to quality_button_clicked function
    relief="flat"
)
button_2.place(
    x=604.0,
    y=378.0,
    width=145.0,
    height=70.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=download_button_clicked,  # Command linked to download_button_clicked function
    relief="flat"
)
button_3.place(
    x=316.0,
    y=378.0,
    width=145.0,
    height=70.0
)

window.resizable(False, False)
window.mainloop()