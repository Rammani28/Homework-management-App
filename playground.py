# import json

# from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk
# from todo import Todo
# from tkcalendar import Calendar, DateEntry
#
# root = Tk()
#
# cal = Calendar()
# cal.pack()
# date_picket = DateEntry()
# date_picket.pack()
#
# root.mainloop()


# # ##----------------this works-------------------#
# user = 'me'
# wholeData = {
#     f'{user}': {
#         'sub': {
#             "title": "title of " + user,
#             'description': "description of" + user
#         },
#     },
# }
# userData = wholeData[f'{user}']
# print(userData)
# print(wholeData)
# newhw = {
#     "new sub": {
#         'titdle': "title3 of " + user,
#         "description": "description3 of " + user
#     }}
#
# userData.update(newhw)
# print(userData)
# print(wholeData)
# # both give the same result


# import tkinter as tk
#
# root = tk.Tk()
# root.title("Button Example")

# def on_click_me():
#     print("You clicked the 'Click Me' button!")
#
# def on_quit():
#     root.quit()
#     root.destroy()
#
# canvas = tk.Canvas(root, height=400, width=200)
# canvas.pack()
#
# click_me_button = tk.Button(canvas, text="Click Me", command=on_click_me, relief=tk.GROOVE, width=10, height=2)
# quit_button = tk.Button(canvas, text="Quit", command=on_quit, relief=tk.GROOVE, width=10, height=2)
#
# click_me_button_window = canvas.create_window(50, 50, anchor="nw", window=click_me_button)
# quit_button_window = canvas.create_window(150, 50, anchor="nw", window=quit_button)
#
# oval1 = canvas.create_oval(30, 30, 70, 70, outline="black", fill="white")
# oval2 = canvas.create_oval(130, 30, 170, 70, outline="black", fill="white")
#
# canvas.tag_bind(oval1, "<Button-1>", on_click_me)
# canvas.tag_bind(oval2, "<Button-1>", on_quit)
#
# root.mainloop()

# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.geometry("200x200")
#
# style = ttk.Style()
# style.configure("Rounded.TButton", background="#2ECC71", relief="flat", borderradius=100,
#                 padding=10, font=("Arial", 12, "bold"), width=20, height=3)
#
# click_me_button = ttk.Button(root, text="Click me", style="Rounded.TButton")
# click_me_button.pack()
#
# quit_button = ttk.Button(root, text="Quit", style="Rounded.TButton", command=root.quit)
# quit_button.pack()
#
# root.mainloop()
#

#
# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("200x200")
#
# flat_button = tk.Button(root, text="Flat", relief=tk.FLAT)
# flat_button.pack()
#
# raised_button = tk.Button(root, text="Raised", relief=tk.RAISED)
# raised_button.pack()
#
# sunken_button = tk.Button(root, text="Sunken", relief=tk.SUNKEN)
# sunken_button.pack()
#
# groove_button = tk.Button(root, text="Groove", relief=tk.GROOVE)
# groove_button.pack()
#
# ridge_button = tk.Button(root, text="Ridge", relief=tk.RIDGE)
# ridge_button.pack()
#
# root.mainloop()

dictt = {
    "ram": {
        'password': "passsswword"
    },
    'sam': {
        'password': "jkasjdff"
    }
}

if 'sams' not in dictt:
    print("ram is not in dictt")