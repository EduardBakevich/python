# """Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и
# “Пам парам”, если с ритмом все не в порядке"""

# def numGlasnye(list_):
#     glasnye = []
#     for i in list_:
#         cnt = 0
#         for j in i:
#             if j in 'аеёиоуыэюя':
#                 cnt += 1
#         glasnye.append(cnt)
#     if glasnye.count(glasnye[0]) == len(glasnye):
#         return 'Парам пам-пам'
#     else:
#         return 'Пам парам'

# a = input('Пример кричалки ').split()
# # пара-ра-рам рам-пам-папам па-ра-па-да
# print(numGlasnye(a))

"""Напишите функцию 
print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов 
таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы 
(подумайте, почему не с нуля)."""


def tablica(n):
    list_ = [x * y for x in range(1, n + 1) for y in range(1, n + 1)]
    return list_


f = 6
print(tablica(f))