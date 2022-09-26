def input_int() :
    while True :
        st = input('Введите целое положительное число : ')
        if st.isdigit() :
            return int(st)

def prime_nums_table(max_num : int) :
    ''' Формирует таблицу простых чисел от 2 до max_num'''
    nums = [i for i in range(3, max_num + 1, 2)]    # задаём множество нечётных чисел

    index_list = [i for i in range(0, len(nums))]   # задаём список индексов
    
    for i in range(0, len(nums)) :
        for j in range(i + nums[i], len(nums)) :
            if nums[j] % nums[i] == 0 :
                index_list[j] = -1                  # -1 - признак удаления из списка

    for i in range(len(nums) - 1, 0, -1) :
        if index_list[i] == -1 :
            nums.pop(i)
    
    return [2] + nums

def list_of_multipliers(n) :
    '''Возвращает список простых множителей числа n'''

    lst = prime_nums_table(n // 2)

    res_list = []
    for i in lst :
         while n % i == 0 :
            n //= i
            res_list.append(i)

    if not res_list :
        return 'Число ' + str(n) + ' является простым. Делится только на 1 и на само себя.'

    return res_list

n = input_int()
print('Данное число является произведением простых множителей : ', list_of_multipliers(n))