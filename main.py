import sys

import database_management
import User
import login_system
import visuals

# Initializing user database
database_management.init_user_database()
users = database_management.get_user_data()

for user in users:
    print(f"Username: {user.username:<18} Password: {user.password:<18} Balance: {user.balance:>10.2f} "
          f"\tNet Profit: {user.net_profit:>10.2f}")

print("\n")

user = login_system.login(users)
if user == -1:
    print("Failed Login! Restart and try again!")
    exit()
else:
    # Main Program Loop
    while True:
        # Initializing visuals
        visuals.menu()
        visuals.user_info(user)
        visuals.menu_options()

        # Main menu options
        option = int(input(''))
        if option == 1:
            visuals.games()
            game_option = int(input(''))
        elif option == 2:
            database_management.save_userdata(users)  # DEMO [save function]
        elif option == 3:
            print('working on')
        elif option == 4:
            print('Thanks for playing!')
            break
