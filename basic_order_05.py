# Version 05 aims to define a function for a group of clients ordering several items at the same time

# Modify the program so in the final bill it includes a line that says
# "Party of X people" 
# "Average cost per customer EUR Y"
# Where X is the number of people sitting in the table and Y is the average spend per customer

# Write a function ask_number_items(item_name)
# - The function asks the user to input a number of items of type item_name
# - The function returns an integer with the number of items

# Change the function ask_client so it uses ask_number_items inside

# Debug the program to see how the flow goes over the functions


print("Hello to the Python bar!")
people = input("How many people?")
print("Perfect. You can sit here")

# Configuration Variables

bill = 0

PRICE_COFFEE = 2
PRICE_CROISSANT = 5
PRICE_JUICE = 3

# Prompt for a Coffee

def ask_client(item_name, item_price, current_bill):
    order = input("Would you like a " + item_name + "? (y for yes, n for no)")
    
    if order == "y":
        item_number = input("How many would you like? (input number)")
        current_bill = current_bill + int(item_number)*item_price        
    elif order == "n":
        current_bill = current_bill
    else:
        print("The input is not valid!")

    return order, current_bill



""" order_coffee = input("Would you like a coffee? (y for yes, n for no) ")

if order_coffee == "y":
    bill = bill + PRICE_COFFEE
elif order_coffee == "n":
    bill = bill
else:
    print("The input is not valid!")
 """

order_coffee, bill = ask_client("coffee", PRICE_COFFEE, bill)
order_croissant, bill = ask_client("croissant", PRICE_CROISSANT, bill)
order_juice, bill = ask_client("juice", PRICE_JUICE, bill)




# Prompt for a Croissant

""" order_croissant = input("Would you like a croissant? (y for yes, n for no) ")

if order_croissant == "y":
    bill = bill + PRICE_CROISSANT
elif order_croissant == "n":
    bill = bill
else:
    print("The input is not valid!")
"""

# Prompt for a Juice

""" order_juice = input("Would you like a juice? (y for yes, n for no) ")

if order_juice == "y":
    bill = bill + PRICE_JUICE
elif order_juice == "n":
    bill = bill
else:
    print("The input is not valid!")
"""

# Summarise the order
# Function str transform a number into a text so we can add (+) elements of the same type 

if order_coffee == "y" and order_croissant == "y" and order_juice == "y" :
    print("You've ordered a coffee, a croissant and a juice!")
    #print("The bill is " + str(bill) + " euros.")
    #print("Thanks!")
elif order_coffee == "y" and order_croissant == "y" and order_juice == "n" :
    print("You've ordered a coffee and a croissant!")
    #print("The bill is " + str(bill) + " euros.")
    #print("Thanks!")
elif order_coffee == "y" and order_croissant == "n" and order_juice == "y":
    print("You've ordered a coffee and a juice!")
    #print("The bill is " + str(bill) + " euros.")
    #print("Thanks!")
elif order_coffee == "n" and order_croissant == "y" and order_juice == "y":
    print("You've ordered a croissant and a juice!")
    #print("The bill is " + str(bill) + " euros.")
    #print("Thanks!")
elif order_coffee == "y" and order_croissant == "n" and order_juice == "n":
    print("You've ordered a coffee!")
    #print("The bill is " + str(bill) + " euros.")
    #print("Thanks!")
elif order_coffee == "n" and order_croissant == "y" and order_juice == "n":
    print("You've ordered a croissant!")
    #print("The bill is " + str(bill) + " euros.")
    #print("Thanks!")
elif order_coffee == "n" and order_croissant == "n" and order_juice == "y":
    print("You've ordered a juice!")
    #print("The bill is " + str(bill) + " euros.")
    #print("Thanks!")
else:
    print("You didn't order anything today!")
    print("Hope you order something next time, thanks!")

print ("The bill is " + str(bill) + " euros.")
print ("Party of " + people + " people")
print ("Average cost per customer EUR " + str(bill/int(people)))
print ("Thanks!")