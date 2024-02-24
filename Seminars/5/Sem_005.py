# Задача №31. 
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fib(n):
#     if n in range(0,2):
#         return 1
#     return fib(n - 1) + fib(n - 2)

# m = int(input())
# print(fib(m))

# -----------------------------------

# Задача 32. 
# Найти факториал, через рекурсию

# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(3))
# print(factorial(5))
# print(factorial(9))

# # -----------------------------------

# Задача 35. 
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# def simple(n, d=2):
#     if d * d > n:
#         return True
#     elif n % d == 0:
#          return False
#     return simple(n, d + 1)

# number = int(input("Введите число: "))
# # number = 5
# if simple(number):
#     print("yes")
# else:
#     print("no")

# # -----------------------------------

# Задача №37
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def reverse_sequence(n):
    if n == 0:  
        return
    else:
        num = int(input())  
        reverse_sequence(n - 1)  
        print(num, end=" ") 

n = int(input("Введите количество элементов: "))
reverse_sequence(n) 



