import random
from User import *

# Constants
ROULETTE_NUMBERS = ["00"] + [str(i) for i in range(0, 37)]
CHIP_VALUES = [1, 5, 10, 25, 50, 100]
BET_PAYOUTS = {
    "straight": 35,
    "split": 17,
    "street": 11,
    "corner": 8,
    "five": 6,
    "line": 5,
    "dozen": 2,
    "column": 2,
    "low": 1,
    "high": 1,
    "red": 1,
    "black": 1,
    "odd": 1,
    "even": 1
}

# Represents the ball used in the roulette game
class Ball:
    def __init__(self):
        self.number = None

    def spin(self):
        self.number = random.choice(ROULETTE_NUMBERS)

# Represents the casino
class Casino:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.bet_amount = 0
        self.bet_type = ""
        self.bet_numbers = []
        self.ball_speed = 0.5
        self.ball = Ball()

    def draw_balance(self):
        print(f"Balance: ${self.balance}")

    def draw_chip_values(self):
        print("Available chip values: $1, $5, $10, $25, $50, $100")

    def draw_bet_area(self):
        print(f"Current bet amount: ${self.bet_amount}")

    def draw_roulette_area(self):
        print("\n    Roulette Wheel")
        print("----------------------------")
        print("  ", end="")
        for i in range(len(ROULETTE_NUMBERS)):
            print(f"{ROULETTE_NUMBERS[i]:<4}", end="")
            if (i + 1) % 6 == 0:
                print("\n  ", end="")
        print("\n----------------------------\n")

    def draw(self):
        self.draw_balance()
        self.draw_chip_values()
        self.draw_bet_area()
        self.draw_roulette_area()

    def update_bet_amount(self, amount):
        self.bet_amount = amount

    def place_bet(self):
        if self.bet_amount > self.balance:
            print("Insufficient balance!")
            return False
        else:
            self.balance -= self.bet_amount
            return True

    def spin_roulette(self):
        self.ball.spin()
        self.ball_speed = random.uniform(0.1, 2.0)

    def calculate_payout(self):
        payout = 0
        ball_number = self.ball.number

        if self.bet_type == "straight":
            if ball_number in self.bet_numbers:
                payout = self.bet_amount * BET_PAYOUTS["straight"]
        elif self.bet_type == "split":
            if ball_number in self.bet_numbers:
                payout = self.bet_amount * BET_PAYOUTS["split"]
        elif self.bet_type == "street":
            if ball_number in self.bet_numbers:
                payout = self.bet_amount * BET_PAYOUTS["street"]
        elif self.bet_type == "corner":
            if ball_number in self.bet_numbers:
                payout = self.bet_amount * BET_PAYOUTS["corner"]
        elif self.bet_type == "five":
            if ball_number in self.bet_numbers:
                payout = self.bet_amount * BET_PAYOUTS["five"]
        elif self.bet_type == "line":
            if ball_number in self.bet_numbers:
                payout = self.bet_amount * BET_PAYOUTS["line"]
        elif self.bet_type == "dozen":
            if ball_number in self.bet_numbers:
                payout = self.bet_amount * BET_PAYOUTS["dozen"]
        elif self.bet_type == "column":
            if ball_number in self.bet_numbers:
                payout = self.bet_amount * BET_PAYOUTS["column"]
        elif self.bet_type in ["low", "high", "red", "black", "odd", "even"]:
            if ball_number == self.bet_type:
                payout = self.bet_amount * BET_PAYOUTS[self.bet_type]

        return payout

    def reset(self):
        self.bet_amount = 0
        self.ball_speed = 0.5
        self.bet_type = ""
        self.bet_numbers = []
        self.ball = Ball()

    def play(self):
        while True:
            self.draw()

            if self.balance <= 0:
                print("Game over! You ran out of money.")
                break

            self.bet_amount = 0
            self.bet_type = ""
            self.bet_numbers = []

            print("Place your bet:")
            print(" 1. Bet on a single number")
            print(" 2. Bet on a split")
            print(" 3. Bet on a street")
            print(" 4. Bet on a corner")
            print(" 5. Bet on five numbers")
            print(" 6. Bet on a line")
            print(" 7. Bet on dozens")
            print(" 8. Bet on a column")
            print(" 9. Bet on low numbers")
            print("10. Bet on high numbers")
            print("11. Bet on red")
            print("12. Bet on black")
            print("13. Bet on odd")
            print("14. Bet on even")
            print("15. Quit\n")

            choice = input("Enter your choice: ")


            if choice == "15":
                print("\nThank you for playing!")
                break

            elif choice != ["1", "15"]:
                print("Invalid input! Please enter a number from 1 to 15.")

            if choice in ["1", "2", "3", "4", "6"]:
                self.bet_type = choice
                while True:
                    try:
                        self.bet_numbers = [input("Enter a number to bet on: ")]
                        if self.bet_numbers[0] not in ROULETTE_NUMBERS:
                            raise ValueError
                        self.update_bet_amount(int(input("Enter your bet amount: $")))
                        break
                    except ValueError:
                        print("Invalid input!")
            elif choice == "5":
                self.bet_type = choice
                while True:
                    try:
                        self.bet_numbers = input("Enter five numbers to bet on (separated by commas): ").split(",")
                        if len(self.bet_numbers) != 5 or any(num not in ROULETTE_NUMBERS for num in self.bet_numbers):
                            raise ValueError
                        self.update_bet_amount(int(input("Enter your bet amount: $")))
                        break
                    except ValueError:
                        print("Invalid input!")
            elif choice in ["7", "8"]:
                self.bet_type = choice
                while True:
                    try:
                        self.bet_numbers = [input("Enter your bet selection: ")]
                        self.update_bet_amount(int(input("Enter your bet amount: $")))
                        break
                    except ValueError:
                        print("Invalid input!")

            else:
                self.bet_type = choice
                self.update_bet_amount(int(input("Enter your bet amount: $")))

            if self.place_bet():
                self.spin_roulette()
                payout = self.calculate_payout()

                if payout > 0:
                    self.balance += payout
                    print(f"\nCongratulations! You won ${payout}.")
                else:
                    print("\nSorry, you lost.")
                print(f"The ball landed on: {self.ball.number}")

                input("\nPress Enter to continue...")
                self.reset()

casino = Casino(1000)