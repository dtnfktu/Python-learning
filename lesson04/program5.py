def read_from_file(file_name) :
    ''' Из файла считывается многочлен и возвращается список коэффициентов '''
    koef = []
    with open(file_name, 'r') as f :
        st = f.readline().split(' = ')[0]   # Удаляем правую часть = 0

    koef_lst = st.split(' + ')              # Разделяем на отдельные члены

    tmp = koef_lst[0].split('*x^')          # определяем степень многочлена
    if len(tmp) > 1 :                       # степень старшего (левого) члена
        power = int(tmp[1])                 # 
    else :                                  # предполагается, что степень 
        power = 1                           # не меньше 1

    
    return power
    #return koef_lst
    

print(read_from_file('test.txt'))