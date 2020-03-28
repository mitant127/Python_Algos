"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
from random import randint

M = int(input('Задайте количество строк в матрице: '))
N = int(input('Задайте количество столбцов в матрице: '))
NXT_ELMT = 0
MY_LIST = [[randint(0, 100) for i in range(N)] for j in range(M)]

for i in range(M):
    for j in range(N):
        print(f'{MY_LIST[i][j]:3}', end=' ')
    print()

INVRT_MTRX = list(zip(*MY_LIST))
# print(INVRT_MTRX)
for i in range(len(INVRT_MTRX)):
    INVRT_MTRX.append(min(INVRT_MTRX[i]))
    print(f'{min(INVRT_MTRX[i]):3}', end=' ')
# for i in range(N):
#     for j in range(M):
#         print(f'{INVRT_MTRX[i][j]:3}', end=' ')
#     print()
# while NXT_ELMT <= len(MY_LIST):
#     for i in range(len(MY_LIST)):
#         pass
