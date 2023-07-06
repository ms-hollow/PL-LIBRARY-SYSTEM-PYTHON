import os
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, font
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "StatementTrans"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def destroyWindow():
    # Function to destroy the window
    window.destroy()

window = Tk()

window.geometry("478x580")
window.configure(bg = "#C19A6B")


canvas = Canvas(
    window,
    bg = "#C19A6B",
    height = 580,
    width = 478,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    239.0,
    247.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
exitbtn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg = "#4B0000"
)
exitbtn.place(
    x=451.203125,
    y=21.0,
    width=14.48486328125,
    height=14.0
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(309.5,205.0,image=entry_image_1)
refnumEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))
refnumEntry.place(
    x=204.0,
    y=200.0,
    width=211.0,
    height=14.0
)

entry_image_2 = PhotoImage( file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(223.5,225.0,image=entry_image_2)
dateEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))
dateEntry.place(
    x=118.0,
    y=220.0,
    width=211.0,
    height=14.0
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image( 222.5, 265.0,image=entry_image_3)
name = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))

name.place(
    x=117.0,
    y=260.0,
    width=211.0,
    height=14.0
)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(237.5,285.0,image=entry_image_4)
tupid = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))

tupid.place(
    x=132.0,
    y=280.0,
    width=211.0,
    height=14.0
)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(309.5,305.0,image=entry_image_5)
yearandSection = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))

yearandSection.place(
    x=204.0,
    y=300.0,
    width=211.0,
    height=14.0
)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(316.5,325.0,image=entry_image_6)
titleEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))
titleEntry.place(
    x=211.0,
    y=320.0,
    width=211.0,
    height=14.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    323.5,
    345.0,
    image=entry_image_7
)
authorEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))
authorEntry.place(
    x=218.0,
    y=340.0,
    width=211.0,
    height=12.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    309.5,
    365.0,
    image=entry_image_8
)
ISBN = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))

ISBN.place(
    x=204.0,
    y=360.0,
    width=211.0,
    height=12.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    287.5,
    385.0,
    image=entry_image_9
)
dateBorrowedEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))
dateBorrowedEntry.place(
    x=182.0,
    y=380.0,
    width=211.0,
    height=14.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    294.5,
    405.0,
    image=entry_image_10
)
dateReturnEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))
dateReturnEntry.place(
    x=189.0,
    y=400.0,
    width=211.0,
    height=14.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    294.5,
    425.0,
    image=entry_image_11
)
remainingDaysEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))
remainingDaysEntry.place(
    x=189.0,
    y=420.0,
    width=211.0,
    height=14.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    315.5,
    445.0,
    image=entry_image_12
)
librarianEntry = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))
librarianEntry.place(
    x=210.0,
    y=440.0,
    width=211.0,
    height=14.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    236.5,
    465.0,
    image=entry_image_13
)
status = Entry(
    bd=0,
    bg="#C19A6B",
    fg="#000716",
    highlightthickness=0, font=font.Font(family="Courier New", size=11, weight="bold"))
status.place(
    x=131.0,
    y=460.0,
    width=211.0,
    height=14.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
okbtn = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= destroyWindow,
    relief="flat",
    bg = "#C19A6B"
)
okbtn.place(
    x=400.0,
    y=530.0,
    width=43.0,
    height=24.0
)
window.resizable(False, False)
window.mainloop()
