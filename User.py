class User:
    def __init__(self, username, password, balance, net_profit):
        self.username = username
        self.password = password
        self.balance = balance
        self.net_profit = net_profit

    def print_info(self):
        print(self.username, self.password, self.balance, self.net_profit)

    def set_username(self, new_username):
        self.username = new_username

    def set_password(self, new_password):
        self.password = new_password

    def set_balance(self, new_balance):
        self.balance = new_balance


