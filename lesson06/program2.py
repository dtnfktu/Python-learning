# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

n = 9

# Задаём список из N случайных чисел
lst = list(map(lambda x: random.randint(1, 10), range(1, n + 1)))
print(f'Исходный список :\n{lst}')

# Нумеруем элементы списка
lst = list(enumerate(lst))

multi_list = [lst[i][1] * lst[len(lst) - 1 - i][1] for i in range(round(len(lst) / 2 + 0.1))]
# Пояснение. Если просто округлять, то 2.5 -> 2, 4.5 -> 4 etc, 
# При увеличении на 0.1 гарантировано при чётном количестве - округление в меньшую сторону
# при нечётном - в бОльшую

print(f'Полученный список:\n{multi_list}')