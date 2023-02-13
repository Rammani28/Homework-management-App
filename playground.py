# if details["due"] in ('today', "tonight", 'aaja', "later"):
#     due_date = datetime.today()
#     due_date = f"{datetime.date(due_date)}".replace('-', '/')
# else:
#     due_date = datetime.strptime(details["due"], "%Y/%m/%d")
# details["date"] = due_date
#
#
#
# Import Module
from tkinter import *
from PIL import Image, ImageTk


def bin_img():
    login_bth_img = Image.open("images/bin.png")
    
    
    resize_image = login_bth_img.resize((100, 100))
    
    img = ImageTk.PhotoImage(resize_image)
    
    return img