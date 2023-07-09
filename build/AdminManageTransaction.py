import os
import subprocess
from pathlib import Path
from tkinter import ttk, Menu, StringVar, messagebox, END
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from PIL import Image, ImageTk
import CTransaction, CBook, CBorrower
from CTransaction import transactionList

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "SearchBook"

option_value = ""
status_value = ""
currentStatus =""

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

def getSummary():
    print("get summary")

def updateTransaction():
    from CBorrower import borrowerList
    from CBook import bookList

    title = titleEntry.get()
    ISBN = isbnEntry.get()
    TUP_ID = tupidEntry.get()
    dateBorrowed = dateborrowedEntry.get()
    dateToReturn =dateReturnEntry.get()
    refNum = referenceNumEntry.get()
    borrower = borrowerEntry.get()
    author = authorEntry.get()
    librarian = librarianEntry.get()
    fine = fineEntry.get()

    # IF PININDOT UPDATE BORROWER:
    index = CTransaction.locateTransaction(refNum)

    if index < 0:
        messagebox.showerror("UPDATE TRANSACTION", "THE REFERENCE NUMBER DOES NOT FOUND A MATCH")
    elif not CTransaction.checkTransactionFields(title, ISBN, TUP_ID, dateBorrowed, dateToReturn, status, refNum, borrower, author, librarian, fine):
        messagebox.showerror("UPDATE TRANSACTION", "PLEASE FILL IN ALL FIELDS")
    else:
        response = messagebox.askyesno(  # creates a yes or no message box
            title="UPDATE TRANSACTION",
            message="ARE YOU SURE TO UPDATE THIS TRANSACTION IN THE RECORD?",
            icon=messagebox.QUESTION
        )
        if response:  # if yes, salin new info
            transactionList[index].title = title
            transactionList[index].ISBN = ISBN
            transactionList[index].TUP_ID = TUP_ID
            transactionList[index].dateBorrowed = dateBorrowed
            transactionList[index].dateToReturn = dateToReturn
            transactionList[index].status = status_value
            transactionList[index].refNum = refNum
            transactionList[index].borrower = borrower
            transactionList[index].author = author
            transactionList[index].librarian = librarian
            transactionList[index].fine = fine

            messagebox.showinfo("UPDATE TRANSACTION", "TRANSACTION UPDATED SUCCESSFULLY! ")
            CTransaction.saveTransaction()
            displayTable.bookTable()
            clearFields()


            #IF INUPDATE SA "RETURNED"
            newStatus = status_value
            if (currentStatus == "TO APPROVE" or currentStatus == "TO RETURN") and newStatus == "RETURNED":
                    indexBook = CBook.locateBook(ISBN)
                    bookList[indexBook].noOfBorrower = int(bookList[indexBook].noOfBorrower) - 1  #if ni-return, babawasan noOfBorrower ng book
                    CBook.saveBook()
                    #indexBorrower = CBorrower.locateBorrower(TUP_ID)
                    #borrowerList[indexBorrower].noOfBorrowed -= 1       #if ni-return, babawasan noOfBorrowed ng borrower
                    #CBorrower.saveBorrower()





def deleteTransaction():
    refNum = referenceNumEntry.get()
    CTransaction.deleteTransaction(refNum)
    displayTable.bookTable()
    # TO DELETE FIELDS
    clearFields()

def dropdownStatus():
    # Create a dropdown menu
    dropdownmenu = Menu(window, tearoff=False, font=("Poppins", 10, "bold"))  # Set custom font and size
    dropdownmenu.configure(bg="#4B0000", fg="#C19A6B")
    options = ["TO APPROVE", "TO RETURN", "RETURNED"]

    def on_option_selected(option):
        global status_value
        status_value = option
        print("Selected Option:", option)
    # Add options to the dropdown menu
    for option in options:
        dropdownmenu.add_command(label=option, command=lambda opt=option: on_option_selected(opt))
    dropdownmenu.post(status.winfo_rootx(), status.winfo_rooty() + status.winfo_height())

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

class DisplayTable:

    def __init__(self):
        self.choice = 0  # Initialize the instance variable

    def dropdownMenu(self):
        # Create a dropdown menu
        dropdownmenu = Menu(window, tearoff=False, font=("Poppins", 10, "bold"))  # Set custom font and size
        dropdownmenu.configure(bg="#4B0000", fg="#C19A6B")  # Set background and foreground colors

        # List of options for the dropdown menu
        options = ["Title", "ISBN", "TUP ID", "Date Borrowed", "Date to Return", "Status"]  # Add your options here

        # Create a StringVar outside the function to store the selected option
        clicked = StringVar()

        # Function to be executed when an option is selected from the dropdown
        def on_option_selected(option):
            self.choice = options.index(option) + 1
            #print(option)  # Print the selected option
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
            DisplayTable.enableEntries(self)
            clearFields()
            titleEntry.insert(0, values[0])
            isbnEntry.insert(0, values[1])
            tupidEntry.insert(0, values[2])
            dateborrowedEntry.insert(0, values[3])
            dateReturnEntry.insert(0, values[4])
            referenceNumEntry.insert(0, values[6])

            index = CTransaction.locateTransaction(referenceNumEntry.get())
            borrowerEntry.insert(0, transactionList[index].borrower)
            authorEntry.insert(0, transactionList[index].author)
            librarianEntry.insert(0, transactionList[index].librarian)
            fineEntry.insert(0, transactionList[index].fine)

            remainingDays = str(CTransaction.calculateRemainingDays(values[4]))
            remainingDaysEntry.insert(0, remainingDays)
            DisplayTable.disableEntries(self)
            global currentStatus
            currentStatus = values[5]       #para makuha ang current status, since walan siyang entry. Para ito sa if babaguhin status to return.

    def enableEntries(self):
        titleEntry.config(state="normal")
        isbnEntry.config(state="normal")
        tupidEntry.config(state="normal")
        dateborrowedEntry.config(state="normal")
        referenceNumEntry.config(state="normal")
        borrowerEntry.config(state="normal")
        authorEntry.config(state="normal")
        librarianEntry.config(state="normal")
        fineEntry.config(state="normal")
        remainingDaysEntry.config(state="normal")

    def disableEntries(self):
        titleEntry.config(state="disable")
        isbnEntry.config(state="disable")
        tupidEntry.config(state="disable")
        dateborrowedEntry.config(state="disable")
        referenceNumEntry.config(state="disable")
        borrowerEntry.config(state="disable")
        authorEntry.config(state="disable")
        librarianEntry.config(state="disable")
        fineEntry.config(state="disable")
        remainingDaysEntry.config(state="disable")

    def bookTable(self):
        # TABLE SEARCH BORROWER
        sub_frame = ttk.Frame(window, width=600, height=350.0)
        sub_frame.place(x=220, y=150)

        # Create the table outside the loop
        table = ttk.Treeview(sub_frame,
                             columns=('Title', 'ISBN', 'TUP ID', 'Date Borrowed', 'Date To Return',
                                      'Status', 'Reference No.'), show='headings')

        table.heading('Title', text='Title')
        table.heading('ISBN', text='ISBN')
        table.heading('TUP ID', text='TUP ID')
        table.heading('Date Borrowed', text='Date Borrowed')
        table.heading('Date To Return', text='Date To Return')
        table.heading('Status', text='Status')
        table.heading('Reference No.', text='Reference No')

        table.column('Title', width=180)
        table.column('ISBN', width=120)
        table.column('TUP ID', width=120)
        table.column('Date Borrowed', width=100)
        table.column('Date To Return', width=100)
        table.column('Status', width=100)
        table.column('Reference No.', width=120)

        table.pack(side='left', fill='y')
        # Bind the function to the table's selection event
        table.bind("<<TreeviewSelect>>", lambda event: self.on_table_select(table))

        # Clear the table before populating it with new search results
        table.delete(*table.get_children())

        keyword = searchEntry.get()
        global option_value
        print(option_value)

        foundMatch = False
        for transaction in transactionList:
            if option_value == "Title":
                attributeValue = transaction.title
            elif option_value == "ISBN":
                attributeValue = transaction.ISBN
            elif option_value == "TUP ID":
                attributeValue = transaction.TUP_ID
            elif option_value == "Date Borrowed":
                attributeValue = transaction.dateBorrowed
            elif option_value == "Date To Return":
                attributeValue = transaction.dateToReturn
            elif option_value == "Status":
                attributeValue = transaction.status
            else:
                attributeValue = transaction.title

            if keyword.lower() in attributeValue.lower():
                table.insert('', 'end', values=(
                transaction.title, transaction.ISBN, transaction.TUP_ID, transaction.dateBorrowed,
                transaction.dateToReturn,
                transaction.status, transaction.refNum))
                foundMatch = True

        if not foundMatch:
            messagebox.showinfo("SEARCH BORROWER", "NO MATCH FOUND ")


# Create an instance of DisplayTable class
displayTable = DisplayTable()

def clearFields():
    displayTable.enableEntries()
    titleEntry.delete(0, END)  # Clear the contents of the Entry widget
    isbnEntry.delete(0, END)
    tupidEntry.delete(0, END)
    dateborrowedEntry.delete(0, END)
    dateReturnEntry.delete(0, END)
    referenceNumEntry.delete(0, END)
    borrowerEntry.delete(0, END)
    authorEntry.delete(0, END)
    librarianEntry.delete(0, END)
    fineEntry.delete(0, END)
    remainingDaysEntry.delete(0, END)



# UNANG MAGRA-RUN
CBook.retrieveBook()
CTransaction.retrieveTransaction()

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
    # command=lambda: print("button_2 clicked"),
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

sumrepimg = PhotoImage(file=relative_to_assets("sumrepo.png"))
sumrep = Button(
    image=sumrepimg,
    borderwidth=0,
    highlightthickness=0,
    command=getSummary,
    relief="flat",
    bg="white"
)
sumrep.place(x=19.0, y=305.0, width=160.0,height=40.0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(250.0, 599.0, image=image_image_1)

image_2_path = relative_to_assets("image_2.png")
image_2 = Image.open(image_2_path)
max_width = 182
max_height = 112
image_2.thumbnail((max_width, max_height), Image.LANCZOS)
resizedlogo = ImageTk.PhotoImage(image_2)
image_2 = canvas.create_image(120.0, 59.0, image=resizedlogo)

canvas.create_text(218.0, 19.0, anchor="nw", text="TRANSACTION", fill="#4B0000",
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

entry_image_1 = PhotoImage(file=relative_to_assets("searchEntry.png"))
entry_bg_1 = canvas.create_image(700.0, 55.5, image=entry_image_1)
searchEntry = Entry(
    bd=0,
    bg="#FFFDFD",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
searchEntry.place(x=620.0, y=40.0, width=160.0, height=30.0)

displayTable.bookTable()
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

statusIcon = PhotoImage(file=relative_to_assets("statusdropdown.png"))
status = Button(
    image=statusIcon,
    borderwidth=0,
    highlightthickness=0,
    command=dropdownStatus,
    relief="flat",
    bg="white"
)
status.place(x=961.0, y=560.0, width=99.0, height=30.0)

font_style = font.Font(family="Poppins", size=11, weight="bold")

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
    command=displayTable.bookTable,
    relief="flat"
)
searchBtn.place(x=790.0, y=38.0, width=80.0, height=35.0)

entry_image_2 = PhotoImage(file=relative_to_assets("titleEntry.png"))
entry_bg_2 = canvas.create_image(
    350.5,
    455.0,
    image=entry_image_2
)
titleEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
titleEntry.place(x=230.0, y=444.0, width=241.0, height=23.0)

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
dateborrowedEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
dateborrowedEntry.place(x=230.0, y=564.0, width=106.0, height=23.0)

entry_image_4 = PhotoImage(file=relative_to_assets("dateReturnEntry.png"))
entry_bg_4 = canvas.create_image(
    420.0,
    575.0,
    image=entry_image_4
)
dateReturnEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
dateReturnEntry.place(x=370.0, y=564.0, width=100.0, height=23.0)

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
authorEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
authorEntry.place(x=230.0, y=504.0, width=241.0, height=23.0)

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
remainingDaysEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
remainingDaysEntry.place(x=809.0, y=564.0, width=115.0, height=23.0)

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
librarianEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
librarianEntry.place(x=809.0, y=504.0, width=241.0, height=23.0)

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
isbnEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
isbnEntry.place(x=520.0, y=444.0, width=241.0, height=23.0)

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
tupidEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
tupidEntry.place(x=520.0, y=504.0, width=241.0, height=23.0)

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
borrowerEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
borrowerEntry.place(x=520.0, y=564.0, width=241.0, height=23.0)

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
    command=updateTransaction,
    relief="flat"
)
refresh.place(x=965.0, y=606.0, width=42.0, height=41.671875)

button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
delete = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=deleteTransaction,
    relief="flat"
)
delete.place(x=1019.0, y=606.0, width=42.0, height=42.0)

referenceIcon = PhotoImage(file=relative_to_assets("referenceNumEntry.png"))
entry_bg_1 = canvas.create_image(
    874.0,
    455.0,
    image=referenceIcon
)
referenceNumEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
referenceNumEntry.place(x=809.0, y=441.0, width=130.0, height=28.0)

canvas.create_text(799.0, 415.0, anchor="nw", text="Reference Number", fill="#4B0000", font=font_style)

fineIcon = PhotoImage(file=relative_to_assets("fineEntry.png"))
entry_bg_2 = canvas.create_image(1015.0, 455.0, image=fineIcon)

fineEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Poppins", size=11, weight="normal")
)
fineEntry.place(x=980.0, y=441.0, width=70.0, height=28.0)

canvas.create_text(970.0, 415.0, anchor="nw", text="Fine", fill="#4B0000", font=font_style)

window.resizable(False, False)
window.mainloop()