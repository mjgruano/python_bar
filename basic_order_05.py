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

# Write a function ask_number_items(item_name)
# - The function asks the user to input a number of items of type item_name
# - The function returns an integer with the number of items

def ask_number_items(item_name, item_price, current_bill):
    items = input("How many " + item_name + " would you like?")
    
    if items == "2":
        print ("You are ordering " + items + " " + item_name)
        current_bill = current_bill + int(items)*item_price

    elif items == "0":
        print ("You are not ordering any " + item_name)
        current_bill = current_bill 

    else:
        print("The input is not valid!")

    return current_bill

number_coffee = ask_number_items("coffee", PRICE_COFFEE, bill)
number_croissant = ask_number_items("croissant", PRICE_CROISSANT, bill)
number_juice = ask_number_items("juice", PRICE_JUICE, bill)


print ("The bill is " + str(bill) + " euros.")
print ("Party of " + people + " people")
print ("Average cost per customer EUR " + str(bill/int(people)))
print ("Thanks!")