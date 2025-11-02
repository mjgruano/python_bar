# Version 08 aims to define a function to take the order not for a single person but for all the people in a table
# We can choose the number of items (not only1 as in version 04)

# Write a function print_bill_item(item_name)
# - The function asks the user to input a number of items of type item_name
# - The function returns an integer with the number of items


print("Hello to the Python bar!")

# Configuration Variables

bill = 0

PRICE_COFFEE = 2
PRICE_CROISSANT = 5
PRICE_JUICE = 3


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

"""
if order_coffee == "y" and order_croissant == "y" and order_juice == "y" :
    print("You've ordered",str(number_coffee), "coffee",str(number_croissant), "croissant", "and ", str(number_juice), "juice")
  
elif order_coffee == "y" and order_croissant == "y" and order_juice == "n" :
    print("You've ordered",str(number_coffee), "coffee","and ", str(number_croissant), "croissant")

elif order_coffee == "y" and order_croissant == "n" and order_juice == "y":
    print("You've ordered",str(number_coffee), "coffee", "and ", str(number_juice), "juice")

elif order_coffee == "n" and order_croissant == "y" and order_juice == "y":
    print("You've ordered",str(number_croissant), "croissant", "and ", str(number_juice), "juice")

elif order_coffee == "y" and order_croissant == "n" and order_juice == "n":
    print("You've ordered", str(number_coffee), "coffee")

elif order_coffee == "n" and order_croissant == "y" and order_juice == "n":
    print("You've ordered",str(number_croissant), "croissants")

elif order_coffee == "n" and order_croissant == "n" and order_juice == "y":
    print("You've ordered",str(number_juice), "juices")

else:
    print("You didn't order anything today!")
    print("Hope you order something next time, thanks!")

print ("The bill is " + str(bill) + " euros.")
print ("Thanks!")

"""