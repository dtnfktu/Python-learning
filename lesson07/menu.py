import os
from macpath import join
import phonenumbers

def mainmenu():
    '''Выводит в консоль меню и возвращает выбранный пункт'''
    os.system('cls')
    print('Выберите действие :')
    print('1 - Просмотр записей')
    print('2 - Добавление записи')
    print('3 - Экспорт данных')
    print('4 - Импорт данных')
    print('0 - Завершить работу')
    key = input()
    return int(key)

def menu_point1() :
    '''Первый пункт меню - просмотр справочника'''
    os.system('cls')
    print('-------------------------------------------------------')
    print('|   Фамилия  |     Имя     | № телефона |  Примечание  |')
    print('-------------------------------------------------------')

    phone_list = phonenumbers.read_from_file('testphones.csv')
    for rec in phone_list :
        print(f'|{rec[0]:13}|{rec[1]:12}|{rec[2]:12}|{rec[3]:14}|')

    print('-------------------------------------------------------')
    print('Нажмите Enter для возврата в меню')
    input()

def menu_point2() :
    '''Добавление записи в справочник'''
    sname = input('Фамилия       : ')
    fname = input('Имя           : ')
    phnum = input('№ телефона    : ')
    other = input('Дополнительно : ')
    key = input('Сохранить (д/н) ? [Д] :')
    if key in ('','Д','д','y','Y') :
        phone_list = phonenumbers.read_from_file('testphones.csv')
        phone_list.append(';'.join([sname, fname, phnum, other]))
        phonenumbers.save_to_file(phone_list, 'testphones.csv')