import os
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, font, messagebox
from PIL import Image, ImageTk
import CBook
import CBorrower
import CTransaction


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "LoginFrame"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

tries = 3
exit = False
def login():

    #Insert here lahat ng retrieve
    CBook.retrieveBook()
    CBorrower.retrieveBorrower()
    CTransaction.retrieveTransaction()


    enteredID = tupid.get()
    enteredPass = password.get()

    index = CBorrower.locateBorrower(enteredID)

    if index >= 0 and enteredPass == CBorrower.borrowerList[index].password:
        messagebox.showinfo("LOG IN ", "LOG IN SUCCESSFULLY!")
        CBorrower.saveBorrower()
        global loggedInAccount  # accessing global variable
        loggedInAccount = index  # modifying global variable

        #Punta sa student frame
        window.destroy()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_directory, "StudentDisplayBook.py")
        subprocess.run(["python", script_path])

    elif enteredID == "ADMIN" and enteredPass == "1234":
        messagebox.showinfo("LOG IN ", "LOG IN SUCCESSFULLY!")

        #Punta sa admin frame
        window.destroy()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_directory, "AdminManageBook.py")
        subprocess.run(["python", script_path])

    elif index < 0:
        messagebox.showerror("LOG IN", "YOUR TUP ID IS NOT YET REGISTERED")

    else:
        messagebox.showerror("LOG IN", "INCORRECT TUP ID OR PASSWORD")
        global tries
        tries -= 1
        print("YOU HAVE", tries, "TRIES LEFT.")

    if tries == 0:
        messagebox.showerror("LOG IN", "YOU HAVE REACHED THE MAXIMUM NUMBER OF ATTEMPTS.\nTRY AGAIN LATER")

        #Punta sa home
        window.destroy()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_directory, "Register.py")
        subprocess.run(["python", script_path])

def gotoRegister():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "Register.py")
    subprocess.run(["python", script_path])


def gotoHome():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "HomePage.py")
    subprocess.run(["python", script_path])


def gotoAboutus():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "AboutUS.py")
    subprocess.run(["python", script_path])

def gotoContactus():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "ContactUs.py")
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
image_2 = canvas.create_image(900.0, 480.0, image=image_image_2)

canvas.create_text(457.0, 146.0, anchor="nw", text="WELCOME ", fill="#4B0000",
                   font=font.Font(family="Poppins", size=30, weight="bold"))
canvas.create_text(372.0, 234.0, anchor="nw", text="Username ", fill="#4B0000",
                   font=font.Font(family="Poppins", size=20, weight="bold"))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(552.0, 296.0, image=entry_image_1)
tupid = Entry(bd=0, bg="#FFFDFD", fg="#000716", highlightthickness=0, font=font.Font(family="Poppins", size=13, weight="normal"))
tupid.place(x=383.0, y=276.0, width=338.0, height=35.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(552.0, 403.0, image=entry_image_2)
password = Entry(bd=0, bg="#FFFDFD", fg="#000716", highlightthickness=0, font=font.Font(family="Poppins", size=13, weight="bold"), show="*")
password.place(x=383.0, y=383.0, width=338.0, height=35.0)

canvas.create_text(372.0, 341.0, anchor="nw", text="Password", fill="#4B0000",
                   font=font.Font(family="Poppins", size=20, weight="bold"))

# SIGN UP
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=gotoRegister,
    relief="flat",
    bg = "white"
)
button_1.place(
    x=959.0,
    y=22.0,
    width=104.0,
    height=29.0
)

# Home Button
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,
                  borderwidth=0,
                  highlightthickness=0,
                  command=gotoHome,
                  relief="flat",
                  bg = "white"
                  )

button_2.place(x=432.0, y=22.0, width=77.0, height=32.0)

# Contact Us
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=gotoContactus,
    relief="flat",
    bg = "white"
)
button_3.place(x=746.0, y=22.0, width=162.0, height=29.0)

# About Us Button
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=gotoAboutus,
    relief="flat",
    bg = "white"
)
button_4.place(x=560.0, y=22.0, width=143.0, height=32.0)

# LOGIN BUTTON
button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_5.place(x=487.0, y=481.0, width=150.0, height=44.0)

image_3_path = relative_to_assets("image_3.png")
image_3 = Image.open(image_3_path)
max_width = 182
max_height = 112
image_3.thumbnail((max_width, max_height), Image.LANCZOS)
resizedlogo = ImageTk.PhotoImage(image_3)
image_3 = canvas.create_image(120.0, 59.0, image=resizedlogo)

window.resizable(False, False)
window.mainloop()

