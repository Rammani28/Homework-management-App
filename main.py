import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from todo import Todo
from tkcalendar import Calendar

# import time

# ------------------------------- CONSTANTS ----------------------------------- #

FONT = ("Arial", 16, 'normal')
DUE_HW_COUNTER = 0
USERNAME: str = ''
PASSWORD_LEN = 2
LOGGED_IN = False


# --------------------------------- LOGIN MANAGEMENT ------------------------------------#


def set_username(var: str):
    global USERNAME
    USERNAME = var


def signup(root, username_, password_, confirm_password_):
    global USERNAME
    password = password_.get()
    username = username_.get()
    confirm_password = confirm_password_.get()
    print(f"password is {password_.get()}")
    # root.destroy()
    print(f"password is {password_.get()}")
    
    try:
        with open("login.json") as login_file:
            login_data = json.load(login_file)
        
        if username in login_data:
            messagebox.showerror(title='Username Error!',
                                 message='This username has been taken. Please chose another one.')
        elif len(password) < PASSWORD_LEN:
            messagebox.showerror(title='Too short password!',
                                 message=f'Password must be at least {PASSWORD_LEN} characters')
        elif password != confirm_password:
            messagebox.showerror(title='Password did not Match',
                                 message='confirmation of new password failed, Enter same password at both fields ')
        else:
            set_username(username)
            messagebox.showinfo(title='Success',
                                message=f"""Your account has been created
                                \n username:{USERNAME}
                                \npassword: {password}""")
            new_user = {
                f"{USERNAME}": {
                    "password": f"{password}"
                }
            }
            login_data.update(new_user)
            with open('login.json', mode='w') as write_file:
                json.dump(login_data, write_file, indent=4)
    
    except FileNotFoundError:
        """Below code is for the first sign up"""

        if len(password) < PASSWORD_LEN:
            messagebox.showerror(title='Too short password!',
                                 message=f'Password must be at least {PASSWORD_LEN} characters')
            # signup_screen()
        elif password != confirm_password:
            messagebox.showerror(title='Password did not Match',
                                 message='confirmation of new password failed, Enter same password at both fields ')
            # signup_screen()
        else:
            set_username(username)
            new_user = {
                f"{USERNAME}": {
                    'password': f"{password}"
                }
            }
            with open("login.json", mode='w') as write_file:
                json.dump(new_user, write_file, indent=4)
            
            

    # check validity of username and password


def signup_screen():
    global username_entry, password_entry
    signup_window = Tk()
    signup_window.title = 'signup screen'
    
    username = StringVar(signup_window)
    password = StringVar(signup_window)
    confirm_password = StringVar(signup_window)
    
    username_label = Label(signup_window, text='Username', font=FONT)
    username_label.pack()
    
    username_entry = Entry(signup_window, font=FONT, textvariable=username)
    username_entry.pack()
    username_entry.focus()
    
    password_label = Label(signup_window, text=f'Password(minimum {PASSWORD_LEN} characters)', font=FONT)
    password_label.pack()
    
    password_entry = Entry(signup_window, font=FONT, textvariable=password)
    password_entry.pack()
    
    Label(signup_window, font=FONT, text='confirm password').pack()
    confirm_password_entry = Entry(signup_window, font=FONT, textvariable=confirm_password)
    confirm_password_entry.pack()
    
    signup_button = Button(signup_window, text="Signup",
                           command=lambda: signup(signup_window, username, password, confirm_password))
    signup_button.pack()
    signup_window.mainloop()


def login(login_window, username, password):
    global LOGGED_IN, USERNAME
    try:
        with open("login.json") as login_file:
            login_data = json.load(login_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Sign Up first!', message="You need to Register/Signup to use the service! ")
    
    else:
        for user in login_data:
            if username.get() == user and password.get() == login_data[user]['password']:
                LOGGED_IN = True
                USERNAME = username.get()
                login_window.destroy()
                return
        messagebox.showerror(title='Error', message='Invalid Username or Password! Try Again.')
        # login_window.destroy()
        # login_screen()


def login_screen():
    global username_label, username_entry, password_entry, password_label
    
    login_window = Tk()
    username = StringVar(login_window)
    password = StringVar(login_window)
    
    Label(text="Login to use the app\n(Create one if you don't have an account)").pack()
    username_label = Label(login_window, text='Username', font=FONT)
    username_label.pack(pady=10, padx=5)
    
    username_entry = Entry(login_window, font=FONT, textvariable=username)
    username_entry.pack(pady=(10, 2), padx=5, ipadx=10)
    username_entry.focus()
    
    password_label = Label(login_window, text=f'Password(minimum {PASSWORD_LEN} characters)', font=FONT)
    password_label.pack(pady=(10, 2), padx=5)
    
    password_entry = Entry(login_window, font=FONT, textvariable=password)
    password_entry.pack(pady=(0, 20), padx=5)
    
    login_button = Button(login_window, text="login", font=FONT,
                          command=lambda: login(login_window, username, password))
    login_button.pack(pady=10, padx=5)
    
    Label(login_window, text="Don't have an account? Register below!").pack(pady=(20, 0))
    Button(login_window, text='Sign up', command=signup_screen).pack(pady=10, padx=5)
    
    login_window.mainloop()


# ----------------------------- CREATE FIVE TABS ------------------------------ #


def create_five_tabs(nb):
    tab1 = ttk.Frame(nb)
    tab2 = ttk.Frame(nb)
    tab3 = ttk.Frame(nb)
    tab4 = ttk.Frame(nb)
    tab5 = ttk.Frame(nb)
    tab_style = ttk.Style()
    tab_style.configure('TNotebook.Tab',
                        font=('Arial', 16, 'bold'),
                        foreground='blue',
                        background='red',
                        width=15,
                        padding=(5, 10, 5, 10))
    nb.add(tab1, text="    Dashboard  ")
    nb.add(tab2, text="   Assignments ")
    nb.add(tab3, text="      Notes  ")
    nb.add(tab4, text="    Todo  ")
    nb.add(tab5, text="Add Assignments", state='hidden')
    nb.pack()
    nb.enable_traversal()
    return tab1, tab2, tab3, tab4, tab5


# ---------------------------- BACKEND?? --------------------------------- #


def insert_to_due_entry(date_picked):
    calendar.destroy()
    confirm_date_button.destroy()
    date = date_picked.get()
    hw_due_entry.delete('0', END)
    hw_due_entry.insert('0', date)


def pick_due_date():
    global calendar, confirm_date_button
    date_picked = StringVar(add_hw_tab, Calendar.date.today().strftime("%d/%m/%y"))
    calendar = Calendar(
        add_hw_tab,
        date_pattern="dd/mm/yyyy",
        textvariable=date_picked,
        showweeknumbers=False,
        showothermonthdays=False
    )
    confirm_date_button = Button(add_hw_tab, text='Confirm date', command=lambda: insert_to_due_entry(date_picked))
    confirm_date_button.grid(row=4, column=5)
    calendar.grid(row=4, column=3)


def add_hw_button(tab_hw):
    global hw_due_entry, pick_date_button, hw_subject_entry, hw_content_entry
    
    # un-hide the hidden tab (tab number 4 is "Add Hw Tab")
    notebook.tab(add_hw_tab, state='normal')
    notebook.select(add_hw_tab)
    
    # 1st row
    Label(tab_hw, text="Enter Subject", font=FONT, pady=10, padx=20).grid(row=1, column=1)
    hw_subject_entry = Entry(tab_hw, width=40, font=FONT)
    hw_subject_entry.focus()
    hw_subject_entry.grid(row=1, column=2)
    
    # 2nd row
    Label(tab_hw, text="Enter Description", font=FONT, pady=10, padx=20).grid(row=2, column=1)
    hw_content_entry = Entry(tab_hw, width=40, font=FONT)
    hw_content_entry.grid(row=2, column=2)
    
    # 3rd row
    Label(tab_hw, text="Enter Due date", font=FONT, pady=10, padx=20).grid(row=3, column=1)
    hw_due_entry = Entry(tab_hw, width=40, font=FONT)
    hw_due_entry.grid(row=3, column=2)
    
    # the calendar emoji  🗓 doses not display correctly
    pick_date_button = Button(tab_hw, text="📅Pick a date 🗓️", font=FONT, command=pick_due_date)
    pick_date_button.grid(row=3, column=3)
    
    # save button
    Button(tab_hw, text="Save Homework", font=FONT, command=save_hw, relief=GROOVE).grid(row=5, column=2)


def refresh_homeworks():
    global DUE_HW_COUNTER
    try:
        with open("data.json") as read_file:
            hw = json.load(read_file)[f'{USERNAME}']['homework']
    except FileNotFoundError:
        messagebox.showerror(title="File not found!", message="No data file has been found!")
    else:
        row = 2
        for subject in hw:
            # display all items in HOMEWORK_LIST
            if hw[subject]['completed'] is False:
                DUE_HW_COUNTER += 1
                checked = IntVar()
                check_button = Checkbutton(assignments_tab, text='Completed?', variable=checked, font=FONT)
                check_button.grid(row=row, column=0)
                Label(assignments_tab, text=f"{subject}", padx=10, font=FONT).grid(row=row, column=1)
                Label(assignments_tab, text=f"{hw[subject]['description']}", padx=20, font=FONT).grid(row=row, column=2)
                Label(assignments_tab, text=f"{hw[subject]['due']}", padx=10, font=FONT).grid(row=row, column=4)
                row += 1


def save_hw():
    global hw_id
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
        current_user_data['homework'].update(new_homework)
        with open("data.json", mode='w') as write_file:
            json.dump(complete_data, write_file, indent=4)
        messagebox.showinfo(title='Homework Added', message="Homework has been added! ")
        
        hw_due_entry.delete(0, END)
        hw_content_entry.delete(0, END)
        hw_subject_entry.delete(0, END)
        
        notebook.tab(add_hw_tab, state='hidden')
        notebook.select(assignments_tab)
        refresh_homeworks()


def save_todo():
    global LATEST_TODO_ID
    LATEST_TODO_ID += 1
    todo_create_button.configure(state='normal')
    new_todo = Todo()
    todo_create_button.configure(state='normal')
    
    with open("todo_id.txt", mode='w') as todo_id_file:
        new_todo.id = todo_id_file.write(f'{LATEST_TODO_ID}')
    
    new_todo.title = todo_title_entry.get()
    new_todo.content = todo_content_entry.get(index1=1.0, index2="end")
    new_todo.id = LATEST_TODO_ID
    
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
        current_user_data['todo'].update(todo_to_be_saved)
        with open("data.json", mode='w') as write_file:
            json.dump(complete_data, write_file, indent=4)
        messagebox.showinfo(title='Todo Added', message='Todo has been created.')
        todo_title_label.destroy()
        todo_title_entry.destroy()
        todo_content_label.destroy()
        todo_content_entry.destroy()
        todo_save_button.destroy()


# ------------------------- MANAGE THE FOUR TABS -------------------------- #

def create_todo():
    global todo_content_entry, todo_title_entry, todo_save_button, todo_content_label, todo_title_label
    
    todo_create_button.configure(state='disabled')
    todo_title_label = Label(todo_tab, text="Title", font=FONT, padx=5, pady=5)
    todo_title_label.grid(row=1, column=0)
    todo_title_entry = Entry(todo_tab, font=FONT, width=40)
    todo_title_entry.focus()
    todo_title_entry.grid(row=2, column=0)
    
    todo_content_label = Label(todo_tab, text="Description: ", font=FONT)
    todo_content_label.grid(row=3, column=0)
    todo_content_entry = Text(todo_tab, font=FONT, width=40, height=6)
    todo_content_entry.grid(row=4, column=0)
    todo_save_button = Button(todo_tab, text="  Save  ", font=FONT, command=save_todo)
    todo_save_button.grid(row=5, column=0)


def show_todos():
    pass


# ---------------------------------- FILE HANDLING -------------------------------------- #

login_screen()

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
        LATEST_TODO_ID = int(id_file.read())
except FileNotFoundError:
    with open("todo_id.txt", mode='w') as id_file:
        LATEST_TODO_ID = 10000
        id_file.write(f'{LATEST_TODO_ID}')

'''
delete this block (below) on completion of code
this block of code is set to count how many times the code has been run
'''
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

""" Login file below """
# try:
#     with open('login.json') as login_file:
#         login_data = json.load(login_file)  # use this line later
#
# except FileNotFoundError:
#     messagebox.showinfo(title='Login or Signup to continue!',
#                         message="You must be logged in to use the service.\nOr create a new account")
#     # signup_screen()

# ---------------------------------- PROGRAM STARTS HERE ------------------------------------- #

if LOGGED_IN:
    
    try:
        with open('data.json') as file:
            complete_data = json.load(file)
            current_user_data = complete_data[f'{USERNAME}']
    except FileNotFoundError:
        with open('data.json', mode='w') as file:
            file_structure = {
                f"{USERNAME}": {
                    "homework": {},
                    "todo": {},
                    "notes": {},
                    "completed_hw": {}
                }
            }
            json.dump(file_structure, file, indent=4)
    
    window = Tk()
    window.title(string="Homework Aid")
    
    # global WIDGETS so that they can be READ/DESTROYED anywhere in the code
    hw_due_entry = Entry()
    hw_content_entry = Entry()
    hw_subject_entry = Entry()
    todo_title_label = Label()
    todo_title_entry = Entry()
    todo_content_label = Label()
    todo_content_entry = Text()
    todo_save_button = Button()
    pick_date_button = Button()
    calendar = Calendar()
    confirm_date_button = Button()
    
    username_label = Label()
    username_entry = Entry()
    password_label = Label()
    password_entry = Entry()
    
    #  uncomment below for ugly styling
    style = ttk.Style(window)
    # style.theme_create("MyStyle", parent="alt", settings={
    #     "TNotebook": {"configure": {"tabmargins": [20, 0, 2, 0]}},
    #     "TNotebook.Tab": {"configure": {"padding": [10, 90, 10, 90]}, }})
    # style.theme_use("MyStyle")
    style.configure('left_tab.TNotebook', tabposition='wn')
    
    notebook = ttk.Notebook(window, style='left_tab.TNotebook')
    all_tabs = create_five_tabs(notebook)
    dash_tab, assignments_tab, notes_tab, todo_tab, add_hw_tab = all_tabs
    
    # DASH TAB
    Label(dash_tab, text="Welcome to your HomeWork assistance system", font=FONT, pady=10).grid(row=1, column=1)
    
    # ASSIGNMENT TAB
    Button(assignments_tab,
           text="Create homework", font=FONT, command=lambda: add_hw_button(add_hw_tab)).grid(row=0, column=4)
    Label(assignments_tab, text="Due Homeworks", font=("Arial", 16, "bold"), padx=10).grid(row=0, column=0)
    Label(assignments_tab, text=" Status ", padx=5, font=("Arial", 16, "bold")).grid(row=1, column=0)
    Label(assignments_tab, text="Subjects", padx=10, font=("Arial", 16, "bold")).grid(row=1, column=1)
    Label(assignments_tab, text="Description", padx=20, font=("Arial", 16, "bold")).grid(row=1, column=2, columnspan=2)
    Label(assignments_tab, text="Due Date", padx=10, font=("Arial", 16, "bold")).grid(row=1, column=4)
    refresh_homeworks()
    
    Label(todo_tab, text="Anything you want to do later? Add them here.", font=FONT, pady=20).grid(row=0, column=0)
    todo_create_button = Button(todo_tab, text="Create", command=create_todo)  # hide it after clicking it
    todo_create_button.grid(row=0, column=4)
    show_todos()
    
    window.mainloop()
