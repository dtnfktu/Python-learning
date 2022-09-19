<<<<<<< HEAD
<<<<<<< HEAD
def read_from_file(file_name) :
    ''' Из файла считывается многочлен и возвращается список коэффициентов '''
=======
=======
>>>>>>> 6a99ab257b550a0dfc7d671a48cd800e42de2843
def make_member(koef, power) :
    '''Формирует элемент многочлена по заданным коэффициенту и степени Х'''
    if koef == 0 :
        return ''
    if power == 0 :
        return str(koef)
    ans = ''
    if koef != 1 :
        ans = str(koef) + '*'
    ans += 'x'
    if power != 1 :
        ans += '^' + str(power)
    
    return ans

def write_in_file(ls:list, file_name) :
    '''По заданному списку коэффицентов формирует многочлен и записывает в файл'''
    list_to_write = []

    for x in range(0, len(ls)) :
        if ls[x] != 0 :
            list_to_write = list_to_write + [make_member(ls[x], len(ls) - x - 1)]

    with open(file_name,'w') as f :
        f.write(' + '.join(list_to_write) + ' = 0')

    return 'The polynomial is formed and written to a file => ' + file_name


def read_from_file(file_name) :
    '''Считывает многочлен из файла и возвращает список коэффициентов'''
<<<<<<< HEAD
>>>>>>> 6a99ab257b550a0dfc7d671a48cd800e42de2843
=======
>>>>>>> 6a99ab257b550a0dfc7d671a48cd800e42de2843
    koef = []
    with open(file_name, 'r') as f :
        st = f.readline().split(' = ')[0]   # Удаляем правую часть = 0

    memers_list = st.split(' + ')           # Разделяем на отдельные члены

<<<<<<< HEAD
<<<<<<< HEAD
    tmp = koef_lst[0].split('*x^')          # определяем степень многочлена
    if len(tmp) > 1 :                       # степень старшего (левого) члена
        power = int(tmp[1])                 # 
    else :                                  # предполагается, что степень 
        power = 1                           # не меньше 1
=======
=======
>>>>>>> 6a99ab257b550a0dfc7d671a48cd800e42de2843
    # Убираем * и ^. Справа от х - коэффициент, слева - степень
    for i in range(0, len(memers_list)) :
        memers_list[i] = memers_list[i].replace('*','').replace('^','')
        if memers_list[i][0] == 'x' :
            memers_list[i] = '1' + memers_list[i]
        # Для элемента степени 1 проводим корректировку
        if memers_list[i][len(memers_list[i]) - 1] == 'x' :
            memers_list[i] = memers_list[i] + '1'
    # Проводим корректировку для свободного члена
    if memers_list[len(memers_list) - 1].isdigit() :
        memers_list[len(memers_list) - 1] = memers_list[len(memers_list) - 1] + 'x0'

    tmp = memers_list[0].split('x')         # определяем
    if len(tmp) > 1 :                       # степень
        power = int(tmp[1])                 # многочлена -
    else :                                  # степень 
        power = 1                           # старшего (левого) члена
>>>>>>> 6a99ab257b550a0dfc7d671a48cd800e42de2843

    # Задаём список коэффициентов, изначально все = 0
    koef_list = [0 for i in range(0, power + 1)]

    # Анализируем каждый элемент
    for mem in memers_list :
        tmp = mem.split('x')
        #print()
        koef_list[len(koef_list) - int(tmp[1]) - 1] = int(tmp[0])
    
    return koef_list

def sum_polynoms(file1 : str, file2 : str, file_res : str) :
    '''Считывает два могочлена из файлов и записывает их сумму в file_res'''
    polynom1 = read_from_file(file1)
    polynom2 = read_from_file(file2)

    # степень результируещего многочлена - наибольшая степень из складываемых
    res_len = max(len(polynom1), len(polynom2))
    # приводим складываемые многочлены к одной длине
    while len(polynom1) < res_len :
        polynom1.insert(0, 0)
    while len(polynom2) < res_len :
        polynom2.insert(0, 0)

    # наконец-то складываем многочлены
    polynom_res = [0 for i in range(0, res_len)]
    for i in range(0, res_len) :
        polynom_res[i] = polynom1[i] + polynom2[i]
    
    write_in_file(polynom_res, file_res)

sum_polynoms('file1.txt', 'file2.txt', 'file3.txt')

with open('file1.txt') as file :
    print('First polynom :\n', file.read())

with open('file2.txt') as file :
    print('Second polynom :\n', file.read())

with open('file3.txt') as file :
    print('Resulting polynom :\n', file.read())