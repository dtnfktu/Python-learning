import os
import lists as l

def mainmenu() :
    '''Главное меню системы'''
    os.system('clear')
    print('1 - Отделы')
    print('2 - Должности')
    print('3 - Сотрудники')
    print('4 - Работа с проектами')
    print('0 - Выход')
    print('')
    key = input('Выберите действие : ')
    return int(key)

def menu1(table : list) :
    '''Первый пункт меню - информация об отделах'''
    l.printtable(table)