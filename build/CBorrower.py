import csv
from tkinter import messagebox

borrowerList = []     #Initializing an empty list of Cborrower objects          datasruct: list
loggedInAccount = 0     #once na nakapag-log in, di na magpapa-enter uli ng TUP_ID, ito na yung index na gagamitin

class CBorrower:
    # Object Constructor
    def __init__(self, name, TUP_ID, password, yearSection, contactNum, email, noOfBorrowed, borrowedBook = []) :
        self.name = name
        self.TUP_ID = TUP_ID
        self.password = password
        self.yearSection = yearSection
        self.contactNum = contactNum
        self.email = email
        self.noOfBorrowed = noOfBorrowed
        self.borrowedBook = []

    #lahat ng mga naka-indent dito ay kasama sa Cborrower Class

#######################  METHODS   ##############################################
def getInfoBorrower():
    print("ENTER COMPLETE INFORMATION BELOW")
    TUP_ID = input("Enter your TUP_ID: ")
    name = input("Enter your name: ")
    yearSection = input("Enter your Year and Section: ")
    contactNum = input("Enter your contact number: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    repassword = input("Re-enter password: ")
    noOfBorrowed = 0

    if locateBorrower(TUP_ID) >= 0:               #if existing na sa borrowerList
        messagebox.showerror("REGISTRATION ", "YOUR TUP ID IS ALREADY REGISTERED")
    elif not checkBorrowerFields(name, TUP_ID, password, yearSection, contactNum, email):    #if di complete fields
        messagebox.showerror("REGISTRATION", "PLEASE FILL IN ALL THE FIELDS")
    elif len(TUP_ID) != 6:
        messagebox.showerror("REGISTRATION", "TUP ID MUST BE 6 DIGITS LONG")
    elif password != repassword:
        messagebox.showerror("REGISTRATION", "PASSWORD DIDN'T MATCH")
    else:
        response = messagebox.askyesno(    #creates a yes or no message box
            title="Confirmation",
            message="DO YOU WANT TO SUBMIT YOUR REGISTRATION?",
            icon=messagebox.QUESTION

        )
        if response:                        #if yes
            borrower = CBorrower(name, TUP_ID, password, yearSection, contactNum, email, noOfBorrowed)
            addBorrower(borrower)
            saveBorrower()
            messagebox.showinfo("REGISTRATION", "YOUR ACCOUNT IS SUCCESSFULLY REGISTERED!")

def getLoggedInIndex():
    return loggedInAccount
def setLoggedInIndex(index):
    global loggedInAccount
    loggedInAccount = index

def addBorrower(borrower):
    # Find the index to insert the borrower alphabetically based on the name
    index = 0
    while index < len(borrowerList) and borrower.name > borrowerList[index].name:
        index += 1
    # Insert the borrower at the determined index
    borrowerList.insert(index, borrower)
    #Note: Pakitawag ang saveBorrower() after mag-add ng borrower sa main.

def deleteBorrower(TUP_ID):
    #ISBN = input("Enter the ISBN of the book you want to delete: ")

#IF PININDOT DELETE BOOK:
    index = locateBorrower(TUP_ID)
    if index <0:
        messagebox.showerror("DELETE  BORROWER", "THE BORROWER DOES NOT FOUND A MATCH")
    #INSERT IF WALANG SINELECT NA ROW

    else:
        response = messagebox.askyesno(  # creates a yes or no message box
            title="DELETE BORROWER",
            message="ARE YOU SURE TO DELETE THIS BORROWER IN THE RECORD?",
            icon=messagebox.QUESTION
        )

        if response:
            deleted_borrower = borrowerList.pop(index)
            messagebox.showinfo("DELETE BOOK", "BOOK DELETED SUCCESSFULLY! ")
            saveBorrower()
            #display Table
            #clear fields

def locateBorrower(TUP_ID):
                print(loggedInAccount)
                for i in range(len(borrowerList)):  # loop through the borrowerList
                    if borrowerList[i].TUP_ID == TUP_ID:  # if nahanap, return index, else return -1
                        return i

                return -1

def displayBorrower():
    for borrower in borrowerList:
        print(borrower.name +" "+ borrower.TUP_ID +" "+ borrower.yearSection +" " + borrower.contactNum + " " +borrower.email)


changePassTries = 3
def changePass():

        global changePassTries

        #TUP_ID = input("Enter your TUP ID:")
        currentPass = input("Enter current password: ")
        newPass = input("Enter new password: ")
        reEnterPass = input("Re-enter new password: ")

        index = loggedInAccount

        if index < 0:
            messagebox.showerror("CHANGE PASSWORD", "ACCOUNT NOT FOUND")
        elif currentPass != borrowerList[index].password:
            messagebox.showerror("CHANGE PASSWORD", "INCORRECT CURRENT PASSWORD")
            changePassTries -= 1
        elif newPass != reEnterPass:
            messagebox.showerror("CHANGE PASSWORD", "NEW PASSWORD DOESN'T MATCH THE RE-ENTERED PASSWORD!")
        elif currentPass == newPass:
            messagebox.showerror("CHANGE PASSWORD", "YOU CAN'T CHANGE IT TO YOUR CURRENT PASSWORD")
        else:
            response = messagebox.askyesno(  # creates a yes or no message box
                title="CHANGE PASSWORD",
                message="CONFIRM CHANGES?",
                icon=messagebox.QUESTION
            )
            if response:
                borrowerList[index].password = newPass      #set password to new pass
                saveBorrower()
                messagebox.showinfo("CHANGE PASSWORD", "YOUR PASSWORD HAS BEEN SUCCESSFULLY CHANGED!")
                #CLEAR FIELDS

        if changePassTries == 0:
            messagebox.showerror("CHANGE PASSWORD", "YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIES. TRY AGAIN LATER")
            #EXIT FRAME
def updateBorrower():
    #TUP_ID = input("ENTER TUP ID: ")
    index = loggedInAccount

    if index >= 0:  # if existing ang STUDENT
        print("[1] NAME\n[2] TUP ID\n[3] YEAR AND SECTION\n[4]CONTACT NUMBER\n[5] EMAIL\n[6] CHANGE PASSWORD\n")
        attributeChoice = int(input("ENTER ATTRIBUTE TO UPDATE: "))

        print("ENTER THE UPDATED INFORMATION: ")
        if attributeChoice > 7:
            updatedInfoInt = int(input())
        else:
            updatedInfo = input()

        #CONFIRM UPDATE
        response = messagebox.askyesno(  # creates a yes or no message box
            title="Confirmation",
            message="ARE YOU SURE TO UPDATE THE INFORMATION?",
            icon=messagebox.QUESTION
        )

        if response:
            if attributeChoice == 1:
                borrowerList[index].name = updatedInfo
            elif attributeChoice == 2:
                borrowerList[index].TUP_ID = updatedInfo
            elif attributeChoice == 3:
                borrowerList[index].yearSection = updatedInfo
            elif attributeChoice == 4:
                borrowerList[index].contactNum = updatedInfo
            elif attributeChoice == 5:
                borrowerList[index].email = updatedInfo
            elif attributeChoice == 6:
                changePass()

            saveBorrower()
            messagebox.showinfo("UPDATE BORROWER INFORMATION ", "UPDATED SUCCESSFULLY!")

    else:
        print("STUDENT NOT FOUND!")


#login
def logInBorrower():
    tries = 3
    exit = False

    while tries > 0 and exit == False:
        print("LOG IN STUDENT")
        enteredID = input("TUP ID (Ex. 123456): TUP-M ")
        enteredPass = input("PASSWORD: ")

        index = locateBorrower(enteredID)

        if index >= 0 and enteredPass == borrowerList[index].password:
            print("LOG IN SUCCESSFULLY!")
            exit = True
            saveBorrower()
            global loggedInAccount      #accessing global variable
            loggedInAccount = index     #modifying global variable
            exit = True

        else:
            print("INCORRECT TUP ID OR PASSWORD")
            tries -= 1
            print("YOU HAVE", tries, "TRIES LEFT.")
            print()

        if tries == 0:
            print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIES.")
            exit = True

def logInAdmin():
    tries = 3
    exit = False

    while tries > 0 and exit == False:
        print("LOG IN ADMIN")
        enteredUsername = input("Username: ")
        enteredPass = input("PASSWORD: ")

        if enteredUsername == "ADMIN" and enteredPass == "1234":
            print("LOG IN SUCCESSFULLY!")
            exit = True
            # PUNTA SA STUDENT PORTAL
            # loggedInIndex = index
        else:
            print("INCORRECT USERNAME OR PASSWORD")
            tries -= 1
            print("YOU HAVE", tries, "TRIES LEFT.")
            print()

        if tries == 0:
            print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIES.")
            exit = True

def searchBorrower():
    print("Select an attribute for searching")
    print("[1] Name")
    print("[2] TUP ID")
    print("[3] Year and Section")
    print("[4] Contact Number")
    print("[5] Email")
    choice = int(input("Enter search category: "))

    keyword = input("Enter the search keyword or substring: ")

    foundMatch = False
    for borrower in borrowerList:
        attributeValue = ""
        if choice == 1:
            attributeValue = borrower.name
        elif choice == 2:
            attributeValue = borrower.TUP_ID
        elif choice == 3:
            attributeValue = borrower.yearSection
        elif choice == 4:
            attributeValue = borrower.contactNum
        elif choice == 5:
            attributeValue = borrower.email
        else:
            attributeValue = borrower.TUP_ID

        if keyword.lower() in attributeValue.lower():
            print(borrower.name, "\t", borrower.TUP_ID, "\t", borrower.yearSection, "\t", borrower.contactNum, "\t", borrower.email)
            foundMatch = True

    if not foundMatch:
        messagebox.showinfo("SEARCH BORROWER", "NO MATCH FOUND ")

def saveBorrower():
    filename = "borrowerRecords.csv"  # Specify the filename for the CSV file

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)  # Create a CSV writer object

        # Write the header row
        writer.writerow(
            ["Name", "TUP_ID", "Password", "Year and Section", "Contact Number", "Email", "No. of Borrowed Books",
             "Borrowed Book(s)"])

        # Write each borrower's data row
        for borrower in borrowerList:
            # ENCRYPTED - encrypts every variable, then write it in the file
            """
            writer.writerow(
                [encrypt((borrower.name)), encrypt((borrower.TUP_ID)), encrypt((borrower.password)),
                 encrypt((borrower.yearSection)),
                 encrypt((borrower.contactNum)), encrypt((borrower.email)), encrypt(str(borrower.noOfBorrowed))])
            """
            # NOT ENCRYPTED
            writer.writerow([borrower.name, borrower.TUP_ID, borrower.password, borrower.yearSection,
                        borrower.contactNum, borrower.email, str(borrower.noOfBorrowed)])


def retrieveBorrower():
    with open("borrowerRecords.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # Create a CSV reader objectatego
        next(reader)  # Skip the header row

        for row in reader:
            # Extract the data from each row and create a CBorrower object
            name = row[0]
            TUP_ID = row[1]
            password = row[2]
            yearSection = row[3]
            contactNum = row[4]
            email = row[5]
            noOfBorrowed = row[6]
            # borrowedborrowers [0] = row[6]

            # create an object of the retrieved borrower
            #DECRYPTYED
            borrower = CBorrower(decrypt(name), decrypt(TUP_ID), decrypt(password), decrypt(yearSection),
               decrypt(contactNum), decrypt(email), decrypt(noOfBorrowed))  # borrowedBook
            #NOT DECRYPTED
            borrower = CBorrower(name, TUP_ID, password, yearSection, contactNum, email, noOfBorrowed)# borrowedBook

            # add borrower in the borrowerList
            addBorrower(borrower)

def save_login_account(login_ID):
    with open('login_account.txt', 'w') as file:
        file.write(str(login_ID))

def retrieve_login_account():
    try:
        with open('login_account.txt', 'r') as file:
            login_ID = int(file.read())
            return login_ID
    except FileNotFoundError:
        return None



def checkBorrowerFields(name, TUP_ID, password, yearSection, contactNum, email):

    if (name == "" or
        TUP_ID == "" or
        password == "" or
        yearSection == "" or
        contactNum == "" or
        email == "" ):
        return False
    else:
        return True

def checkBorrowerFieldsAdmin(name, TUP_ID, yearSection, contactNum, email):

    if (name == "" or
        TUP_ID == "" or
        yearSection == "" or
        contactNum == "" or
        email == "" ):
        return False
    else:
        return True

def encrypt(text):
    key =29
    encrypted = ""
    for char in text:
        if char.isalpha():  # Encrypt only alphabetical characters
            encrypted += chr((ord(char) - 32 + key) % 95 + 32)
        else:  # Keep non-alphabetical characters unchanged
            encrypted += char
    return encrypted

def decrypt(text):
    key=29
    decrypted = ""
    for char in text:
        if char.isalpha():  # Decrypt only alphabetical characters
            decrypted += chr((ord(char) - 32 - key) % 95 + 32)
        else:  # Keep non-alphabetical characters unchanged
            decrypted += char
    return decrypted




def displayBorrowedBook(TUP_ID):
    from CTransaction import transactionList

    i = 0
    bookBorrowed = ["", "", ""]
    print(TUP_ID)
    # Loop through transaction mula sa dulo since ang latest transaction ay naa-add sa unahan
    for transaction in reversed(transactionList):
        if transaction.TUP_ID == TUP_ID and i <3:
            if transaction.status == "TO APPROVE" or transaction.status == "TO RETURN":
                bookBorrowed[i] = transaction.title
                i = i+1
        else:
            continue

    return bookBorrowed
