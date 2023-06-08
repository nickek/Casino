from database_management import *


def login(users):
    while True:
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
        elif count == 1:
            break







