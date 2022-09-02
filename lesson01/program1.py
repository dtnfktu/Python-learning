week_day = int(input('Введите день недели (число от 1 до 7) : '))

if week_day <= 0 or week_day > 7:
    print('Ошибка! Введено некорректное число')
elif week_day == 6 or week_day == 7:
    print('да')
else:
    print('нет')