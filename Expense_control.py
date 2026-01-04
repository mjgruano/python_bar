# Step 1 - Add two numbers

expenses = [2.50, 3]
total = 0

total = total + 2.5 + 3
print ("The expense list adds up to ", total)

# Step 2 - Add all numbers using a loop

expenses = [2.50, 3, 5, 10]

def total_expenses(list):
    total = 0
    for num in list:
        total = total + num
    return total

result = total_expenses(expenses)
print ("The expense list adds up to ", result)