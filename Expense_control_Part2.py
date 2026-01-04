# Part 2 - Step 4 - Two expenses lists, no loop yet

expenses1 = [2.50, 3, 5, 10]
expenses2 = [15, 2, 1]

def total_spent (list):
    total = 0
    for num in list:
        total = total + num
    return total

total1 = total_spent(expenses1)
total2 = total_spent(expenses2)

print("Expense list 1 adds up to ",total1)
print("Expense list 2 adds up to ",total2)


# Part 2 - Step 5 - Look over a list of lists

all_expenses = [
    [2.50, 3, 5, 10],
    [15, 2, 1]
]

for expense_list in all_expenses:
    total = total_spent(expense_list)
    print("Expense list adds up to ", total)

# Part 2 - Step 6 - Save all totals into a list

totals = []

for expense_list in all_expenses:
    total = total_spent(expense_list)
    totals.append(total)

print (totals)

# Part 2 - Step 7 - Wrap the whole process in a function

all_expenses = [
    [3.50, 4, 6, 11],
    [16, 3, 2]
]

def calculate_all_totals(items):
    totals = []

    for expense_list in all_expenses:
        total = total_spent(expense_list)
        totals.append(total)
    return totals

result = calculate_all_totals (all_expenses)
print (result)