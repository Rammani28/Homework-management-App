# if details["due"] in ('today', "tonight", 'aaja', "later"):
#     due_date = datetime.today()
#     due_date = f"{datetime.date(due_date)}".replace('-', '/')
# else:
#     due_date = datetime.strptime(details["due"], "%Y/%m/%d")
# details["date"] = due_date
#
#
#

# # TAKEAWAY: YOU NEED TO HAVE AN ACTIVE REFERENCE TO THE IMAGE IN MEMORY, OTHERWISE PYTHON GARBAGE COLLECTOR WILL
# # DESTROY IT, AND IT WON'T BE DISPLAYED ON THE SCREEN
from tkinter import *
from PIL import Image, ImageTk


def bin_img():
    login_btn_img = Image.open("images/bin.png")
    resize_image = login_btn_img.resize((100, 100))
    img = ImageTk.PhotoImage(resize_image)
    return img

