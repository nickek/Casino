import csv
from User import *


def read_user_database(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header row

        username_index = headers.index('Username')
        password_index = headers.index('Password')
        balance_index = headers.index('Balance')
        net_profit_index = headers.index('Net_Profit')

        user_info = []
        for row in reader:
            username = row[username_index]
            password = row[password_index]
            balance = float(row[balance_index])
            net_profit = float(row[net_profit_index])
            user_info.append((username, password, balance, net_profit))

        user_database = []
        for line in user_info:
            user = User(line[0], line[1], line[2], line[3])
            user_database.append(user)

    return user_database
