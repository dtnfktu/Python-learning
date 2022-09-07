import random

list = [i for i in range(1, 16)]
print('Sorted list')
print(list)

list_length = len(list)
for i in range(list_length):
    index = random.randint(0, list_length - 1)
    list[i], list[index] = list[index], list[i]

print('Unsorted list')
print(list)