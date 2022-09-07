str = input('Enter the integer number >0 : ')
while not str.isdigit():
    str = input('Enter the integer number >0 : ')
n = int(str)

list = []
multiply = 1

for i in range(1, n + 1):
    multiply *= i
    list.append(multiply)
    
print(list)