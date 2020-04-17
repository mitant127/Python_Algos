"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
""" Python 3.8
    OS - 64"""

from memory_profiler import profile
import memory_profiler
import time


@profile
def func1():
    """Line #    Mem usage    Increment   Line Contents
    ================================================
        20     13.6 MiB     13.6 MiB   @profile
        21                             def func1():
        22     13.6 MiB      0.0 MiB       f = 10000
        23     13.6 MiB      0.0 MiB       MY_DIKT = {a: 0 for a in range(2, int(f / 10))}  # создаем словарь с ключами 2 - 9 и значением 0
        24     13.6 MiB      0.0 MiB       print(MY_DIKT)
        25
        26     13.6 MiB      0.0 MiB       for i in range(2, f):  # перебор значений 2 - 99
        27     13.6 MiB      0.0 MiB           for j in range(2, 10):  # проверка каждого числа на кратность каждому ключу словаря
        28     13.6 MiB      0.0 MiB               if i % j == 0:
        29     13.6 MiB      0.0 MiB                   MY_DIKT[j] += 1
        30
        31     13.6 MiB      0.0 MiB       for i in range(2, 9):
        32     13.6 MiB      0.0 MiB           print(f'В диапазоне 2-99: {MY_DIKT[i]} чисел кратны {i}')


    Выполнение заняло 10.75 сек and 0.17578125 Мб
    Выполнение заняло 0.015625 сек and 0.01953125 Мб - без @profile"""
    f = 10000
    MY_DIKT = {a: 0 for a in range(2, int(f / 10))}  # создаем словарь с ключами 2 - 9 и значением 0
    print(MY_DIKT)

    for i in range(2, f):  # перебор значений 2 - 99
        for j in range(2, 10):  # проверка каждого числа на кратность каждому ключу словаря
            if i % j == 0:
                MY_DIKT[j] += 1

    for i in range(2, 9):
        print(f'В диапазоне 2-99: {MY_DIKT[i]} чисел кратны {i}')


@profile
def func2():
    """Line #    Mem usage    Increment   Line Contents
    ================================================
        53     13.6 MiB     13.6 MiB   @profile
        54                             def func2():
        55     13.6 MiB      0.1 MiB       from random import randint
        56
        57     15.7 MiB      0.3 MiB       MY_LIST = [randint(-1000, 1000) for i in range(100000)]
        58     15.3 MiB      0.0 MiB       print(MY_LIST)
        59     15.6 MiB      0.0 MiB       print(list(i for i in MY_LIST if i % 2 == 0))


    Выполнение заняло 16.953125 сек and 0.53515625 Мб
    Выполнение заняло 0.265625 сек and 0.09765625 Мб - без @profile"""
    from random import randint

    MY_LIST = [randint(-1000, 1000) for i in range(100000)]
    print(MY_LIST)
    print(list(i for i in MY_LIST if i % 2 == 0))


# @profile
def func3():
    """Line #    Mem usage    Increment   Line Contents
    ================================================
        74     13.6 MiB     13.6 MiB   @profile
        75                             def func3():
        76                                 """"""
        77     13.6 MiB      0.1 MiB       from random import randint
        78                             
        79     13.7 MiB      0.0 MiB       MY_LIST = [randint(0, 9) for i in range(10000)]
        80     13.7 MiB      0.0 MiB       MY_DICT = dict()
        81                             
        82     13.7 MiB      0.0 MiB       for i in MY_LIST:
        83     13.7 MiB      0.0 MiB           if MY_DICT.get(i) is None:
        84     13.7 MiB      0.0 MiB               MY_DICT.update({i: 1})
        85                                     else:
        86     13.7 MiB      0.0 MiB               MY_DICT[i] += 1
        87                             
        88     13.7 MiB      0.0 MiB       print(
        89     13.7 MiB      0.1 MiB           f'В массиве {MY_LIST}, \nчаше всего встречается число - {max(MY_DICT, key=MY_DICT.get)},'
        90                                     f' {MY_DICT[max(MY_DICT, key=MY_DICT.get)]} раз.')
    
    
    Выполнение заняло 2.578125 сек and 0.24609375 Мб
    Выполнение заняло 0.0625 сек and 0.09765625 Мб - без @profile"""
    from random import randint

    MY_LIST = [randint(0, 9) for i in range(10000)]
    MY_DICT = dict()

    for i in MY_LIST:
        if MY_DICT.get(i) is None:
            MY_DICT.update({i: 1})
        else:
            MY_DICT[i] += 1

    print(
        f'В массиве {MY_LIST}, \nчаше всего встречается число - {max(MY_DICT, key=MY_DICT.get)},'
        f' {MY_DICT[max(MY_DICT, key=MY_DICT.get)]} раз.')


# @profile
def func4():
    """Line #    Mem usage    Increment   Line Contents
    ================================================
       114     13.6 MiB     13.6 MiB   @profile
       115                             def func4():
       116                                 """"""
       117     13.6 MiB      0.0 MiB       MY_LIST = []
       118                             
       119     13.6 MiB      0.0 MiB       for i in range(5):
       120     13.6 MiB      0.0 MiB           print(f'{i + 1}-я строка: ')
       121     13.6 MiB      0.0 MiB           MY_LIST.append([])
       122     13.6 MiB      0.0 MiB           for j in range(4):
       123     13.6 MiB      0.1 MiB               MY_LIST[i].append(int(input('')))
       124                             
       125     13.5 MiB      0.0 MiB       for k in range(len(MY_LIST)):
       126     13.5 MiB      0.0 MiB           MY_LIST[k].append(sum(MY_LIST[k]))
       127     13.5 MiB      0.0 MiB           print(MY_LIST[k])
    
    
    Выполнение заняло 0.09375 сек and 0.1328125 Мб
    Выполнение заняло 0.0 сек and 0.0625 Мб - без @profile"""
    MY_LIST = []

    for i in range(5):
        print(f'{i + 1}-я строка: ')
        MY_LIST.append([])
        for j in range(4):
            MY_LIST[i].append(int(input('')))

    for k in range(len(MY_LIST)):
        MY_LIST[k].append(sum(MY_LIST[k]))
        print(MY_LIST[k])


# @profile
def func5():
    """Line #    Mem usage    Increment   Line Contents
    ================================================
       148     13.6 MiB     13.6 MiB   @profile
       149                             def func5():
       150                                 """"""
       151     13.6 MiB      0.0 MiB       from math import sqrt
       152     13.6 MiB      0.0 MiB       NUMB = 0
       153                             
       154                                 # recursion(число элементов ряда/текущий элемент, сумма элементов ряда, значение текушего элемент ряда)
       155     14.3 MiB      0.1 MiB       def recursion(numb, summ, series_element):
       156     14.3 MiB      0.0 MiB           if numb == 0:
       157                                         # print(numb, summ, series_element)  # подглядываем за процессом
       158     14.3 MiB      0.0 MiB               return summ + series_element  # прибавляем посделний элемент ряда
       159                                     else:
       160                                         # print(numb, summ, series_element)  # подглядываем за процессом
       161     14.3 MiB      0.0 MiB               return recursion(numb - 1, summ + series_element, series_element / -2)
       162                             
       163     14.3 MiB      0.0 MiB       print(recursion(800, 0, 1))
    
    
    Выполнение заняло 0.25 сек and 0.88671875 Мб
    Выполнение заняло 0.0 сек and 0.58984375 Мб - без @profile"""
    NUMB = 0

    # recursion(число элементов ряда/текущий элемент, сумма элементов ряда, значение текушего элемент ряда)
    def recursion(numb, summ, series_element):
        if numb == 0:
            # print(numb, summ, series_element)  # подглядываем за процессом
            return summ + series_element  # прибавляем посделний элемент ряда
        else:
            # print(numb, summ, series_element)  # подглядываем за процессом
            return recursion(numb - 1, summ + series_element, series_element / -2)

    print(recursion(800, 0, 1))


# @profile
def func6():
    """Line #    Mem usage    Increment   Line Contents
================================================
   185     13.6 MiB     13.6 MiB   @profile
   186                             def func6():
   187                                 """"""
   188     13.6 MiB      0.0 MiB       NUMB = 800
   189                             
   190     13.6 MiB      0.0 MiB       SUMM = 1
   191     13.6 MiB      0.0 MiB       SERIES_ELEMENT = 1
   192                             
   193     13.6 MiB      0.0 MiB       while NUMB > 0:
   194     13.6 MiB      0.0 MiB           SERIES_ELEMENT = SERIES_ELEMENT / -2
   195     13.6 MiB      0.0 MiB           SUMM += SERIES_ELEMENT
   196     13.6 MiB      0.0 MiB           NUMB -= 1
   197                             
   198     13.6 MiB      0.0 MiB       print(f'{SUMM}')


Выполнение заняло 0.234375 сек and 0.171875 Мб
Выполнение заняло 0.0 сек and 0.0234375 Мб - без @profile"""
    NUMB = 800

    SUMM = 1
    SERIES_ELEMENT = 1

    while NUMB > 0:
        SERIES_ELEMENT = SERIES_ELEMENT / -2
        SUMM += SERIES_ELEMENT
        NUMB -= 1

    print(f'{SUMM}')


# @profile
def func7():
    """Line #    Mem usage    Increment   Line Contents
    ================================================
       219     13.6 MiB     13.6 MiB   @profile
       220                             def func7():
       221                                 """"""
       222     13.6 MiB      0.0 MiB       def recursion(numb, even, uneven):
       223                                     # mathematical character
       224     13.6 MiB      0.0 MiB           if numb < 10:
       225     13.6 MiB      0.0 MiB               if numb % 2 == 0:
       226                                             even += 1
       227                                         else:
       228     13.6 MiB      0.0 MiB                   uneven += 1
       229     13.6 MiB      0.0 MiB               print(f'Четные {even}   Нечетные {uneven}')
       230     13.6 MiB      0.0 MiB               return 0
       231                                     else:
       232     13.6 MiB      0.0 MiB               if (numb % 10) % 2 == 0:
       233     13.6 MiB      0.0 MiB                   even += 1
       234                                         else:
       235     13.6 MiB      0.0 MiB                   uneven += 1
       236     13.6 MiB      0.0 MiB               return recursion(numb // 10, even, uneven)
       237                             
       238     13.6 MiB      0.0 MiB       recursion(123456789012345678901234567890123456789012345678901234567890, 0, 0)
    
    
    Выполнение заняло 0.09375 сек and 0.203125 Мб
    Выполнение заняло 0.0 сек and 0.0078125 Мб - без @profile"""
    def recursion(numb, even, uneven):
        # mathematical character
        if numb < 10:
            if numb % 2 == 0:
                even += 1
            else:
                uneven += 1
            print(f'Четные {even}   Нечетные {uneven}')
            return 0
        else:
            if (numb % 10) % 2 == 0:
                even += 1
            else:
                uneven += 1
            return recursion(numb // 10, even, uneven)

    recursion(123456789012345678901234567890123456789012345678901234567890, 0, 0)


# @profile
def func8():
    """Line #    Mem usage    Increment   Line Contents
    ================================================
       264     13.6 MiB     13.6 MiB   @profile
       265                             def func8():
       266     13.6 MiB      0.0 MiB       NUMB = 123456789012345678901234567890123456789012345678901234567890
       267     13.6 MiB      0.0 MiB       EVEN = 0
       268     13.6 MiB      0.0 MiB       UNEVEN = 0
       269
       270     13.6 MiB      0.0 MiB       while NUMB > 9:
       271     13.6 MiB      0.0 MiB           if (NUMB % 10) % 2 == 0:
       272     13.6 MiB      0.0 MiB               EVEN += 1
       273                                     else:
       274     13.6 MiB      0.0 MiB               UNEVEN += 1
       275
       276     13.6 MiB      0.0 MiB           NUMB = NUMB // 10
       277
       278     13.6 MiB      0.0 MiB       if NUMB % 2 == 0:
       279                                     EVEN += 1
       280                                 else:
       281     13.6 MiB      0.0 MiB           UNEVEN += 1
       282
       283     13.6 MiB      0.0 MiB       print(f'Четные {EVEN}   Нечетные {UNEVEN}')


    Выполнение заняло 0.078125 сек and 0.171875 Мб
    Выполнение заняло 0.0 сек and 0.00390625 Мб - без @profile"""
    NUMB = 123456789012345678901234567890123456789012345678901234567890
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

    print(f'Четные {EVEN}   Нечетные {UNEVEN}')


if __name__ == '__main__':

    # левые отсечки времени и памяти
    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()

    func1()
    # func2()
    # func3()
    # func4()
    # func5()
    # func6()
    # func7()
    # func8()

    # правые отсечки времени и памяти
    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]

    print(f"Выполнение заняло {time_diff} сек and {mem_diff} Мб")


"""Аналитика
Программы которые были напсаны на 1-3 уроке достаточно просты.
Если отключать # @profile то большенство программ выполняются почти мгновенно.
При этом значительный прирост памяти происходит только при создании больших массивов.
Обработка созданных массивов почти не увеличивает использование пямяти (при замерах memory_profiler)
На примерах функций func5(), func6(), func7(), func8(). При этом func5(), func6() и func7(), func8()
решают одинаковые задачи, но func5(), func7() решают ее через рекурсию.
Видно что рекурсия потребляет значительно больше памяти"""


