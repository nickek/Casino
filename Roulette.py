import random
from User import *
import time

red, black, green = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36], [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35], [0]

game_still_going = True
broke = False
bet_options = ["red", "black", "green", "high", "low", "odd", "even", "specific"]
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
bank = 0
betamount = 0
colour_choice = ""
roll_result = ""
win_red = False
win_green = False
win_black = False
lose = False
resulting_number = None

def intro():
    global bank
    print('Welcome to Roulette! \n')
    time.sleep(0.5)
    bank = int(input('Enter starting bankroll: '))

def display_table():
    print("Roulette Table")
    print("Red: ")
    print(red)
    print("Black:")
    print(black)
    print("Green:")
    print(green)

def handle_turn():
    global colour_choice
    global betamount
    global bank

    bet_options_str = ", ".join(bet_options)
    print("Available betting options: " + bet_options_str)

    valid_bet = False
    while not valid_bet:
        try:
            bet_choice = input("\nChoose a betting option: ").lower()
            if bet_choice not in bet_options:
                raise ValueError("Invalid bet option.")

            betamount = int(input(f"\nBet amount? (€{bank} available)\n"))
            if betamount <= 0 or betamount > bank:
                raise ValueError("Invalid bet amount.")

            valid_bet = True
        except ValueError as ve:
            print(ve)

    print("€" + str(betamount))
    colour_choice = bet_choice
    print("€" + str(betamount) + " on " + colour_choice)
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
            print("You lose! €" + str(betamount))
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
            print("You lose! €" + str(betamount))


def check_if_broke():
    global broke
    if bank < 1:
        broke = True
        print("Broke! Please leave!")
    else:
        pass

def increment_bank():
    global bank
    if win_red:
        bank += betamount * payouts[colour_choice]
    else:
        bank -= betamount

    print("Bank: €" + str(bank))

def play_game():
    handle_turn()
    roll_ball()
    check_win()
    increment_bank()
    check_if_broke()

intro()
display_table()

while game_still_going:
    play_game()
    if broke:
        break
    if input("Continue? (y/n)").strip().upper() != 'Y':
        break