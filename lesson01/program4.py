quarter_number = int(input('Введите номер четверти (1..4) : '))

if not quarter_number in range(1, 5):
    print('Ошибка! Допустимые значения : 1,2,3,4')
elif quarter_number == 1:
    print('x = (0..Infinity)')
    print('y = (0..Infinity)')
elif quarter_number == 2:
    print('x = (0..-Infinity)')
    print('y = (0..Infinity)')
elif quarter_number == 3:
    print('x = (0..-Infinity)')
    print('y = (0..-Infinity)')
else:
    print('x = (0..Infinity)')
    print('y = (0..-Infinity)')