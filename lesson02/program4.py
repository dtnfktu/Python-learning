str = input('Enter the integer number N > 0 : ')
while not str.isdigit():
    str = input('Enter the integer number N > 0 : ')
n = int(str)

list = [i for i in range(-n, n + 1)]

print("Your list is...")
print(list)

str = input(f'Enter position of number A : ')
while not str.isdigit():
    str = input(f'Enter position of number A : ')
a = int(str)

str = input(f'Enter position of number B : ')
while not str.isdigit():
    str = input(f'Enter position of number B : ')
b = int(str)

print("Multiplication of numbers on A and B = ", list[a - 1] * list[b - 1])