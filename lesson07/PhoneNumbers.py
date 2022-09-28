def save_to_file(lst:list, filename: str) :
    '''Записывает в файл кортежи из списка'''
    with open(filename,'w') as f:
        for cortege in lst :
            f.write(';'.join(cortege) + '\r')

def read_from_file(filename : str) :
    '''Считывает справочник из файла и возвращает список кортежей '''
    lst = []
    with open(filename,'r') as f :
        temp_list = f.read().splitlines()

    for abonent in temp_list :
        lst.append(tuple(abonent.split(';')))

    return lst

c1 = ('Иванов','Василий','+79831112233','основной')
c2 = ('Петров','Степан','+77051842323','рабочий')
c3 = ('Сидоров','Арнольд','+380923212','корпоративный')
c4 = ('Курачев','Алексей','+43215463212','')