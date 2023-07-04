import os
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, font, messagebox
from PIL import Image, ImageTk
import CBorrower

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "RegisterFrame"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def register():

    name = nameEntry.get()
    TUP_ID = tupidEntry.get()
    password = passwordEntry.get()
    yearSection = "BSCS"
    repassword = reenterpassEntry.get()
    contactNum = contactnumEntry.get()
    email = emailEntry.get()
    noOfBorrowed = "0"

    if CBorrower.locateBorrower(TUP_ID) >= 0:               #if existing na sa borrowerList
        messagebox.showerror("REGISTRATION ", "YOUR TUP ID IS ALREADY REGISTERED")
    elif not CBorrower.checkBorrowerFields(name, TUP_ID, password, yearSection, contactNum, email):    #if di complete fields
        messagebox.showerror("REGISTRATION", "PLEASE FILL IN ALL THE FIELDS")
    elif len(TUP_ID) != 6:
        messagebox.showerror("REGISTRATION", "TUP ID MUST BE 6 DIGITS LONG")
    elif password != repassword:
        messagebox.showerror("REGISTRATION", "PASSWORD DIDN'T MATCH")
    else:
        response = messagebox.askyesno(    #creates a yes or no message box
            title="Confirmation",
            message="DO YOU WANT TO SUBMIT YOUR REGISTRATION?",
            icon=messagebox.QUESTION,
        )
        if response:                        #if yes
            borrower = CBorrower.CBorrower(name, TUP_ID, password, yearSection, contactNum, email, noOfBorrowed)
            CBorrower.addBorrower(borrower)
            CBorrower.saveBorrower()
            messagebox.showinfo("REGISTRATION", "YOUR ACCOUNT IS SUCCESSFULLY REGISTERED!")

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
nameEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="normal")
)
nameEntry.place(x=664.0, y=230.0, width=339.0, height=25.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(833.5, 175.0, image=entry_image_2)
tupidEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="normal")
)
tupidEntry.place(x=664.0, y=160.0, width=339.0, height=25.0)

canvas.create_text(652.0, 194.0, anchor="nw", text="Name", fill="#4B0000", font=font_style)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(833.0, 315.0, image=entry_image_3)
passwordEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="bold"),
    show="*"
)
passwordEntry.place(x=664.0, y=300.0, width=338.0, height=25.0)

canvas.create_text(652.0, 263.0, anchor="nw", text="Password", fill="#4B0000", font=font_style)
canvas.create_text(653.0, 334.0, anchor="nw", text="Re-Enter Password", fill="#4B0000", font=font_style)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(833.0, 455.0, image=entry_image_4)
contactnumEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="normal")
)
contactnumEntry.place(x=664.0, y=440.0, width=338.0, height=25.0)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(833.0, 385.0, image=entry_image_5)
reenterpassEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="bold"),
    show="*"
)
reenterpassEntry.place(x=664.0, y=370.0, width=338.0, height=25.0)

canvas.create_text(652.0, 403.0, anchor="nw", text="Contact Number", fill="#4B0000", font=font_style)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(833.0, 525.0, image=entry_image_6)
emailEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="normal")
)
emailEntry.place(x=664.0, y=510.0, width=338.0, height=25.0)

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
