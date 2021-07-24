names = []
phone_numbers = []

open = int(input("please enter your request: 1- add , 2- search\n"))

if open == 1 :
    num = int(input("how many numbers you want to add? \n"))
    for i in range(num):
        name = input("name: ")
        try:
            phone_number = int(input("phone number: "))
        except ValueError:
            print("your entery incorrect")

        names.append(name)
        try:
            phone_numbers.append(phone_number)
        except ValueError:
            print("your entery incorrect")
        
        

    print("\nName\t\t\tPhone Number")

    for i in range(num):
        print("{}\t\t\t{}".format(name[i] , phone_number[i]))

elif open == 2 :
    num = int(input("how many numbers you want to search? \n"))
    search_term = input("\Enter search term: ")

    print("search Result: ")

    if search_term in names:
        index = names.index(search_term)
        phone_number = phone_numbers[index]
        print("name: {} , Phone Number: {}".format(search_term, phone_number))
    else:
        print("name not Found")