
words = ["horse", "caw", "zebra", "duck", "bear"]



def count_long_words(sample, min_length):
    long_item = []
    for item in sample:
        lenght = len (item)
        if lenght > min_length:
            long_item.append(item)
    return len(long_item)

result = count_long_words(words, 2)
print(result)
