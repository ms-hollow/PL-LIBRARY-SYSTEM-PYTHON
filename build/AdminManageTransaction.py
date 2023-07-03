import os
import subprocess
from pathlib import Path
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "SearchBook"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


'''
def gotoBook():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "studentDispBookFrame.py")
    subprocess.run(["python", script_path])

def gotoStudent():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "studentDispBookFrame.py")
    subprocess.run(["python", script_path])
'''


def searchBook():
    print("Search Book")


def refreshPage():
    print("refresh")
    # insert code here (POPUP)


def addBook():
    print("add")
    # this function will search the book, display the table and diplay lahat ng info ng book sa entry.
    # insert code here para sa search book


def deleteBook():
    print("delete")
    # insert code here (POPUP)


'''#
def gotoLogout():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "studentDispBookFrame.py")
    subprocess.run(["python", script_path])
'''

'''#
def gotoNotif():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "studentDispBookFrame.py")
    subprocess.run(["python", script_path])
'''

'''#
def gotoHome():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "studentDispBookFrame.py")
    subprocess.run(["python", script_path])
'''


def bookTable():
    # TABLE SEARCH BOOK
    sub_frame = ttk.Frame(window, width=600, height=350.0)
    sub_frame.place(x=220, y=150)

    # treeview
    table = ttk.Treeview(sub_frame,
                         columns=('Title', 'Edition', 'Author', 'Year', 'ISBN',
                                  'Material', 'Category', 'Shelf No.', 'Total Stock',
                                  'No. of Borrowers'), show='headings')
    table.heading('Title', text='Title')
    table.heading('Edition', text='Edition')
    table.heading('Author', text='Author')
    table.heading('Year', text='Year')
    table.heading('ISBN', text='ISBN')
    table.heading('Material', text='Material')
    table.heading('Category', text='Category')
    table.heading('Shelf No.', text='Shelf No.')
    table.heading('Total Stock', text='Total Stock')
    table.heading('No. of Borrowers', text='No. of Borrowers')

    table.column('Title', width=150)
    table.column('Edition', width=50)
    table.column('Author', width=120)
    table.column('Year', width=50)
    table.column('ISBN', width=100)
    table.column('Material', width=100)
    table.column('Category', width=120)
    table.column('Shelf No.', width=50)
    table.column('Total Stock', width=50)
    table.column('No. of Borrowers', width=50)

    table.pack(side='left', fill='y')

    '''
    # adding data to the table
    for i in range(len(titles)):
        table.insert('', 'end', values=(titles[i], editions[i], authors[i], years[i], isbns[i], materials[i], categories[i], shelf_nos[i], total_stocks[i], no_of_borrowers[i]))
    '''


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

canvas = Canvas(window, bg="#FFFFFF", height=670, width=1125, bd=0, highlightthickness=0, relief="ridge")

canvas.place(x=0, y=0)

manageBookIcon = PhotoImage(file=relative_to_assets("manageBook.png"))
manageBook = Button(
    image=manageBookIcon,
    borderwidth=0,
    highlightthickness=0,
    #command=gotoBook,
    relief="flat",
    bg="white"
)
manageBook.place(x=20.0, y=145.0, width=160.0, height=40.0)

manageTransactionIcon = PhotoImage(file=relative_to_assets("manageTransactions.png"))
manageTransation = Button(
    image=manageTransactionIcon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg="white"
)
manageTransation.place(
    x=12.0,
    y=199.0,
    width=177.0,
    height=32.0
)

manageStudentIcon = PhotoImage(file=relative_to_assets("manageStudent.png"))
manageStudent = Button(
    image=manageStudentIcon,
    borderwidth=0,
    highlightthickness=0,
    #command=gotoStudent,
    relief="flat",
    bg="white"
)
manageStudent.place(x=20.0, y=253.0, width=160.0, height=32.0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(250.0, 599.0, image=image_image_1)

image_2_path = relative_to_assets("image_2.png")
image_2 = Image.open(image_2_path)
max_width = 182
max_height = 112
image_2.thumbnail((max_width, max_height), Image.LANCZOS)
resizedlogo = ImageTk.PhotoImage(image_2)
image_2 = canvas.create_image(120.0, 59.0, image=resizedlogo)

canvas.create_text(218.0, 18.0, anchor="nw", text="SEARCH", fill="#4B0000",
                   font=font.Font(family="Poppins", size=40, weight="bold"))

notifButton = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = Button(
    image=notifButton,
    borderwidth=1,
    highlightthickness=0,
    # command=gotoNotif,
    relief="flat",
    bg="white"
)
image_3.place(x=993.0, y=30.0, width=38.0, height=43.0)

homeImage = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = Button(
    image=homeImage,
    borderwidth=1,
    highlightthickness=0,
    # command=gotoHome,
    relief="flat",
    bg="white"
)
image_4.place(x=924.0, y=31.0, width=42.0, height=42.0)

logoutImage = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = Button(
    image=logoutImage,
    borderwidth=1,
    highlightthickness=0,
    # command=gotoLogout,
    relief="flat",
    bg="white"
)
image_5.place(x=1054.0, y=30.0, width=43.0, height=43.0)
bookTable()

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(641.0, 264.0, image=image_image_6)

entry_image_12 = PhotoImage(file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(606.0, 56.5, image=entry_image_12)
searchEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
searchEntry.place(x=460.0, y=43.0, width=290.0, height=30.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
categoryBtn = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
categoryBtn.place(x=908.0, y=99.0, width=173.0, height=20.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
searchBtn = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=searchBook,
    relief="flat",
    bg="white"
)
searchBtn.place(x=758.0, y=39.0, width=80.0, height=35.0)

window.resizable(False, False)
window.mainloop()