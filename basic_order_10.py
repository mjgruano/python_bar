# Version 10 aims to make available items generic 

# Configuration Variables

PRICE_ITEM_1 = 3
PRICE_ITEM_2 = 6
PRICE_ITEM_3 = 2
PRICE_ITEM_4 = 4

ITEM_1 = "tea"
ITEM_2 = "cake"
ITEM_3 = "milk"
ITEM_4 = "cookie"

# Configuration Functions

def ask_number_client ():
    print ("Hello to the Python bar!")
    clients = input("How many people in your party?")
    return clients

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

def print_bill_item (item_name, item_units, item_cost):
    if item_units == 0:
        pass
    else:
        print (f"{item_name:<20} {item_units:>10} units {item_cost:>10} euros")

def printline(num,sym):
    for i in range(num):
        bill_line = (num*sym)
    return bill_line
    
def print_bill_customer ():
    print (f"Total cost is {bill:>34} euros")
    print ("The average cost per customer is ", round(bill/int(number_clients), 2), "euros")

# Program body

bill = 0

number_clients = ask_number_client()

number_item_1, order_item_1, bill = ask_client(ITEM_1, PRICE_ITEM_1, bill)
number_item_2, order_item_2, bill = ask_client(ITEM_2, PRICE_ITEM_2, bill)
number_item_3, order_item_3, bill = ask_client(ITEM_3, PRICE_ITEM_3, bill)
number_item_4, order_item_4, bill = ask_client(ITEM_4, PRICE_ITEM_4, bill)

print_bill_item (ITEM_1, number_item_1, + number_item_1 * PRICE_ITEM_1)
print_bill_item (ITEM_2, number_item_2, + number_item_2 * PRICE_ITEM_2)
print_bill_item (ITEM_3, number_item_3, number_item_3 * PRICE_ITEM_3)
print_bill_item (ITEM_4, number_item_4, number_item_4 * PRICE_ITEM_4)

print_bill_line = printline(54,'_')
print (print_bill_line)
print_bill_customer ()