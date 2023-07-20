import sqlite3
from User import *


def init_user_database():

    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    # Make sure value in table
    cursor.execute("CREATE TABLE IF NOT EXISTS user(username TEXT, password TEXT, balance FLOAT, net_profit FLOAT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS cheater(username TEXT, password TEXT, "
                   "balance FLOAT, net_profit FLOAT, status INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS vip(username TEXT, password TEXT, "
                   "balance FLOAT, net_profit FLOAT, status INT)")
    # cursor.execute("""INSERT INTO user VALUES
    #     ('Nickek', 'thatguy1', 150000.00, 0.00),
    #     ('ethanseca', 'ffokcuf', 15000.00, 0.00),
    #     ('TheMFTenorio', 'iamhimothy123', 15000.00, 0.00),
    #     ('Brutuss', 'BananaBus', 15000.00, 0.00),
    #     ('Zebbypoo', 'Slutmeout123', 15000.00, 0.00),
    #     ('TH3_QU13T_K1DD', 'UtHoTiWuzFeElInU?', 15000.00, 0.00),
    #     ('Odog', 'Iluvwomen', 15000.00, 0.00),
    #     ('J', 'Bean', 15000.00, 0.00),
    #     ('User', 'Pass', 15000.00, 0.00)
    # """)
    conn.commit()
    conn.close()


def print_user_data():
    # Connect to the database
    print('Connecting to database...')
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    print('Successfully connected to database!')
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
    print('Connecting to database...')
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Select all rows from the 'user' table
    select_query = 'SELECT * FROM user'
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print('Successfully connected to database!')
    # Create a list to store user objects
    user_database = []
    print('Importing database...')
    # Iterate through the rows and create User objects
    for row in rows:
        username = row[0]
        password = row[1]
        balance = row[2]
        net_profit = row[3]
        user = User(username, password, balance, net_profit)
        user_database.append(user)
    print('Database import successful!')
    # Close the connection
    conn.close()

    # Return the list of user objects
    return user_database


def save_userdata(users):
    # Connect to the database
    print('Connecting to database...')
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    print('Successfully connected to database!')
    print('Saving userdata into database...')
    for user in users:
        select_query = '''
                    SELECT * FROM user WHERE username = ?
                '''
        cursor.execute(select_query, (user.username,))
        existing_user = cursor.fetchone()

        if existing_user:
            update_query = '''
                        UPDATE user SET password = ?, balance = ?, net_profit = ?
                        WHERE username = ?
                    '''
            cursor.execute(update_query, (user.password, user.balance, user.net_profit, user.username))
            conn.commit()
            print(f"User '{user.username}' updated\t Balance: '{user.balance}'")
            if user.balance >= 100000:
                insert_query = '''
                                        INSERT INTO vip (username, password, balance, net_profit)
                                        VALUES (?, ?, ?, ?)
                                    '''
                cursor.execute(insert_query, (user.username, user.password, user.balance, user.net_profit))
                conn.commit()

        else:
            insert_query = '''
                        INSERT INTO user (username, password, balance, net_profit)
                        VALUES (?, ?, ?, ?)
                    '''
            cursor.execute(insert_query, (user.username, user.password, user.balance, user.net_profit))
            conn.commit()
            print(f"New user '{user.username}' added!\t Balance: '{user.balance}'")

