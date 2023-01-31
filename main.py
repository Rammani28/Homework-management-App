import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from todo import Todo

# ------------------------------- CONSTANTS ----------------------------------- #

FONT = ("Arial", 16, 'normal')


# ------------------------------ FILE HANDLING -------------------------------- #

# ----------------------------- CREATE FIVE TABS ------------------------------ #

def create_five_tabs(nb):
    tab1 = ttk.Frame(nb)
    tab2 = ttk.Frame(nb)
    tab3 = ttk.Frame(nb)
    tab4 = ttk.Frame(nb)
    tab5 = ttk.Frame(nb)
    
    nb.add(tab1, text="    Dashboard  ")
    nb.add(tab2, text="   Assignments ")
    nb.add(tab3, text="      Notes  ")
    nb.add(tab4, text="    Todo  ")
    nb.add(tab5, text="Add Assignments", state='hidden')
    nb.grid(row=0, column=0, sticky="")
    nb.enable_traversal()
    return tab1, tab2, tab3, tab4, tab5


# ---------------------------- BACKEND?? --------------------------------- #

def add_hw_button(hw_tab):
    global notebook, due_entry, subject_entry, description_entry
    notebook.tab(4, state='normal')
    notebook.select(4)
    
    # 1st row
    Label(hw_tab, text="Enter Subject", font=FONT, pady=10, padx=20).grid(row=1, column=1)
    subject_entry = Entry(hw_tab, width=40, font=FONT)
    subject_entry.grid(row=1, column=2)
    
    # 2nd row
    Label(hw_tab, text="Enter Description", font=FONT, pady=10, padx=20).grid(row=2, column=1)
    description_entry = Entry(hw_tab, width=40, font=FONT)
    description_entry.grid(row=2, column=2)
    
    # 3rd row
    Label(hw_tab, text="Enter Due date", font=FONT, pady=10, padx=20).grid(row=3, column=1)
    due_entry = Entry(hw_tab, width=40, font=FONT)
    due_entry.grid(row=3, column=2)
    
    # add button
    Button(hw_tab, text="  Save  ", font=FONT, command=save_hw).grid(row=9, column=5)


def show_homework():
    global assignments_tab
    try:
        with open("data.json") as file:
            hw = json.load(file)['homework']
    except FileNotFoundError:
        messagebox.showerror(title="File not found!", message="No data file has been found!")
    else:
        row = 2
        for subject in hw:
            # display all items in HOMEWORK_LIST
            check_button = Checkbutton(assignments_tab, text='Completed?', font=FONT)
            check_button.grid(row=row, column=0)
            Label(assignments_tab, text=f"{subject}", padx=10, font=FONT).grid(row=row, column=1)
            Label(assignments_tab, text=f"{hw[subject]['description']}", padx=20, font=FONT).grid(row=row, column=2)
            Label(assignments_tab, text=f"{hw[subject]['due']}", padx=10, font=FONT).grid(row=row, column=4)
            row += 1


def save_hw():
    global due_entry, subject_entry, description_entry, sub_id
    sub_id += 1
    with open("id.txt", mode='w') as id_file:
        id_file.write(f"{sub_id}")
    
    subject = subject_entry.get()
    due = due_entry.get()
    description = description_entry.get()
    
    new_data = {
        f"{subject}": {
            "description": f"{description}",
            "due": f"{due}",
            "completed": False,
            "id": sub_id
        }
    }
    
    if len(subject) == 0 or len(description) == 0:
        messagebox.showerror(title="EmptyFieldError!", message="Please don't leave any field empty.")
    else:
        try:
            with open("data.json", mode='r') as file:
                Whole_json_data = json.load(file)
        
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                file_structure = {
                    "homework": new_data,
                    "todo": {},
                    "notes": {},
                    "completed_hw": {}
                }
                json.dump(file_structure, file, indent=4)
        
        else:
            Whole_json_data['homework'].update(new_data)
            with open("data.json", mode='w') as file:
                json.dump(Whole_json_data, file, indent=4)
        
        finally:
            messagebox.showinfo(title='Homework Added', message="Homework has been added! ")
            messagebox.Message(notebook)
            due_entry.delete(0, END)
            description_entry.delete(0, END)
            subject_entry.delete(0, END)
            
            notebook.tab(4, state='hidden')
            notebook.select(1)
            show_homework()


def save_todo():
    create_todo_button.configure(state='normal')


# ------------------------- MANAGE THE FOUR TABS -------------------------- #

def create_todo():
    global todo_description_entry, todo_title_entry, todo_tab, create_todo_button
    create_todo_button.configure(state='disabled')

    Label(todo_tab, text="Title", font=FONT, padx=5, pady=5).grid(row=1, column=0)
    todo_title_entry = Entry(todo_tab, font=FONT, width=40)
    todo_title_entry.grid(row=2, column=0)
    
    Label(todo_tab, text="Description: ", font=FONT).grid(row=3, column=0)
    todo_description_entry = Text(todo_tab, font=FONT, width=40, height=6)
    todo_description_entry.grid(row=4, column=0)
    save_todo_button = Button(todo_tab, text="  Save  ", font=FONT, command=save_todo)
    save_todo_button.grid(row=5, column=0)


def show_todos():
    pass


# ------------------------------ UI SETUP ----------------------------------- #

# delete this block on completion of code
try:
    with open('run_counter.txt') as run_file:
        run_count = int(run_file.read())
except FileNotFoundError:
    with open('run_counter.txt', mode='w') as run_file:
        run_file.write("80")
else:
    with open('run_counter.txt', mode='w') as run_file:
        run_count += 1
        run_file.write(f"{run_count}")
        print(run_count)

window = Tk()
window.title(string="Homework Aid")

due_entry = Entry()
description_entry = Entry()
subject_entry = Entry()
todo_description_entry = Entry()
todo_title_entry = Entry()
create_todo_button = Button()

try:
    with open("id.txt") as id_file:
        sub_id = int(id_file.read())
except FileNotFoundError:
    with open("id.txt", mode='w') as id_file:
        id_file.write("100")

#  uncomment below for ugly styling
style = ttk.Style(window)
style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [20, 0, 2, 0]}},
    "TNotebook.Tab": {"configure": {"padding": [10, 90, 10, 90]}, }})
style.theme_use("MyStyle")
style.configure('left_tab.TNotebook', tabposition='wn')

notebook = ttk.Notebook(window, style='left_tab.TNotebook', width=1800, height=1000)
all_tabs = create_five_tabs(notebook)
dash_tab, assignments_tab, notes_tab, todo_tab, hw_tab = all_tabs

# DASH TAB
Label(dash_tab, text="Welcome to your HomeWork assistance system", font=FONT, pady=10).grid(row=1, column=1)

# ASSIGNMENT TAB
Button(assignments_tab, text="Create homework", font=("times", 16, "normal"), command=lambda: add_hw_button(hw_tab)).grid(row=0, column=4, sticky=W)
Label(assignments_tab, text="Due Homeworks", font=("Arial", 16, "bold"), padx=10).grid(row=0, column=0)
Label(assignments_tab, text="✔/x", padx=5, font=("Arial", 16, "bold")).grid(row=1, column=0)
Label(assignments_tab, text="Subjects", padx=10, font=("Arial", 16, "bold")).grid(row=1, column=1)
Label(assignments_tab, text="Description", padx=20, font=("Arial", 16, "bold")).grid(row=1, column=2, columnspan=2)
Label(assignments_tab, text="Due Date", padx=10, font=("Arial", 16, "bold")).grid(row=1, column=4)
show_homework()

Label(todo_tab, text="Anything you want to do later? Add them here.", font=FONT, pady=20).grid(row=0, column=0)
create_todo_button = Button(todo_tab, text="Create", command=create_todo)  # hide it after clicking it
create_todo_button.grid(row=0, column=4)

show_todos()

window.mainloop()
