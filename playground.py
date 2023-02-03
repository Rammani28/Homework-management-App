import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from todo import Todo
from tkcalendar import Calendar, DateEntry

root = Tk()

cal = Calendar()
cal.pack()
date_picket = DateEntry()
date_picket.pack()

root.mainloop()