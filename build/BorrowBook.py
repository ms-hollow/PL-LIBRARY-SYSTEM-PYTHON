import os
import subprocess
from pathlib import Path
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font, Toplevel, OptionMenu, Menu, StringVar
from PIL import Image, ImageTk
import CBook
import CTransaction
import CBorrower
from CBook import bookList
from CBorrower import borrowerList

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "BorrowBook"

CTransaction.retrieveTransaction()
CBorrower.retrieveBorrower()
CBook.retrieveBook()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def gotoSearchDisplayBook():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "StudentSearchBorrow.py")
    subprocess.run(["python", script_path])
def gotoStatement():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "StatementTrans.py")
    subprocess.run(["python", script_path])

indexBook = 0
indexBorrower = 0

def getInfoTransaction(ISBN):
    from StudentSearchBorrow import getISBN
    global indexBook
    global indexBorrower
    print("GET INFO TRANSACTION")
    ISBN = getISBN()
    print(ISBN)

    # Set the background color

    indexBook = CBook.locateBook(ISBN)                #kinuha index ng book na hihiramin
    title = bookList[indexBook].title
    author = bookList[indexBook].author

    indexBorrower = CBorrower.loggedInAccount   #kinuha index ng currently account logged in.
    TUP_ID = borrowerList[indexBorrower].TUP_ID
    borrower = borrowerList[indexBorrower].name
    yearSection = borrowerList[indexBorrower].yearSection

    titleEntry.insert(0, title)
    authorEntry.insert(0, author)
    tupid.insert(0, TUP_ID)
    name.insert(0, borrower)
    yearandSection.insert(0, yearSection)


   # dateBorrowedEntry.insert(0, )


window = Tk()

window.geometry("660x580")
window.configure(bg = "#4B0000")

# Calculate the center coordinates of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - 660) // 2
y = (screen_height - 580) // 2

# Set the window position to the center of the screen
window.geometry(f"+{x}+{y}")

window.lift()
canvas = Canvas(
    window,
    bg = "#4B0000",
    height = 580,
    width = 660,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    330.0,
    279.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
closebtn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg = "#C19A6B"
)
closebtn.place(
    x=623.0,
    y=21.0,
    width=20.0,
    height=14.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
submitbtn = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=gotoStatement,
    relief="flat",
    bg = "#C19A6B"
)
submitbtn.place(
    x=462.0,
    y=494.0,
    width=112.0,
    height=24.0
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(409.5,308.5,image=entry_image_1)
authorEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="white",
    highlightthickness=0, font=font.Font(family="Poppins", size=11, weight="bold"))
authorEntry.place(
    x=239.0,
    y=302.0,
    width=341.0,
    height=12.0
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image( 379.0,158.5,image=entry_image_2)
name = Entry(
    bd=0,
    bg="#C19A6B",
    fg="white",
    highlightthickness=0, font=font.Font(family="Poppins", size=11, weight="bold"))
name.place(
    x=180.0,
    y=152.0,
    width=398.0,
    height=12.0
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(389.0,188.5,image=entry_image_3)
tupid = Entry(
    bd=0,
    bg="#C19A6B",
    fg="white",
    highlightthickness=0, font=font.Font(family="Poppins", size=11, weight="bold"))
tupid.place(
    x=190.0,
    y=182.0,
    width=398.0,
    height=12.0
)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(426.5,278.5,image=entry_image_4)
titleEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="white",
    highlightthickness=0, font=font.Font(family="Poppins", size=11, weight="bold"))
titleEntry.place(
    x=265.0,
    y=272.0,
    width=323.0,
    height=12.0
)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(422.5,398.5,image=entry_image_5)
dateReturnEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="white",
    highlightthickness=0, font=font.Font(family="Poppins", size=11, weight="bold"))
dateReturnEntry.place(
    x=255.0,
    y=392.0,
    width=335.0,
    height=12.0
)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(425.5,368.5,image=entry_image_6)
dateBorrowedEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="white",
    highlightthickness=0, font=font.Font(family="Poppins", size=11, weight="bold"))
dateBorrowedEntry.place(
    x=261.0,
    y=362.0,
    width=329.0,
    height=11.0
)

entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(435.5,428.5,image=entry_image_7)
librarianEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="white",
    highlightthickness=0, font=font.Font(family="Poppins", size=11, weight="bold"))
librarianEntry.place(
    x=281.0,
    y=422.0,
    width=309.0,
    height=11.0
)

entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(387.5,458.5,image=entry_image_8)
status = Entry(
    bd=0,
    bg="#C19A6B",
    fg="white",
    highlightthickness=0, font=font.Font(family="Poppins", size=11, weight="bold"))
status.place(
    x=185.0,
    y=452.0,
    width=405.0,
    height=11.0
)

entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(381.5,338.5,image=entry_image_9)
ISBN = Entry(
    bd=0,
    bg="#C19A6B",
    fg="white",
    highlightthickness=0, font=font.Font(family="Poppins", size=11, weight="bold"))
ISBN.place(
    x=173.0,
    y=332.0,
    width=417.0,
    height=11.0
)

entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(426.0,218.5,image=entry_image_10)
yearandSection = Entry(
    bd=0,
    bg="#C19A6B",
    fg="white",
    highlightthickness=0, font=font.Font(family="Poppins", size=11, weight="bold"))
yearandSection.place(
    x=272.0,
    y=212.0,
    width=308.0,
    height=11.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
backbtn = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=gotoSearchDisplayBook,
    relief="flat",
    bg = "#C19A6B"
)
backbtn.place(
    x=20.0,
    y=21.0,
    width=20.0,
    height=20.0
)
window.resizable(False, False)
window.mainloop()
