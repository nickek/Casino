from database_management import *


def login(users):
    attempts = 0
    while attempts < 3:
        count = 0
        in_username = str(input("USERNAME: "))
        in_password = str(input("PASSWORD: "))

        for user in users:
            if in_username == user.username and in_password == user.password:
                print("Login Successful!")
                count += 1
                return user
        if count == 0:
            print("Invalid credentials try again.")
            attempts += 1
        elif count == 1:
            break
        if attempts == 3:
            return -1


def register(users):
    print('Connecting to database...')
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    print('Successfully connected to database!')

    while True:
        new_user = input("Enter new username: ")
        check_user = cursor.execute("SELECT username FROM user WHERE username = '{}'".format(new_user))
        if new_user == check_user:
            print("User already exist! Try again.")
        else:
            new_pass = input("Enter new password: ")
            new_bal = input("Enter start balance: ")

            print("Creating new account...")
            cursor.execute("INSERT INTO user VALUES ('{}','{}','{}', 0.00)".format(new_user, new_pass, new_bal))
            conn.commit()
            print("Account created! Welcome!")

            complete_user = User(new_user, new_pass, new_bal, 0.00)

            return complete_user









