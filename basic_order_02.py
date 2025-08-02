print("Hello to the Python bar!")

# Configuration Variables

bill = 0

PRICE_COFFEE = 2
PRICE_CROISSANT = 5

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

# Summarise the order

if order_coffee == "y" and order_croissant == "y":
    print("You've ordered a coffee and a croissant!")
    print("The bill is " + str(bill) + " euros.")
    print("Thanks!")
elif order_coffee == "y" and order_croissant == "n":
    print("You've ordered a coffee!")
    print("The bill is " + str(bill) + " euros.")
    print("Thanks!")
elif order_coffee == "n" and order_croissant == "y":
    print("You've ordered a croissant!")
    print("The bill is " + str(bill) + " euros.")
    print("Thanks!")
else:
    print("You didn't order anything today!")
    print("Hope you order something next time, thanks!")

