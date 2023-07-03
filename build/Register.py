import os
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, font
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "RegisterFrame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def register():
    name_value = name.get()
    tupid_value = tupid.get()
    password_value = password.get()
    reenterpass_value = reenterpass.get()
    contactnum_value = contactnum.get()
    email_value = email.get()

    # Process the entered values as needed
    print("Name:", name_value)
    print("TUP ID:", tupid_value)
    print("Password:", password_value)
    print("Re-enter Password:", reenterpass_value)
    print("Contact Number:", contactnum_value)
    print("Email:", email_value)

    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "Login.py")
    subprocess.run(["python", script_path])

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

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    499.0,
    1125.0,
    670.0,
    fill="#C19A6B",
    outline="")

font_style = font.Font(family="Poppins", size=15, weight="bold")

canvas.create_text(
    596.0,
    53.0,
    anchor="nw",
    text="FLY WITH OUR SHELVES",
    fill="#4B0000",
    font=font.Font(family="Poppins", size=30, weight="bold")
)

canvas.create_text(
    653.0,
    124.0,
    anchor="nw",
    text="TUP ID",
    fill="#4B0000",
    font=font_style
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(833.5, 245.0, image=entry_image_1)
name = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="normal")
)
name.place(x=664.0, y=230.0, width=339.0, height=25.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(833.5, 175.0, image=entry_image_2)
tupid = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="normal")
)
tupid.place(x=664.0, y=160.0, width=339.0, height=25.0)

canvas.create_text(652.0, 194.0, anchor="nw", text="Name", fill="#4B0000", font=font_style)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(833.0, 315.0, image=entry_image_3)
password = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="bold"),
    show="*"
)
password.place(x=664.0, y=300.0, width=338.0, height=25.0)

canvas.create_text(652.0, 263.0, anchor="nw", text="Password", fill="#4B0000", font=font_style)
canvas.create_text(653.0, 334.0, anchor="nw", text="Re-Enter Password", fill="#4B0000", font=font_style)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(833.0, 455.0, image=entry_image_4)
contactnum = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="normal")
)
contactnum.place(x=664.0, y=440.0, width=338.0, height=25.0)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(833.0, 385.0, image=entry_image_5)
reenterpass = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="bold"),
    show="*"
)
reenterpass.place(x=664.0, y=370.0, width=338.0, height=25.0)

canvas.create_text(652.0, 403.0, anchor="nw", text="Contact Number", fill="#4B0000", font=font_style)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(833.0, 525.0, image=entry_image_6)
email = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="normal")
)
email.place(x=664.0, y=510.0, width=338.0, height=25.0)

canvas.create_text(653.0, 474.0, anchor="nw", text="Email", fill="#4B0000", font=font_style)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=1,
    highlightthickness=0,
    command=register,
    relief="flat",
    bg = "#C19A6B"
)
button_1.place(x=749.0, y=580.0, width=170.0, height=44.0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(349.0, 298.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(134.0, 71.0, image=image_image_2)

window.resizable(False, False)
window.mainloop()
