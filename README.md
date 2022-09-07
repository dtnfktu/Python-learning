# Python-learning

#### В качестве IDE используется Visual Studio Code

## Задания с первого семинара - папка lesson01

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

## Задания со второго семинара - папка lesson02

1. ***Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.***  
Программный код в файле [***program1.py***](https://github.com/dtnfktu/Python-learning/blob/main/lesson02/program1.py). Методом *def IsFloatNumber(a)* осуществляется проверка корректности введённого числа, т.е., что введено именно вещественное число (можно и целое), отрицательное или положительное - не важно. *При вводе в качестве разделителя дробной и целой части допускается использовать как точку, так и запятую.* Затем из числа удаляются символы, не являющиеся цифрами (разделитель - точка, знак минус). Затем сумма цифр находится двумя способами: а) число рассматриватеся как строка, состоящая из цифр; строка перебирается, цифры суммируются; б) число рассматривается как целое число, на каждой итерации цикла суммируем остаток от деления на 10, само число делим на 10; и так до тех пор, пока исходное число не станет равным нулю.  
*Строку не переводил в вещественное число (float), т.к. при приведении типов в вещественном числе в дробной части имеет место быть "мусор", который усложняет задачу. А если мы знаем, что введено дробное число (проверено при вводе) и оно типа string, то проще привести его к целому типу.*