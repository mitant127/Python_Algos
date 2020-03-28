"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""

# from random import randint

# MY_LIST = [[randint(0, 9) for i in range(4)] for j in range(5)]
# print(MY_LIST)

MY_LIST = []

for i in range(5):
    print(f'{i + 1}-я строка: ')
    MY_LIST.append([])
    for j in range(4):
        MY_LIST[i].append(int(input('')))

for k in range(len(MY_LIST)):
    MY_LIST[k].append(sum(MY_LIST[k]))
    print(MY_LIST[k])
