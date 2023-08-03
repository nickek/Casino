import random
import time
import sqlite3

connector = sqlite3.connect("user_database.db")  # added to connect game to our user database
cursor = connector.cursor()

cursor.execute

connector.commit()

red, black, green = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36], [2, 4, 6, 8, 10, 11, 13, 15,
                                                                                          17, 20, 22, 24, 26, 28, 29,
                                                                                          31, 33, 35], [0]

game_still_going = True
broke = False
bet_options = {
    1: "red",
    2: "black",
    3: "green",
    4: "high",
    5: "low",
    6: "odd",
    7: "even",
    8: "specific"
}
payouts = {
    "red": 2,
    "black": 2,
    "green": 35,
    "high": 2,
    "low": 2,
    "odd": 2,
    "even": 2,
    "specific": 35
}

colour_choice = ""
roll_result = ""
win_red = False
win_green = False
win_black = False
lose = False
resulting_number = None


def handle_turn(user):
    global colour_choice
    global betamount

    print("\nBet options:")
    for key, value in bet_options.items():
        print(f"{key}: {value.capitalize()}")

    valid_bet = False
    while not valid_bet:
        try:
            bet_choice = int(input("\nChoose a betting option (1-8): "))
            if bet_choice not in bet_options:
                raise ValueError("Invalid bet option.")

            betamount = int(input(f"\nBet amount? (€{user.balance} available)\n"))
            if betamount <= 0 or betamount > user.balance:
                raise ValueError("Invalid bet amount.")

            valid_bet = True
        except ValueError as ve:
            print(ve)

    print("$" + str(betamount))
    colour_choice = bet_options[bet_choice]
    print("$" + str(betamount) + " on " + colour_choice)
    time.sleep(0.5)


def roll_ball():
    global roll_result
    global resulting_number

    resulting_number = random.randint(0, 36)
    if resulting_number in red:
        roll_result = "Red"
    elif resulting_number in black:
        roll_result = "Black"
    elif resulting_number in green:
        roll_result = "Green"
    else:
        roll_result = "Specific"

    if colour_choice != "specific":
        print(roll_result, resulting_number)


def check_win():
    global win_black
    global win_red
    global win_green
    global lose

    win_red = False
    win_green = False
    win_black = False
    lose = False

    if colour_choice == "specific":
        valid_specific = False
        while not valid_specific:
            specific_number = int(input("Enter the specific number you want to bet on (0-36): "))
            if specific_number >= 0 and specific_number <= 36:
                valid_specific = True
            else:
                print("Invalid number. Please enter a number between 0 and 36.")

        print("$" + str(betamount) + " on specific number " + str(specific_number))
        if specific_number == resulting_number:
            win_red = True
            print("Specific number wins!")
        else:
            lose = True
            print("You lose! $" + str(betamount))
    elif colour_choice in ["red", "black", "green", "high", "low", "odd", "even"]:
        if (colour_choice == "red" and roll_result == "Red") or (
                colour_choice == "black" and roll_result == "Black") or (
                colour_choice == "green" and roll_result == "Green"):
            win_red = True
            print(colour_choice.capitalize() + " wins!")
        elif (colour_choice == "high" and resulting_number > 18) or (colour_choice == "low" and resulting_number <= 18):
            win_red = True
            print(colour_choice.capitalize() + " wins!")
        elif (colour_choice == "odd" and resulting_number % 2 != 0) or (
                colour_choice == "even" and resulting_number % 2 == 0):
            win_red = True
            print(colour_choice.capitalize() + " wins!")
        else:
            lose = True
            print("You lose! $" + str(betamount))



def check_if_broke(user):
    global broke
    if user.balance < 1:
        broke = True
        print("Broke! Please leave!")
    else:
        pass


def increment_bank(user):
    global win_red

    if win_red:
        user.balance += betamount * payouts[colour_choice]
    else:
        user.balance -= betamount


    connector.commit()

    print("Bank: $" + str(user.balance))



def play(user):
    global broke

    while not broke:
        handle_turn(user)
        roll_ball()
        check_win()
        increment_bank(user)
        check_if_broke(user)

        if broke:
            print("Game Over! You have gone broke.")
            return

        print("Bank: $" + str(user.balance))
        play_again = input("Continue playing? (y/n): ")
        if play_again.strip().lower() != 'y':
            print("Thanks for playing!\n")
            return

class User:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance


if __name__ == "__main__":
    main()