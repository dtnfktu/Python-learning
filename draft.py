# Подсчёт суммы цифр вещественного числа

def IsFloatNumber(a):
    try:
        float(a)
        return True
    except:
        return False

str = input('Enter the float number: ').replace(',','.')
while not IsFloatNumber(str):
    str = input('Enter the float number: ').replace(',','.')

str = str.replace('-','').replace('.','')
print(str)

summa = 0
for s in str:
    summa += int(s)
    
print('Summa = ', summa)

# Подсчёт суммы цифр вещественного числа ####################################

# Список произведений чисел #################################################

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

# Список произведений чисел #################################################

# Палиндром #################################################################

def ReverseNumber(num):
    ans = 0
    while num != 0:
        ans = ans * 10 + num % 10
        num //= 10
    return ans

str = input('Enter the integer number >0 : ')
while not str.isdigit():
    str = input('Enter the integer number >0 : ')
n = int(str)

while n != ReverseNumber(n):
    n += ReverseNumber(n)
    
print('Palindrome is :', n)

# Палиндром #################################################################

# Random ####################################################################

import time

def GetRandomNumber(a, b):
    return a + int((time.time() - int(time.time())) * (10 ** 11)) % (b - a)


RandomList = []
for i in range(1,100):
    RandomList.append(GetRandomNumber(1,100))


print(RandomList)
RandomList.sort()
print()
print(RandomList)

# Random ####################################################################

# Последовательность ########################################################

n = int(input('Enter N '))

list = []

for i in range(1, n):
    list.append((1 + 1/i) ** i)

print(list)

s = 0
for i in list:
    s += i
    
print("{:.3f}".format(s))

# Последовательность ########################################################
