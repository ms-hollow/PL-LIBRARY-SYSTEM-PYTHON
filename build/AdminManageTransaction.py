import os
import subprocess
from pathlib import Path
from tkinter import ttk, Menu
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "SearchBook"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def gotoStudent():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "AdminManageStudent.py")
    subprocess.run(["python", script_path])


def gotoBook():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "AdminManageBook.py")
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



def gotoLogout():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "Login.py")
    subprocess.run(["python", script_path])


'''#
def gotoNotif():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "studentDispBookFrame.py")
    subprocess.run(["python", script_path])
'''


def gotoHome():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "HomePage.py")
    subprocess.run(["python", script_path])


def dropdownMenu():
    # Create a dropdown menu
    dropdownmenu = Menu(window, tearoff=False, font=("Poppins", 10, "bold"))  # Set custom font and size
    dropdownmenu.configure(bg="#4B0000", fg="#C19A6B")  # Set background and foreground colors

    # List of options for the dropdown menu
    options = ["Title", "Author", "Year", "Material", "Genre                       "]  # Add your options here

    # Function to be executed when an option is selected from the dropdown
    def on_option_selected(option):
        print("Selected Option:", option)

    # Add options to the dropdown menu
    for option in options:
        dropdownmenu.add_command(label=option, command=lambda opt=option: on_option_selected(opt))

    # Display the dropdown menu under the category button
    dropdownmenu.post(categoryBtn.winfo_rootx(), categoryBtn.winfo_rooty() + categoryBtn.winfo_height())

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

manageBookIcon = PhotoImage(file=relative_to_assets("manageBook_transac.png"))
manageBook = Button(
    image=manageBookIcon,
    borderwidth=0,
    highlightthickness=0,
    command=gotoBook,
    relief="flat",
    bg="white"
)

manageBook.place(
    x=20.0,
    y=146.0,
    width=160.0,
    height=40.0
)

manageTransactionIcon = PhotoImage(file=relative_to_assets("manageTransaction.png"))
manageTransaction = Button(
    image=manageTransactionIcon,
    borderwidth=0,
    highlightthickness=0,
    #command=lambda: print("button_2 clicked"),
    relief="flat",
    bg="white"
)
manageTransaction.place(
    x=11.0,
    y=200.0,
    width=177.0,
    height=32.0
)

manageStudentIcon = PhotoImage(file=relative_to_assets("manageStudent.png"))
manageStudent = Button(
    image=manageStudentIcon,
    borderwidth=0,
    highlightthickness=0,
    command=gotoStudent,
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

canvas.create_text(218.0, 19.0, anchor="nw", text="TRANSACTION", fill="#4B0000", font=font.Font(family="Poppins", size=40, weight="bold"))

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
    command=gotoHome,
    relief="flat",
    bg="white"
)
image_4.place(x=924.0, y=31.0, width=42.0, height=42.0)

logoutImage = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = Button(
    image=logoutImage,
    borderwidth=1,
    highlightthickness=0,
    command=gotoLogout,
    relief="flat",
    bg="white"
)
image_5.place(x=1054.0, y=30.0, width=43.0, height=43.0)
bookTable()

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(641.0, 264.0, image=image_image_6)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
categoryBtn = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=dropdownMenu,
    relief="flat"
)
categoryBtn.place(x=908.0, y=99.0, width=173.0, height=20.0)

font_style = font.Font(family="Poppins", size=11, weight="bold")

entry_image_1 = PhotoImage(file=relative_to_assets("searchEntry.png"))
entry_bg_1 = canvas.create_image(700.0, 55.5, image=entry_image_1)
searchEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font = font.Font(family="Poppins", size=11, weight="normal")
)
searchEntry.place(x=620.0, y=40.0, width=160.0, height=30.0)

canvas.create_text(
    218.0,
    19.0,
    anchor="nw",
    text="TRANSACTION",
    fill="#4B0000",
    font=font.Font(family="Poppins", size=40, weight="bold")
)

searchIcon = PhotoImage(file=relative_to_assets("searchBtn.png"))
searchBtn = Button(
    image=searchIcon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
searchBtn.place(x=790.0, y=38.0, width=80.0, height=35.0)

entry_image_2 = PhotoImage(file=relative_to_assets("titleEntry.png"))
entry_bg_2 = canvas.create_image(
    350.5,
    455.0,
    image=entry_image_2
)
title = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font = font.Font(family="Poppins", size=11, weight="normal")
)
title.place(x=230.0, y=444.0, width=241.0, height=23.0)

canvas.create_text(
    220.0,
    415.0,
    anchor="nw",
    text="Title",
    fill="#4B0000",
    font=font_style
)

entry_image_3 = PhotoImage(file=relative_to_assets("dateBorrowedEntry.png"))
entry_bg_3 = canvas.create_image(
    283.0,
    575.0,
    image=entry_image_3
)
dateborrowed = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
dateborrowed.place(x=230.0, y=564.0, width=106.0, height=23.0)

entry_image_4 = PhotoImage(file=relative_to_assets("dateReturnEntry.png"))
entry_bg_4 = canvas.create_image(
    420.0,
    575.0,
    image=entry_image_4
)
dateReturn= Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
dateReturn.place(x=370.0, y=564.0, width=100.0, height=23.0)

canvas.create_text(
    225.0,
    535.0,
    anchor="nw",
    text="Date Borrowed",
    fill="#4B0000",
    font=font_style
)

canvas.create_text(
    365.0,
    535.0,
    anchor="nw",
    text="Date to Return",
    fill="#4B0000",
    font=font_style
)

entry_image_5 = PhotoImage(file=relative_to_assets("authorEntry.png"))
entry_bg_5 = canvas.create_image(
    350.5,
    515.0,
    image=entry_image_5
)
author = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
author.place(x=230.0, y=504.0, width=241.0, height=23.0)

canvas.create_text(
    220.0,
    475.0,
    anchor="nw",
    text="Author",
    fill="#4B0000",
    font=font_style
)

entry_image_7 = PhotoImage(file=relative_to_assets("remainingDays.png"))
entry_bg_7 = canvas.create_image(
    866.5,
    575.0,
    image=entry_image_7
)
remainingDays = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
remainingDays.place(x=809.0, y=564.0, width=115.0, height=23.0)

statusIcon = PhotoImage(file=relative_to_assets("statusdropdown.png"))
status = Button(
    image=statusIcon,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg="white"
)
status.place(x=961.0, y=560.0, width=99.0, height=30.0)

canvas.create_text(
    799.0,
    535.0,
    anchor="nw",
    text="Remaining Days",
    fill="#4B0000",
    font=font_style
)

entry_image_9 = PhotoImage(file=relative_to_assets("librarianEntry.png"))
entry_bg_9 = canvas.create_image(
    929.5,
    515.0,
    image=entry_image_9
)
librarian = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font = font.Font(family="Poppins", size=11, weight="normal")
)
librarian.place(x=809.0, y=504.0, width=241.0, height=23.0)

canvas.create_text(
    799.0,
    475.0,
    anchor="nw",
    text="Librarian",
    fill="#4B0000",
    font=font_style
)

entry_image_10 = PhotoImage(file=relative_to_assets("isbnEntry.png"))
entry_bg_10 = canvas.create_image(640.5, 455.0, image=entry_image_10)
isbn = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
isbn.place(x=520.0, y=444.0, width=241.0, height=23.0)

canvas.create_text(
    510.0,
    415.0,
    anchor="nw",
    text="ISBN",
    fill="#4B0000",
    font=font_style
)

entry_image_11 = PhotoImage(file=relative_to_assets("tupidEntry.png"))
entry_bg_11 = canvas.create_image(640.5, 515.0, image=entry_image_11)
tupid = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
tupid.place(x=520.0, y=504.0, width=241.0, height=23.0)

canvas.create_text(
    510.0,
    475.0,
    anchor="nw",
    text="TUP ID",
    fill="#4B0000",
    font=font_style
)

entry_image_12 = PhotoImage(file=relative_to_assets("borrowerEntry.png"))
entry_bg_12 = canvas.create_image(640.5, 575.0, image=entry_image_12)
borrower = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
borrower.place(x=520.0, y=564.0, width=241.0, height=23.0)

canvas.create_text(
    515.0,
    535.0,
    anchor="nw",
    text="BORROWER",
    fill="#4B0000",
    font=font_style
)

button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
refresh = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
refresh.place(x=965.0, y=606.0, width=42.0, height=41.671875)

button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
refresh = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
refresh.place(x=1019.0, y=606.0, width=42.0, height=42.0)

referenceIcon = PhotoImage(file=relative_to_assets("referenceNumEntry.png"))
entry_bg_1 = canvas.create_image(
    874.0,
    455.0,
    image=referenceIcon
)
referenceNum = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
referenceNum.place(x=809.0, y=441.0, width=130.0, height=28.0)

canvas.create_text(799.0, 415.0, anchor="nw", text="Reference Number", fill="#4B0000", font=font_style)

fineIcon = PhotoImage(file=relative_to_assets("fineEntry.png"))
entry_bg_2 = canvas.create_image(1015.0, 455.0, image=fineIcon)

fine = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
fine.place(x=980.0, y=441.0, width=70.0, height=28.0)

canvas.create_text(970.0, 415.0, anchor="nw", text="Fine", fill="#4B0000", font=font_style)

window.resizable(False, False)
window.mainloop()
