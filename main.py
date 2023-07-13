import sys
import sqlite3
import database_management
import User
import login_system
import visuals
import Slots

# Initializing user database
database_management.init_user_database()
users = database_management.get_user_data()

for user in users:
    print(f"Username: {user.username:<18} Password: {user.password:<18} Balance: {user.balance:>10.2f} "
          f"\tNet Profit: {user.net_profit:>10.2f}")

print("\n")

print("Do you have an existing account?\n"
      "1) Yes\n"
      "2) No\n")
existing_account = int(input(''))

if existing_account == 1:
    user = login_system.login(users)
if existing_account == 2:
    user = login_system.register(users)

if user == -1:
    print("Failed Login! Restart and try again!")
    exit()
else:
    # Main Program Loop
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    while True:
        # Initializing visuals
        visuals.menu()
        cursor.execute("SELECT * FROM vip WHERE username = ?", (user.username,))
        vip = cursor.fetchone()
        if vip:
            print('\t\t\t\t\tVIP!')
            status = 1
            visuals.user_info(user)
        else:
            status = 0
            visuals.user_info(user)
        visuals.menu_options()

        # Main menu options
        option = int(input(''))
        if option == 1:
            visuals.games()
            game_option = int(input(''))
            if game_option == 2:
                Slots.play(user)

        elif option == 2:
            database_management.save_userdata(users)  # DEMO [save function]
        elif option == 3:
            print('working on 7/13')
        elif option == 4:
            print('Thanks for playing!')
            break
