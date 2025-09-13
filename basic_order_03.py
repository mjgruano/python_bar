# Version 03 aims to add a new variable to the list of products

print("Hello to the Python bar!")

# Configuration Variables

bill = 0

PRICE_COFFEE = 2
PRICE_CROISSANT = 5
PRICE_JUICE = 3

# Prompt for a Coffee

order_coffee = input("Would you like a coffee? (y for yes, n for no) ")

if order_coffee == "y":
    bill = bill + PRICE_COFFEE
elif order_coffee == "n":
    bill = bill
else:
    print("The input is not valid!")

# Prompt for a Croissant

order_croissant = input("Would you like a croissant? (y for yes, n for no) ")

if order_croissant == "y":
    bill = bill + PRICE_CROISSANT
elif order_croissant == "n":
    bill = bill
else:
    print("The input is not valid!")

# Prompt for a Juice

order_juice = input("Would you like a juice? (y for yes, n for no) ")

if order_juice == "y":
    bill = bill + PRICE_JUICE
elif order_juice == "n":
    bill = bill
else:
    print("The input is not valid!")

# Summarise the order
# Function str transform a number into a text so we can add (+) elements of the same type 

if order_coffee == "y" and order_croissant == "y" and order_juice == "y" :
    print("You've ordered a coffee, a croissant and a juice!")
    print("The bill is " + str(bill) + " euros.")
    print("Thanks!")
elif order_coffee == "y" and order_croissant == "y" and order_juice == "n" :
    print("You've ordered a coffee and a croissant!")
    print("The bill is " + str(bill) + " euros.")
    print("Thanks!")
elif order_coffee == "y" and order_croissant == "n" and order_juice == "y":
    print("You've ordered a coffee and a juice!")
    print("The bill is " + str(bill) + " euros.")
    print("Thanks!")
elif order_coffee == "n" and order_croissant == "y" and order_juice == "y":
    print("You've ordered a croissant and a juice!")
    print("The bill is " + str(bill) + " euros.")
    print("Thanks!")
elif order_coffee == "y" and order_croissant == "n" and order_juice == "n":
    print("You've ordered a coffee!")
    print("The bill is " + str(bill) + " euros.")
    print("Thanks!")
elif order_coffee == "n" and order_croissant == "y" and order_juice == "n":
    print("You've ordered a croissant!")
    print("The bill is " + str(bill) + " euros.")
    print("Thanks!")
elif order_coffee == "n" and order_croissant == "n" and order_juice == "y":
    print("You've ordered a juice!")
    print("The bill is " + str(bill) + " euros.")
    print("Thanks!")
else:
    print("You didn't order anything today!")
    print("Hope you order something next time, thanks!")

