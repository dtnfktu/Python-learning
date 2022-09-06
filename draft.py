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

# Подсчёт суммы цифр вещественного числа
