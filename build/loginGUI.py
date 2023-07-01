import os
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, font
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "LoginFrame"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1125x670")

# Calculate the center coordinates of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - 1125) // 2
y = (screen_height - 670) // 2

# Set the window position to the center of the screen
window.geometry(f"+{x}+{y}")

window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=670,
    width=1125,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
# Rectangle crimson
canvas.place(x=0, y=0)
canvas.create_rectangle(0.0, 499.0, 1125.0, 670.0, fill="#4B0000", outline="")

# Load the image
image_path = relative_to_assets("image_4.png")
image = Image.open(image_path)

# Define the desired maximum width and height for the image
max_width = 432
max_height = 464

# Resize the image while preserving its aspect ratio
image.thumbnail((max_width, max_height), Image.LANCZOS)

# Convert the resized image to PhotoImage
photo = ImageTk.PhotoImage(image)

# Create the image on the canvas
image_4 = canvas.create_image(563.0, 345.0, image=photo)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(170, 396, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(900.0, 480.0, image=image_image_2)

canvas.create_text(457.0, 146.0, anchor="nw", text="WELCOME ", fill="#4B0000",
                   font=font.Font(family="Poppins", size=30, weight="bold"))
canvas.create_text(372.0, 234.0, anchor="nw", text="Username ", fill="#4B0000",
                   font=font.Font(family="Poppins", size=20, weight="bold"))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(552.0, 296.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#FFFDFD", fg="#000716", highlightthickness=0,
                font=font.Font(family="Poppins", size=15, weight="normal"))
entry_1.place(x=383.0, y=276.0, width=338.0, height=35.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(552.0, 403.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#FFFDFD", fg="#000716", highlightthickness=0,
                font=font.Font(family="Poppins", size=18, weight="bold"), show="*")
entry_2.place(x=383.0, y=383.0, width=338.0, height=35.0)

canvas.create_text(372.0, 341.0, anchor="nw", text="Password", fill="#4B0000",
                   font=font.Font(family="Poppins", size=20, weight="bold"))

# SIGN UP
'''#
def gotoSignup():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "studentDispBookFrame.py")
    subprocess.run(["python", script_path])
'''
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=959.0,
    y=22.0,
    width=104.0,
    height=29.0
)

# Home Button
'''#
def gotoHome():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "studentDispBookFrame.py")
    subprocess.run(["python", script_path])
'''
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,
                  borderwidth=0,
                  highlightthickness=0,
                  command=lambda: print("button_2 clicked"),
                  relief="flat"
                  )

button_2.place(x=432.0, y=22.0, width=77.0, height=32.0)

# Contact Us
'''#
def gotoContactus():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "studentDispBookFrame.py")
    subprocess.run(["python", script_path])
'''
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(x=746.0, y=22.0, width=162.0, height=29.0)

# About Us Button
'''#
def gotoAboutus():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "studentDispBookFrame.py")
    subprocess.run(["python", script_path])
'''
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(x=560.0, y=22.0, width=143.0, height=32.0)

# LOGIN BUTTON
def gotoStudentPortal():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "studentDispBookFrame.py")
    subprocess.run(["python", script_path])

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=gotoStudentPortal,
    relief="flat",
)
button_5.place(x=487.0, y=481.0, width=150.0, height=44.0)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(101.0, 56.0, image=image_image_3)
window.resizable(False, False)
window.mainloop()
