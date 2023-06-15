from database_management import *
import sys


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









