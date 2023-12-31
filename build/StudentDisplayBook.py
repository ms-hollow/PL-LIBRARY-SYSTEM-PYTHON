import os
import subprocess
from pathlib import Path
from tkinter import ttk, Menu, StringVar, messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from PIL import Image, ImageTk
import CBook, CTransaction, CBorrower
from CBook import bookList
from CBorrower import borrowerList

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "DisplayBook"

CBook.retrieveBook()
CBorrower.retrieveBorrower()
CTransaction.retrieveTransaction()

indexBorrower = 0
index = 0
option_value = ""

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


def gotoNotif():
    # Create the dropdown menu
    dropdown_menu = Menu(window, tearoff=False, font=("Poppins", 10, "bold"))
    dropdown_menu.configure(bg="#C19A6B", fg="#4B0000")

    # Retrieve the indexBorrower value
    indexBorrower = CBorrower.retrieve_login_account()
    print(indexBorrower)

    # Collect transactions
    transactions = []

    #if 0 <= indexBorrower < len(CBorrower.borrowerList):
    borrower_tup_id = CBorrower.borrowerList[indexBorrower].TUP_ID

    for transaction in CTransaction.transactionList:
        if transaction.TUP_ID == borrower_tup_id:
            status = transaction.status
            refNum = transaction.refNum
            transactions.append(f"{refNum} : {status}")

    # Add options to the dropdown menu
    for transaction in transactions:
        dropdown_menu.add_command(label=transaction)

    # Display the dropdown menu below the image_2 button
    dropdown_menu.post(image_3.winfo_rootx(), image_3.winfo_rooty() + image_3.winfo_height())

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

class DisplayTable:

    def __init__(self):
        self.choice = 0  # Initialize the instance variable

    def dropdownMenu(self):
        # Create a dropdown menu
        dropdownmenu = Menu(window, tearoff=False, font=("Poppins", 10, "bold"))  # Set custom font and size
        dropdownmenu.configure(bg="#4B0000", fg="#C19A6B")  # Set background and foreground colors

        # List of options for the dropdown menu
        options = ["Title", "Author", "Year", "Material", "Genre"]  # Add your options here

        # Create a StringVar outside the function to store the selected option
        clicked = StringVar()

        # Function to be executed when an option is selected from the dropdown
        def on_option_selected(option):
            self.choice = options.index(option) + 1
            print(option)  # Print the selected option
            global option_value
            option_value = option

        # Add options to the dropdown menu
        for option in options:
            dropdownmenu.add_command(label=option, command=lambda opt=option: on_option_selected(opt))

        # Display the dropdown menu under the category button
        dropdownmenu.post(categoryBtn.winfo_rootx(), categoryBtn.winfo_rooty() + categoryBtn.winfo_height())

    def recommendedBooks(self):

        recommendation = CTransaction.recom()
        first.insert(0, recommendation[0])
        second.insert(0, recommendation[1])
        last.insert(0, recommendation[2])

    def bookTable(self):
        # TABLE SEARCH BOOK
        sub_frame = ttk.Frame(window, width=600, height=350.0)
        sub_frame.place(x=220, y=170)

        # Create the table outside the loop
        table = ttk.Treeview(sub_frame,
                             columns=('Title', 'Edition', 'Author', 'Year', 'ISBN',
                                      'Material', 'Genre', 'Shelf No.'), show='headings')

        table.heading('Title', text='Title')
        table.heading('Edition', text='Edition')
        table.heading('Author', text='Author')
        table.heading('Year', text='Year')
        table.heading('ISBN', text='ISBN')
        table.heading('Material', text='Material')
        table.heading('Genre', text='Genre')
        table.heading('Shelf No.', text='Shelf No.')

        table.column('Title', width=150)
        table.column('Edition', width=80)
        table.column('Author', width=120)
        table.column('Year', width=90)
        table.column('ISBN', width=100)
        table.column('Material', width=100)
        table.column('Genre', width=120)
        table.column('Shelf No.', width=80)

        table.pack(side='left', fill='y')

        # Clear the table before populating it with new search results
        table.delete(*table.get_children())

        keyword = searchEntry.get()
        global option_value
        print(option_value)

        foundMatch = False
        for book in bookList:
            if option_value == "Title":
                attributeValue = book.title
            elif option_value == "Author":
                attributeValue = book.author
            elif option_value == "Year":
                attributeValue = book.yearPublished
            elif option_value == "Material":
                attributeValue = book.material
            elif option_value == "Genre":
                attributeValue = book.category
            else:
                attributeValue = book.title

            if keyword.lower() in attributeValue.lower():
                table.insert('', 'end', values=(book.title, book.edition, book.author, book.yearPublished, book.ISBN,
                                                book.material, book.category, book.shelfNo))
                foundMatch = True

        if not foundMatch:
           messagebox.showinfo("SEARCH BOOK", "NO MATCH FOUND ")


displayTable = DisplayTable()

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
window.title("TUP Reads")
image_path = relative_to_assets("TUP_Reads.png")
image = Image.open(image_path)
icon = ImageTk.PhotoImage(image)
window.iconphoto(True, icon)

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
gotoSearchBtn = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=gotoSearchBook,
    relief="flat",
    bg = "white"
)
gotoSearchBtn.place(x=20.0, y=199.0, width=160.0, height=32.0)

#BORROW BOOK

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
    command=gotoNotif,
    relief="flat",
    bg = "white"
)
image_2.place(x=993.0,y=30.0,width=38.0,height=43.0)

#HOME BUTTON
homeImage = PhotoImage(file=relative_to_assets("image_3.png"))
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
searchEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0
)
searchEntry.place(
    x=405.0,
    y=40.0,
    width=350.0,
    height=33.0
)


lastimg = PhotoImage(
    file=relative_to_assets("last.png"))
lastbg = canvas.create_image(
    910.0,
    542.5,
    image=lastimg
)
last = Entry(
    bd=0,
    bg="#4B0000",
    fg="#FFFFFF",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=8, weight="normal")
)
last.place(
    x=806.0,
    y=525.0,
    width=218.0,
    height=38.0
)

secondimg = PhotoImage(
    file=relative_to_assets("second.png"))
secondbg = canvas.create_image(
    640.0,
    542.5,
    image=secondimg
)
second = Entry(
    bd=0,
    bg="#4B0000",
    fg="#FFFFFF",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=8, weight="normal")
)
second.place(
    x=536.0,
    y=525.0,
    width=218.0,
    height=38.0
)

firstimg = PhotoImage(
    file=relative_to_assets("first.png"))
firstbg = canvas.create_image(
    369.0,
    542.5,
    image=firstimg
)
first = Entry(
    bd=0,
    bg="#4B0000",
    fg="#FFFFFF",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=8, weight="normal")
)
first.place(x=265.0, y=525.0, width=218.0,height=39.0)

bgimg = PhotoImage(
    file=relative_to_assets("bgimg.png"))
bg_bg = canvas.create_image(
    639.0,
    380.0,
    image=bgimg
)
displayTable.bookTable()
displayTable.recommendedBooks()

#CATEGORY DROPDOWN
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
categoryBtn = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=displayTable.dropdownMenu,
    relief="flat",
)
categoryBtn.place(
    x=907.0,
    y=100.0,
    width=173.0,
    height=20.0
)

#search book button
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
searchBtn= Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=displayTable.bookTable,
    relief="flat",
    bg="white"
)
searchBtn.place(x=758.0, y=40.0, width=80.0, height=35.0)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(250.0, 599.0, image=image_image_6)
# Move the image to the bottom of the stacking order
canvas.lower(image_6)


window.resizable(False, False)
window.mainloop()

