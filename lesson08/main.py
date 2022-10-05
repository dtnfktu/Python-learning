import dbase
import files
import menu

def start() :
    '''Запуск приложения'''
# Загружаем БД
    depts = files.loadfromjson('depts.json')
    positions = files.loadfromjson('positions.json')
    people = files.loadfromjson('people.json')
    
    while True:
        key = menu.mainmenu()
        if key == 0 :
            break
        elif key == 1 :
            menu.tablemenu(depts)
        elif key == 2 :
            menu.tablemenu(positions)   
        elif key == 3 :
            menu.tablemenu(people)            
        elif key == 4 :
            menu.bdaysmenu([depts,positions,people])


    files.savetojson(depts)
    files.savetojson(positions)
    files.savetojson(people)
    print('The application has shut down')

# Запускаем оболочку
start()