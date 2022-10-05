import utils as u
import dbase as l

def mainmenu() :
    '''Главное меню системы'''
    print('1 - Departmnets')
    print('2 - Positions')
    print('3 - Employees ')
    print('4 - Birthdays')
    print('0 - Exit')
    key = u.inputtype('\nChoose menu point : ',int)
    return key

def tablemenu(table : list) :
    '''Работа с заданным справочником'''
    while True :
        key = l.printtable(table)
        if key == 0 :
            break
        elif key == 1 :
            l.addrecord(table)
        elif key == 3 :
            idd = input('id :')
            l.delrecord(table, idd)
        elif key == 2 :
            idd = input('id :')
            l.editrecord(table, idd)
        
    