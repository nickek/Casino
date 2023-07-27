import random

class Card(object):
    def __init__(self, name, value, suit):
        # CARD ATTRIBUTES
        self.value = value
        self.suit = suit
        self.name = name
        self.showing = False  # False = Face Down, True = Face Up

    def __repr__(self):
        # HOW THE CARD IS REPRESENTED (SHOWING / NOT SHOWING)
        if self.showing:
            return f"{self.name}{self.suit}"
        else:
            return "??"

class Deck(list):
    def shuffle(self):
        random.shuffle(self)

    def deal(self):
        return self.pop(0)

# INHERITS FROM THE DECK CLASS
class StandardDeck(Deck):
    def __init__(self):
        # DECK ATTRIBUTES
        suits = ["♥", "♠", "♣", "♦"]
        values = {"2": 2,
                  "3": 3,
                  "4": 4,
                  "5": 5,
                  "6": 6,
                  "7": 7,
                  "8": 8,
                  "9": 9,
                  "10": 10,
                  "J": 11,
                  "Q": 12,
                  "K": 13,
                  "A": 14}

        # NESTED LOOP TO CREATE DECK (LIST)
        for name in values:
            for suit in suits:
                self.append(Card(name, values[name], suit))

    def __repr__(self):
        # HOW THE DECK IS REPRESENTED
        return "Standard deck of cards: {0} remaining.".format(len(self))

class Player(object):
    def __init__(self):
        # PLAYER ATTRIBUTES
        self.cards = []
        self.money = 0

    def cardCount(self):
        return len(self.cards)
        pass

    def addCard(self, card):
        self.cards.append(card)

def interpreter():
    player = Player()

    # INITIAL AMOUNT
    player.money = 10000

    # NUMBER OF CARDS DEALT
    num_cards = 0

    # BET AMOUNT
    bet_amount = 0

    # BET CHOICE
    bet_low = False
    bet_mid = False
    bet_high = False

    # WRONG GUESS
    wrong_guess = False

    end = False

    while not end:

        # HAND LOOP
        deck = StandardDeck()
        deck.shuffle()

        validInput = False
        while not validInput:
            print(f"You have: ${player.money}")
            print("Do you want to place a low, mid, or high bet?")
            print("Low: ($500 = 5 cards), Mid: ($2500 = 10 cards), High: ($5000 = 15 cards)")
            print("Type 'exit' to Exit")
            inputStr = input()

            if inputStr == "exit":
                end = True
                break

            if inputStr == "low":
                print("You chose a low bet!")
                bet_amount = 500
                bet_low = True
                num_cards = 5

            if inputStr == "mid":
                print("You chose a mid bet!")
                bet_amount = 2500
                bet_mid = True
                num_cards = 10

            if inputStr == "high":
                print("You chose a high bet!")
                bet_amount = 5000
                bet_high = True
                num_cards = 15

            try:
                # CHECK IF USER'S BET IS UNDER THEIR CURRENT EARNINGS
                    if player.money - bet_amount > 0:
                        player.money = player.money - bet_amount
                        validInput = True
            except:
                print("Not enough money: Please choose a lower bet / exit the game")

        # DEAL OUT
        for i in range(num_cards):
            player.addCard(deck.deal())

        for card in player.cards:
            card.showing = True
            print(player.cards)
            for i in range(num_cards - 1):
                print("Is the next card higher, lower, or equal (h,l,e)?")
                inputStr = input()

                if inputStr == "h" and (player.cards[i + 1].value > player.cards[i].value):
                    print("Correct!")
                    player.cards[i + 1].showing = True
                    print(player.cards)
                    continue
                if inputStr == "e" and (player.cards[i + 1].value == player.cards[i].value):
                    print("Correct!")
                    player.cards[i + 1].showing = True
                    print(player.cards)
                    continue
                if inputStr == "l" and (player.cards[i + 1].value < player.cards[i].value):
                    print("Correct!")
                    player.cards[i + 1].showing = True
                    print(player.cards)
                    continue
                else:
                    print(f"Wrong! Lost ${bet_amount}!")
                    wrong_guess = True
                    break
            if wrong_guess:
                player.cards = []
                break
            else:
                if bet_low:
                    print(f"You won {bet_amount * 2}")
                if bet_mid:
                    print(f"You won {bet_amount * 4}")
                if bet_high:
                    print(f"You won {bet_amount * 8}")
                player.money = player.money + bet_amount
                player.cards = []
                break

# MAIN
interpreter()
