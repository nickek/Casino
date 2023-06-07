import sqlite3
from User import *


def init_user_database():

    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Make sure value in table
    cursor.execute("CREATE TABLE IF NOT EXISTS user(username, password, balance, net_profit)")
    cursor.execute("""INSERT INTO user VALUES
        ('Nickek', 'thatguy1', 15000.00, 0.00),
        ('ethanseca', 'ffokcuf', 15000.00, 0.00),
        ('TheMFTenorio', 'iamhimothy123', 15000.00, 0.00),
        ('Brutuss', 'BananaBus', 15000.00, 0.00),
        ('Zebbypoo', 'Slutmeout123', 15000.00, 0.00),
        ('TH3_QU13T_K1DD', 'UtHoTiWuzFeElInU?', 15000.00, 0.00),
        ('Odog', 'Iluvwomen', 15000.00, 0.00),
        ('J', 'Bean', 15000.00, 0.00),
        ('User', 'Pass', 15000.00, 0.00)
    """)
    conn.commit()
    conn.close()


def print_user_data():
    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Select all rows from the 'user' table
    select_query = 'SELECT * FROM user'
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Print the user data
    for row in rows:
        print(f"Username: {row[0]}, Password: {row[1]}, Balance: {row[2]:,.2f}, Net_Profit: {row[3]:,.2f}")

    conn.close()


def get_user_data():
    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Select all rows from the 'user' table
    select_query = 'SELECT * FROM user'
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Create a list to store user objects
    user_database = []

    # Iterate through the rows and create User objects
    for row in rows:
        username = row[0]
        password = row[1]
        balance = row[2]
        net_profit = row[3]
        user = User(username, password, balance, net_profit)
        user_database.append(user)

    # Close the connection
    conn.close()

    # Return the list of user objects
    return user_database
