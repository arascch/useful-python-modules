from IPython.display import clear_output
#Global list variable
cart = []

#function for adding item to the cart
def additem(item):
    clear_output()
    cart.append(item)
    print("{} has been added".format(item))

#function for remove items from carts

def removeitem(item):
    clear_output()
    try:
        cart.remove(item)
        print("{} has been removed.".format(item))
    except :
        print("sorry you item can't remove form cart")

#function for showing the items in cart

def showCart():
    clear_output()
    if cart:
        print("here is your cart:")
        for item in cart:
            print("- {}".format(item))
    else:
        print("your cart is empty")

#the main function for do every thing user need to do and loops until the user quits
def clearCart():
    cart.clear()
    print("all items delet from the cart")


def main():
    done = False
    while not done:
        ans = input("/add/remove/show/clear/quit:").lower()
        
        if ans =="quit":
            print("thanks for using our program.")
            showCart()
            done=True
        elif ans == "add":
            item = input("what would you like to add?").title()
            additem(item)
        elif ans == "remove":
            showCart()
            item = input("what would you like to remove from the cart?").title()
            removeitem(item)
        elif ans == "show":
            showCart()
        elif ans == "clear":
            clearCart()
        else:
            print("sorry that was not an option")
    
main()
