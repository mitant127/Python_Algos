"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

"""При написании программы нашел статью https://habr.com/ru/post/122538/
в ней рассматривается постепенное доработка алгоритма.
Тк написанная мной программа была похожа на 3-ю версию программы из статьи
я решил не изобретать велосипед, а проверить все версии приведенных в статье программ."""


from timeit import Timer
from math import sqrt, log1p
import matplotlib.pyplot as plt
G2 = [100, 200, 400, 600, 800, 1000]
G1 = [10, 20, 40, 60, 80, 100]
Z = 5  # количество циклов для замера времени
# N = 10  # искомое простое число
Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z4_2, Z5_2, Z6_2, Z7_2, Z8_2 = [
], [], [], [], [], [], [], [], [], [], [], [], []
# массивы для заполнения времени

"""Первый алгоритм с перебором всех чисел и всех делителей и подсчетом найденых делителей
Занимает много времени тк мы перебираем все числа и все делители. """


def srch_prm_num_1(n):
    prime_num = []
    k = 0
    i = 1
    while n > int(len(prime_num)):
        i += 1
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            prime_num.append(i)
        else:
            k = 0
    # print(prime_num)


""""Избавляемся от подсчета делителей тк если найден хотябы один то число составное
и дальше делители можно не перебирать."""


def srch_prm_num_2(n):
    prime_num = []
    i = 1
    while n > int(len(prime_num)):
        i += 1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_num.append(i)
    # print(prime_num)


"""Тут делаем перебор делителей только по уже найденным простым числам"""


def srch_prm_num_3(n):
    prime_num = []
    i = 1
    while n > int(len(prime_num)):
        i += 1
        for j in prime_num:
            if i % j == 0:
                break
        else:
            prime_num.append(i)
    # print(prime_num)


"""Тут добавляем проверку на то, что делитель не превышает корня из числа для котороно ищем делитель"""


def srch_prm_num_4(n):
    prime_num = []
    i = 1
    while n > int(len(prime_num)):
        i += 1
        for j in prime_num:
            if j > int((sqrt(i)) + 1):
                prime_num.append(i)
                break
            if i % j == 0:
                break
        else:
            prime_num.append(i)
    # print(prime_num)


"""Тут добавляем отсеивание чисела кратные 2 и 5"""


def srch_prm_num_5(n):
    prime_num = []
    i = 1
    while n > int(len(prime_num)):
        i += 1
        if i > 10:
            if i % 2 == 0 or i % 10 == 5:
                continue
        for j in prime_num:
            if j > int((sqrt(i)) + 1):
                prime_num.append(i)
                break
            if i % j == 0:
                break
        else:
            prime_num.append(i)
    # print(prime_num)


"""Тут перебираем делители с шагом 2 что позволяет сразу отсеять четные числа."""


def srch_prm_num_6(n):
    prime_num = [2]
    i = 1
    while n > int(len(prime_num)):
        i += 2
        if i > 10 and i % 10 == 5:
            continue
        for j in prime_num:
            if j > int((sqrt(i)) + 1):
                prime_num.append(i)
                break
            if i % j == 0:
                break
        else:
            prime_num.append(i)
    # print(prime_num)


"""Заменяем извлечение корня на возведение в степень"""


def srch_prm_num_7(n):
    prime_num = [2]
    i = 1
    while n > int(len(prime_num)):
        i += 2
        if i > 10 and i % 10 == 5:
            continue
        for j in prime_num:   # деление очередного числа на уже найденные простые числа
            if j * j - 1 > i:
                prime_num.append(i)
                break  # если делитель найден выходим из цикла
            if i % j == 0:  # проверка делимости очередного числа на элементы массива
                break
        else:
            # если делитель не найден добавляем число в массив простых чисел
            prime_num.append(i)
    # print(prime_num[int(len(prime_num)) - 1])


def eratosfen(n):
    p = int(n * log1p(2 * n)) + n
    prime_num = []
    a = [i for i in range(p)]
    i = 2
    while i <= p - 1:
        if a[i] != 0:
            prime_num.append(a[i])
            if n <= int(len(prime_num)):
                break
            for j in range(i, p, i):
                a[j] = 0
        i += 1
    # print(prime_num[int(len(prime_num)) - 1])


for elm in G1:
    print(G1.index(elm))
    t1 = Timer(
        "srch_prm_num_1(elm)",
        "from __main__ import srch_prm_num_1, elm")
    # print("concat 1", t1.timeit(number=Z), "miliseconds")
    Z1.append(t1.timeit(number=Z))
    t2 = Timer(
        "srch_prm_num_2(elm)",
        "from __main__ import srch_prm_num_2, elm")
    # print("concat 2", t2.timeit(number=Z), "miliseconds")
    Z2.append(t2.timeit(number=Z))
    t3 = Timer(
        "srch_prm_num_3(elm)",
        "from __main__ import srch_prm_num_3, elm")
    # print("concat 3", t3.timeit(number=Z), "miliseconds")
    Z3.append(t3.timeit(number=Z))
    t4 = Timer(
        "srch_prm_num_4(elm)",
        "from __main__ import srch_prm_num_4, elm")
    # print("concat 4", t4.timeit(number=Z), "miliseconds")
    Z4.append(t4.timeit(number=Z))
    t5 = Timer(
        "srch_prm_num_5(elm)",
        "from __main__ import srch_prm_num_5, elm")
    # print("concat 5", t5.timeit(number=Z), "miliseconds")
    Z5.append(t5.timeit(number=Z))
    t6 = Timer(
        "srch_prm_num_6(elm)",
        "from __main__ import srch_prm_num_6, elm")
    # print("concat 6", t6.timeit(number=Z) , "miliseconds")
    Z6.append(t6.timeit(number=Z))
    t7 = Timer(
        "srch_prm_num_7(elm)",
        "from __main__ import srch_prm_num_7, elm")
    # print("concat 7", t7.timeit(number=Z), "miliseconds")
    Z7.append(t7.timeit(number=Z))
    t8 = Timer("eratosfen(elm)", "from __main__ import eratosfen, elm")
    # print("concat 8", t8.timeit(number=Z), "miliseconds")
    Z8.append(t8.timeit(number=Z))

for el in G2:
    print(G2.index(el))
    t4 = Timer("srch_prm_num_4(el)", "from __main__ import srch_prm_num_4, el")
    # print("concat 4", t4.timeit(number=Z), "miliseconds")
    Z4_2.append(t4.timeit(number=Z))
    t5 = Timer("srch_prm_num_5(el)", "from __main__ import srch_prm_num_5, el")
    # print("concat 5", t5.timeit(number=Z), "miliseconds")
    Z5_2.append(t5.timeit(number=Z))
    t6 = Timer("srch_prm_num_6(el)", "from __main__ import srch_prm_num_6, el")
    # print("concat 6", t6.timeit(number=Z) , "miliseconds")
    Z6_2.append(t6.timeit(number=Z))
    t7 = Timer("srch_prm_num_7(el)", "from __main__ import srch_prm_num_7, el")
    # print("concat 7", t7.timeit(number=Z), "miliseconds")
    Z7_2.append(t7.timeit(number=Z))
    t8 = Timer("eratosfen(el)", "from __main__ import eratosfen, el")
    # print("concat 8", t8.timeit(number=Z), "miliseconds")
    Z8_2.append(t8.timeit(number=Z))

print(f'{Z1}\n{Z2}\n{Z3}\n{Z4}\n{Z5}\n{Z6}\n{Z7}\n{Z8}\n{Z4_2}\n{Z5_2}\n{Z6_2}\n{Z7_2}\n{Z8_2}')

# Построение графика

plt.figure(figsize=(15, 10))

plt.subplot(2, 1, 1)
plt.title("Зависимости: времени от количества простых чисел")  # заголовок
plt.xlabel("кол-во прост. чисел")         # ось абсцисс
plt.ylabel("время млс")    # ось ординат
plt.grid()              # включение отображение сетки
plt.plot(G1, Z1, c="brown", label="1")
plt.plot(G1, Z2, c="blue", label="2")
plt.plot(G1, Z3, c="yellow", label="3")
plt.plot(G1, Z4, c="black", label="4")
plt.plot(G1, Z5, c="green", label="5")
plt.plot(G1, Z6, c="orange", label="6")
plt.plot(G1, Z7, c="gray", label="7")
plt.plot(G1, Z8, c="red", label="8")
plt.legend()
# plt.show()

# Построение графика
plt.subplot(2, 1, 2)
plt.title("Зависимости: времени от количества простых чисел")  # заголовок
plt.xlabel("кол-во прост. чисел")         # ось абсцисс
plt.ylabel("время млс")    # ось ординат
plt.grid()              # включение отображение сетки
plt.plot(G2, Z4_2, c="black", label="4")
plt.plot(G2, Z5_2, c="green", label="5")
plt.plot(G2, Z6_2, c="orange", label="6")
plt.plot(G2, Z7_2, c="gray", label="7")
plt.plot(G2, Z8_2, c="red", label="8")
plt.legend()
plt.show()


"""Выводы:
Как и ожидалось первый алгоритм с перебором всех чисел по порядку и всех делителей
 дает худшие результаты тк получается квадратичная сложность O(N^2)

 На малых значениях N хорошо себя показывае алгоритм 3 и 7
 Алгоритмы 4, 5, 6 скорее всего "проседают" по скорости из-за использования
 функции sqrt(i)

На больших значениях хорошо работает алгоритм 7 и решето Эратосфена, оно показывает себя лучше всего
сложность алгоритма O(N)"""
