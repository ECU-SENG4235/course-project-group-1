# Import necessary libraries
from tkinter import Tk, Canvas, Text, Entry, Button, PhotoImage
from PIL import Image, ImageTk
import io
from pathlib import Path

# Function to convert white pixels in an image to transparent
def make_white_transparent(image_path):
    img = Image.open(image_path).convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] > 220 and item[1] > 220 and item[2] > 220:
            newData.append((255, 255, 255, 0))  # Making the pixel fully transparent
        else:
            newData.append(item)

    img.putdata(newData)
    # Save to a bytes buffer
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return ImageTk.PhotoImage(Image.open(buffer))

# Path to your assets
ASSETS_PATH = Path(__file__).parent / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path

# Initialize the window
window = Tk()
window.geometry("1108x506")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg="#FFFFFF", height=506, width=1108, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# Load images and apply transparency conversion
image_1_path = relative_to_assets("image_1.png")
image_1 = make_white_transparent(image_1_path)
canvas.create_image(554.0, 253.0, image=image_1)

entry_image_1_path = relative_to_assets("entry_1.png")
entry_image_1 = make_white_transparent(entry_image_1_path)
entry_bg_1 = canvas.create_image(551.5, 304.5, image=entry_image_1)

entry_1 = Text(bd=0, bg="#EDECEC", highlightthickness=0)
entry_1.place(x=201.0, y=243.0, width=701.0, height=121.0)

entry_image_2_path = relative_to_assets("entry_2.png")
entry_image_2 = make_white_transparent(entry_image_2_path)
entry_bg_2 = canvas.create_image(524.5, 202.5, image=entry_image_2)

entry_2 = Entry(bd=0, bg="#FFFFFF", highlightthickness=0)
entry_2.place(x=231.0, y=175.0, width=587.0, height=53.0)

canvas.create_text(415.0, 16.0, anchor="nw", text="Your GUI Title", fill="#000000", font=("Roboto", 40 * -1))

button_image_1_path = relative_to_assets("button_1.png")
button_image_1 = make_white_transparent(button_image_1_path)
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, relief="flat")
button_1.place(x=842.0, y=175.0, width=145.0, height=68.0)

button_image_2_path = relative_to_assets("button_2.png")
button_image_2 = make_white_transparent(button_image_2_path)
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, relief="flat")
button_2.place(x=604.0, y=378.0, width=145.0, height=70.0)

button_image_3_path = relative_to_assets("button_3.png")
button_image_3 = make_white_transparent(button_image_3_path)
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, relief="flat")
button_3.place(x=316.0, y=378.0, width=145.0, height=70.0)

window.resizable(False, False)
window.mainloop()
