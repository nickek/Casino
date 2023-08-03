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
    def __init__(self, deck, balance):
        self.balance = balance
        self.hand = Hand()
        self.deck = deck
        self.hit()
        self.hit()  #add two cards to player hand

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
    def value(self):
        return self.hand.get_value()

class Dealer(Player):
    def see_card(self):
        print("Dealer's cards:")
        print(f"{self.hand.cards[0].rank} of {self.hand.cards[0].suit}")

    def final_see_card(self):
        print("Dealer's cards:")
        for card in self.hand.cards:
            print(f"{card.rank} of {card.suit}")
        print("Total value:", self.hand.get_value())

    def game(self, user):
        while self.hand.get_value() < 17:
            self.hit()
        #self.see_card()
        if self.hand.get_value() > 21:
            self.final_see_card()
            print("Dealer busts! You win!")
            #user wins bet
            user.balance = money + (bet*2)

        elif self.hand.get_value() > user.hand.get_value():
            self.final_see_card()
            print("Dealer wins!")
            user.balance = money - bet
        elif self.hand.get_value() < user.hand.get_value():
            self.final_see_card()
            print("You beat the dealer! You win!")
            user.balance = money + (bet * 2)
        else:
            self.final_see_card()
            print("It's a tie!")
            money = money + bet

def main(user):
    random.seed()
    print("Your balance:", user.balance)
    print('Lets play Blackjack!')
    print("-------------------------")
    bet = int(input("Please place your bet (min. $25) before playing: "))

    if bet > user.balance:
        print("Insufficient funds. Please add funds to your account.")
        return

    user.balance -= bet  # Reduce user's balance by the bet amount
    print("Good Luck!")
    deck = Deck()  # creates a deck
    user = Player(deck,user.balance)  # creates a player that will use deck
    pc = Dealer(deck,user.balance)  # creates a dealer that will use the same deck
    user.see_cards()
    pc.see_card()
    if user.win():  # checks user's hand to see if they win
        print("----------------------------------")
        pc.final_see_card()
        print("Blackjack! You win!")
        winnings = int(bet * 2.5)
        user.balance += winnings
    elif pc.win():  # checks dealer's hand to see if they win
        print("----------------------------------")
        pc.final_see_card()
        print("The dealer won!")
    else:
        while not user.lose():  # while user has not lost yet
            choice = input("Hit (1), Stand (2), or Double Down (3)?: ")  # ask user to hit or stand
            print("-------------------------")
            user.see_cards()
            pc.see_card()
            if choice == '1':  # hit
                user.hit()
                if user.value() > 21:
                    print("You bust! Dealer wins!")
                    user.see_cards()
                    pc.final_see_card()
                    break
            elif choice == '2':  # stand
                user.stand()
                pc.game(user)
                break
            elif choice == '3': # double down
                if user.balance < bet:
                    print('Please add funds to your account')
                else:
                    #line to double initial bet
                    bet *= 2
                    user.hit()
                    user.see_cards()
                    pc.game(user)
            elif choice != '1' '2' '3':  # will ask user to try again if there is wrong input
                print("Invalid input, please input 1, 2, or 3")
                print("----------------------------------")
                user.see_cards()  # shows user's cards
                pc.see_card()  # shows dealer's card
# Update user balance in the database
cursor.execute("UPDATE user SET balance = ? WHERE username = ?", (user.balance, user.username))
connector.commit()

if __name__ == "__main__":
    username = input("Enter your username: ")
    cursor.execute("SELECT balance FROM users WHERE username = ?", (username,))
    balance = cursor.fetchone()[0]
    user = Player(Deck(), balance)
    main(user)