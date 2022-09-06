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
