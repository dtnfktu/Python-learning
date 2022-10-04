
def newtable() :
    '''Создаёт новую таблицу данных - возвращает заголовок - структуру таблицы'''
    tname = input('Enter table name : ')
    thead = (tname,)
    while True :
        aname = input('Enter field name : ')
        if aname == '-' :
            break
        asize = int(input('Enter field size : '))
        thead = (thead) + (aname, asize)
    
    lst = [thead]
    return lst

def addrecord(lst : list) :
    '''Добавляет в текущий список новый элемент'''
    tablehead = lst[0]
    newelement = ()
    for i in range(1, len(tablehead), 2) :
        newelement = newelement + (input(tablehead[i] + " : "),)
    lst.append(newelement)


def printtable(lst : list) :
    '''Выводит на экран список кортежей в виде таблицы'''
    '''Первый элемент списка - заголовок таблицы с длинами полей'''
    # Формируем шапку таблицы
    head = lst[0]
    s = '|'
    for i in range(1, len(head),2) :
        fname = head[i]
        fleng = head[i + 1]
        s += ' ' * ((fleng - len(fname))//2) + fname + ' ' * ((fleng - len(fname))//2) + '|'
    print('-' * len(s))
    print(s)
    print('-' * len(s))
    # Заполняем таблицу данными из списка
    
    for record in lst[1:] :
        c = '|'
        i = 0
        for element in range(0,len(record)) :
            flen = head[i + 2]
            i += 2
            c += record[element] + ' ' * (flen - len(record[element]) - 1) + '|'
        print(c)
        print('-' * len(c))
