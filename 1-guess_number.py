from random import randint
from IPython.display import clear_output
gussed = False
number = randint(0 , 100)
guesses = 0
while not gussed :
    ans = input("try to guess the number I am thinking of!")
    guesses +=1
    clear_output()
    if int(ans) == number:
        print("Congrates! you Guessed it correctly.")
        print("it took you {} guesses!".format(guesses))
        break
    elif int(ans)>number:
        print("the number is lower than what you guessed.")
    elif int(ans)<number:
        print("the number is greater than what you guessed.")