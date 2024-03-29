# Задача 1. Встречаемость элемента в массиве
'''
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его.
Input:
list_1 = [1, 2, 3, 4, 5]
k = 3
Output:
# 1
'''
# list_1 = [1, 2, 3, 4, 5]
# k = 3

# frequency = {}

# for num in list_1:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# if k in frequency:
#     print(frequency[k])
# else:
#     print(0)

# # -------------------
# list_1 = [1, 2, 3, 4, 5]
# k = 3

# count = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count += 1
# print(count)

# # ---------------------------------------------

# Задача 2. Ближайший элемент в массиве
'''
Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

Пример:
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
'''

# list_1 = [1, 2, 3, 4, 5]
# k = 6

# closest = min(list_1, key=lambda x: abs(x - k))
# print(closest)

# # -------------------

# list_1 = [1, 2, 3, 4, 5]
# k = 6

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

# # ---------------------------------------------
'''
# Задача 3. Скрабл

В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

В случае с английским алфавитом очки распределяются так:

A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:

А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

Пример:


k = 'ноутбук'
# 12
'''

# k = 'ноутбук'

# # Словарь со стоимостями букв для английского алфавита
# english_scores = {
#     'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
#     'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
#     'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
# }

# # Словарь со стоимостями букв для русского алфавита
# russian_scores = {
#     'А': 1, 'Б': 3, 'В': 1, 'Г': 2, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1,
#     'Й': 4, 'К': 2, 'Л': 2, 'М': 2, 'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1,
#     'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'Ы': 4,
#     'Ь': 3, 'Э': 8, 'Ю': 8, 'Я': 3
# }

# # Определяем, какой алфавит используется в слове
# if all(letter.upper() in english_scores for letter in k):
#     scores = english_scores  # Если все буквы английские, используем английский алфавит
# else:
#     scores = russian_scores  # Иначе используем русский алфавит

# # Суммируем стоимость каждой буквы в слове
# total_score = sum(scores[letter.upper()] for letter in k)

# print(total_score)

# # -------------------

k = 'ноутбук'

points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)