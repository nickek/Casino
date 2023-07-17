import random

class Card( object ):
  def __init__(self, name, value, suit):
    self.value = value
    self.suit = suit
    self.name = name
    self.showing = False # False = Face Down, True = Face Up

  def __repr__(self):
    # HOW THE CARD IS REPRESENTED (SHOWING / NOT SHOWING)
    if self.showing:
      return f"{self.name}{self.suit}"
    else:
      return "Card"

class Deck(object):
  def shuffle(self):
    random.shuffle(self.cards)
    print("Deck Shuffled")

  def deal(self):
    return self.cards.pop(0)

class StandardDeck(Deck):
  def __init__(self):
    # DECK ATTRIBUTES
    self.cards = []
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

    # CREATE THE DECK
    for name in values:
      for suit in suits:
        self.cards.append(Card(name, values[name], suit))

  def __repr__(self):
    # HOW THE DECK IS REPRESENTED
    return "Standard deck of cards:{0} remaining".format(len(self.cards))

class Player(object):
  def __init__(self):
    # PLAYER ATTRIBUTES
    self.cards = []

  def cardCount(self):
    return len(self.cards)

  def addCard(self, card):
    self.cards.append(card)


class PokerScorer(object):
  def __init__(self, cards):
    # NUMBER OF CARDS MUST BE 5 TO CREATE A POKER HAND
    if not len(cards) == 5:
      return "Error: Wrong number of cards"

    self.cards = cards

  def flush(self):
    suits = [card.suit for card in self.cards]
    if len(set(suits)) == 1:
      return True
    return False

  def straight(self):
    values = [card.value for card in self.cards]
    values.sort()

    if not len(set(values)) == 5:
      return False 

    if values[4] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
      return 5

    else:
      if not values[0] + 1 == values[1]: return False 
      if not values[1] + 1 == values[2]: return False
      if not values[2] + 1 == values[3]: return False
      if not values[3] + 1 == values[4]: return False

    return values[4]

  def highCard(self):
    values = [card.value for card in self.cards]
    highCard = None
    for card in self.cards:
      if highCard is None:
        highCard = card
      elif highCard.value < card.value: 
        highCard=card

    return highCard

  def highestCount(self):
    count = 0
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) > count:
        count = values.count(value)

    return count

  def pairs(self):
    pairs = []
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 2 and value not in pairs:
        pairs.append(value)

    return pairs
        
  def fourKind(self):
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 4:
        return True

  def fullHouse(self):
    two = False
    three = False
    
    values = [card.value for card in self.cards]
    if values.count(values) == 2:
      two = True
    elif values.count(values) == 3:
      three = True

    if two and three:
      return True

    return False

def interpreterVideoPoker():
  player = Player()

  # INITIAL AMOUNT
  points = 100

  # COST PER HAND
  handCost = 5

  end = False
  while not end:
    print()
    print("You have {0} points".format(points))

    points -= 5

    # HAND LOOP
    deck = StandardDeck()
    deck.shuffle()

    # DEAL OUT
    for i in range(5):
      player.addCard(deck.deal())

    # MAKE CARDS VISIBLE
    for card in player.cards:
      card.showing = True
    print(player.cards)

    validInput = False
    while not validInput:
      print("Which cards do you want to discard? ( ie. 1, 2, 3 )")
      print("*Hit Return to hold all, type 'exit' to quit")
      inputStr = input()

      if inputStr == "exit":
        end = True
        break

      try:
        inputList = [int(inp.strip()) for inp in inputStr.split(",") if inp]

        # CHECK IF USER'S INPUT IS IN THE APPROPRIATE RANGE (BTWN 1 AND 5)
        for inp in inputList:
          if inp > 6:
            continue 
          if inp < 1:
            continue 

        for inp in inputList:
          player.cards[inp - 1] = deck.deal()
          player.cards[inp - 1].showing = True

        validInput = True
      except:
        print("Input Error: use commas to separated the cards you want to hold")

    print(player.cards)

    # SCORE
    score = PokerScorer(player.cards)
    straight = score.straight()
    flush = score.flush()
    highestCount = score.highestCount()
    pairs = score.pairs()

    # ROYAL FLUSH
    if straight and flush and straight == 14:
      print("ROYAL FLUSH!")
      print("+2000")
      points += 2000

    # STRAIGHT FLUSH
    elif straight and flush:
      print("Straight Flush!")
      print("+250")
      points += 250

    # 4 OF A KIND
    elif score.fourKind():
      print("Four of a Kind!")
      print("+125")
      points += 125

    # FULL HOUSE
    elif score.fullHouse():
      print("Full House!")
      print("+40")
      points += 40

    # FLUSH
    elif flush:
      print("Flush!")
      print("+25")
      points += 25

    # STRAIGHT
    elif straight:
      print("Straight!")
      print("+20")
      points += 20

    # 3 OF A KIND
    elif highestCount == 3:
      print("Three of a Kind!")
      print("+15")
      points += 15

    # 2 PAIR
    elif len(pairs) == 2:
      print("Two Pairs!")
      print("+10")
      points += 10

    # JACKS OR BETTER
    elif pairs and pairs[0] > 10:
      print ("Jacks or Better!")
      print("+5")
      points += 5

    player.cards = []

interpreterVideoPoker()


  
  


    
