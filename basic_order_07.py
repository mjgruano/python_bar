# Version 07 aims to define a function to take the order not for a single person but for all the people in a table

# Write a function ask_number_items(item_name)
# - The function asks the user to input a number of items of type item_name
# - The function returns an integer with the number of items

# Change the function ask_client so it uses ask_number_items inside

# Debug the program to see how the flow goes over the functions

PRICE_COFFEE = 2
PRICE_CROISSANT = 5

print("Hello to the Python bar!")
people = input("How many people?")
print("Perfect. You can sit here")

def ask_number(item_name):
    number_items = input("How many " + item_name + " would you like?")

    if number_items != "0":
        print("You are ordering " + number_items + " " + item_name)
    elif number_items == "0":
        print("You are not ordering any " + item_name)
    else:
        print("The input is not valid!")

    return number_items

number_coffee = ask_number("coffee")
number_croissant = ask_number("croissant")

bill = int(number_coffee) * PRICE_COFFEE + int(number_croissant) * PRICE_CROISSANT

print("The bill is " + str(bill))
