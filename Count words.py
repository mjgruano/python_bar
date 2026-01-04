
# Configuration 

words = ["cat", "elephant", "dog", "giraffe", "tiger"]

long_words = []

for word in words:
    lenght = len (word)
    if lenght > 4:
        # print(lenght)
        long_words.append(word)
    # else:
        # print("Too short")

print(len(long_words))

sample = ["horse", "caw", "zebra", "duck", "bear"]

long_item = []

def count_long_words(sample, min_length):
    for item in sample:
        lenght = len (item)
        if lenght > min_length:
            long_item.append(item)

print(len(long_item))

count_long_words(sample, 4)


'''first_item = words [0]
lenght = len (first_item)
if lenght > 4:
    print(lenght)
else:
    print("Too short")

second_item = words [1]
lenght = len (second_item)
if lenght > 4:
    print(lenght)
else:
    print("Too short")

third_item = words [2]
lenght = len (third_item)
if lenght > 4:
    print(lenght)
else:
    print("Too short")

fourth_item = words [3]
lenght = len (fourth_item)
if lenght > 4:
    print(lenght)
else:
    print("Too short")'''