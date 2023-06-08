import database_management
import User
import login_system
import visuals

# Initializing user database
users = database_management.get_user_data()

for user in users:
    print(f"Username: {user.username:<18} Password: {user.password:<18} Balance: {user.balance:>10.2f} "
          f"\tNet Profit: {user.net_profit:>10.2f}")

print("\n")
user = login_system.login(users)
visuals.menu()
