import database_management
import User
# TEST COMMENT
# Initializing user database
user_database = database_management.read_user_database("user_database.csv")

for users in user_database:
    print(users.username, users.password, users.balance, users.net_profit)


