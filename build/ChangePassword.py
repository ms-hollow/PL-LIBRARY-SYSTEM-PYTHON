import os
import subprocess
from pathlib import Path
from tkinter import ttk, messagebox, END
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, font, Menu
import CBorrower

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

def gotoBack():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "StudentDisplayBook.py")
    subprocess.run(["python", script_path])

def Student_dropdownMenu():
    # Create a dropdown menu
    dropdown_menu = Menu(window, tearoff=False, font=("Poppins", 10, "bold"))  # Set custom font and size
    dropdown_menu.configure(bg="#C19A6B", fg="#4B0000")  # Set background and foreground colors

    # List of options for the dropdown menu
    options = ["Back to Display Books", "Log out"]  # Add your options here

    # Function to be executed when an option is selected from the dropdown
    def on_option_selected(option):
        if option == "Log out":
            gotoLogin()
        elif option == "Back to Display Books":
            gotoBack()
        else:
            print("Selected Option:", option)

    # Add options to the dropdown menu
    for option in options:
        dropdown_menu.add_command(label=option, command=lambda opt=option: on_option_selected(opt))

    # Display the dropdown menu under the image_5 button
    dropdown_menu.post(logoutbtn.winfo_rootx(), logoutbtn.winfo_rooty() + logoutbtn.winfo_height())

changePassTries = 3
def changePass():

    global changePassTries

    TUP_ID = tupidEntry.get()
    currentPass = currpassEntry.get()
    newPass = newPassEntry.get()
    reEnterPass = repassEntry.get()

    index = CBorrower.locateBorrower(TUP_ID)

    if index < 0:
        messagebox.showerror("CHANGE PASSWORD", "ACCOUNT NOT FOUND")
    elif currentPass != CBorrower.borrowerList[index].password:
        messagebox.showerror("CHANGE PASSWORD", "INCORRECT CURRENT PASSWORD")
        changePassTries -= 1
        clearFields()
    elif newPass != reEnterPass:
        messagebox.showerror("CHANGE PASSWORD", "NEW PASSWORD DOESN'T MATCH THE RE-ENTERED PASSWORD!")
        clearFields()
    elif currentPass == newPass:
        messagebox.showerror("CHANGE PASSWORD", "YOU CAN'T CHANGE IT TO YOUR CURRENT PASSWORD")
        clearFields()
    else:
        response = messagebox.askyesno(  # creates a yes or no message box
            title="CHANGE PASSWORD",
            message="CONFIRM CHANGES?",
            icon=messagebox.QUESTION
        )
        if response:
            CBorrower.borrowerList[index].password = newPass  # set password to new pass
            CBorrower.saveBorrower()
            messagebox.showinfo("CHANGE PASSWORD", "YOUR PASSWORD HAS BEEN SUCCESSFULLY CHANGED!")

            window.destroy()
            current_directory = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(current_directory, "StudentDisplayBook.py")
            subprocess.run(["python", script_path])
            # CLEAR FIELDS

    if changePassTries == 0:
        messagebox.showerror("CHANGE PASSWORD", "YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIES. TRY AGAIN LATER")
        window.destroy()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_directory, "StudentDisplayBook.py")
        subprocess.run(["python", script_path])

def clearFields():

    currpassEntry.delete(0, END)  # Clear the contents of the Entry widget
    newPassEntry.delete(0, END)
    repassEntry.delete(0, END)

CBorrower.retrieveBorrower()
window = Tk()

window.geometry("1125x670")
window.configure(bg = "#FFFFFF")

# Calculate the center coordinates of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - 1125) // 2
y = (screen_height - 670) // 2

# Set the window position to the center of the screen
window.geometry(f"+{x}+{y}")

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

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    775.0,
    416.0,
    image=entry_image_1
)
newPassEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="bold"), show="*"
)
newPassEntry.place(x=552.0, y=396.0, width=446.0, height=33.0)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    775.0,
    496.0,
    image=entry_image_2
)
repassEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="bold"), show="*"
)
repassEntry.place(
    x=552.0,
    y=476.0,
    width=446.0,
    height=33.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    775.0,
    336.0,
    image=entry_image_3
)
currpassEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="bold"), show="*"
)
currpassEntry.place(
    x=552.0,
    y=316.0,
    width=446.0,
    height=33.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    125.0,
    66.0,
    image=image_image_2
)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    776.0,
    256.0,
    image=entry_image_4
)
tupidEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=13, weight="bold")
)
tupidEntry.place(
    x=553.0,
    y=236.0,
    width=446.0,
    height=33.0
)
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
changepassbtn = Button(image=button_image_1,borderwidth=0,
    highlightthickness=0,
    command=changePass,
    relief="flat",
    bg = "white"
)
changepassbtn.place(
    x=649.0,
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
