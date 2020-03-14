"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

NUMB_1 = int(input('Введите первое число: '))
try:
    NUMB_1 = int(NUMB_1)
except ValueError:
    print('Вы ввели не число')
NUMB_2 = int(input('Введите второе число: '))
try:
    NUMB_2 = int(NUMB_2)
except ValueError:
    print('Вы ввели не число')
NUMB_3 = int(input('Введите третье число: '))
try:
    NUMB_2 = int(NUMB_2)
except ValueError:
    print('Вы ввели не число!')

if NUMB_1 == NUMB_2 or NUMB_2 == NUMB_3 or NUMB_3 == NUMB_1:
    print(f"Вы ввели одинаковые числа!")
else:
    # MAX_NUMB = NUMB_1
    if NUMB_1 < NUMB_2:
        NUMB_1, NUMB_2 = NUMB_2, NUMB_1
    if NUMB_2 < NUMB_3:
        NUMB_2, NUMB_3 = NUMB_3, NUMB_2
    if NUMB_3 > NUMB_1:
        NUMB_3, NUMB_1 = NUMB_1, NUMB_3
    if NUMB_1 < NUMB_2:
        NUMB_1, NUMB_2 = NUMB_2, NUMB_1

    print(f"Среднее число: {NUMB_2}")
