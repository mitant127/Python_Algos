"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from math import sqrt
NUMB = 0


# recursion(число элементов ряда/текущий элемент, сумма элементов ряда, значение текушего элемент ряда)
def recursion(numb, summ, series_element):
    if numb == 0:
        print(numb, summ, series_element)  # подглядываем за процессом
        return summ + series_element  # прибавляем посделний элемент ряда
    else:
        print(numb, summ, series_element)   # подглядываем за процессом
        return recursion(numb - 1, summ + series_element, series_element / -2)


try:
    NUMB = int(input('Введите количество элементов: ')) - 1
    sqrt(NUMB)  # проверка что NUMB > 0
except ValueError:
    if NUMB < 0:
        print('Вы ввели отрицательное число.')
    else:
        print('Это не число.')
else:
    print(recursion(NUMB, 0, 1))
