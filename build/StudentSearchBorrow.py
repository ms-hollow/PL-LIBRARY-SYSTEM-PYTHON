import os
import subprocess
from pathlib import Path
from tkinter import ttk, Menu, END, messagebox, OptionMenu, StringVar
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from PIL import Image, ImageTk
import CBook, CTransaction, CBorrower
from CBook import bookList
import CTransaction
from CTransaction import transactionList
from CBorrower import borrowerList

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "SearchBook"

option_value = ""

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def gotoDisplayBooks():

    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "StudentDisplayBook.py")
    subprocess.run(["python", script_path])


def borrowBook():

    CTransaction.getInfoTransaction(str(isbnEntry.get()))

    #current_directory = os.path.dirname(os.path.abspath(__file__))
    #script_path = os.path.join(current_directory, "StatementTrans.py") #TINAWAG YUNG SUMMARY
    #subprocess.run(["python", script_path])

def getISBN():
    ISBN = isbnEntry.get()
    return ISBN

def gotoLogin():
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

        # Return the StringVar 'clicked' so that it can be accessed outside the method
        return clicked

    def on_table_select(self, table):
        selected_item = table.focus()  # Get the selected item (row) in the table
        values = table.item(selected_item)["values"]  # Get the values of the selected item
        if values:  # Check if values exist (a row is selected)

            DisplayTable.enableEntries(self)  # enable
            clearFields()  # clear lahat
            titleEntry.insert(0, values[0])
            editionEntry.insert(0, values[1])
            authorEntry.insert(0, values[2])
            yearEntry.insert(0, values[3])
            isbnEntry.insert(0, values[4])
            materialEntry.insert(0, values[5])
            genreEntry.insert(0, values[6])
            shelfEntry.insert(0, values[7])

            index = CBook.locateBook(isbnEntry.get())
            totalStocksEntry.insert(0, bookList[index].totalStocks)
            noBorrowersEntry.insert(0, bookList[index].noOfBorrower)
            currentStock = str(int(bookList[index].totalStocks) - int(bookList[index].noOfBorrower))
            currentStocksEntry.insert(0, currentStock)

            DisplayTable.disableEntries(self)  # disable

    def enableEntries(self):
        titleEntry.config(state="normal")
        authorEntry.config(state="normal")
        isbnEntry.config(state="normal")
        editionEntry.config(state="normal")
        yearEntry.config(state="normal")
        materialEntry.config(state="normal")
        shelfEntry.config(state="normal")
        totalStocksEntry.config(state="normal")
        noBorrowersEntry.config(state="normal")
        currentStocksEntry.config(state="normal")
        genreEntry.config(state="normal")

    def disableEntries(self):
        titleEntry.config(state="disable")
        authorEntry.config(state="disable")
        isbnEntry.config(state="disable")
        editionEntry.config(state="disable")
        yearEntry.config(state="disable")
        materialEntry.config(state="disable")
        shelfEntry.config(state="disable")
        totalStocksEntry.config(state="disable")
        noBorrowersEntry.config(state="disable")
        currentStocksEntry.config(state="disable")
        genreEntry.config(state="disable")

    def bookTable(self):
        # TABLE SEARCH BOOK
        sub_frame = ttk.Frame(window, width=600, height=350.0)
        sub_frame.place(x=220, y=150)

        # Create the table outside the loop
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

        table.column('Title', width=250)
        table.column('Edition', width=50)
        table.column('Author', width=120)
        table.column('Year', width=50)
        table.column('ISBN', width=100)
        table.column('Material', width=100)
        table.column('Category', width=100)
        table.column('Shelf No.', width=70)

        table.pack(side='left', fill='y')
        # Bind the function to the table's selection event
        table.bind("<<TreeviewSelect>>", lambda event: self.on_table_select(table))

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


# Create an instance of DisplayTable class
displayTable = DisplayTable()
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
CBorrower.retrieveBorrower()
CTransaction.retrieveTransaction()
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

window.title("TUP Reads")
image_path = relative_to_assets("TUP_Reads.png")
image = Image.open(image_path)
icon = ImageTk.PhotoImage(image)
window.iconphoto(True, icon)

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
    command=displayTable.bookTable,
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

image_5.place(x=1054.0, y=30.0, width=43.0, height=43.0)
displayTable.bookTable()

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(350.5, 455.0, image=entry_image_1)
titleEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
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
    font=font.Font(family="Poppins", size=9, weight="normal")
)
editionEntry.place(x=230.0, y=565.0, width=100.0, height=24.0)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(425.0, 575.0, image=entry_image_3)

yearEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
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
    font=font.Font(family="Poppins", size=9, weight="normal")
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
    font=font.Font(family="Poppins", size=9, weight="normal")
)
shelfEntry.place(x=809.0, y=445.0, width=241.0, height=24.0)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(859.0, 575.0, image=entry_image_6)
currentStocksEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
currentStocksEntry.place(x=809.0, y=565.0, width=100.0, height=24.0)

entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(999.0, 575.0, image=entry_image_7)
noBorrowersEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
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
    font=font.Font(family="Poppins", size=9, weight="bold")
)
totalStocksEntry.place(x=809.0, y=505.0, width=241.0, height=24.0)

canvas.create_text(799.0, 475.0, anchor="nw", text="Total Stocks", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

canvas.create_text(804.0, 415.0, anchor="nw", text="Shelf Number", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(640.5, 455.0, image=entry_image_9)
isbnEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
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
    font=font.Font(family="Poppins", size=9, weight="normal")
)
materialEntry.place(x=520.0, y=501.0, width=241.0, height=24.0)

canvas.create_text(510.0, 475.0, anchor="nw", text="Material", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

entry_image_11 = PhotoImage(file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(640.5, 575.0, image=entry_image_11)

genreEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=9, weight="normal")
)
genreEntry.place(x=520.0, y=565.0, width=241.0, height=24.0)

canvas.create_text(515.0, 535.0, anchor="nw", text="Genre", fill="#4B0000", font= font.Font(family="Poppins", size=10, weight="bold"))

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(641.0, 264.0, image=image_image_6)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
categoryBtn = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=displayTable.dropdownMenu,
    relief="flat"
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
    command=displayTable.bookTable,
    relief="flat",
    bg="white"
)
searchBtn.place(x=758.0, y=39.0, width=80.0,height=35.0)

window.resizable(False, False)
window.mainloop()
