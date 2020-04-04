"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import timeit
from random import randint
import cProfile


def hw3_tsk2_v1():
    MY_LIST = [randint(-100, 100) for i in range(1000)]
    # print(MY_LIST)
    x1 = list(i for i in MY_LIST if i % 2 == 0)


def hw3_tsk2_v2():
    MY_LIST = [randint(-100, 100) for i in range(1000)]
    # print(MY_LIST)
    x2 = []
    for i in MY_LIST:
        if i % 2 == 0:
            x2.append(i)


def main():
    hw3_tsk2_v1()
    hw3_tsk2_v2()


print(timeit.timeit("hw3_tsk2_v1()", setup="from __main__ import hw3_tsk2_v1", number=10000))
print(timeit.timeit("hw3_tsk2_v2()", setup="from __main__ import hw3_tsk2_v2", number=10000))


cProfile.run("main()")


"""Попробовал ухудшить алгоритм. При использовании цикла вместо генератора наблюдается незначительное 
увеличение времение выполнения. Но значительное время все равно занимает генератор заполнения массива MY_LIST"""


"""NUMB = 932850971070143275070239750527932850971070143275070239750527


def recursion(numb, even, uneven):
    # mathematical character
    if numb < 10:
        if numb % 2 == 0:
            even += 1
        else:
            uneven += 1
        # print(f'Четные {even}   Нечетные {uneven}')
        return 0
    else:
        if (numb % 10) % 2 == 0:
            even += 1
        else:
            uneven += 1
        return recursion(numb // 10, even, uneven)


def funct():
    NUMB = 932850971070143275070239750527932850971070143275070239750527
    EVEN = 0
    UNEVEN = 0

    while NUMB > 9:
        if (NUMB % 10) % 2 == 0:
            EVEN += 1
        else:
            UNEVEN += 1

        NUMB = NUMB // 10

    if NUMB % 2 == 0:
        EVEN += 1
    else:
        UNEVEN += 1

    # print(f'Четные {EVEN}   Нечетные {UNEVEN}')


def main():
    recursion(NUMB, 0, 0)
    funct()


cProfile.run('main()')"""

"""NUMB = 35982093509283092039850932


def recursion(numb, inverse_numb):
    # mathematical character
    if numb == 0:
        print(f'Перевернутое число: {inverse_numb}')
        return 0
    else:
        excess = numb % 10  # находим остаток - последнюю цифру числа
        inverse_numb = inverse_numb * 10  # увеличиваем разрядность второго числа
        return recursion(numb // 10, inverse_numb + excess)


def funct(NUMB):
    INVERSE_NUMB = 0
    while NUMB > 0:
        excess = NUMB % 10  # находим остаток - последнюю цифру числа
        NUMB = NUMB // 10  # делим нацело - убираем из числа последнюю цифру
        INVERSE_NUMB = INVERSE_NUMB * 10  # увеличиваем разрядность второго числа
        INVERSE_NUMB = INVERSE_NUMB + excess  # добавляем очередную цифру


def main():
    recursion(NUMB, 0)
    funct(NUMB)


cProfile.run('main()')"""


def hw3_tsk4_v1():
    MY_LIST = [randint(0, 2) for i in range(10)]
    MY_DICT = dict()
    for i in MY_LIST:
        if MY_DICT.get(i) is None:
            MY_DICT.update({i: 1})
        else:
            MY_DICT[i] += 1

    x1 = max(MY_DICT, key=MY_DICT.get)


def hw3_tsk1_v1():
    MY_DIKT = {a: 0 for a in range(2, 10)}  # создаем словарь с ключами 2 - 9 и значением 0
    # print(MY_DIKT)

    for i in range(2, 100):  # перебор значений 2 - 99
        for j in range(2, 10):  # проверка каждого числа на кратность каждому ключу словаря
            if i % j == 0:
                MY_DIKT[j] += 1


def hw3_tsk5_v1():
    MY_LIST = [randint(-100, 100) for i in range(10)]
    # print(f'Базовый список: {MY_LIST}')

    MAX_NEGATIVE = min(MY_LIST)
    for i in MY_LIST:
        if MAX_NEGATIVE < i < 0:
            MAX_NEGATIVE = i


def hw3_tsk6_v1():
    MY_LIST = [randint(0, 100) for i in range(10)]
    # print(f'Исходный список {MY_LIST}')

    INDX_1 = max(MY_LIST)
    INDX_2 = min(MY_LIST)
    SUMM = 0
    # print(f'{MY_LIST.index(INDX_1)}, {MY_LIST.index(INDX_2)}')
    if MY_LIST.index(INDX_1) > MY_LIST.index(INDX_2):
        for i in range(MY_LIST.index(INDX_2) + 1, MY_LIST.index(INDX_1)):
            SUMM += MY_LIST[i]
    else:
        for i in range(MY_LIST.index(INDX_1) + 1, MY_LIST.index(INDX_2)):
            SUMM += MY_LIST[i]


def hw3_tsk7_v1():
    MY_LIST = [randint(-10000, 10000) for i in range(100000)]
    # print(f'Исходный массив: {MY_LIST}')
    MINN = None

    for i in range(2):
        if i > 0:
            if MINN != min(MY_LIST):
                MINN = min(MY_LIST)
                # print(f'Второй наименьший элемент: {MINN}')
                MY_LIST.remove(MINN)
            # else:
                # print(f'Встречается в этом массиве 2 раз')
        else:
            MINN = min(MY_LIST)
            # print(f'Наименьший элемент: {MINN}')
            MY_LIST.remove(MINN)


def hw3_tsk7_v2():
    MY_LIST = [randint(-10000, 10000) for i in range(100000)]
    # print(f'Исходный массив: {MY_LIST}')
    MINN = None

    for i in range(2):
        if i > 0:
            if MINN != min(MY_LIST):
                MINN = min(MY_LIST)
                # print(f'Второй наименьший элемент: {MINN}')
                MY_LIST.remove(MINN)
            # else:
                # print(f'Встречается в этом массиве 2 раз')
        else:
            MINN = min(MY_LIST)
            # print(f'Наименьший элемент: {MINN}')
            MY_LIST.remove(MINN)


def hw3_tsk8_v1():
    MY_LIST = [[randint(-1000, 1000) for i in range(1000)] for j in range(1000)]
    # print(MY_LIST)

    # for i in range(5):
    #     print(f'{i + 1}-я строка: ')
    #     MY_LIST.append([])
    #     for j in range(4):
    #         MY_LIST[i].append(int(input('')))

    for k in range(len(MY_LIST)):
        MY_LIST[k].append(sum(MY_LIST[k]))
        # print(MY_LIST[k])


# def main():
#     hw3_tsk7_v1()
#
#
# cProfile.run('main()')


"""cProfile везде показывает по 0.000. При увеличении исходных массивов может наблюдаться 
увеличение времени, но она касается только создания самого массива, а алгоритм его обработки 
 так и показывает нули."""