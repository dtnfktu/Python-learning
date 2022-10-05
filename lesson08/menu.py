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
        
def bdaysmenu(tables : list) :
    d = u.inputtype('Enter day : ', int)
    m = u.inputtype('Enter month : ',int)
    bd = str(d) if d >= 10 else ('0' + str(d))
    bd += '.' + (str(m) if m >= 10 else ('0' + str(m)))
    l.printtable(l.bdquery(tables, bd), False)
