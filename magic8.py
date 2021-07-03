import sys 
import random

answer=True 

while answer:
    question = input("ask the magic ball a question:\n (if you don't write anything, program is closing) :\t")

    answers = random.randint(1,8)
    if question == "":
        sys.exit()
    elif answers ==1:
        print ("exactly do it or happening")
    elif answers ==2:
        print("may be good to you")
    elif answers == 3:
        print("rely on it")
    elif answers == 4:
        print("think more")
    elif answers == 5 :
        print ("don't think of it")
    elif answers == 6 : 
        print("my openion is No")
    elif answers == 7 :
        print("think more")
    elif answers == 8 :
        print("ask again")
        
    