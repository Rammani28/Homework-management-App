# # if details["due"] in ('today', "tonight", 'aaja', "later"):
# #     due_date = datetime.today()
# #     due_date = f"{datetime.date(due_date)}".replace('-', '/')
# # else:
# #     due_date = datetime.strptime(details["due"], "%Y/%m/%d")
# # details["date"] = due_date
# #
# #
# #
#
# # # TAKEAWAY: YOU NEED TO HAVE AN ACTIVE REFERENCE TO THE IMAGE IN MEMORY, OTHERWISE PYTHON GARBAGE COLLECTOR WILL
# # # DESTROY IT, AND IT WON'T BE DISPLAYED ON THE SCREEN
#
# # TAKEAWAY: PROGRAM ANYTHING IN OOP IF POSSIBLE, IT'LL MAKE CODING EASIER, AND SAVES TIME, REDUCE THE NEED OF MULTIPLE
# # GLOBAL VARIABLES
#
# # HAVE AN IDEA? SEARCH FOR IT. PROBABLY OTHERS TOO THOUGHT ABOUT IT.
#
# #
# # from tkinter import *
# # from tkinter import ttk
# #
# # # Create root window
# # root = Tk()
# #
# # # Create Notebook
# # notebook = ttk.Notebook(root)
# #
# # # Create tab 1
# # tab1 = Frame(notebook, bg="white")
# # tab1.pack(fill="both", expand=True)
# # notebook.add(tab1, text="Tab 1")
# #
# # # Add content to tab 1
# # Label(tab1, text="This is tab 1", font=("Arial", 16), bg="white").pack()
# #
# # # Create tab 2
# # tab2 = Frame(notebook, bg="white")
# # tab2.pack(fill="both", expand=True)
# # notebook.add(tab2, text="Tab 2")
# #
# # # Add content to tab 2
# # Label(tab2, text="This is tab 2", font=("Arial", 16), bg="white").pack()
# #
# # # Pack the notebook
# # notebook.pack(fill="both", expand=True)
# #
# # # Start the mainloop
# # root.mainloop()
# #
# #
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.title("Treeview Example")
#
# # Create Treeview widget
# tree = ttk.Treeview(root, columns=("column1", "column2"), show="headings")
#
#
# def on_keypress(event, name):
#     if event.keycode == 36:
#         item_id = tree.focus()
#         if item_id:
#             column = tree.identify_column(event.x)
#             if column == '#2':
#                 name = tree.item(item_id)['text']
#                 print(f"hello {name}")
#                 print(name)
#
#
# tree.bind('<KeyPress>', on_keypress(evern, name='jalle'))
#
# style = ttk.Style()
# style.theme_use("clam")
#
# style.configure("Treeview",
#                 background="white",
#                 fieldbackground="white",
#                 foreground="black",
#                 rowheight=25,
#                 font=("Arial", 16))
#
# # Define columns for treeview
# tree['columns'] = ('name', 'age', 'gender')
#
# # Format columns
# tree.column('#0', width=0, stretch=tk.NO)
# tree.column('name', anchor=tk.CENTER, width=100)
# tree.column('age', anchor=tk.CENTER, width=100)
# tree.column('gender', anchor=tk.CENTER, width=100)
#
# # Add column headings
# tree.heading('#0', text='', anchor=tk.CENTER)
# tree.heading('name', text='Name', anchor=tk.CENTER)
# tree.heading('age', text='Age', anchor=tk.CENTER)
# tree.heading('gender', text='Gender', anchor=tk.CENTER)
#
# # Add data to the treeview
# tree.insert(parent='', index='end', iid='0', text='', values=('John', 35, 'Male'))
# tree.insert(parent='', index='end', iid='1', text='', values=('Jane', 27, 'Female'))
# tree.insert(parent='', index='end', iid='2', text='', values=('Bob', 42, 'Male'))
#
# # Pack the treeview widget
# tree.pack()
#
# root.mainloop()
# import tkinter as tk
# from tkinter import messagebox
#
# root = tk.Tk()
#
# def show_message():
#     messagebox.showinfo("Title", "Message")
#     root.after(2000, lambda: root.focus_force())
#
# button = tk.Button(root, text="Show Message", command=show_message)
# button.pack()
#
# root.mainloop()


# import tkinter as tk
# import tkinter.ttk as ttk

# def find(word, *word_lists):
#     result = []
#     if word in word_lists[0][0]:
#         result.append(('dash', word))
#     if word in word_lists[0][1]:
#         result.append(('assignment', word))
#     if word in word_lists[0][2]:
#         result.append(('todo', word))
#     if word in word_lists[0][3]:
#         result.append(('notes', word))
#     if not result:
#         result.append(('not found', word))
#     return result

# root = tk.Tk()
# root.geometry('400x400')
#
# # create a Treeview widget
# tv = ttk.Treeview(root, columns=('col1', 'col2'), show='headings')
#
# # add column headings
# tv.heading('col1', text='List')
# tv.heading('col2', text='Word')
#
# # add rows to the Treeview
# word_lists = ([['foo', 'bar'], ['assignment1', 'assignment2'], ['todo1', 'todo2'], ['notes1', 'notes2']])
# for word in ['foo', 'assignment1', 'notes3', 'bar']:
#     results = find(word, word_lists)
#     for r in results:
#         tv.insert('', 'end', values=r)
#
# # set Treeview style
# style = ttk.Style()
# style.configure('Treeview', rowheight=30, font=('Arial', 16, 'normal'))
# style.configure('Treeview.Heading', font=('Arial', 16, 'normal'))
# tv.tag_configure('not found', foreground='red')
#
# # pack and run the app
# tv.pack(fill='both', expand=True)
# root.mainloop()
#
#
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.configure(background='white')
#
# tree = ttk.Treeview(root)
# tree.heading('#0', text='Result')
#
# tree.insert(parent='', index='end', iid=0, text='Parent')
# tree.insert(parent='', index='end', iid=1, text='Child', open=False)
#
# tree.pack()
#
# root.mainloop()

import tkinter as tk

root = tk.Tk()

text = tk.Text(root)
scrollbar = tk.Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scrollbar.set)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()
