import os
import subprocess
from pathlib import Path
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font, Toplevel, OptionMenu, Menu, StringVar
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "SearchBook"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def gotoDisplayBooks():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "StudentDisplayBook.py")
    subprocess.run(["python", script_path])

def searchBook():
    print("SearchBook")
    # this function will search the book, display the table and diplay lahat ng info ng book sa entry.
    #insert code here para sa search book

def borrowBook():
    print("Borrow Book")
    # insert code here (POPUP)
def gotoLogin():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "Login.py")
    subprocess.run(["python", script_path])
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


def gotoHome():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "HomePage.py")
    subprocess.run(["python", script_path])
def gotoChangePass():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "ChangePassword.py")
    subprocess.run(["python", script_path])

def dropdownMenu():
    # Create a dropdown menu
    dropdownmenu = Menu(window, tearoff=False, font=("Poppins", 10, "bold"))  # Set custom font and size
    dropdownmenu.configure(bg="#4B0000", fg="#C19A6B")  # Set background and foreground color
    options = ["Title", "Author", "Year", "Material", "Genre                       "]  # Add your options here

    # Function to be executed when an option is selected from the dropdown
    def on_option_selected(option):
        print("Selected Option:", option)

    # Add options to the dropdown menu
    for option in options:
        dropdownmenu.add_command(label=option, command=lambda opt=option: on_option_selected(opt))
    dropdownmenu.post(categoryBtn.winfo_rootx(), categoryBtn.winfo_rooty() + categoryBtn.winfo_height())
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
    dropdown_menu.post(image_5.winfo_rootx(), image_5.winfo_rooty() + image_5.winfo_height())

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
window.configure(bg = "#FFFFFF")

# Calculate the center coordinates of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - 1125) // 2
y = (screen_height - 670) // 2

# Set the window position to the center of the screen
window.geometry(f"+{x}+{y}")

canvas = Canvas(window, bg = "#FFFFFF", height = 670, width = 1125, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
displayBooks = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=gotoDisplayBooks,
    relief="flat",
    bg="white"
)
displayBooks.place(x=21.0, y=144.0, width=160.0, height=32.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
searchBooks = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg="white"
)
searchBooks.place(x=21.0, y=198.0, width=160.0, height=32.0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(250.0, 599.0, image=image_image_1)

image_2_path = relative_to_assets("image_2.png")
image_2 = Image.open(image_2_path)
max_width = 182
max_height = 112
image_2.thumbnail((max_width, max_height), Image.LANCZOS)
resizedlogo = ImageTk.PhotoImage(image_2)
image_2 = canvas.create_image(120.0, 59.0, image=resizedlogo)

canvas.create_text(218.0, 18.0, anchor="nw", text="SEARCH", fill="#4B0000", font= font.Font(family="Poppins", size=40, weight="bold"))

notifButton = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = Button(
    image=notifButton,
    borderwidth=1,
    highlightthickness=0,
    #command=gotoNotif,
    relief="flat",
    bg = "white"
)
image_3.place(x=993.0,y=30.0,width=38.0,height=43.0)

homeImage = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = Button(
    image=homeImage,
    borderwidth=1,
    highlightthickness=0,
    command=gotoHome,
    relief="flat",
    bg = "white"
)
image_4.place(x=924.0, y=31.0, width=42.0, height=42.0)

logoutImage = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = Button(
    image=logoutImage,
    borderwidth=1,
    highlightthickness=0,
    command=Student_dropdownMenu,
    relief="flat",
    bg = "white"
)
image_5.place(x=1054.0, y=30.0, width=43.0, height=43.0)
bookTable()

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(350.5, 455.0, image=entry_image_1)
title = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
title.place(x=230.0, y=445.0, width=241.0, height=24.0)

canvas.create_text(220.0, 415.0, anchor="nw", text="Title", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))


entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(280.0, 575.0, image=entry_image_2)
edition = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
edition.place(x=230.0, y=565.0, width=100.0, height=24.0)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(425.0, 575.0, image=entry_image_3)

year = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
year.place(x=375.0, y=565.0, width=100.0, height=24.0)

canvas.create_text(220.0, 535.0, anchor="nw", text="Edition", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

canvas.create_text(365.0, 535.0, anchor="nw", text="Year Published", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(350.5, 515.0, image=entry_image_4)
author = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
author.place(x=230.0, y=505.0, width=241.0, height=24.0)

canvas.create_text(220.0, 475.0, anchor="nw", text="Author", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(929.5, 455.0, image=entry_image_5)
shelf = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
shelf.place(x=809.0, y=445.0, width=241.0, height=24.0)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(859.0, 575.0, image=entry_image_6)
currentStocks = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
currentStocks.place(x=809.0, y=565.0, width=100.0, height=24.0)

entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(999.0, 575.0, image=entry_image_7)
noBorrowers= Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
noBorrowers.place(x=949.0, y=565.0, width=100.0, height=24.0)

canvas.create_text(804.0, 535.0, anchor="nw", text="Current Stocks", fill="#4B0000", font=font.Font(family="Poppins", size=10, weight="bold"))

canvas.create_text(944.0, 535.0, anchor="nw", text="No. of Borrowers", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(929.5, 515.0, image=entry_image_8)
totalStocks = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
totalStocks.place(x=809.0, y=505.0, width=241.0, height=24.0)

canvas.create_text(799.0, 475.0, anchor="nw", text="Total Stocks", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

canvas.create_text(804.0, 415.0, anchor="nw", text="Shelf Number", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(640.5, 455.0, image=entry_image_9)
isbn= Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
isbn.place(x=520.0, y=445.0, width=241.0, height=24.0)

canvas.create_text(510.0, 415.0, anchor="nw", text="ISBN", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(640.5, 515.0,image=entry_image_10)

material = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
material.place(x=520.0, y=505.0, width=241.0, height=24.0)

canvas.create_text(510.0, 475.0, anchor="nw", text="Material", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_11 = PhotoImage(file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(640.5, 575.0, image=entry_image_11)

genre = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
genre.place(x=520.0, y=565.0, width=241.0, height=24.0)

canvas.create_text(515.0, 535.0, anchor="nw", text="Genre", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

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
    command=dropdownMenu,
    relief="flat",
    bg = "white",
)
categoryBtn.place(x=908.0, y=99.0, width=173.0, height=20.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
borrow = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=borrowBook,
    relief="flat",
    bg="white"
)
borrow.place(x=893.0, y=610.0, width=173.0, height=30.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
searchBtn = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=searchBook,
    relief="flat",
    bg="white"
)
searchBtn.place(x=758.0, y=39.0, width=80.0,height=35.0)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
borrowBookFrame = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
    bg="white"
)
borrowBookFrame.place(x=21.0, y=252.0, width=160.0, height=32.0)

window.resizable(False, False)
window.mainloop()
