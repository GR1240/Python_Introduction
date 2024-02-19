# # Задача 1. Сумма цифр трехзначного числа
# # Найдите сумму цифр трехзначного числа n.
# # Результат сохраните в перменную res.
# # Пример:
# # n = 123 -> res = 6 (1 + 2 + 3)
# # n = 100 -> res = 1 (1 + 0 + 0)

# n = 123
# # n = 100
# res = (n // 100) + ((n % 100) // 10) + (n % 10)
# print(res)


# # n = 123
# n = 100
# n1 = n // 100 # Нахождение первой цифры числа
# n2 = (n % 100) // 10 # Нахождение второй цифры числа
# n3 = n % 10 # Нахождение третьей цифры числа
# res = n1 + n2 + n3
# print(res)

# ============================

# # Задача 2. Бумажные журавлики
# # Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# # Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# # а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# # Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.
# # Пример:
# # n = 6 -> 1 4 1  
# # n = 24 -> 4 16 4    
# # n = 60 -> 10 40 10 

# n = 24
# # Количество журавликов, сделанных Петей и Сережей вместе
# x = n // 3
# # Количество журавликов, сделанных Петей и Сережей
# petya = sereja = x // 2
# # Количество журавликов, сделанных Катей
# katya = 2 * x
# print(petya, katya, sereja)

n = 24
n1 = n // 6
n2 = n // 6
n3 = (n // 6) * 4
print(n1, n3, n2)

# ------------------------------

# # Задача 3. Счастливый билет
# # Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# # Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# # Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# # Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
# # Пример:
# # n = 385916 -> yes
# # n = 123456 -> no

# n = 123456
# # n = 123456
# # Разбиваем номер билета на отдельные цифры
# digit1 = n // 100000
# digit2 = n // 10000 % 10
# digit3 = n // 1000 % 10
# digit4 = n // 100 % 10
# digit5 = n // 10 % 10
# digit6 = n % 10
# # Проверяем билет, является ли он счастливым?
# if digit1 + digit2 + digit3 == digit4 + digit5 + digit6:
#     print("yes")
# else:
#     print("no")


# ------------------------------

# # Задача 4. Деление шоколадки
# # Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом 
# # по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# # Выведите yes или no соответственно.
# # Пример:
# # a, b, c = 3, 2, 4 -> yes
# # a, b, c = 3, 2, 1 -> no

# a = 3
# b = 2
# c = 4
# if 0 < c <= a * b and ((c % a == 0) or (c % b == 0) or (c == a + b - 1)):
#     print("yes")
# else:
#     print("no")

a = 3
b = 2
c = 1
if c <= b * a and (c % a == 0 or c % b == 0):
    print('yes')
else:
    print('no')