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

# Part 3 - Step 8 - Count expenses above a limit (single list)

def count_above_limit(expenses, limit):
    n_above = 0

    for number in expenses:
        if number > limit:
            n_above += 1

    return n_above


above4 = count_above_limit([2.50, 3, 5, 10], 4)
print(above4)

# Part 3 - Step 9 - Use the function on multiple lists

for expense_list in all_expenses:
    above4 = count_above_limit(expense_list, 4)
    print(above4 ," expenses above the limit")

# Part 3 - Step 10 - Combine totals and limits

for expense_list in all_expenses:
    total = total_spent(expense_list)
    totals.append(total)
    above4 = count_above_limit(expense_list, 4)
    print("Total =" , total, " - " , " Above limit : ", above4)

# Part 3 - Step 11 - Final Function (Main Goal)

def analyze_expenses(all_expenses, limit):
    total_limit = []

    for expense_list in all_expenses:
    total = total_spent(expense_list)
    totals.append(total)
    above4 = count_above_limit(expense_list, 4)
  

