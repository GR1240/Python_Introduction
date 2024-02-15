# Вывод текста в консоль.
# print (5, 8, 6)


"""
# Базовые типы данных
n = 5 # None # 1.89
print(n)
"""


"""
# Одинарные или двойные кавычки
n= 'fdjs'
n1 = "sdfs"
print(n, n1)
"""


"""
# функция type() позволяет определить тип переменной
n = 5
print(type(n))

n = 'fsdf'
print(type(n))

n = 1.89
print(type(n))
"""

"""
# одинарные и двойные кавычки внутри строки
n = 'fd\'df'
print(n)

n = 'fd"gbdg"df'
print(n)
"""


"""
# Интерполяция - получение сложной строки из нескольких простых с помощью шаблонов
a = 5
b = 5.89
c = 'hello'
#print(a, b, c)
print(a,'-', b,'-', c)
print('{} - {} - {}'.format(a,b,c))
print(f'{a} - {b} - {c}')
"""

"""
# # Оператор ввода данных
print('Введите первое число: ')
a = input()
b = input('Введите второе число: ')
print(a, '+', b, '=', a + b)

# c = 5.89
# print(c)
# print(type(c))

# c = str(c)
# print(c)
# print(type(c))

# # c = int(c)
# # print(c)
# # print(type(c))

# c = bool(c)
# print(c)
# print(type(c))

print('Введите первое число: ')
a = int(input())
b = int(input('Введите второе число: '))
print(a, '+', b, '=', a + b)
"""


"""
# Округление чисел
a = 5.89956
b = 6.556551
print(a*b)
print(round(a*b, 3))
"""

"""
# Сокращенное присваивание
iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5 
"""


"""
# Логические операции
a = 1 > 4
print(a)

a = 1 < 4 and 5 > 2
print(a)

a = 1 == 2
print(a)

a = 1 != 2
print(a)

a = 'qwe'
b = 'qwe'
print(a == b)

a = 1 < 3 < 5 < 10
print(a)
"""

"""
# Управляющие конструкции: if, if-else
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так рад Вам, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)
"""


"""
# Цикл While
i = 0
while i < 5:
    # if i == 3:
    #     break
    i = i + 1
else:
    print('Пожалуй')
    print('Хватит')
print(i)

# Метод flag
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1
"""


# Цикл for, функция range()
a = 'qwerty'

#print(a[0])
for i in a:
    print(i)

# ----------------------
    
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

# ----------------------
    
text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.lower()) # съешь ещё этих мягких французских булок
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

# ----------------------

# Срезы
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...
print(text)

