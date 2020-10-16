#ask user for calculation

operation = input("would you like to add/subtract/multiply/divide?").lower()
print ("you chose {}.".format(operation))

#ask for numbers to calculate

if operation =="subtract" or operation=="divide":
    print("you chose{}.".format(operation))
    print("please keep in mind that the order of your number matter")

num1 = input("what is the first number?")
num2 = input("what is the second number?")
print("first number:{}".format(num1))
print("the second number:{}".format(num2))