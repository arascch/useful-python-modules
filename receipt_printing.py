#product and prices
p1_name , p1_price = "books",49.95
p2_name , p2_price = "Computer",579.99
p3_name , p3_price = "Monitor",124.89

#company and information
company_name = "coding temple, inc."
company_address = "283 Franklin st."
company_city = "boston , ma"

#ending message as you like to say
message = "Thanks for shopping with us today!"

#borders
print("*" * 50)

#print company information
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))

#between sections 
print("=" * 50)

#print product info
print("\tProduct Name\tProdict Price")

#statement of each product
print("\t{}\t\t${}".format(p1_name.title() , p1_price))
print("\t{}\t\t${}".format(p2_name.title() , p2_price))
print("\t{}\t\t${}".format(p3_name.title() , p3_price))

#lines between sections 
print('='*50)

#print out total header
print("\t\t\tTotal")

#price calculation
total = p1_price + p2_price + p3_price
print("\t\t\t${}".format(total))

#between section 
print("="*50)

#ending message 
print("\n\t{}\n".format(message))

#bottom border
print("*"*50)
