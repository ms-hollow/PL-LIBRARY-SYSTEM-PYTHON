import os
import subprocess
from pathlib import Path
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font, Toplevel, OptionMenu, Menu, StringVar
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "ChangePassword"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def gotoHome():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "HomePage.py")
    subprocess.run(["python", script_path])
def gotoLogin():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "Login.py")
    subprocess.run(["python", script_path])

def gotoChangePass():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "ChangePassword.py")
    subprocess.run(["python", script_path])
def Student_dropdownMenu():
    # Create a dropdown menu
    dropdown_menu = Menu(window, tearoff=False, font=("Poppins", 10, "bold"))  # Set custom font and size
    dropdown_menu.configure(bg="#C19A6B", fg="#4B0000")  # Set background and foreground colors

    # List of options for the dropdown menu
    options = ["Log out", "Change Password"]  # Add your options here

    # Function to be executed when an option is selected from the dropdown
    def on_option_selected(option):
        if option == "Log out":
            gotoLogin()
        elif option == "Change Password":
            gotoChangePass()
        else:
            print("Selected Option:", option)

    # Add options to the dropdown menu
    for option in options:
        dropdown_menu.add_command(label=option, command=lambda opt=option: on_option_selected(opt))

    # Display the dropdown menu under the image_5 button
    dropdown_menu.post(logoutbtn.winfo_rootx(), logoutbtn.winfo_rooty() + logoutbtn.winfo_height())

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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    562.0,
    383.0,
    image=image_image_1
)
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    125.0,
    66.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    247.0,
    372.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(773.0,395.0,image=entry_image_1)
newpassword = Entry(bd=0,bg="#FFFDFD",fg="#000716",highlightthickness=0)
newpassword.place(
    x=550.0,
    y=375.0,
    width=446.0,
    height=33.0
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(775.0,494.0,image=entry_image_2)
reenterpass = Entry(bd=0,bg="#FFFDFD",fg="#000716",highlightthickness=0)
reenterpass.place(
    x=552.0,
    y=474.0,
    width=446.0,
    height=33.0
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(773.0,286.0,image=entry_image_3)
currentpass = Entry(bd=0,bg="#FFFDFD",fg="#000716",highlightthickness=0)
currentpass.place(
    x=550.0,
    y=266.0,
    width=446.0,
    height=33.0
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
changepassbtn = Button(image=button_image_1,borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg = "white"
)
changepassbtn.place(
    x=647.0,
    y=541.0,
    width=268.0,
    height=44.0
)

button_image_2 = PhotoImage(
file=relative_to_assets("button_2.png"))
notifbtn = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg = "white"
)
notifbtn.place(
    x=994.0,
    y=31.0,
    width=38.0,
    height=43.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
homebtn = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=gotoHome,
    relief="flat",
    bg = "white"
)
homebtn.place(
    x=925.0,
    y=32.0,
    width=42.0,
    height=42.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
logoutbtn = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=Student_dropdownMenu,
    relief="flat",
    bg = "white"
)
logoutbtn.place(
    x=1055.0,
    y=31.0,
    width=43.0,
    height=43.0
)

window.resizable(False, False)
window.mainloop()
