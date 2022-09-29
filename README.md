# <a id="texthead"/>Python-learning

#### В качестве IDE используется Visual Studio Code

[Семинар 1](#lesson1)  
[Семинар 2](#lesson2)  
[Семинар 3](#lesson3)  
[Семинар 4](#lesson4)  
[Семинар 5](#lesson5)  
[Семинар 6](#lesson6)  
[Семинар 7](#lesson7)

## <a id="lesson1"/> Задания с семинара 1 - папка lesson01

1. **Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.**  
Программный код в файле [***program1.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson01/program1.py). Необходимо ввести целое число от 1 до 7. Если число 6 или 7, то ответ - "да", иначе - "нет". Если пользователем вводится текст (не число) или число меньше нуля, то предлагается ввести число заново. Если введено число больше 7, то берётся остаток от деления на 7 (в квадратных скобках выводится полученное значение). Если остаток от деления на 7 получился равным нулю, то это означает, что было введено число кратное 7, поэтому производится корректировка - в переменную записывается число 7.
2. **Напишите программу для проверки истинности утверждения  
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  
для всех значений предикат.**  
Программный код в файле [***program2.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson01/program2.py).Здесь используются три логические переменные, каждая из которых может принимать одно из двух значений (истина или ложь). Всего возможных комбинаций значений 2 в степени 3, т.е. 8. Чтобы не создавать условный оператор под каждую комбинацию (и не запутаться при этом), использованы три вложенных цикла. В каждом цикле переменная принимает значение True или False, и построчно выводится таблица истинности. На каждом шаге идёт проверка истинности логического выражения. Перед циклом задаётся перемнная count = 2^3 = 8. На каждом шаге цикла происходит проверка истинности выражения, если значение True, то count уменьшается на 1. Т.о. при прохождении всех комбинаций count должен быть равен нулю: если ноль, то равенство верно, иначе - равенство не верно, о чём выводится сообщение в конце работы программы.
3. **Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).**
Программный код в файле [***program3.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson01/program3.py). Условие неоднозначно, т.к. сначала оговорено, что X ≠ 0 и Y ≠ 0, а после допускается, что точка лежит на одной из осей координат (т.е. нулевое значение всё-таки допускается). Условным оператором проверяются возможные варианты: если координата (0,0), то выдаётся сообщение, что это точка пересечения координатных прямых (центр плоскости). Если одно из значений равно нулю, то выдаётся сообщение о принадлежности координантной прямой (Ох или Оу). В остальных случаях в зависимости от знака *х* и *у* выдаётся сообщение одной из четвертей. Проверка на корректность ввода исходных данных не производится, т.к. в библиотеках *python* соответствующий метод не нашёл (можно решить проблему используя исключение, но это тема следующих занятий). 
4. ***Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).***  
Программный код в файле [***program4.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson01/program4.py). Задача обратная предыдущей. При вводе номера четверти проверяется введённое число, если оно не входит в диапазон 1..4, то выдаётся сообщение об обшибке. Если всё нормально, то в зависимости от четверти выводится возможный диапазон принимаемых значений для *х* и *у*. Здесь *Infinity* означает *бесконечность*.  
5. ***Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.***  
Программный код в файле [***program5.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson01/program5.py). Задача решается с помощью теоремы Пифагора, где искомое расстояние - гипотенуза прямоугольгого треугольника. Катеты треугольника - разность между соответствующими координатами по *х* и по *у*. Здесь на знак разности не обращаем внимания, т.к. идёт возведение в квадрат (всегда положительное значение). Для извлечения квадратного корня возводим сумму квадратов катетов в степень 1/2. При выводе ответа полученное число приводим к строковому типу.  
[В начало](#texthead)  

## <a id="lesson2"/> Задания с семинара 2 - папка lesson02

1. ***Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.***  
Программный код в файле [***program1.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson02/program1.py).  
Методом *def IsFloatNumber(a)* осуществляется проверка корректности введённого числа, т.е., что введено именно вещественное число (можно и целое), отрицательное или положительное - не важно. *При вводе в качестве разделителя дробной и целой части допускается использовать как точку, так и запятую.* Затем из числа удаляются символы, не являющиеся цифрами (разделитель - точка, знак минус). Затем сумма цифр находится двумя способами: а) число рассматриватеся как строка, состоящая из цифр; строка перебирается, цифры суммируются; б) число рассматривается как целое число, на каждой итерации цикла суммируем остаток от деления на 10, само число делим на 10; и так до тех пор, пока исходное число не станет равным нулю.  
*Строку не переводил в вещественное число (float), т.к. при приведении типов в вещественном числе в дробной части имеет место быть "мусор", который усложняет задачу. А если мы знаем, что введено дробное число (проверено при вводе) и оно типа string, то проще привести его к целому типу.*  
2. ***Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.***  
Программный код в файле [***program2.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson02/program2.py).  
При вводе количества элементов списка проводится проверка на корректность введённых данных. Список формируется в цикле. Перед началом цикла задаётся переменная *multiply* = 1, это первый элемент в формируемом списке. Далее, на каждом шаге переменная домножается на номер текущего шага, *i*, и заносится новым элементом в список.
3. ***Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх знаков после точки.***  
Программный код в файле [***program3.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson02/program3.py).  
Список *list* формируется в строке 6. Затем подсчитывается сумма элементов списка и выводится на экран с точностью до трёх знаков после точки. Здесь используется один из вариантов форматированного вывода - *format*.
4. ***Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b. Значения N, a и b вводит пользователь с клавиатуры.***  
Программный код в файле [***program4.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson02/program4.py).  
Пользователь число N. В строке 6 формируется список, после чего он выводится на экран. Затем, пользователю предлагается ввести номера элементов А и В. В строке 21 элементы перемножаются и выводятся на экран. Здесь учитывается, что индексация в списке начинается с нуля, т.е. первому элементу соответствует индекс 0, второму - 1 и т.д. 
5. ***Реализуйте алгоритм перемешивания списка.***  
Программный код в файле [***program5.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson02/program5.py).  
Сначала, в цикле *for*, формируется упорядоченный список (длина списка взята равной 15, можно длину изменить). Затем, в новом цикле *for* (количество шагов = длине списка) на каждом шаге задаётся случайное число - индекс элемента последовательности. Элементы списка (текущий и случайный) меняются местами.
6. ***Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.***  
Программный код в файле [***program6.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson02/program6.py).  
В основной строке, в диапазоне от 0 до элемента с индексом = длина основной строки - длина подстроки, в цикле производится сравнение текущей подстроки (текущий индекс + длина подстроки) в основной строке с заданной подстрокой. Каждое положительное сравнение фиксируется в переменной counter.  
[В начало](#texthead)  

## <a id="lesson3"/> Задания с семинара 3 - папка lesson03

1. ***Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.***  
Програмный код в файле [***program1.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson03/program1.py)  
Список создаётся методом *CreateRandomList(ListLen = 10, MinNum = 0, MaxNum = 25)*, который принимает три параметра: *ListLen* - длина списка (по умолчанию = 10), левая граница диапазона принимаемых значений *MinNum* (по умолчанию = 0), правая граница диапазона принимаемых значений (по умолчанию = 25) включительно.  
Метод *GetSumInOddPosition(AList)* принимает список, в котором суммируются элементы на нечётных позициях и возвращает результат. Подсчёт идёт в цикле *for* начиная с позиции = 1 (первая нечётная позиция) с шагом +2. 
2. ***Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.***  
Програмный код в файле [***program2.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson03/program2.py)  
Для генерации списка используется метод *CreateRandomList* из [***program1.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson03/program1.py).  
Метод *CountMultiplicationOfPairNumbers(AList)* принимает рассматриваемый список и возвращает новый список, сформированный в соответствии с уловием задачи. Здесь задаются две переменные: *LeftIndex* - начальный индекс левой границы рассматриваемого списка, *RightIndex* - соответственно правая граница. Далее в цикле *while* на каждом шаге перемножаются текущие левый и правый элементы списка и заносится в новый формируемый список. Затем левая граница сдвигается вправо на 1, правая сдвигается влево на 1. Цикл останавливается когда *LeftIndex* окажется правее *RightIndex*. Если количество элементов исходного списка нечетное, последним шагом цикла будет ситуация когда *LeftIndex* = *RightIndex*, т.е. текущий элемент просто умножается сам на себя.
3. ***Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.***  
Програмный код в файле [***program3.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson03/program3.py).  
Список вещественных чисел можно было вводить с клавиатуры... Но я решил его генерировать рандомно. Метод *CreateRandomList* формирует список случайных вещественных чисел. К каждому случайному вещественному числу прибавляется случайное целое число, для наглядности решения.  
Метод *GetMaxFractionalPart(List)* получает исходный список, который просматривается в цикле. Т.к. интересует именно дробная часть, на каждом шаге от текущего элемента отнимается его целая часть, вещественная часть сравнивается с текущим максимумом. Метод *GetMinFractionalPart(List)* работает так же, как и на нахождение максимальной дробной части, но возвращает минимум.
4. ***Напишите программу, которая будет преобразовывать десятичное число в двоичное.***  
Програмный код в файле [***program4.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson03/program4.py).  
Метод *def DecToBin(dec)* получает целое число в десятичной системе счисления, возвращает это же число (тип *str*), но уже в двоичной системе счисления. Используется цикл *while*. Т.к. в *Python* цикла с постусловием нет, используется бесконечный цикл с предусловием, в котором после всех проведенных действий проверяется следует ли остановиться, и, если да, то - *break*. Сам алгоритм перевода из 10 в 2 стандартный - на каждом шаге делим на 2, остаток от деления записываем.
5. ***Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.***  
Програмный код в файле [***program5.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson03/program5.py)  
Последовательность Фибоначчи/негаФибоначчи находится двумя способами. Первый - использование цикла, где явно используется формула нахождения k-го числа последовательности. Реализовано в методе *Fibonacci(n)*, который возвращает список, содержащий последовательность от -k-го до +k-го числа. Второй способ - использование рекурсии. Рекурсивно находится k-е число последовательности (методы *RecFibonacci(k)* и *RecNegaFibonacci(k)*). Оба метода используются в циклах в методе *RecFibonacciList(n)*, в котором формируется список.  
[В начало](#texthead)  

## <a id="lesson4"/> Задания с семинара 4 - папка lesson04  
1. ***Вычислить число π c заданной точностью d***  
Програмный код в файле [***program1.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson04/program1.py).  
Вычисление числа *π* разложением в ряд арктангенса, функция *def arctan_pi(accuracy)*. Точность вычислений, параметр *accuracy*, задаётся целым числом - количество знаков после точки.
2. ***Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.***  
Програмный код в файле [***program2.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson04/program2.py).  
С помощью функции *input_int()* вводится целое число, для которого находятся простые множители. Функция *prime_nums_table(max_num : int)* формирует список простых чисел от 2 до *max_num*. Функция *list_of_multipliers(n)* используя список простых чисел, возвращает список множителей для числа *n*. Если число *n* является простым, то выводится соответствующее сообщение.  
3. ***Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.***  
Програмный код в файле [***program3.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson04/program3.py).    
Исходный список формируется случайным образом функией *randint*. Функция *non_repetitive_elements(ls)* принимает исходный список и возвращает новый список, в который каждый элемент исходного списка входит только один раз. Если все элементы исходного списка присутствют более одного раза, то результат - пустой список.
4. ***Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.***  
Пользователь задаёт степень многочлена *k*. Формируется список коэффициентов многочлена, состоящий из случайных положительных чисел. В многочлене количество слагаемых *k + 1*, т.к. присутствует слагаемое с переменной в нулевой степени. Функция *ake_member(koef, power)* принимает коэффициент *koef* и степень *power* многочлена и возвращает текцщий член в виде *koef\*x^power*. Функция *write_in_file(ls:list, file_name)* по заданному списку коэффициентов *list* формирует многочлен
и записывает его в файл *file_name*.
5. ***Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.*** Функция *read_from_file(file_name)* считывает многочлен из файла *file_name* и возвращает список коэффициентов. Количество элементов списка равно *k + 1*, где *k* - степень многочлена. Запись многочлена в файл с помощью *write_in_file(ls:list, file_name)* из предыдущей задачи. Функция *read_from_file(file_name)* считывает многочлен из файла *file_name* и возвращает список коэффициентов. Сложение многочленов осуществляется в функции *sum_polynoms(file1 : str, file2 : str, file_res : str)*: первый считывается из *file1*, второй - из *file2*. Результат сложения записывается в файл *file_res*

[В начало](#texthead)  

## <a id="lesson5"/> Задания с семинара 5 - папка lesson05  
1. ***Напишите программу, удаляющую из текста все слова, содержащие ""абв"".***  
Програмный код в файле [***program1.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson05/program1.py).  
Из текстового файла *testin.txt* считывается текст. Разделяется на слова, и отсеивает все слова по заданному условию. Результат записывается в файл *testout.txt*.  

2. ***Создайте программу для игры с конфетами человек против человека.***
***Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?***
***a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного или больше чем имеется в куче.***
***b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать 29 конфет, то он, однозначно, проиграет. Достаточно довести игру до такой ситуации.***  
Програмный код в файле [***program2.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson05/program2.py).  
При запуске игра инициализируется. Значения по умолчанию указаны в квадратных скобках - досточно просто нажать клавишу Enter. Можно задать свои начальные условия - сколько конфет в коробке, по сколько максимум брать за каждый шаг. На этапе инициализации выбираем второго игрока (человек или бот). Если выбрали бота, выбираем уровень игры: 1 - бот случайное количество конфет, 2 - бот ориентируется на ход оппонента.  
3. ***Создайте программу для игры в ""Крестики-нолики"".***  
Програмный код в файле [***program3.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson05/program3.py).  
В начале выбираем режим игры: 1 - оба игрока - люди, 2 - второй игрок - бот. Бота наделять интеллектом не стал, т.к. в условии задачи ничего об этом не сказано. Когда ходит бот выбирается случайным образом незаполненная ячейка. Чей ход первый - определяется случайным образом.  
4. ***Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.***  
Програмный код в файле [***program4.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson05/program4.py).  
Берётся текст из файла opentext.txt. Проверятся повторное вхождение символов. Если символ повторяется, то записывается пара число-символ, если нет, то просто символ. Для разделения связок число-символ использован символ **|**. Закодированный текст сохраняется в файле closedtext.txt. Функция *encode_rle(txt : str)*  сжимает заданный текст, функция *decode_rle(txt : str)* - восстанавливает.

[В начало](#texthead)  
## <a id="lesson6"/> Задания с семинара 6 - папка lesson06

1. ***Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.***  
Програмный код в файле [***program1.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson06/program1.py).  
Здесь используется *list comprehension* при создании списка. Затем с помощью *zip* к элементам списка добавляются индексы. Здесь логичнее использовать *enumerate*, *zip* использован для демонстрации его применения. С использованием *filter* отфильтровываются элементы с нечётными индексами через *lambda*. Сумма элементов находится с помощью *sum* для списка.  
2. ***Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.***  
Програмный код в файле [***program2.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson06/program2.py).  
Исходный список задаётся с использованием *map*. Можно было сразу использовать *enumerate*, но используется позже для вывода исходного списка без индексов элементов. С *list comprehension* выолняется заданное условие.  
3. ***Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.***  
Програмный код в файле [***program3.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson06/program3.py).  
Каждый элемент списка - факториал его порядкового номера (не индекса, а номера начиная с 1). Для нахождения факториала выделена *lambda fact*, которая вызвает себя (рекурсия) и используется в *map*.  
4. ***Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх знаков после точки.***  
Програмный код в файле [***program4.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson06/program4.py).  
Последовательность задаётся с помощью *map*, в которой используется *lambda*.  
[В начало](#texthead)  

## <a id="lesson7"/> Задания с семинара 7 - папка lesson07
***Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. При необходимости, программа должна уметь импортировать записи из файла, который сама экспортировала.***  
Программа запускается из файла [***main.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson07/main.py). В файле [***phonenumbers.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson07/phonenumbers.py) функции, используемые в основном модуле.  
При запуске программы в меню предлагется выбрать что делать. По умолчанию справочник загружается из файла *phonebook.csv*. Если данный файл не обнаружен - начальный справочник пустой.  
[В начало](#texthead)  