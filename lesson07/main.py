from cmath import phase
import menu
import phonenumbers
import os

os.system('chcp 65001')
# справочник, который загружается по умолчанию
# phone_list = phonenumbers.read_from_file('testphones.csv')

while True :
    point = menu.mainmenu()
    if point == 0 :
        break
    if point == 1 :
        menu.menu_point1()
    if point == 2 :
        menu.menu_point2()

print('Работа завршена...')
