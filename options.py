import sqlite3

# Connect to the database
print('Connecting to database...')
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()
print('Successfully connected to database!')


def user_options(user):
    while True:
        print('''
    Please select an option:
[1] - Change username
[2] - Change password
[3] - Deposit
[4] - Withdraw
[5] - Exit
        ''')
        user_op = int(input(''))

        if user_op == 1:
            new_user = input('Please enter your new username: ')
            update_query = '''
                            UPDATE user SET username = ?
                            WHERE username = ?
                                            '''
            cursor.execute(update_query, (new_user, user.username))
            conn.commit()
            user.set_username(new_user)
            print(f"User '{new_user}' successfully updated!")
        elif user_op == 2:
            new_pass = input('Please enter your new password: ')
            update_query = '''
                                UPDATE user SET password = ?
                                WHERE username = ?
                                '''
            cursor.execute(update_query, (new_pass, user.username))
            conn.commit()
            user.set_password(new_pass)
            print("Password successfully updated!")
        elif user_op == 3:
            deposit_amount = float(input('Please select the amount to deposit: '))
            # Code to update balance in the database and in the user instance
            update_query = '''
                                UPDATE user SET balance = balance + ?
                                WHERE username = ?
                                '''
            cursor.execute(update_query, (deposit_amount, user.username))
            conn.commit()
            user.set_balance(user.balance + deposit_amount)
            print("Deposit successful!")
        elif user_op == 4:
            withdraw_amount = float(input('Please select the amount to withdraw: '))
            if withdraw_amount > user.balance:
                print("Insufficient balance!")
            else:
                # Code to update balance in the database and in the user instance
                update_query = '''
                                    UPDATE user SET balance = balance - ?
                                    WHERE username = ?
                                    '''
                cursor.execute(update_query, (withdraw_amount, user.username))
                conn.commit()
                user.set_balance(user.balance - withdraw_amount)
                print("Withdrawal successful!")
        elif user_op == 5:
            break
        else:
            print('Invalid input! Try again')

