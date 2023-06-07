import database_management
import User

# Initializing user database
users = database_management.get_user_data()

for user in users:
    print(user.username, user.password, user.balance, user.net_profit)
