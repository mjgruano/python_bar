# Version 11 aims to include dictionaries  

# Configuration Dictionary

menu = { 
    1: {"item": "juice" , "price": 3},
    2: {"item": "chocolate" , "price": 4},
    3: {"item": "water" , "price": 1}
}

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

order = []

for item in menu:
    number_item, order_item, bill = ask_client(menu[item]["item"], menu[item]["price"], bill)
    order.append ((item, number_item))

for item, number_item in order:
    print_bill_item (menu[item]["item"], number_item, + number_item * menu[item]["price"])

print_bill_line = printline(54,'_')
print (print_bill_line)
print_bill_customer ()