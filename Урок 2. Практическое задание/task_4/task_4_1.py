"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
from math import sqrt
NUMB = 0

try:
    NUMB = int(input('Введите количество элементов: ')) - 1
    sqrt(NUMB)
except ValueError:
    if NUMB < 0:
        print('Вы ввели отрицательное число.')
    else:
        print('Это не число.')
else:
    SUMM = 1
    SERIES_ELEMENT = 1

    while NUMB > 0:
        SERIES_ELEMENT = SERIES_ELEMENT / -2
        SUMM += SERIES_ELEMENT
        NUMB -= 1

    print(f'{SUMM}')
