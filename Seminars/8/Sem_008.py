'''
Задача.
Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
При решении задачи используйте комбинацию функций filter, map, sum.

Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.
'''


# # Генерация всех двузначных чисел
# two_digit_numbers = range(10, 100)

# # Фильтрация чисел, делящихся на 9
# divisible_by_9 = filter(lambda x: x % 9 == 0, two_digit_numbers)

# # Возведение в квадрат и нахождение суммы квадратов
# sum_of_squares = sum(map(lambda x: x ** 2, divisible_by_9))

# print(sum_of_squares)

# -------------------

# print(sum(map(lambda x: x * x, filter(lambda x: x % 9 == 0, range(10, 100)))))

# ---------------------------------------------------------------------------------
'''
Задача.
Вывести из списка только двузначные числа (в порядке возрастания)

num = '20 -14 88 1 9 -7'
'''

# num = '20 -14 88 1 9 -7'

# # Разбиваем строку на отдельные элементы
# numbers = num.split()

# # Преобразуем элементы в числа и фильтруем только двузначные и положительные
# two_digit_numbers = filter(lambda x: len(x) == 2 and x[0] != '0' and int(x) > 0, numbers)

# # Сортируем числа по возрастанию
# sorted_numbers = sorted(two_digit_numbers)

# print(*sorted_numbers)

# --------------------------
num = '20 -14 88 1 9 -7'
def check_numbers(str_to_check):
    num_list = list(filter(lambda x : len(str(abs(int(x)))) == 2, str_to_check.split()))
    print(num_list)

check_numbers(num)


