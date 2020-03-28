"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
from random import randint

MY_LIST = [randint(0, 2) for i in range(10)]
MY_DICT = dict()

for i in MY_LIST:
    if MY_DICT.get(i) is None:
        MY_DICT.update({i: 1})
    else:
        MY_DICT[i] += 1

print(
    f'В массиве {MY_LIST}, \nчаше всего встречается число - {max(MY_DICT, key=MY_DICT.get)},'
    f' {MY_DICT[max(MY_DICT, key=MY_DICT.get)]} раз.')
