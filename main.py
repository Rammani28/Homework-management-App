import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from todo import Todo
from tkcalendar import Calendar
from sort import sort_hw

# ------------------------------- CONSTANTS ----------------------------------- #

FONT = ("Arial", 16, 'normal')
FONT_LOGIN = ('Noto Sans Canadian Aboriginal', 25, 'bold')
DUE_HW_COUNTER = 0
PASSWORD_LEN = 2
WHITE = 'white'
GREEN = 'green'

# LOGGED_IN = False
# USERNAME: str

USERNAME = 'ram'  # TODO remove this line and use above line
LOGGED_IN = True  # TODO remove this line and use above line


# --------------------------------- LOGIN MANAGEMENT ------------------------------------#


def set_username_globally(var: str):
    global USERNAME
    USERNAME = var


def signup(root, username_, password_, confirm_password_):
    global USERNAME, complete_data, current_user_data
    password = password_.get()
    username = username_.get()
    confirm_password = confirm_password_.get()
    
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
            set_username_globally(username)
            messagebox.showinfo(title='Success',
                                message=f"""Your account has been created
                                \n username:{USERNAME}
                                \npassword: {password}""")
            root.destroy()
            new_user = {
                f"{USERNAME}": {
                    "password": f"{password}"
                }
            }
            login_data.update(new_user)
            with open('login.json', mode='w') as write_file:
                json.dump(login_data, write_file, indent=4)
            
            try:
                with open('data.json') as read_file:
                    complete_data = json.load(read_file)
                
                current_user_data = {
                    f"{USERNAME}": {
                        "homework": {},
                        "todo": {},
                        "notes": {},
                        "completed_hw": {}
                    }
                }
                complete_data.update(current_user_data)
                with open('data.json', mode='w') as write_file:
                    json.dump(complete_data, write_file, indent=4)
            except FileNotFoundError:
                messagebox.showerror(title='FileNotFoundError!', message='data.json file seems to be deleted!')
                pass
    
    except FileNotFoundError:
        """Below code is for THE VERY FIRST sign up"""
        
        if len(password) < PASSWORD_LEN:
            messagebox.showerror(title='Too short password!',
                                 message=f'Password must be at least {PASSWORD_LEN} characters')
            # signup_screen()
        elif password != confirm_password:
            messagebox.showerror(title='Password did not Match',
                                 message='confirmation of new password failed, Enter same password at both fields ')
            # signup_screen()
        else:
            set_username_globally(username)
            new_user = {
                f"{USERNAME}": {
                    'password': f"{password}"
                }
            }
            with open("login.json", mode='w') as write_file:
                json.dump(new_user, write_file, indent=4)
    
    # check validity of username and password


#

def signup_screen():
    global username_entry, password_entry
    
    xc = 100
    yc = 100
    
    signup_window = Toplevel()
    signup_window.title('signup')
    signup_window.configure(bg='white')
    signup_window.geometry('925x500+300+200')
    signup_window.resizable(False, False)
    
    username = StringVar(signup_window)
    password = StringVar(signup_window)
    confirm_password = StringVar(signup_window)
    
    img = PhotoImage(file='login_img.png')
    Label(signup_window, image=img, bg='white').place(x=50, y=50)
    
    frame = Frame(signup_window, width=500, height=500, bg='white')
    frame.place(x=600, y=30)
    
    heading = Label(frame, text="SIGN UP", font=FONT_LOGIN, bg='white')
    heading.pack(padx=50, pady=30)
    
    username_label = Label(frame, text='Username', font=FONT, bg='white')
    username_label.pack(pady=10)
    username_entry = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Noto Sans Myanmar UI', 11),
                           textvariable=username)
    username_entry.pack()
    username_entry.focus()
    username_entry.insert(0, 'username')
    username_entry.bind('<FocusIn>', on_enter)
    username_entry.bind('<FocusOut>', on_leave)
    
    password_label = Label(frame, text='Password', font=FONT, bg='white')
    password_label.pack(pady=10)
    
    password_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Noto Sans Myanmar UI', 11),
                           textvariable=password, show='*')
    password_entry.bind('<FocusIn>', p_on_enter)
    password_entry.pack(pady=10)
    
    Label(frame, font=FONT, text='confirm password', bg='white').pack(pady=10)
    confirm_password_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Noto Sans Myanmar UI', 11),
                                   textvariable=confirm_password, show='*')
    confirm_password_entry.pack(pady=10)
    
    signup_button = Button(frame, text="Sign Up",
                           command=lambda: signup(signup_window, username, password, confirm_password), pady=7,
                           bg='#57a1f8', fg='white', border=0, cursor='hand2')
    signup_button.pack(pady=10)
    signup_window.mainloop()


def login(login_window, username, password):
    global LOGGED_IN, USERNAME
    try:
        with open("login.json") as login_file:
            login_data = json.load(login_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Sign Up first!', message="Register by creating an account below")
    
    else:
        for user in login_data:
            if username.get() == user and password.get() == login_data[user]['password']:
                LOGGED_IN = True
                USERNAME = username.get()
                login_window.destroy()
                return
        messagebox.showerror(title='Error', message='Invalid Username or Password! Try Again.')
        login_window.destroy()
        login_screen()


def on_enter(event):
    username_entry.delete(0, END)


def on_leave(event):
    name = username_entry.get()
    if name == '':
        username_entry.insert(0, 'username')


def p_on_enter(event):
    password_entry.delete(0, END)


def login_screen():
    global username_label, username_entry, password_entry, password_label
    
    xc = 100
    yc = 100
    
    login_window = Tk()
    login_window.title('login')
    login_window.configure(bg='white')
    login_window.geometry('925x500+300+200')
    login_window.resizable(False, False)
    
    img = PhotoImage(file='login_img.png')
    Label(login_window, image=img, bg='white').place(x=50, y=50)
    
    frame = Frame(login_window, width=500, height=500, bg='white')
    frame.place(x=480, y=0)
    
    heading = Label(frame, text="SIGN IN ", font=FONT_LOGIN, bg='white')
    heading.place(x=xc + 50, y=yc - 30)
    username = StringVar(login_window)
    password = StringVar(login_window)
    
    username_label = Label(frame, text='Username', font=FONT, bg='white')
    username_label.place(x=xc + 80, y=yc + 50)
    username_entry = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Noto Sans Myanmar UI', 11),
                           textvariable=username)
    username_entry.place(x=xc, y=yc + 80 + 10)
    username_entry.insert(0, 'username')
    username_entry.bind('<FocusIn>', on_enter)
    username_entry.bind('<FocusOut>', on_leave)
    
    password_label = Label(frame, text='Password', font=FONT, bg='white')
    password_label.place(x=182, y=yc + 120 + 10)
    
    password_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Noto Sans Myanmar UI', 11),
                           textvariable=password, show='*')
    password_entry.bind('<FocusIn>', p_on_enter)
    password_entry.place(x=100, y=yc + 160 + 10)
    
    login_button = Button(frame, pady=7, text="login", bg='#57a1f8', fg='white', border=0, font=FONT, cursor='hand1',
                          command=lambda: login(login_window, username, password))
    login_button.place(x=190, y=yc + 200 + 10)
    
    Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Noto Sans Myanmar UI', 15)).place(x=130,
                                                                                                                 y=yc + 310)
    Button(frame, text='Sign up', border=0, bg='white', cursor='hand1', fg='#57a1f8', command=signup_screen).place(
        x=200, y=yc + 350)
    
    login_window.mainloop()


# ----------------------------- CREATE FIVE TABS ------------------------------ #


def create_five_tabs(nb):
    tab1 = ttk.Frame(nb)
    tab1.config()
    tab2 = ttk.Frame(nb)
    tab3 = ttk.Frame(nb)
    tab4 = ttk.Frame(nb)
    tab5 = ttk.Frame(nb)
    tab_style = ttk.Style()
    tab_style.configure('TNotebook.Tab',
                        font=('Arial', 16, 'bold'),
                        foreground='blue',
                        background=WHITE,
                        width=15,
                        padding=(5, 10, 5, 10))
    nb.add(tab1, text="    Dashboard  ")
    nb.add(tab2, text="   Assignments ")
    nb.add(tab3, text="      Notes  ")
    nb.add(tab4, text="    Todo  ")
    nb.add(tab5, text="Add Assignments", state='hidden')
    nb.pack()
    nb.enable_traversal()
    nb.configure()
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
    confirm_date_button = Button(add_hw_tab, text='Confirm date', cursor='hand1',
                                 command=lambda: insert_to_due_entry(date_picked))
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
    pick_date_button = Button(tab_hw, text="📅Pick a date 🗓️", cursor='hand2', font=FONT, command=pick_due_date)
    pick_date_button.grid(row=3, column=3)
    
    # save button
    Button(tab_hw, text="Save Homework", font=FONT, command=save_hw, cursor='hand1').grid(row=5, column=2)


def refresh_homeworks():
    global DUE_HW_COUNTER
    try:
        with open("data.json") as read_file:
            hw = json.load(read_file)[f'{USERNAME}']['homework']
            hw = sort_hw(hw)
    except FileNotFoundError:
        messagebox.showerror(title="File not found!", message="No data file has been found!")
    else:
        row = 2
        for subject in hw:
            # display items with show=true from HOMEWORK_LIST
            if hw[subject]['show'] is True:
                DUE_HW_COUNTER += 1
                
                status_label = Label(assignments_tab, text='Due', fg='red', font=FONT)
                status_label.grid(row=row, column=0)
                if hw[subject]['completed'] is True:
                    status_label.configure(text='Completed', fg=GREEN)
                Label(assignments_tab, text=f"{subject}", padx=10, font=FONT).grid(row=row, column=1)
                Label(assignments_tab, text=f"{hw[subject]['description']}", padx=20, font=FONT).grid(row=row, column=2)
                Label(assignments_tab, text=f"{hw[subject]['due_date']}", padx=10, font=FONT).grid(row=row, column=4)
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
            "id": hw_id,
            "show": True
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


def show_todos():
    with open('data.json') as read_file:
        todos = json.load(read_file)[f"{USERNAME}"]['todo']
    row = 2
    for a_title in todos:
        Label(todo_tab, text=f'{a_title}', font=FONT).grid(row=row, column=0)  # title
        Label(todo_tab, text=f"{todos[a_title]['description']}", font=FONT).grid(row=row, column=1)
        
        row += 1


def create_todo():
    global todo_content_entry, todo_title_entry, todo_save_button, todo_content_label, todo_title_label, temp_frame
    temp_frame = Frame(todo_tab, background='white')
    temp_frame.grid(row=1, columnspan=2)
    
    todo_create_button.configure(state='disabled', font=FONT)
    todo_title_label = Label(temp_frame, text="Title", font=FONT, padx=5, pady=0)
    todo_title_label.grid(row=1, column=0)
    todo_title_entry = Entry(temp_frame, font=FONT, width=40)
    
    todo_title_entry.focus()
    todo_title_entry.grid(row=2, column=0)
    
    todo_content_label = Label(temp_frame, text="Description: ", font=FONT)
    todo_content_label.grid(row=3, column=0)
    
    todo_content_entry = Text(temp_frame, font=FONT, width=40, height=6)
    todo_content_entry.grid(row=4, column=0)
    todo_save_button = Button(temp_frame, text="  Save  ", font=FONT, command=save_todo, cursor='hand1')
    todo_save_button.grid(row=5, column=0)


def save_todo():
    global LATEST_TODO_ID
    LATEST_TODO_ID += 1
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
        temp_frame.destroy()
        show_todos()


# ---------------------------------- FILE HANDLING -------------------------------------- #

# login_screen()  # TODO Uncomment this line on completion of code

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
            complete_data = file_structure
            current_user_data = file_structure[f"{USERNAME}"]
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
    
    temp_frame = Frame()
    
    #  uncomment below for ugly styling
    style = ttk.Style(window)
    # style.theme_create("MyStyle", parent="alt", settings={
    #     "TNotebook": {"configure": {"tabmargins": [20, 0, 2, 0]}},
    #     "TNotebook.Tab": {"configure": {"padding": [10, 90, 10, 90]}, }})
    # style.theme_use("MyStyle")
    style.configure('left_tab.TNotebook', tabposition='wn')
    style.configure('TNotebook')
    
    notebook = ttk.Notebook(window, style='left_tab.TNotebook')
    all_tabs = create_five_tabs(notebook)
    dash_tab, assignments_tab, notes_tab, todo_tab, add_hw_tab = all_tabs
    
    # DASH TAB
    Label(dash_tab, text="Welcome to your HomeWork assistance system", font=FONT, pady=10).grid(row=1, column=1)
    
    # ASSIGNMENT TAB
    Button(assignments_tab,
           text="Create homework",
           cursor='hand1',
           font=FONT, command=lambda: add_hw_button(add_hw_tab)
           ).grid(row=0, column=4)
    Label(assignments_tab, text="Due Homeworks", font=("Arial", 16, "bold"), padx=10).grid(row=0, column=0)
    Label(assignments_tab, text=" Status ", padx=5, font=("Arial", 16, "bold")).grid(row=1, column=0)
    Label(assignments_tab, text="Subjects", padx=10, font=("Arial", 16, "bold")).grid(row=1, column=1)
    Label(assignments_tab, text="Description", padx=20, font=("Arial", 16, "bold")).grid(row=1, column=2)
    Label(assignments_tab, text="Due Date", padx=10, font=("Arial", 16, "bold")).grid(row=1, column=4)
    refresh_homeworks()
    
    # todo_tab
    Label(todo_tab, text="Anything you want to do later? Add them here.", font=FONT).grid(row=0, column=0, columnspan=2)
    todo_create_button = Button(todo_tab, text="Create", command=create_todo, cursor='hand1', font=FONT,
                                background='white', borderwidth=0)
    todo_create_button.grid(row=0, column=2)
    show_todos()
    
    window.mainloop()
