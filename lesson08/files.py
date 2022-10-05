import json

def loadfromfile(fname:str) :
    '''Загружает справочник из файла, формирует список кортежей'''
    outlist = []
    with open(fname, 'r', encoding='UTF-8') as f :
        s = f.read().splitlines()
    for string in s :
        outlist.append(tuple(string.split(';')))
    return outlist

def savetofile(fname : str, lst : list) :
    '''Сохраняет список кортежей в заданный файл'''
    with open(fname, 'w', encoding='UTF-8') as f :
        for record in lst :
            f.write(';'.join(record) + '\r')

def savetojson(lst : list) :
    '''Сохраняет в JSON текущий список'''
    head = {}
    listhead = lst[0]
    fname = listhead[0]
    for i in range(1, len(listhead) - 1, 2) :
        head[listhead[i]] = listhead[i + 1]

    table = {}
    table[fname] = head
    n = 1
    for element in lst[1:] :
        rec = {}
        i = 1
        for field in element :
            rec['f' + str(i)] = field
            i += 1
        table['rec' + str(n)] = rec
        n += 1

    with open(fname + '.json', 'w') as wfile :
        json.dump(table, wfile)

def loadfromjson(fname : str) :
    '''Считывает данные из JSON-файла и преобразует их в список'''
    with open(fname,'r',encoding='UTF-8') as f :
        table = json.load(f)
    keys = list(table.keys())
    head = keys[0]
    # Формируем заголовок таблицы
    felement = (head,)
    for headelement in table[head] :
        felement = felement + (headelement, table[head][headelement])
    outlist = [felement]
    # Теперь кортежи с данными
    for element in keys[1:] :
        currentrec = table[element]
        rec = ()
        for field in currentrec :
            rec = rec + (currentrec[field],)
        outlist.append(rec)

    return outlist
    