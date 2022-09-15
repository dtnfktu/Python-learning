from ntpath import join
import random

def make_member(koef, power) :
    '''Формирует элемент многочлена по заданным коэффициенту и степени Х'''
    if koef == 0 :
        return ''
    if power == 0 :
        return str(koef)
    ans = ''
    if koef != 1 :
        ans = str(koef) + '*'
    ans += 'x'
    if power != 1 :
        ans += '^' + str(power)
    
    return ans


def write_in_file(ls:list, file_name) :
    '''По заданному списку коэффицентов формирует многочлен и записывает в файл'''
    list_to_write = []

    for x in range(0, len(ls)) :
        if ls[x] != 0 :
            list_to_write = list_to_write + [make_member(ls[x], len(ls) - x - 1)]

    with open(file_name,'w') as f :
        f.write(' + '.join(list_to_write) + ' = 0')

    return 'The polynomial is formed and written to a file => ' + file_name


k = int(input('k (> 0) = '))
lst = [random.randint(0, 100) for i in range(0, k + 1)]

print(write_in_file(lst,'test.txt'))