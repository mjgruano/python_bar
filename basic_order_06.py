# Version 06 

# Write a function ask_number_items(item_name)
# - The function asks the user to input a number of items of type item_name
# - The function returns an integer with the number of items



PRICE_COFFEE = 2
PRICE_CROISSANT = 5


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

