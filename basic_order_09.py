# Version 09 aims to include new functions and give a cleaner look to the code

# Write a function print_bill_customer() and call it to show the cost per customer


print("Hello to the Python bar!")

# Configuration Variables

bill = 0

PRICE_COFFEE = 2
PRICE_CROISSANT = 5
PRICE_JUICE = 3

# Configuration Functions

def ask_number_items(item_name):
    items = input("How many " + item_name + " would you like to have?")
    return int(items)

def ask_client(item_name, item_price, current_bill):
    order = input("Would you like a " + item_name + "? (y for yes, n for no)")
    
    if order == "y":
        number_items = ask_number_items(item_name)
        current_bill = current_bill + item_price * number_items
    elif order == "n":
        number_items = 0
        current_bill = current_bill
    else:
        print("The input is not valid!")

    return number_items, order, current_bill

number_coffee, order_coffee, bill = ask_client("coffee", PRICE_COFFEE, bill)
number_croissant, order_croissant, bill = ask_client("croissant", PRICE_CROISSANT, bill)
number_juice, order_juice, bill = ask_client("juice", PRICE_JUICE, bill)

def print_bill_item (item_name, item_units, item_cost):
    if item_units == 0:
        pass
    else:
        """print (item_name + "_______", + item_units," units", "______", item_cost, " euros")"""
        print (f"{item_name:<20} {item_units:>10} units {item_cost:>10} euros")


print_bill_item ("coffee", number_coffee, + number_coffee * PRICE_COFFEE)
print_bill_item ("croissant", number_croissant, + number_croissant * PRICE_CROISSANT)
print_bill_item ("juice", number_juice, number_juice * PRICE_JUICE)

def print_bill_customer ():
    