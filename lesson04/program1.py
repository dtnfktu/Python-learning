def arctan_pi(accuracy) :
    '''Нахождение числа ПИ степенным рядом арктангенса с точностью accuracy
    '''
    koef = 2 * (3 ** 0.5)
    final_ans = koef
    prev_ans = 0.0
    n = 1

    while abs(final_ans - prev_ans) >= accuracy :
        prev_ans = final_ans
        final_ans += koef * (1 / ((2 * n + 1) * ((-3) ** n)))
        n += 1

    return final_ans

acc = int(input('Точность вычислений (целое число - количество знаков после точки) = '))
print(("Pi = {:." + str(acc) + "f}").format(arctan_pi(10 ** -acc)))