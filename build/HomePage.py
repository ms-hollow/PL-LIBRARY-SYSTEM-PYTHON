import os
import subprocess
from pathlib import Path
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from PIL import Image, ImageTk



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "Homepage"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def gotoAboutUs():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "AboutUS.py")
    subprocess.run(["python", script_path])

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
def gotoRegister():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "Register.py")
    subprocess.run(["python", script_path])

def gotoLogin():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "Login.py")
    subprocess.run(["python", script_path])

window = Tk()

window.geometry("1125x670")
window.configure(bg="#FFFFFF")

# Calculate the center coordinates of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - 1125) // 2
y = (screen_height - 670) // 2

# Set the window position to the center of the screen
window.geometry(f"+{x}+{y}")
window.title("TUP Reads")
image_path = relative_to_assets("TUP_Reads.png")
image = Image.open(image_path)
icon = ImageTk.PhotoImage(image)
window.iconphoto(True, icon)

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

#Sign Up
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
registerBtn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=gotoRegister,
    relief="flat",
    bg = "white"
)

registerBtn.place(x=959.0,y=22.0,width=104.0,height=29.0)

#Contact US
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
Contactbtn = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=gotoContactUs,
    relief="flat",
    bg = "white"
)

Contactbtn.place(x=746.0,y=22.0,width=162.0,height=29.0)

#About US
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
Aboutbtn = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=gotoAboutUs,
    relief="flat",
    bg = "white"
)

Aboutbtn.place(x=560.0,y=22.0,width=143.0,height=32.0)

#Get Started
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
getstartedbtn = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=gotoLogin,
    relief="flat",
    bg = "white"
)
getstartedbtn.place( x=696.0,y=565.0,width=213.0,height=44.0)

#HOME
button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
homebtn = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=gotoHome,
    relief="flat",
    bg = "white"
)

homebtn.place(x=432.0,y=22.0,width=77.0,height=32.0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    134.0,
    71.0,
    image=image_image_1
)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    791.0,
    261.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    789.0,
    301.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    803.0,
    372.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    271.0,
    395.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    801.0,
    506.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    802.0,
    466.0,
    image=image_image_8
)


window.resizable(False, False)
window.mainloop()
