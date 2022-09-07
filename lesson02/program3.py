str = input('Enter the integer number N > 0 : ')
while not str.isdigit():
    str = input('Enter the integer number N > 0 : ')
n = int(str)

list = [(1 + 1 / i) ** i for i in range(1, n + 1)]

s = 0
for i in list:
    s += i
    
print("Summa = {:.3f}".format(s))