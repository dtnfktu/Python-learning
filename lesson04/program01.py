def arctan_pi(accuracy) :
    '''Нахождение числа ПИ степенным рядом арктангенса с точностью accuracy
    '''
    koef = 2 * (3 ** 0.5)
    final_ans = koef
    prev_ans = 0.0
    n = 1

    while abs(prev_ans - final_ans) >= accuracy :
        prev_ans = final_ans
        final_ans += koef * (1 / ((2 * n + 1) * ((-3) ** n)))
        n += 1

    return final_ans

acc = int(input('Количество знаков после запятой = '))
print(("Пи = {:." + str(acc) + "f}").format(arctan_pi(10 ** -acc)))
