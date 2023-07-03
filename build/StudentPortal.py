'''#"This file is not included in the main system.
    This file is still a work in progress."
#'''
from pathlib import Path
import tkinter as tk
from tkinter import ttk, Tk, Canvas, Entry, Text, Button, PhotoImage, font

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "DisplayBook"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DisplayTableFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.table = ttk.Treeview(self, columns=('Title', 'Edition', 'Author', 'Year', 'ISBN',
                                  'Material', 'Category', 'Shelf No.', 'Total Stock',
                                  'No. of Borrowers'), show='headings')
        self.table.heading('Title', text='Title')
        self.table.heading('Edition', text='Edition')
        self.table.heading('Author', text='Author')
        self.table.heading('Year', text='Year')
        self.table.heading('ISBN', text='ISBN')
        self.table.heading('Material', text='Material')
        self.table.heading('Category', text='Category')
        self.table.heading('Shelf No.', text='Shelf No.')
        self.table.heading('Total Stock', text='Total Stock')
        self.table.heading('No. of Borrowers', text='No. of Borrowers')

        self.table.column('Title', width=150)
        self.table.column('Edition', width=50)
        self.table.column('Author', width=120)
        self.table.column('Year', width=50)
        self.table.column('ISBN', width=100)
        self.table.column('Material', width=100)
        self.table.column('Category', width=120)
        self.table.column('Shelf No.', width=50)
        self.table.column('Total Stock', width=50)
        self.table.column('No. of Borrowers', width=50)

        self.table.pack(side='left', fill='y')

class DisplayBookFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = tk.Canvas(self)  # Initialize the canvas attribute
        self.canvas.pack(fill='both', expand=True)  # Pack the canvas widget

        # DISPLAY ALL BOOKS
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(x=20.0, y=145.0, width=160.0, height=32.0)

        # SEARCH BOOK
        '''#
        def gotoSearchBook():
            window.destroy()
            current_directory = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(current_directory, "studentDispBookFrame.py")
            subprocess.run(["python", script_path])
        '''
        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(x=20.0, y=199.0, width=160.0, height=32.0)

        # BORROW BOOK
        '''#
        def gotoBorrowBook():
            window.destroy()
            current_directory = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(current_directory, "studentDispBookFrame.py")
            subprocess.run(["python", script_path])
        '''
        borrowButton = PhotoImage(file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=borrowButton,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(x=20.0, y=253.0, width=160.0, height=32.0)

        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(99.0, 59.0, image=image_image_1)

        self.canvas.create_text(
            219.0,
            17.0,
            anchor="nw",
            text="BOOK",
            fill="#4B0000",
            font=font.Font(family="Poppins", size=40, weight="bold")
        )

        notifButton = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            1012.0,
            51.0,
            image=notifButton
        )

        '''#
        def gotoHome():
            window.destroy()
            current_directory = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(current_directory, "studentDispBookFrame.py")
            subprocess.run(["python", script_path])
        '''
        homeImage = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            945.0,
            52.0,
            image=homeImage
        )

        '''#
        def gotoLogout():
            window.destroy()
            current_directory = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(current_directory, "studentDispBookFrame.py")
            subprocess.run(["python", script_path])
        '''
        logoutImage = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(1075.0, 51.0, image=logoutImage)

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=759.0,
            y=38.0,
            width=80.0,
            height=37.0
        )

        # TEXTBOX
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(577.5, 56.5, image=entry_image_1)
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
        self.image_5 = self.canvas.create_image(
            640.0,
            380.0,
            image=image_image_5
        )

        self.frame1 = DisplayTableFrame(parent)
        self.frame1.place(x=220, y=150)
        '''
        # adding data to the table
        for i in range(len(titles)):
            table.insert('', 'end', values=(titles[i], editions[i], authors[i], years[i], isbns[i], materials[i], categories[i], shelf_nos[i], total_stocks[i], no_of_borrowers[i]))
        '''

        # CATEGORY DROPDOWN
        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=907.0,
            y=100.0,
            width=173.0,
            height=20.0
        )

        image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(250.0, 599.0, image=image_image_6)
        # Move the image to the bottom of the stacking order
        self.canvas.lower(image_6)


class SearchandBorrow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Add your borrow book frame code here

class ChangePassword(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Add your borrow book frame code here



class StudentMainFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Main Frame")
        self.geometry("1125x670")
        self.configure(bg="#FFFFFF")
        self.create_subframes()
        self.center_window()

    def create_subframes(self):
        self.displayBook = DisplayBookFrame(self)
        # Place the search book frame wherever you want

        self.searchBorrow = SearchandBorrow(self)
        # Place the borrow book frame wherever you want

        self.changePassword = ChangePassword(self)
        # Place the borrow book frame wherever you want

        # Add your other main window widgets here

    def center_window(self):
        # Calculate the center coordinates of the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 1125) // 2
        y = (screen_height - 670) // 2

        # Set the window position to the center of the screen
        self.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    root = StudentMainFrame()
    root.mainloop()

