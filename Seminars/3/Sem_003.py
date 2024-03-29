'''
Задача №17. 
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''

# lst = [1, 1, 2, 0, -1, 3, 4, 4]

# #Создаем переменную для хранения уникальных чисел
# unique_numbers = []

# # Перебираем каждое число в списке
# # Если число еще не встречалось в списке уникальных чисел, добавляем его
# for num in lst:    
#     if num not in unique_numbers:
#         unique_numbers.append(num)

# print(len(unique_numbers)) 




'''
Задача №19. 
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.
'''

# # Получаем входные данные от пользователя
# lst = [1, 2, 3, 4, 5]
# k = 2
# # Вычисляем длину списка
# n = len(lst)
# # Вычисляем фактическое количество сдвигов (чтобы избежать повторных сдвигов на целое количество периодов)
# k = k % n

# # Выполняем сдвиг списка
# shifted_lst = lst[-k:] + lst[:-k]

# print(shifted_lst)

# # -----------

# # Решение с использованием циклического сдвига
# lst = [1, 2, 3, 4, 5]
# k = 2

# for i in range(k):
#     temp = lst.pop() # Удаляем последний элемент списка
#     lst.insert(0, temp) # Вставляем его в начало списка
#     print(lst)

'''
Задача №21. 
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
'''
dic = [
{"V": "S001"},
{"V": "S002"},
{"VI": "S001"},
{"VI": "S005"},
{"VII": " S005 "},
{" V ": " S009 "},
{" VIII ": " S007 "},
]

# s = set()
# for i in dic:
# for k, v in i.items():
# s.add(v)

# print(s)

s = set()
for i in dic:
    for v in i.values():
        s.add(v)
        
print(str(s))