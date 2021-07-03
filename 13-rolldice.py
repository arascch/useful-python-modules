from random import randint
min = 1 
max = 6 

roll_again = "yes"

while roll_again == "yes" or roll_again=="y":
    print ("Rolling the dices ...")
    print ("the value are ...")
    print (randint(min , max))
    print (randint(min , max))

    roll_again = input("Roll the dices again? YES/Y or NO/N\n")
