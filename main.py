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

def add_hw_button(tab_hw):
    global notebook, hw_due_entry, hw_subject_entry, hw_content_entry
    notebook.tab(4, state='normal')
    notebook.select(4)
    
    # 1st row
    Label(tab_hw, text="Enter Subject", font=FONT, pady=10, padx=20).grid(row=1, column=1)
    hw_subject_entry = Entry(tab_hw, width=40, font=FONT)
    hw_subject_entry.grid(row=1, column=2)
    
    # 2nd row
    Label(tab_hw, text="Enter Description", font=FONT, pady=10, padx=20).grid(row=2, column=1)
    hw_content_entry = Entry(tab_hw, width=40, font=FONT)
    hw_content_entry.grid(row=2, column=2)
    
    # 3rd row
    Label(tab_hw, text="Enter Due date", font=FONT, pady=10, padx=20).grid(row=3, column=1)
    hw_due_entry = Entry(tab_hw, width=40, font=FONT)
    hw_due_entry.grid(row=3, column=2)
    
    # add button
    Button(tab_hw, text="  Save  ", font=FONT, command=save_hw).grid(row=9, column=5)


def show_homework():
    global assignments_tab
    try:
        with open("data.json") as read_file:
            hw = json.load(read_file)['homework']
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
    global hw_due_entry, hw_subject_entry, hw_content_entry, hw_id, whole_json_data
    hw_id += 1
    with open("id.txt", mode='w') as write_file:
        write_file.write(f"{hw_id}")
    
    subject = hw_subject_entry.get()
    due = hw_due_entry.get()
    description = hw_content_entry.get()
    
    new_homework = {
        f"{subject}": {
            "description": f"{description}",
            "due": f"{due}",
            "completed": False,
            "id": hw_id
        }
    }
    field_is_empty = len(subject) == 0 or len(description) == 0
    if field_is_empty:
        messagebox.showerror(title="EmptyFieldError!", message="Please don't leave any field empty.")
    else:
        whole_json_data['homework'].update(new_homework)
        with open("data.json", mode='w') as write_file:
            json.dump(whole_json_data, write_file, indent=4)
        
        messagebox.showinfo(title='Homework Added', message="Homework has been added! ")
        messagebox.Message(notebook)
        hw_due_entry.delete(0, END)
        hw_content_entry.delete(0, END)
        hw_subject_entry.delete(0, END)
        
        notebook.tab(4, state='hidden')
        notebook.select(1)
        show_homework()


def save_todo():
    global todo_content_entry, todo_title_entry, todo_tab, todo_create_button, todo_content_label, todo_title_label, todo_id, whole_json_data
    todo_id += 1
    todo_create_button.configure(state='normal')
    new_todo = Todo()
    todo_create_button.configure(state='normal')
    
    with open("todo_id.txt", mode='w') as todo_id_file:
        new_todo.id = todo_id_file.write(f'{todo_id}')
    
    new_todo.title = todo_title_entry.get()
    new_todo.content = todo_content_entry.get(index1=1.0, index2="end")
    new_todo.id = todo_id
    
    todo_to_be_saved = {
        f"{new_todo.title}": {
            "description": new_todo.content,
            "id": new_todo.id,
        }
    }
    
    field_is_empty = len(new_todo.title) == 0 or len(new_todo.content) == 0
    if field_is_empty:
        messagebox.showerror(title="EmptyFieldError!", message="Please don't leave any field empty.")
    else:
        whole_json_data['todo'].update(todo_to_be_saved)
        with open("data.json", mode='w') as write_file:
            json.dump(whole_json_data, write_file, indent=4)
        messagebox.showinfo(title='Todo Added', message='Todo has been created.')
        todo_title_label.destroy()
        todo_title_entry.destroy()
        todo_content_label.destroy()
        todo_content_entry.destroy()
        todo_save_button.destroy()


# ------------------------- MANAGE THE FOUR TABS -------------------------- #

def create_todo():
    global todo_content_entry, todo_title_entry, todo_tab, todo_save_button, todo_create_button, todo_content_label, todo_title_label
    todo_create_button.configure(state='disabled')
    
    todo_title_label = Label(todo_tab, text="Title", font=FONT, padx=5, pady=5)
    todo_title_label.grid(row=1, column=0)
    todo_title_entry = Entry(todo_tab, font=FONT, width=40)
    # todo_title_entry.focus()
    todo_title_entry.grid(row=2, column=0)
    
    todo_content_label = Label(todo_tab, text="Description: ", font=FONT)
    todo_content_label.grid(row=3, column=0)
    todo_content_entry = Text(todo_tab, font=FONT, width=40, height=6)
    todo_content_entry.grid(row=4, column=0)
    todo_save_button = Button(todo_tab, text="  Save  ", font=FONT, command=save_todo)
    todo_save_button.grid(row=5, column=0)


def show_todos():
    pass


# ---------------------------------- FILE HANDLING --------------------------------------

# todo_id and sub_id handling
try:
    with open("id.txt") as id_file:
        hw_id = int(id_file.read())
except FileNotFoundError:
    with open("id.txt", mode='w') as id_file:
        first_hw_id = 100
        id_file.write(f'{first_hw_id}')

try:
    with open("todo_id.txt") as id_file:
        todo_id = int(id_file.read())
except FileNotFoundError:
    with open("todo_id.txt", mode='w') as id_file:
        todo_id = 1000
        id_file.write(f'{todo_id}')

try:
    with open('data.json', mode='r') as file:
        whole_json_data = json.load(file)
except FileNotFoundError:
    with open('data.json', mode='w') as file:
        file_structure = {
            "homework": {},
            "todo": {},
            "notes": {},
            "completed_hw": {}
        }
        json.dump(file_structure, file, indent=4)

# ------------------------------ UI SETUP ----------------------------------- #

# delete this block on completion of code
try:
    with open('run_counter.txt') as run_file:
        run_count = int(run_file.read())
except FileNotFoundError:
    with open('run_counter.txt', mode='w') as run_file:
        run_file.write("1")
else:
    with open('run_counter.txt', mode='w') as run_file:
        run_count += 1
        run_file.write(f"{run_count}")
        print(run_count)

window = Tk()
window.title(string="Homework Aid")

# global variables so that their value can be read/destroyed anywhere in this code
hw_due_entry = Entry()
hw_content_entry = Entry()
hw_subject_entry = Entry()
todo_title_label = Label()
todo_title_entry = Entry()
todo_content_label = Label()
todo_content_entry = Text()
todo_save_button = Button()

#  uncomment below for ugly styling
style = ttk.Style(window)
# style.theme_create("MyStyle", parent="alt", settings={
#     "TNotebook": {"configure": {"tabmargins": [20, 0, 2, 0]}},
#     "TNotebook.Tab": {"configure": {"padding": [10, 90, 10, 90]}, }})
# style.theme_use("MyStyle")
style.configure('left_tab.TNotebook', tabposition='wn')

notebook = ttk.Notebook(window, style='left_tab.TNotebook', width=1800, height=1000)
all_tabs = create_five_tabs(notebook)
dash_tab, assignments_tab, notes_tab, todo_tab, hw_tab = all_tabs

# DASH TAB
Label(dash_tab, text="Welcome to your HomeWork assistance system", font=FONT, pady=10).grid(row=1, column=1)

# ASSIGNMENT TAB
Button(assignments_tab, text="Create homework", font=FONT, command=lambda: add_hw_button(hw_tab)) \
    .grid(row=0, column=4, sticky=W)
Label(assignments_tab, text="Due Homeworks", font=("Arial", 16, "bold"), padx=10).grid(row=0, column=0)
Label(assignments_tab, text="✔/x", padx=5, font=("Arial", 16, "bold")).grid(row=1, column=0)
Label(assignments_tab, text="Subjects", padx=10, font=("Arial", 16, "bold")).grid(row=1, column=1)
Label(assignments_tab, text="Description", padx=20, font=("Arial", 16, "bold")).grid(row=1, column=2, columnspan=2)
Label(assignments_tab, text="Due Date", padx=10, font=("Arial", 16, "bold")).grid(row=1, column=4)
show_homework()

Label(todo_tab, text="Anything you want to do later? Add them here.", font=FONT, pady=20).grid(row=0, column=0)
todo_create_button = Button(todo_tab, text="Create", command=create_todo)  # hide it after clicking it
todo_create_button.grid(row=0, column=4)
show_todos()

window.mainloop()
