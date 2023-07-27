from database_management import *
from tkinter import *
from tkinter import messagebox as ms


# gui
def existing_account():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")

    Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    main_screen.mainloop()
    return user


def login():
    main_screen.destroy()
    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify
    global count
    global attempts



    username_verify = StringVar()
    password_verify = StringVar()
    attempts = 0
    count = 1



    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()


def register():
    main_screen.destroy()
    global register_screen
    register_screen = Tk()
    register_screen.title("Register")
    register_screen.geometry("300x250")
    Label(register_screen, text="Please enter details below to register").pack()
    Label(register_screen, text="").pack()

    global start_balance
    global username_register
    global password_register

    username_register = StringVar()
    password_register = StringVar()
    start_balance = IntVar()

    Label(register_screen, text="Username * ").pack()
    username_register_entry = Entry(register_screen, textvariable=username_register)
    username_register_entry.pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="Password * ").pack()
    password_register_entry = Entry(register_screen, textvariable=password_register, show='*')
    password_register_entry.pack()
    Label(register_screen, text="").pack()
    balance_register_entry = Entry(register_screen, textvariable=start_balance)
    balance_register_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command=registration_verification).pack()


def registration_verification():
    global user
    print("working...")
    print('Connecting to database...')
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    print('Successfully connected to database!')

    cursor.execute("INSERT into user VALUES('{}','{}','{}','{}')".format(username_register.get(), password_register.get(), start_balance.get(), 0))
    conn.commit()
    cursor.execute("SELECT balance FROM user WHERE username = '{}'".format(username_register.get()))
    y = cursor.fetchone()
    # ADD VIP CHECK????
    if y:
        ms.showinfo("Congrats!", "Registration Successful!")
        user = User(username_register.get(), password_register.get(), start_balance.get(), 0)
        register_screen.destroy()
        return user
    else:
        ms.showerror("ERROR", "Registration failed!")
        return None


def login_verification():
    global user
    global username_verify
    global password_verify
    global count
    global attempts

    if (count == 1):
        attempts = 1
        count += 1

    print("working...")
    print('Connecting to database...')
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    print('Successfully connected to database!')

    cursor.execute("SELECT balance FROM user WHERE username = '{}'".format(username_verify.get()))
    x = cursor.fetchone()
    print("Attempts: ", attempts)

    while attempts < 4:
        if attempts == 3:
            ms.showerror("ERROR", "TOO MANY LOGIN ATTEMPTS! EXITING...")
            exit()
        if x:
            balance = x[0]
            user = User(username_verify.get(), password_verify.get(), balance, 0)
            print(user.username)
            ms.showinfo("Success", "Login Succeeded!")
            login_screen.destroy()
            return user
        else:
            attempts += 1
            ms.showerror("ERROR", "User Not Found!")
            username_verify.set("")
            password_verify.set("")
            print("Count:", count)
            print("Attempts: ", attempts)
            break





















