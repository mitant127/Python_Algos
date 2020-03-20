"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

from math import sqrt

NUMB = 0
try:
    NUMB = int(input('Введите количество элементов: '))
    sqrt(NUMB)
    SUMM_1 = NUMB
    SUMM_2 = (NUMB * (NUMB + 1)) / 2
except ValueError:
    if NUMB < 0:
        print('Вы ввели отрицательное число.')
    else:
        print('Это не число.')
else:
    while NUMB > 0:
        SUMM_1 = SUMM_1 + (NUMB - 1)
        NUMB -= 1
    else:
        print(f'Равенство верно: {SUMM_1} = {SUMM_2}')
