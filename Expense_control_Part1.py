# Part 1 - Step 1 - Add two numbers

expenses = [2.50, 3]
total = 0

total = total + 2.5 + 3
print ("The expense list adds up to ", total)

# Part 1 - Step 2 - Add all numbers using a loop

expenses = [2.50, 3, 5, 10]

total = 0

for num in expenses:
    total = total + num

print ("The expense list adds up to ", total)

# Part 1 - Step 3 - Encapslate the total in a function

expenses = [2.50, 3, 5, 10]

def total_spent (list):
    total = 0
    for num in list:
        total = total + num
    return total

result = total_spent(expenses)
print ("The expense list adds up to ", result)