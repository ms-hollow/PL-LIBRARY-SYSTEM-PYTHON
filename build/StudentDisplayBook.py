import os
import subprocess
from pathlib import Path
from tkinter import ttk, Menu
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "DisplayBook"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def gotoSearchBook():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "StudentSearchBorrow.py")
    subprocess.run(["python", script_path])

'''#
def gotoBorrowBook():
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

def gotoLogin():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "Login.py")
    subprocess.run(["python", script_path])


def gotoChangePass():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "ChangePassword.py")
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
    dropdown_menu.post(image_4.winfo_rootx(), image_4.winfo_rooty() + image_4.winfo_height())

def bookTable():
    #BOOK TABLE
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

window.geometry("1125x670")

# Calculate the center coordinates of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - 1125) // 2
y = (screen_height - 670) // 2

# Set the window position to the center of the screen
window.geometry(f"+{x}+{y}")

canvas = Canvas(window, bg = "#FFFFFF", height = 670, width = 1125, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)

#DISPLAY ALL BOOKS
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    #command=gotoDisplayBooks,
    relief="flat",
    bg = "white"
)
button_1.place(x=20.0,y=145.0,width=160.0,height=32.0)

#SEARCH BOOK
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=gotoSearchBook,
    relief="flat",
    bg = "white"
)
button_2.place(x=20.0, y=199.0, width=160.0, height=32.0)

#BORROW BOOK
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    bg = "white"
)
button_3.place(x=20.0, y=253.0, width=160.0, height=32.0)

image_1_path = relative_to_assets("image_1.png")
image_1 = Image.open(image_1_path)
max_width = 182
max_height = 112
image_1.thumbnail((max_width, max_height), Image.LANCZOS)
resizedlogo = ImageTk.PhotoImage(image_1)
image_1 = canvas.create_image(120.0, 59.0, image=resizedlogo)

canvas.create_text(219.0, 17.0, anchor="nw", text="BOOK", fill="#4B0000", font= font.Font(family="Poppins", size=40, weight="bold"))

#NOTIFICATION/BELL BUTTON
notifButton = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = Button(
    image=notifButton,
    borderwidth=1,
    highlightthickness=0,
    #command=gotoNotif,
    relief="flat",
    bg = "white"
)
image_2.place(x=993.0,y=30.0,width=38.0,height=43.0)

#HOME BUTTON
homeImage = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = Button(
    image=homeImage,
    borderwidth=1,
    highlightthickness=0,
    command=gotoHome,
    relief="flat",
    bg = "white"
)
image_3.place(x=924.0, y=31.0, width=42.0, height=42.0)

#LOGOUT BUTTON
logoutImage = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = Button(
    image=logoutImage,
    borderwidth=1,
    highlightthickness=0,
    command=Student_dropdownMenu,
    relief="flat",
    bg = "white"
)
image_4.place(x=1054.0, y=30.0, width=43.0, height=43.0)

#TEXTBOX
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(577.5, 56.5, image=entry_image_1)
entry_1 = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=405.0,
    y=40.0,
    width=350.0,
    height=33.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(640.0, 380.0, image=image_image_5)
bookTable()

#CATEGORY DROPDOWN
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
categoryBtn = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=dropdownMenu,
    relief="flat",
)
categoryBtn.place(
    x=907.0,
    y=100.0,
    width=173.0,
    height=20.0
)

#search book button
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(x=758.0, y=40.0, width=80.0, height=35.0)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(250.0, 599.0, image=image_image_6)
# Move the image to the bottom of the stacking order
canvas.lower(image_6)

window.resizable(False, False)
window.mainloop()

