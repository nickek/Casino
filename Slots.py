import random
from User import *
from main import *
print('''Welcome to the Slot Machine! You'll be asked if you want to play. Answer with yes/no. 
You win if you get any of the following combinations:
BAR\tBAR\tBAR\t\twins\t$250
BELL\tBELL\tBELL/BAR\twins\t$20
PLUM\tPLUM\tPLUM/BAR\twins\t$14
ORANGE\tORANGE\tORANGE/wins\tpays\t$10
CHERRY\tCHERRY\tCHERRY\t\twins\t$7
CHERRY\tCHERRY\t  -\t\twins\t$5
CHERRY\t  -\t  -\t\twins\t$2
''')
#Constants:
ITEMS = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR"]

firstWheel = None
secondWheel = None
thirdWheel = None
money = users.balance

def play():
    global money, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while(money != 0 and playQuestion == True):
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()
        playQuestion = askPlayer()

def askPlayer():
    '''
    Asks the player if he wants to play again.
    '''
    global money
    while(True):
        answer = input("You have $" + str(money) + ". Would you like to play? ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("You ended the game with $" + str(money) + " in your hand.")
            return False
        else:
            print("wrong input!")

def spinWheel():
    '''
    returns a random item from the wheel
    '''
    randomNumber = random.randint(0, 5)
    return ITEMS[randomNumber]

def printScore():
    '''
    prints the current score
    '''
    global money, firstWheel, secondWheel, thirdWheel
    if((firstWheel == "CHERRY") and (secondWheel != "CHERRY")):
        win = 2
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel != "CHERRY")):
        win = 5
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel == "CHERRY")):
        win = 7
    elif((firstWheel == "ORANGE") and (secondWheel == "ORANGE") and ((thirdWheel == "ORANGE") or (thirdWheel == "BAR"))):
        win = 10
    elif((firstWheel == "PLUM") and (secondWheel == "PLUM") and ((thirdWheel == "PLUM") or (thirdWheel == "BAR"))):
        win = 14
    elif((firstWheel == "BELL") and (secondWheel == "BELL") and ((thirdWheel == "BELL") or (thirdWheel == "BAR"))):
        win = 20
    elif((firstWheel == "BAR") and (secondWheel == "BAR") and (thirdWheel == "BAR")):
        win = 250
    else:
        win = -1

    money += win
    if(win > 0):
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You win $' + str(win))
    else:
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You lose')

play()