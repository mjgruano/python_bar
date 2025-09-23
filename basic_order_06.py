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

PRICE_COFFEE = 2
PRICE_CROISSANT = 5

"""
print("Hello to the Python bar!")
people = input("How many people?")
print("Perfect. You can sit here")
"""

"""
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
"""

def get_price_coffee():
    return PRICE_COFFEE

def get_price_croissant():
    return PRICE_CROISSANT

# Use functions

# Calculate the price of 2 coffees

bill_coffees = 2 * get_price_coffee()

print("The price of 2 coffees is " + str(bill_coffees))

# Calculate the price of 4 croissants

bill_croissants = 4 * get_price_croissant()

print("The price of 4 croissants is " + str(bill_croissants)) 

# Calculate the price of 3 coffees and 2 croissants

bill_combo = 3 * get_price_coffee() + 2 * get_price_croissant()

print("The price of 3 coffees and 2 croissants is " + str(bill_combo))

def order_coffee():
    number_coffee = input("How many coffees would you like?")
    return number_coffee

cost_coffee = PRICE_COFFEE * int(order_coffee())

print("The total cost is " + str(cost_coffee))

def get_price_n_coffees(n):
    price = n * PRICE_COFFEE
    return price

# Calculate the price of 2 coffees

bill_coffees = get_price_n_coffees(2) 

print("The price of 2 coffees is " + str(bill_coffees))

print("The price of 2 coffees is " + str(get_price_n_coffees(2)))

print("The price of 2 coffees is " + str(2 * PRICE_COFFEE))

# Create the function multiply(number_1, number_2) that calculates the product number_1 * number_2 and prints the result
# Use the function to calculate 2*3 + 4*5 calling the function multiply to solve the multiplications

def multiply(number_1, number_2):
    return number_1 * number_2

op1 = multiply(2, 3)
op2 = multiply(4, 5)
op3 = op1 + op2
print("The result of 2*3 + 4*5 is " + str(op3))
