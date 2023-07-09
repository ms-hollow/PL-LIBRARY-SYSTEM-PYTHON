import os
import subprocess
from pathlib import Path
from tkinter import ttk, messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "ContactUs"
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def gotoHome():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "HomePage.py")
    subprocess.run(["python", script_path])
def gotoAboutUs():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "AboutUS.py")
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

def displayMessage():
    messagebox.showinfo("CONTACT US",
                        "Thank you for messaging TUP Reads Library! We greatly appreciate your messages and value your engagement with our library. Your feedback, inquiries, and suggestions are important to us as we strive to provide the best possible services and resources to our valued patrons. If you have any further questions or need assistance, please don't hesitate to reach out. Thank you once again for your support and involvement with TUP Reads Library!")

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

caramel = "#C19A6B"


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

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(562.0,584.0,image=image_image_1)
canvas.create_text(653.0,124.0,anchor="nw",text="TUP ID",fill="#4B0000",  font=font.Font(family="Poppins", size=18, weight="bold"))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(833.5,245.0 ,image=entry_image_1)
name = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="bold")
)

name.place(x=664.0,y=230.0,width=339.0,height=20.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(833.5,175.0,image=entry_image_2)
tupid = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="bold")
)
tupid.place(x=664.0,y=160.0,width=339.0,height=20.0)

canvas.create_text(652.0,194.0,anchor="nw",text="Name",fill="#4B0000",font=font.Font(family="Poppins", size=18, weight="bold"))

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(833.0,315.0,image=entry_image_3)
email = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="bold")
)
email.place(x=664.0,y=300.0,width=338.0,height=20.0)
canvas.create_text(652.0,263.0,anchor="nw",text="Email",fill="#4B0000",font=font.Font(family="Poppins", size=18, weight="bold"))

canvas.create_text(653.0,334.0,anchor="nw",text="Message",fill="#4B0000",font=font.Font(family="Poppins", size=18, weight="bold"))
entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(833.0,448.5,image=entry_image_4)
entry_4 = Text(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="bold")
)
entry_4.place(
    x=673.0,
    y=370.0,
    width=320.0,
    height=150.0
)

#SEND
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
sendbtn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=displayMessage,
    relief="flat",
    bg = caramel
)
sendbtn.place(
    x=760.0,
    y=570.0,
    width=170.0,
    height=44.0
)
#SIGN UP
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
registerbtn = Button(
    image=button_image_2,
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

#CONTACT US
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
Contactbtn = Button(
    image=button_image_3,
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

#About US
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
Aboutbtn = Button(
    image=button_image_4,
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

#Home
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
homebtn = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=gotoHome,
    relief="flat",
    bg = "white"
)
homebtn.place(
    x=432.0,
    y=22.0,
    width=77.0,
    height=32.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    324.0,
    350.0,
    image=image_image_2
)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    134.0,
    71.0,
    image=image_image_3
)


window.resizable(False, False)
window.mainloop()
