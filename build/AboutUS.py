import os
import subprocess
from pathlib import Path
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "AboutUs"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def gotoHome():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "HomePage.py")
    subprocess.run(["python", script_path])

def gotoContactUs():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "ContactUs.py")
    subprocess.run(["python", script_path])
def gotoAboutUs():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "AboutUS.py")
    subprocess.run(["python", script_path])
def gotoRegister():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "Register.py")
    subprocess.run(["python", script_path])

window = Tk()

window.geometry("1125x670")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 670,
    width = 1125,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

#Signup
button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
registerbtn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=gotoRegister,
    relief="flat",
    bg = "white"
)
registerbtn.place(
    x=959.0,
    y=22.0,
    width=104.0,
    height=29.0
)
#Contact Us
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
Contactbtn = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=gotoContactUs,
    relief="flat",
    bg = "white"
)
Contactbtn.place(
    x=746.0,
    y=22.0,
    width=162.0,
    height=29.0
)

#About us
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
Aboutbtn = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=gotoAboutUs,
    relief="flat",
    bg = "white"
)

Aboutbtn.place(
    x=560.0,
    y=22.0,
    width=143.0,
    height=32.0
)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
homebtn = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command= gotoHome,
    relief="flat",
    bg = "white"
)
homebtn.place(
    x=432.0,
    y=22.0,
    width=77.0,
    height=32.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    101.0,
    56.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    560.0,
    214.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    101.0,
    56.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    558.0,
    254.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    562.0,
    487.0,
    image=image_image_5
)


window.resizable(False, False)
window.mainloop()
