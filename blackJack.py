import random
import sqlite3
connector = sqlite3.connect("user_database.db") #added to connect game to our user database
cursor = connector.cursor()


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.rank in ['K', 'Q', 'J']:
                value += 10
            elif card.rank == 'A':
                value += 11
                num_aces += 1
            else:
                value += int(card.rank)

        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value

class Player:
    def __init__(self, deck):
        self.hand = Hand()
        self.deck = deck
        self.hit()
        self.hit()

    def hit(self):
        card = self.deck.cards.pop()
        self.hand.add_card(card)

    def see_cards(self):
        print("Your cards:")
        for card in self.hand.cards:
            print(f"{card.rank} of {card.suit}")
        print("Total value:", self.hand.get_value())

    def win(self):
        return self.hand.get_value() == 21

    def lose(self):
        return self.hand.get_value() > 21

    def stand(self):
        pass

class Dealer(Player):
    def see_card(self):
        print("Dealer's card:")
        print(f"{self.hand.cards[0].rank} of {self.hand.cards[0].suit}")

    def game(self, user):
        while self.hand.get_value() < 17:
            self.hit()
        self.see_cards()
        if self.hand.get_value() > 21:
            print("Dealer busts! You win!")
        elif self.hand.get_value() > user.hand.get_value():
            print("Dealer wins!")
        elif self.hand.get_value() < user.hand.get_value():
            print("You win!")
        else:
            print("It's a tie!")

def main():
    random.seed()  # sets random seed
    print("Welcome to my Casino!")
    print("Let's play Blackjack!")
    print("Good Luck!")
    print("-------------------------")

    deck = Deck()  # creates a deck
    user = Player(deck)  # creates a player that will use deck
    pc = Dealer(deck)  # creates a dealer that will use the same deck

    user.see_cards()
    pc.see_card()

    if user.win():  # checks user's hand to see if they win
        print("You won!")
    elif pc.win():  # checks dealer's hand to see if they win
        print("The dealer won!")
    else:
        while not user.lose():  # while user has not lost yet
            choice = input("Hit (1) or Stand (2)?: ")  # ask user to hit or stand
            if choice == '1':  # hit
                user.hit()
            elif choice == '2':  # stand
                user.stand()
                pc.game(user)
                break
            else:  # will ask user to try again if there is wrong input
                print("Invalid input, please input 1 or 2")
                print("----------------------------------")
            user.see_cards()  # shows user's cards
            pc.see_card()  # shows dealer's card

if __name__ == "__main__":
    main()