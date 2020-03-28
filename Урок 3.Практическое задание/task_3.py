"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
from random import randint

MY_LIST = [randint(-100, 100) for i in range(10)]
print(f'Исходный список \t{MY_LIST}')
print(
    f'В данном массиве чисел максимальное число {max(MY_LIST)} стоит на {MY_LIST.index(max(MY_LIST))} '
    f'\nпозиции, а минимальное число {min(MY_LIST)} стоит на {MY_LIST.index(min(MY_LIST))} позиции.')
MAXX = MY_LIST.index(max(MY_LIST))
MINN = MY_LIST.index(min(MY_LIST))
# MY_LIST[MY_LIST.index(min(MY_LIST))], MY_LIST[MY_LIST.index(max(MY_LIST))] =
#   MY_LIST[MY_LIST.index(max(MY_LIST))], MY_LIST[MY_LIST.index(min(MY_LIST))]
""""пришлось добавить цикл тк простая замена значений не работает если
    s[s.index(min(s))] > s[s.index(max(s))]     """
if MAXX < MINN:
    MY_LIST[MAXX], MY_LIST[MINN] = MY_LIST[MINN], MY_LIST[MAXX]
else:
    MY_LIST[MINN], MY_LIST[MAXX] = MY_LIST[MAXX], MY_LIST[MINN]
print(f'Заменяем их \t\t{MY_LIST}')
