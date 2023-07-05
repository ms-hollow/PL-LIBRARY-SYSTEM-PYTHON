import os
import subprocess
from pathlib import Path
from tkinter import ttk, Menu, END, messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from PIL import Image, ImageTk
import CBook
from CBook import bookList

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "SearchBook"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def gotoTransaction():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "AdminManageTransaction.py")
    subprocess.run(["python", script_path])

def gotoStudent():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "AdminManageStudent.py")
    subprocess.run(["python", script_path])

def searchBook():
    print("Search Book")

def addBook():

    title = titleEntry.get()
    author = authorEntry.get()
    ISBN = isbnEntry.get()
    edition = editionEntry.get()
    yearPublished = yearEntry.get()
    material = materialEntry.get()
    category = genreEntry.get()
    shelfNo = shelfEntry.get()
    totalStocks = totalStocksEntry.get()
    noOfBorrower = noBorrowersEntry.get()

    if CBook.locateBook(ISBN) >= 0:  # if existing na sa bookList
        messagebox.showerror("ADD BOOK", "THE BOOK ALREADY EXISTS IN THE RECORD")
    elif not CBook.checkBookFields(title, author, ISBN, edition, yearPublished, material, category, shelfNo, totalStocks):  # if di complete fields
        messagebox.showerror("ADD BOOK", "PLEASE FILL IN ALL FIELDS")
    else:
        response = messagebox.askyesno(  # creates a yes or no message box
            title="ADD BOOK",
            message="ARE YOU SURE TO ADD THIS BOOK IN THE RECORD?",
            icon=messagebox.QUESTION
        )
        if response:  # if yes
            book = CBook.CBook(title, author, ISBN, edition, yearPublished, material, category, shelfNo, totalStocks, noOfBorrower)
            CBook.addBook(book)
            CBook.saveBook()
            messagebox.showinfo("ADD BOOK", "BOOK ADDED SUCCESSFULLY")
            clearFields()
            bookTable()

def updateBook():

    title = titleEntry.get()
    author = authorEntry.get()
    ISBN = isbnEntry.get()
    edition = editionEntry.get()
    yearPublished = yearEntry.get()
    material = materialEntry.get()
    category = genreEntry.get()
    shelfNo = shelfEntry.get()
    totalStocks = totalStocksEntry.get()
    noOfBorrower = noBorrowersEntry.get()

#IF PININDOT UPDATE BOOK:
    index = CBook.locateBook(ISBN)

    if index <0:
        messagebox.showerror("UPDATE BOOK", "THE ISBN DOES NOT FOUND A MATCH")
    elif not CBook.checkBookFields(title, author, ISBN, edition, yearPublished, material, category, shelfNo, totalStocks):
        messagebox.showerror("UPDATE BOOK", "PLEASE FILL IN ALL FIELDS")
    else:
        response = messagebox.askyesno(  # creates a yes or no message box
            title="UPDATE BOOK",
            message="ARE YOU SURE TO UPDATE THIS BOOK IN THE RECORD?",
            icon=messagebox.QUESTION
        )
        if response:  # if yes, salin new info
            bookList[index].title = title
            bookList[index].author = author
            bookList[index].ISBN = ISBN
            bookList[index].edition = edition
            bookList[index].yearPublished = yearPublished
            bookList[index].material = material
            bookList[index].category = category
            bookList[index].shelfNo = shelfNo
            bookList[index].totalStocks = totalStocks
            bookList[index].noOfBorrower = noOfBorrower

            messagebox.showinfo("UPDATE BOOK", "BOOK UPDATED SUCCESSFULLY! ")
            CBook.saveBook()
            bookTable()
            clearFields()

def deleteBook():

    ISBN = isbnEntry.get()
    CBook.deleteBook(ISBN)
    bookTable()
    clearFields()

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

def on_table_select(table):
    selected_item = table.focus()  # Get the selected item (row) in the table
    values = table.item(selected_item)["values"]  # Get the values of the selected item
    if values:  # Check if values exist (a row is selected)
        clearFields()
        titleEntry.insert(0, values[0])
        authorEntry.insert(0, values[1])
        isbnEntry.insert(0, values[2])
        editionEntry.insert(0, values[3])
        yearEntry.insert(0, values[4])
        materialEntry.insert(0, values[5])
        genreEntry.insert(0, values[6])
        shelfEntry.insert(0, values[7])

        index = CBook.locateBook(isbnEntry.get())
        totalStocksEntry.insert(0, bookList[index].totalStocks)
        noBorrowersEntry.insert(0, bookList[index].noOfBorrower)
        currentStock = str(int(bookList[index].totalStocks) - int(bookList[index].noOfBorrower))
        currentStocksEntry.insert(0, currentStock)
        #INSERT HERE SA CURRENT STOCKS
        #currentStocksEntry.put()


def bookTable():
    # TABLE SEARCH BOOK
    sub_frame = ttk.Frame(window, width=600, height=350.0)
    sub_frame.place(x=220, y=150)

    # treeview
    table = ttk.Treeview(sub_frame,
                         columns=('Title', 'Edition', 'Author', 'Year', 'ISBN',
                                  'Material', 'Category', 'Shelf No.'), show='headings')
    table.heading('Title', text='Title')
    table.heading('Edition', text='Edition')
    table.heading('Author', text='Author')
    table.heading('Year', text='Year')
    table.heading('ISBN', text='ISBN')
    table.heading('Material', text='Material')
    table.heading('Category', text='Category')
    table.heading('Shelf No.', text='Shelf No.')

    table.column('Title', width=150)
    table.column('Edition', width=80)
    table.column('Author', width=120)
    table.column('Year', width=90)
    table.column('ISBN', width=100)
    table.column('Material', width=100)
    table.column('Category', width=120)
    table.column('Shelf No.', width=80)

    table.pack(side='left', fill='y')
    # Bind the function to the table's selection event
    table.bind("<<TreeviewSelect>>", lambda event: on_table_select(table))

    # Add retrieved books to the table
    for book in bookList:
        table.insert('', 'end', values=(book.title, book.edition, book.author, book.yearPublished, book.ISBN,
                                        book.material, book.category, book.shelfNo))


def clearFields():
    titleEntry.delete(0, END)  # Clear the contents of the Entry widget
    editionEntry.delete(0, END)
    yearEntry.delete(0, END)
    authorEntry.delete(0, END)
    shelfEntry.delete(0, END)
    currentStocksEntry.delete(0, END)
    noBorrowersEntry.delete(0, END)
    totalStocksEntry.delete(0, END)
    isbnEntry.delete(0, END)
    materialEntry.delete(0, END)
    genreEntry.delete(0, END)

CBook.retrieveBook()
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

manageBookIcon = PhotoImage(file=relative_to_assets("manageBook.png"))
manageBook = Button(
    image=manageBookIcon,
    borderwidth=0,
    highlightthickness=0,
    #command=lambda: print("button_1 clicked"),
    relief="flat",
    bg = "white"
)
manageBook.place(x=20.0, y=145.0, width=160.0, height=40.0)

manageTransactionIcon = PhotoImage(file=relative_to_assets("manageTransactions.png"))
manageTransation = Button(
    image=manageTransactionIcon,
    borderwidth=0,
    highlightthickness=0,
    command=gotoTransaction,
    relief="flat",
    bg="white"
)
manageTransation.place(
    x=12.0,
    y=199.0,
    width=177.0,
    height=32.0
)

manageStudentIcon= PhotoImage(file=relative_to_assets("manageStudent.png"))
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

canvas.create_text(250.0, 17.0, anchor="nw", text="BOOK", fill="#4B0000", font= font.Font(family="Poppins", size=40, weight="bold"))

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
    command=gotoLogout,
    relief="flat",
    bg = "white"
)
image_5.place(x=1054.0, y=30.0, width=43.0, height=43.0)
bookTable()

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(350.5, 455.0, image=entry_image_1)
titleEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="normal")
)
titleEntry.place(x=230.0, y=445.0, width=241.0, height=24.0)

canvas.create_text(220.0, 415.0, anchor="nw", text="Title", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(280.0, 575.0, image=entry_image_2)
editionEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="normal")
)
editionEntry.place(x=230.0, y=565.0, width=100.0, height=24.0)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(425.0, 575.0, image=entry_image_3)

yearEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="normal")
)
yearEntry.place(x=375.0, y=565.0, width=100.0, height=24.0)

canvas.create_text(220.0, 535.0, anchor="nw", text="Edition", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

canvas.create_text(365.0, 535.0, anchor="nw", text="Year Published", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(350.5, 515.0, image=entry_image_4)
authorEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="normal")
)
authorEntry.place(x=230.0, y=505.0, width=241.0, height=24.0)

canvas.create_text(220.0, 475.0, anchor="nw", text="Author", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(929.5, 455.0, image=entry_image_5)
shelfEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="normal")
)
shelfEntry.place(x=809.0, y=445.0, width=241.0, height=24.0)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(859.0, 575.0, image=entry_image_6)
currentStocksEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="normal")
)
currentStocksEntry.place(x=809.0, y=565.0, width=100.0, height=24.0)

entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(999.0, 575.0, image=entry_image_7)
noBorrowersEntry= Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="normal")
)
noBorrowersEntry.place(x=949.0, y=565.0, width=100.0, height=24.0)

canvas.create_text(804.0, 535.0, anchor="nw", text="Current Stocks", fill="#4B0000", font=font.Font(family="Poppins", size=10, weight="bold"))

canvas.create_text(944.0, 535.0, anchor="nw", text="No. of Borrowers", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(929.5, 515.0, image=entry_image_8)
totalStocksEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="normal")
)
totalStocksEntry.place(x=809.0, y=505.0, width=241.0, height=24.0)

canvas.create_text(799.0, 475.0, anchor="nw", text="Total Stocks", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

canvas.create_text(804.0, 415.0, anchor="nw", text="Shelf Number", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(640.5, 455.0, image=entry_image_9)
isbnEntry= Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="normal")
)
isbnEntry.place(x=520.0, y=445.0, width=241.0, height=24.0)

canvas.create_text(510.0, 415.0, anchor="nw", text="ISBN", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(640.5, 515.0,image=entry_image_10)

materialEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="normal")
)
materialEntry.place(x=520.0, y=505.0, width=241.0, height=24.0)

canvas.create_text(510.0, 475.0, anchor="nw", text="Material", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_11 = PhotoImage(file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(640.5, 575.0, image=entry_image_11)

genreEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=10, weight="normal")
)
genreEntry.place(x=520.0, y=565.0, width=241.0, height=24.0)

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
    font=font.Font(family="Poppins", size=10, weight="normal")
)
searchEntry.place(x=460.0, y=43.0, width=290.0, height=30.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
categoryBtn = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=dropdownMenu,
    relief="flat"
)
categoryBtn.place(x=908.0, y=99.0, width=173.0, height=20.0)

refreshBtnImage = PhotoImage(file=relative_to_assets("refresh.png"))
refreshBtn = Button(
    image=refreshBtnImage,
    borderwidth=0,
    highlightthickness=0,
    command=updateBook,
    relief="flat",
    bg="white"
)
refreshBtn.place(x=921.0, y=606.0, width=42.0,height=42.0)

addBtnImage= PhotoImage(file=relative_to_assets("add.png"))
addBtn = Button(
    image=addBtnImage,
    borderwidth=0,
    highlightthickness=0,
    command=addBook,
    relief="flat"
)
addBtn.place(x=968.0, y=605.0, width=42.0, height=42.0)

deleteBtnImage = PhotoImage(file=relative_to_assets("delete.png"))
deleteBtn = Button(
    image=deleteBtnImage,
    borderwidth=0,
    highlightthickness=0,
    command=deleteBook,
    relief="flat",
    bg="white"
)
deleteBtn.place(x=1018.0, y=605.0, width=42.0, height=42.0)

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

window.resizable(False, False)
window.mainloop()
