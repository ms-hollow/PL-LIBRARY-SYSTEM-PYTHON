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

def gotoBook():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "AdminManageBook.py")
    subprocess.run(["python", script_path])

def gotoTransaction():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "AdminManageTransaction.py")
    subprocess.run(["python", script_path])

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

manageBookIcon = PhotoImage(file=relative_to_assets("button_3_3.png"))
manageBook= Button(
    image=manageBookIcon,
    borderwidth=0,
    highlightthickness=0,
    command=gotoBook,
    relief="flat",
    bg="white"
)
manageBook.place(x=20.0, y=146.0, width=160.0, height=40.0)

transaction = PhotoImage(file=relative_to_assets("button_4_4.png"))
manageTransaction = Button(
    image=transaction,
    borderwidth=0,
    highlightthickness=0,
    command=gotoTransaction,
    relief="flat",
    bg="white"
)
manageTransaction.place(x=11.0, y=200.0, width=177.0, height=32.0)

student = PhotoImage(file=relative_to_assets("button_5_5.png"))
manageStudent = Button(
    image=student,
    borderwidth=0,
    highlightthickness=0,
    #command=lambda: print("button_5 clicked"),
    relief="flat",
    bg="white"
)
manageStudent.place(x=20.0, y=254.0, width=160.0, height=32.0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(250.0, 599.0, image=image_image_1)

image_2_path = relative_to_assets("image_2.png")
image_2 = Image.open(image_2_path)
max_width = 182
max_height = 112
image_2.thumbnail((max_width, max_height), Image.LANCZOS)
resizedlogo = ImageTk.PhotoImage(image_2)
image_2 = canvas.create_image(120.0, 59.0, image=resizedlogo)

canvas.create_text(220.0, 23.0, anchor="nw", text="STUDENT", fill="#4B0000", font= font.Font(family="Poppins", size=40, weight="bold"))

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

button_image_6 = PhotoImage(file=relative_to_assets("button_6_6.png"))
refreshStudent = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
refreshStudent.place(x=964.0, y=606.0, width=42.0, height=42.0)

button_image_7 = PhotoImage(file=relative_to_assets("button_7_7.png"))
deleteStudent = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
deleteStudent.place(x=1018.0, y=606.0, width=42.0, height=42.0)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(641.0, 264.0, image=image_image_6)

font_style = font.Font(family="Poppins", size=11, weight="bold")

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1_1.png"))
entry_bg_1 = canvas.create_image(
    351.5,
    455.0,
    image=entry_image_1
)
tupidEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font= font.Font(family="Poppins", size=12, weight="normal")
)
tupidEntry.place(
    x=231.0,
    y=444.0,
    width=241.0,
    height=23.0
)

canvas.create_text(221.0, 415.0, anchor="nw", text="TUP ID", fill="#4B0000", font=font_style)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2_2.png"))
entry_bg_2 = canvas.create_image(
    351.5,
    515.0,
    image=entry_image_2
)
nameEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=12, weight="normal")
)
nameEntry.place(x=231.0, y=504.0, width=241.0, height=23.0)

canvas.create_text(221.0, 475.0, anchor="nw", text="Name", fill="#4B0000", font=font_style)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3_3.png"))
entry_bg_3 = canvas.create_image(
    641.5,
    455.0,
    image=entry_image_3
)
courseSecEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=12, weight="normal")
)
courseSecEntry.place(x=521.0, y=444.0, width=241.0, height=23.0)

canvas.create_text(511.0, 415.0, anchor="nw", text="Course & Section", fill="#4B0000", font=font_style)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4_4.png"))
entry_bg_4 = canvas.create_image(
    932.5,
    455.0,
    image=entry_image_4
)
emailEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=12, weight="normal")
)
emailEntry.place(x=815.0, y=444.0, width=235.0, height=23.0)

canvas.create_text(805.0, 415.0, anchor="nw", text="Email", fill="#4B0000", font=font_style)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5_5.png"))
entry_bg_5 = canvas.create_image(
    351.5,
    581.0,
    image=entry_image_5
)
book1Entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=12, weight="normal")
)
book1Entry.place(x=231.0, y=570.0, width=241.0, height=23.0)

canvas.create_text(221.0, 541.0, anchor="nw", text="Book 1", fill="#4B0000", font=font_style)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6_6.png"))
entry_bg_6 = canvas.create_image(
    641.5,
    581.0,
    image=entry_image_6
)
book2Entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=12, weight="normal")
)
book2Entry.place(x=521.0, y=570.0, width=241.0, height=23.0)

canvas.create_text(511.0, 541.0, anchor="nw", text="Book 2", fill="#4B0000", font=font_style)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7_7.png"))
entry_bg_7 = canvas.create_image(
    932.5,
    581.0,
    image=entry_image_7
)
book3Entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=12, weight="normal")
)
book3Entry.place(x=815.0, y=570.0, width=235.0, height=23.0)

canvas.create_text(805.0, 541.0, anchor="nw", text="Book3", fill="#4B0000", font=font_style)

entry_image_8 = PhotoImage(file=relative_to_assets("entry_8_8.png"))
entry_bg_8 = canvas.create_image(
    641.5,
    515.0,
    image=entry_image_8
)
contactEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=12, weight="normal")
)
contactEntry.place(x=521.0, y=504.0, width=241.0, height=23.0)

canvas.create_text(511.0, 475.0, anchor="nw", text="Contact No.", fill="#4B0000", font=font_style)

entry_image_9 = PhotoImage(file=relative_to_assets("entry_9_9.png"))
entry_bg_9 = canvas.create_image(
    623.0,
    56.5,
    image=entry_image_9
)
searchEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=12, weight="normal")
)
searchEntry.place(x=492.0, y=42.0, width=263.0, height=30.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=760.0,
    y=39.0,
    width=80.0,
    height=35.0
)

window.resizable(False, False)
window.mainloop()
