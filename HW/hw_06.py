# Задача 1. Элементы из заданного диапазона
'''
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.

На входе:
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

На выходе:
1
2
3
6
7
9
10
11
13
14
16
19
'''

# def find_indices_in_range(lst, min_number, max_number):
#     result_indices = []
#     for i, num in enumerate(lst):
#         if min_number <= num <= max_number:
#             result_indices.append(i)
#     return result_indices

# # Входные данные
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# # Поиск индексов элементов в заданном диапазоне
# result = find_indices_in_range(list_1, min_number, max_number)

# # Вывод результатов
# for index in result:
#     print(index)

# # ------------

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# for i in range(len(list_1)):
#   if min_number <= list_1[i] <= max_number:
#     print(i)

# # ------------------------------------------------------

# Задача 2. Арифметическая прогрессия
'''
Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , 
разность d и количество элементов n будет задано автоматически. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

На входе:
a1 = 2
d = 3
n = 4

На выходе:
2
5
8
11

'''

# def arithmetic_progression(a1, d, n):
#     progression = [a1 + (i * d) for i in range(n)]
#     return progression

# # Входные данные
# a1 = 2
# d = 3
# n = 4

# # Создание массива элементов арифметической прогрессии
# result = arithmetic_progression(a1, d, n)

# # Вывод результатов
# for elem in result:
#     print(elem)

# # --------------

a1 = 2
d = 3
n = 4

for i in range(n):
  print(a1 + i * d)