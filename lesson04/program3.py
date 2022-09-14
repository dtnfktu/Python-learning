import random

def non_repetitive_elements(ls):
    '''Определяет все неповторяющиеся элементы в заданном списке ls'''
    ls.sort()
    result_list = []

    count = 1
    num = ls[0]
    for i in range(1, len(ls)) :
        if ls[i] == num :
            count += 1
        else :
            if count == 1 :
                result_list.append(num)
            count = 1
            num = ls[i]
    # Чтоб не потерять последний элемент
    if count == 1 :
        result_list.append(num)

    return result_list

lst = [random.randint(1, 101) for i in range(0,20)]
print('Исходный список :')
print(lst)

print('Список неповторяющихся элементов :')
print(non_repetitive_elements(lst))