class User:
    def __init__(self, username, password, balance, net_profit):
        self.username = username
        self.password = password
        self.balance = balance
        self.net_profit = net_profit

    def print_info(self):
        print(self.username, self.password, self.balance, self.net_profit)