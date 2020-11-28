import csv
from ipython.display import clear_output

#user registeration
def registerUser():
    with open("user.csv", mode="a" , newline="") as f:
        writer = csv.writer(f,delimiter=",")
        print =("To register , please enter your info:" )
        email = input("E-mail:")
        password = input("password=")
        password2 = input("re-enter your password=")
        clear_output()
        if password == password2:
            writer.writerow([email , password])
            print("you are now registered")
        else:
            print("something wrong . Try agine.")
        
#ask for user login

def loginUser():
    print("login , please enter your info:")
    email = input("E-mail:")
    password = input("password :")
    clear_output()
    with open("users.csv" , mode="r") as f:
        reader = csv.reader(f , delimiter=",")
        for row in reader:
            if row==[email , password]:
                print("you are now logged in!")
                return True
    print("something wrong ,Try again.")
    return False

#main loop for register and something else user want to do
active = True
logged_in=False

while active:
    if logged_in:
        print("1. Logout \n2. Quit")
    else:
        print("1. Login\n 2.Register \n 3.Quit")
    choice = input("what Would you like to do ?").lower()
    clear_output()
    if choice == "register" and logged_in==False:
        registerUser()
    elif choice=="login" and logged_in==False:
        logged_in = loginUser()
    elif choice=="Quit":
        active = False
        print("thanks for using our application")
    elif choice=="logout" and logged_in==True:
        logged_in==False
        print("you are now logged out")
    else:
        print("sorry please try again!")
        