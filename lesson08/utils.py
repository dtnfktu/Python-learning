import datetime

def strtodate(s : str) :
    '''Перевод типа строка в тип дата '''
    return datetime.datetime.strptime(s.replace('.',''), '%d%m%Y').date()

def inputtype(title:str, t:type) :
    '''Ввод данных указанного типа'''
    while True :
        temp = input(title)
        try :
            out = t(temp)
            break
        except :
            print('Wrong type!')
    return out