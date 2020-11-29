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

game = blackjack()
game.makeDeck()
print(game.deck)

