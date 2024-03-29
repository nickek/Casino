import random
import sqlite3
import database_management

connector = sqlite3.connect("user_database.db")
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

    def value(self):
        return self.hand.get_value()


class Dealer(Player):
    def see_card(self):
        print("Dealer's card:")
        print(f"{self.hand.cards[0].rank} of {self.hand.cards[0].suit}")

    def final_see_card(self):
        print("Dealer's cards:")
        for card in self.hand.cards:
            print(f"{card.rank} of {card.suit}")
        print("Total value:", self.hand.get_value())

    def game(self, user, j):
        j = 0
        while self.hand.get_value() < 17:
            self.hit()
        if self.hand.get_value() > 21:
            self.final_see_card()
            print("Dealer busts! You win!")
            j = 1
            return j
        elif self.hand.get_value() > user.hand.get_value():
            self.final_see_card()
            print("Dealer wins!")
            j = 2
            return j
        elif self.hand.get_value() < user.hand.get_value() & user.hand.get_value() <= 21:
            self.final_see_card()
            print("You beat the dealer! You win!")
            j = 1
            return j
        else:
            self.final_see_card()
            print("It's a tie!")
            j = 3
            return j


def main(user):

    playing = True
    while playing:
        random.seed()
        balance = user.balance
        print("-------------------------")
        print('Lets play Blackjack!')
        print('Your Balance: ' + str(balance))
        bet = int(input('Please place your bets: '))
        if bet > balance:
            print("Insufficient balance. Please place a valid bet.")
            break
        deck = Deck()
        player = Player(deck)
        pc = Dealer(deck)
        player.see_cards()
        pc.see_card()
        j=0
        p=0

        if player.win():
            print("----------------------------------")
            pc.final_see_card()
            print("Blackjack! You win!")
            p = 4
            # player_op = input('Do you want to keep playing? y/n ')
            # if player_op == n:
            #     break
        elif pc.win():
            print("----------------------------------")
            pc.final_see_card()
            print("The dealer won!")
            p = 2
        else:
            while not player.lose():
                if j == 0:
                    choice = input("Hit (1), Stand (2), or Double Down (3)?: ")
                    print("-------------------------")
                else:
                    choice = input("Hit (1), Stand (2): ")
                    print("-------------------------")


                pc.see_card()
                if choice == '1':
                    player.hit()
                    player.see_cards()
                    j = 1
                    if player.value() > 21:
                        print("You bust! Dealer wins!")
                        player.see_cards()
                        pc.final_see_card()
                        p = 2
                        break
                elif choice == '2':
                    player.stand()
                    p = pc.game(player, p)
                    break
                elif choice == '3':
                    if j == 0:
                        player.hit()
                        player.see_cards()
                        p = pc.game(player, p)
                        break
                    else:
                        print("Invalid input, please input 1 or 2")
                        print("----------------------------------")
                else:
                    print("Invalid input, please input 1, 2, or 3")
                    print("----------------------------------")
                    player.see_cards()
                    pc.see_card()

            if p == 1: #regular win
                user.balance = bet + balance
                user.net_profit += bet
                #print(user.balance)
                player_op = input('Do you want to play again? y/n ')
                if player_op == 'n':
                    break
            elif p == 2: #dealer win
                user.balance = balance - bet
                user.net_profit -= bet
                #print(user.balance)
                player_op = input('Do you want to play again? y/n ')
                if player_op == 'n':
                    break
            elif p == 3: #push
                user.balance = balance
                #print(user.balance)
                player_op = input('Do you want to play again? y/n ')
                if player_op == 'n':
                    break
            elif p == 4: #blackjack
                user.balance = (bet*2.5) + balance
                user.net_profit += (bet * 2.5)
                #print(user.balance)
                player_op = input('Do you want to play again? y/n ')
                if player_op == 'n':
                    break

if __name__ == "__main__":
    main()