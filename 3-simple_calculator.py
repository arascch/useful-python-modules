#ask user for calculation

operation = input("would you like to add/subtract/multiply/divide?").lower()

#ask for numbers to calculate

if operation =="subtract" or operation=="divide":
    print("you chose{}.".format(operation))
    print("please keep in mind that the order of your number matter")

num1 = input("what is the first number?")
num2 = input("what is the second number?")


#try/except for mathematical operation

try:
    num1 , num2 = float(num1) , float(num2)
    if operation == "add":
        result = num1+num2
        print("{} + {} = {}".format(num1 , num2, result))
    elif operation == "subtract":
        result = num1 - num2
        print("{} - {} = {}".format(num1, num2,result))
    elif operation == "multiply":
        result = num1 * num2
        print("{} * {} = {}".format(num1, num2, result))
    elif operation == "divide":
        result = num1/num2
        print("{} / {} = {}".format(num1, num2,result))
    else:
        print("sorry , but '{}' is not an option".format(operation))
except :
    print("Error: Improper numbers used. please try again")

#finall