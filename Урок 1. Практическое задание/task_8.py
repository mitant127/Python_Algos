"""
Задание 8.	Определить, является ли год, который ввел пользователем,
високосным или не високосным.

Подсказка:
Год является високосным в двух случаях: либо он кратен 4,
но при этом не кратен 100, либо кратен 400.

Попробуйте решить задачу двумя способами:
1. Обычное ветвление
2. Тернарный оператор

П.С. - Тернарные операторы, также известные как условные выражения,
представляют собой операторы, которые оценивают что-либо на основе условия,
являющегося истинным или ложным. Он был добавлен в Python в версии 2.5 .
Он просто позволяет протестировать условие в одной строке,
заменяя многострочное if-else, делая код компактным.
"""

YEAR = input('Введите год: ')

try:
    YEAR = int(YEAR)
except ValueError:
    print('Вы ввели не число')
else:
    if YEAR % 4 != 0:
        print(f" 1 Год {YEAR} невисокосный")
    elif YEAR % 100 == 0:
        if YEAR % 400 == 0:
            print(f"Год {YEAR} високосный")
        else:
            print(f" 2 Год {YEAR} невисокосный")
    else:
        print(f"Год {YEAR} високосный")

# с помощью тернарного опреатора
LEAP = 'невисокосный' if YEAR % 4 != 0 or (
    YEAR % 100 == 0 and YEAR % 400 != 0) else 'високосный'
print(f"Год {YEAR} {LEAP}")
