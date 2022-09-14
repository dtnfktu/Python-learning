
def prime_numbers(lim):
    ''' Возвращает список простых чисел от 2 до lim включительно
    '''
    nums = [i for i in range(3, lim + 1, 2)]
 
    indexlist = []
    index = 0
    while (index < len(nums)):

        for i in range(index + 1, len(nums)):
            if nums[i] % nums[index] == 0:
                indexlist.append(i)

        index += 1

    indexlist.sort(reverse=True)
    
    index = 0
    while index < len(indexlist):
        sindex = index + 1
        while sindex < len(indexlist) and indexlist[index] == indexlist[sindex]:
            indexlist.pop(sindex)
        index += 1

    for i in range(len(indexlist)):
        nums.pop(indexlist[i])

    return [2] + nums

def list_of_multipliers(n):
    '''Возвращает список простых множителей числа n
    '''
    lst = prime_numbers(round(n ** 0.5))

    res_list = []
    for i in range(0, len(lst)):
        if n % lst[i] == 0:
            res_list.append(lst[i])

    return res_list

def leibnitz_pi(n) :
    '''Нахождение числа П степенным рядом Лейбница
    '''
    sum = 0.0

    for i in range(0, 100_000_000) :
        sum += (1 / (2 * i + 1)) * ((-1) ** i)
    return sum * 4

def arctan_pi(accuracy) :
    '''Нахождение числа ПИ степенным рядом арктангенса с точностью accuracy
    '''
    koef = 2 * (3 ** 0.5)
    final_ans = 1.0
    last_ans = 0.0
    n = 1

    while abs(koef * final_ans - koef * last_ans) >= accuracy :
        last_ans = final_ans
        final_ans += 1 / ((2 * n + 1) * ((-3) ** n))
        n += 1

    return final_ans * koef
    


print(list_of_multipliers(1234))