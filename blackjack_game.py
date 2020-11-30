#the simple blackjack game 

from random import randint
from IPython.display import clear_output

class blackjack():
    def __init__(self):
        self.deck=[]
        self.suits = ("spades" , "hearts" , "diamonds" , "clubs")
        self.values = (2,3,4,5,6,7,8,9,10,"J","Q","K","A")

    def makeDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value , suit))
    
    def pullCard(self):
        return self.deck.pop(randint(0 , len(self.deck)-1))

#create a class for the dealer and player objects
class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []

    def addCard(self , card):
        self.hand.append(card)

    def showHand(self , dealer_start = True):
        print("\n{}".format(self.name))
        print("================")
        for i in range(len(self.hand)):
            if self.name == "dealer" and i==0 and dealer_start:
                print("- of -")
            else:
                card = self.hand[ i ]
                print("{} of {}".format(card[0] , card[1]))
            print ("Total = {}".format(self.calcHand(dealer_start)))

#if not dealer's turn give back total of second card
def calcHand(self , dealer_start=True):
    total = 0
    aces = 0
    card_values = {1:1 , 2:2 , 3:3 , 4:4 , 5:5 , 6:6 , 7:7 , 8:8 , 9:9, 10:10 , "J":10 , "Q":10 , "K":10,"A":11}
    if self.name == "dealer" and dealer_start:
        card = self.hand[1]
        return card_values[card[0]]
    for card in self.hand:
        if card[0] == "A":
            aces +=1
        else:
            total += card_values[card[0]]
    for i in range(aces):
        if total+11>21:
            total+=1
        else: 
            total+=11
    return total
game = blackjack()
game.makeDeck()
name = input("whats your name?")
player = Player(name)
dealer = Player("dealer")

for i in range(2):
    player.addCard(game.pullCard())
    dealer.addCard(game.pullCard())

player.showHand()
dealer.showHand()

