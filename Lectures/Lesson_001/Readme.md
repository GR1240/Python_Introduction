## Знакомство с языком программирования Python

### История языка Python
История языка Python
В качестве названия Guido van Rossum выбрал Python в честь
комедийных серий BBC "Летающий цирк Монти-Пайтона", а вовсе
не по названию змеи.
Требовался второй язык программирования на C или C++ для
решения задач, для которых написание программы на C было
просто неэффективным.
Первая «официальная» версия языка увидела свет в 1994 году,
когда Гвидо еще работал в CWI. Среди прочего в первой версии
появились инструменты функционального программирования и
поддержка комплексных чисел. Но самое главное, что следующий
шаг сделал не только проект, но и его сообщество.
В том же 1994 году состоялась первая рабочая встреча
пользователей Python. Встреча прошла в государственном бюро
стандартов США (NBS, сегодня это государственный институт
стандартов и технологий — NIST).
### Начало работы с Python
1. Python является интерпретируемым ЯП, поэтому перед тем, как
начать изучать синтаксис необходимо установить интерпретатор: по
[ссылке](https://www.python.org/downloads/)
2. На macOS и Linux версию необходимо обновить, так как уже
Python предустановлен
3. В Windows, начиная с версии 8 и выше, можно смело
устанавливать последнюю версию интерпретатора, но с Windows 7
или ниже необходимо установить версию 3.8 или ниже

### Как запустить скрипт?
Если после выполнения команды в терминале остаются стрелки >>>, то
нажмите ctrl + Z, чтобы выйти непосредственно в терминал.
Чтобы запустить программный код, используйте следующую команду в
терминале:
python name_file.py
Где name_file - имя вашего файла

### Оператор вывода данных.
**print(var1, var2, var3)** - функция, которая выводит данные на экран, где var1,
var2, var3 - переменные или значения.
Синтаксис Python
Синтаксис Python очень простой и примитивный, приведу пример с языком
программирования C#
| C#               |  Python |
| -------------------------------------------- | ---------------- |
| Console.WriteLine(1);                                                                    | print(1)                         |
| int n = 1;                                                                               | n = 1                            |
| int n = Convert.ToInt32(Console.ReadLine());                                             | n = int(input())                 |






| Базовые типы данных Python                |  |
| -------------------- | --------------------- |
| int                  | Целые числа           |
| float                | Дробные числа         |
| bool    | Логический тип данных (True/False) |
| str                  | Строка                |


Объявление переменной \
● название переменной = значение переменной (один знак
равенства обозначает присвоение значения к переменной)

Программный код:          
```py
a = 123 
b = 1.23
print(a)
print(b)
```
Вывод:
```
123
1.23
```
>Нельзя указать переменную, не присвоив ей какое-либо значение. Но
можно присвоить значение None и использовать переменную дальше по
коду.
Программный код:          
```py
value = None
a = 123
b = 1.23
print(a)
print(b)
value = 1234
print(value) 
```
Вывод:
```
123
1.23
1234
```

### Как узнать какой тип данных в переменной?
Часто в процессе программирования на языке Python возникает необходимость определить тип переменной, можно использовать встроенную функцию type(). 

Это может быть полезно во многих случаях, например, при работе с различными структурами данных.

```py
print(type(name)) # функция, которая указывает на тип данных
```

### Как объявить строку?
Чтобы создать строку и сохранить ее в переменную необходимо написать
следующим образом:
```py
s = ‘hello,’ # создание 1-ой строки
s = “world” # создание 2-ой строки
print(s, w)
```
### Как объявить строку?
Строка — это упорядоченная последовательность символов, которая предназначена для хранения информации в виде простого текста. Чтобы создать строку в Python, нужно использовать одинарные или двойные кавычки. Если же мы хотим определить многострочный текст можно использовать тройные двойные или тройные одинарные кавычки:
```py
first = 'Привет, мир!'
second = "Привет, мир!"
third = """У лукоморья дуб зелёный,
златая цепь на дубе том."""
```

### Использование одинарных и двойных кавычек внутри строки
Можно ли писать кавычки в виде текста внутри строки? Пример: *my mom
shouted: “good luck!”*. Но для того чтобы создать строку мы должны
использовать еще одни кавычки, как это сделать?
Используйте разные кавычки для объявления переменной и внутри
строки:
```py
s = 'hello "world"'
s = "hello 'world'"
s = 'hello \"world'
```

### Как сделать комментарий?
Если Вы хотите закомментировать 1 строку достаточно применить
специальный символ “#”, если Вам нужно закомментировать сразу
несколько строк используйте тройные кавычки ‘’’
```py
# print(1)
# —------------------
’’’print(1)
print(1)
print(1)
print(1)
print(1)’’’
```

### Интерполяция
Иногда возникают такие ситуации, когда нужно вывести в одном
предложение и числа и текст, но как это сделать более рационально и
красиво, обратимся к такому понятию, как интерполяция.
Интерполяция — способ получить сложную строку из нескольких простых
с использованием специальных шаблонов.
```py
a = 3
b = 11
s = 2022
print(a, b, s)
print(a,'-'b,'-'s)
print('{} - {} - {}'.format(a,b,s))
print(f'first - {a} second - {b} third - {s}')
```

### Оператор ввода данных
Как и в любом языке программирования, у Python есть
операторы ввода данных. Не все так просто, как может
показаться :) \
Функция input() по умолчанию вводит строку.

> Например мы ввели 2 числа(a, b).  
> a = ‘5’                                                                 
> b = ‘7’

Как получить сумму двух чисел?

Программный код: 
```py
print('Введите первое число: ')
a = input() 
b = input('Введите второе число: ')
print(a, '+', b, '=', a + b)
```
Вывод:
```
57
```
Так как по умолчанию c помощью функции input() вводится
строка, мы видим, что программа выводит 57, хотя в реальной жизни 5 + 7 будет 12 Чтобы это исправить необходимо воспользоваться вспомогательными
функциями:
- int() - функция, которая позволяет преобразовывать любой тип данных в число(если это возможно)
- str() - функция, которая позволяет преобразовывать любой тип данных в строку(если это возможно)
- float() - функция, которая позволяет преобразовывать любой тип данных в дробное число (если это возможно)

Программный код: 
```py
print('Введите первое число: ')
a = int(input())  # a = 5
b = int(input('Введите второе число: '))  # b = 7
print(a, '+', b, '=', a + b)
```
Вывод:
```
12
```

### Арифметические операции.
Давайте посмотрим какой синтаксис в Python у базовых
арифметический операций.
| Приоритет      | Знак операции         | Операция |
| --------- | -------------- | --------------------- |
| 1                  | **                           | Возведение в степень                       |
| 2                  | *                            | Умножение                                  |
| 3                  | /                            | Деление                                    |
| 4                  | //                           | Целочисленное деление                      |
| 5                  | %                            | Остаток от деления                         |
| 6                  | +                            | Сложение                                   |
| 7                  | -                            | Вычитание                                  |

>В Python нет лимита по хранению данных (нет ограничения по битам для
хранения числа из-за динамической типизации данных)

### Округление числа
Можно указать количество знаков после запятой:
```py
a = 1.43425
b = 2.2983
c = round(a * b, 5) # 3,29633
```

### Сокращенные операции присваивания
Если в C# внутри цикла for используется i++ для сокращения i = i + 1, 
то в Python можно сокращать операторы присваивания следующим образом:
```py
iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5
```

### Логические операции.
| Знак операции                              | Операция |
| ------------- | ------------------------------------------ |
| >                          | Больше                                                                               |
| >=                         | Больше или равно                                                                     |
| <                          | Меньше                                                                               |
| <=                         | Меньше или равно                                                                     |
| ==                         | Равно (проверяет, равны ли числа)                                                    |
| !=                         | Не равно (проверяет, не равны ли значения)                                           |
| not                        | Не (отрицание)                                                                       |
| and                        | И (конъюнкция)                                                                       |
| or                         | Или (дизъюнкция)                                                                     |


### Сравнение в Python
В Python мы можем выполнять следующие сравнения. Результатом
чего будет либо True, либо False
```py
a = 1 > 4
print(a) # False
# —------------------------------------
a = 1 < 4 and 5 > 2
print(a) # True
# —------------------------------------
a = 1 == 2
print(a) # False
# —------------------------------------
a = 1 != 2
print(a) # True
```

Можно сравнивать не только числовые значения, но и строки:
```py
a = 'qwe'
b = 'qwe'
print(a == b) # True
```
В Python можно использовать тройные и даже четверные
неравенства:
```py
a = 1 < 3 < 5 < 10
print (a) # True
```

### Управляющие конструкции: if, if-else

Пример оформления программного кода с операторами ветвления:
```py
if condition:
 # operator 1
 # operator 2
 # ...
 # operator n
else:
 # operator n + 1
 # operator n + 2
 # ...
 # operator n + m
 ```

 Ещё один вариант использования операторов else-if → в связке с elif
(else if)
Проверяем первое условие, если оно не выполняется, проверяем
второе и так далее. Как только будет найдено верное условие, все
остальные будут игнорироваться.
```py
if condition1:
 # operator
elif condition2:
 # operator
elif condition3:
 # operator
else:
 # operator
 ```

 Сложные условия создаются с помощью логических операторов, таких как: and, or, not
 ```py
if condition1 and condition2: # выполнится, когда оба условия окажутся верными
# operator
if condition3 or condition4: # выполнится, когда хотя бы одно из условий окажется верным
# operator
```

### Цикл While
Цикл позволяет выполнить блок кода, пока условие является верным.
while condition:
```py
# operator 1
# operator 2
  # ...
  # operator n
    n = 423
    summa = 0
    while n > 0:
          x = n % 10
          summa = summa + x
          n = n // 10
    print(summa) # 9
```

### Управляющие конструкции: while-else
```py
while condition:
 # operator 1
 # operator 2
# ...
# operator n
else:
# operator n + 1
# operator n + 2
# ...
# operator n + m
```
Блок else выполняется, когда основное тело цикла перестает работать самостоятельно. А
разве кто-то может прекратить работу цикла? Если мы вспомним C#, то да и это конструкция
break.

Внутри Python она также существует и используется точно также. Пример:
```py
i = 0
while i < 5:
 if i == 3:
 break
 i = i + 1
else:
 print('Пожалуй')
 print('хватит )')
print(i)
```
После выполнения данного кода в консоль выведется только цифра 3, то что находится
внутри else будет игнорироваться, так как цикл завершился не самостоятельно.

Пример программного кода без использования break:
```py
n = 423
summa = 0
while n > 0:
x = n % 10
summa = summa + x
n = n // 10
else:
print('Пожалуй')
print('хватит )')
print(summa)
# Пожалуй
# хватит )
# 9
```

После того, как мы с Вами обговорили оператор break и цикл while, стоит рассказать почему
не стоит использовать break и как в этом случае нам поможет Булевский тип данных?
Давайте разбираться. break отличная конструкция, которую нельзя не использовать в
некоторых алгоритмах, но break не функциональный стиль программирования. В ООП нет
ничего, что предполагает break внутри метода-плохая идея, так как может произойти
путаница. На замену break отлично подходит метод флажка.

Задача
Пользователь вводит число, необходимо найти минимальный делитель данного числа
Решение:
```py
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
 ```
Данный алгоритм будет работать до тех пор, пока не найдется минимальный делитель
введенного числа. Когда будет найден первый делитель цикл остановит свою работу, так как
условие, которое находится внутри станет ложным(False)

### Цикл for, функция range()
В Python цикл for в основном используется для перебора значений
Пример использования цикла for:
```py
for i in enumeration:
    # operator 1
    # operator 2
    # ...
    # operator n
for i in 1, -2, 3, 14, 5:
    print(i)
# 1 -2 3 15 5
```
- Range выдает значения из диапазона с шагом 1.
- Если указано только одно число — от 0 до заданного числа.
- Если нужен другой шаг, третьим аргументоv можно задать приращение.
```py
r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20) # 100 80 60 40 20
r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
print(i)
# 100 80 60 40 20
```

Можно использовать цикл for() и со строками, так как у строк есть нумерация, такая же как и у массивов, начинается с 0:
```py
 for i in 'qwerty':
     print(i)
 # q
 # w
 # e
 # r
 # t
 # y
 ```

### Можно использовать вложенные циклы:
```py
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)
 ```
Программный код выведет 5 строк “******”. Сначала запускается внешний цикл с i(счетчик
цикла). После этого запускается внутренний цикл с j(счетчик цикла). После того как
внутренний цикл завершил свою работу, переменная line = “*****” и выводится на экран,
далее опять повторяется внешний цикл и так 5 раз.

### Немного о строках
Возникают ситуации, когда в некоторых задачах необходимо поработать со строкой,
которую ввел пользователь. Например: необходимо сделать все буквы маленькими, или
поменять все буквы “ё” на “е”.
```py
text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.lower()) # съешь ещё этих мягких французских булок
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок
```

### Срезы
- Мы представляем строку в виде массива символов. Значит мы можем обращаться к
элементам по индексам.
- Отрицательное число в индексе — счёт с конца строки
```py
 text = 'съешь ещё этих мягких французских булок'
 print(text[0]) # c
 print(text[1]) # ъ
 print(text[len(text)-1]) # к
 print(text[-5]) # б
 print(text[:]) # съешь ещё этих мягких французских булок
 print(text[:2]) # съ
 ```

- Мы представляем строку в виде массива символов. Значит мы можем обращаться к
элементам по индексам.
- Отрицательное число в индексе — счёт с конца строки
```py
 print(text[len(text)-2:]) # ок
 print(text[2:9]) # ешь ещё
 print(text[6:-18]) # ещё этих мягких
 print(text[0:len(text):6]) # сеикакл
 print(text[::6]) # сеикакл
 text = text[2:9] + text[-5] + text[:2] # ...
 ```

### Итоги
- Изучили историю создания языка программирования Python и
проанализировали востребованность на рынке
- Познакомились с функциями ввода и вывод данных
- Изучили операторы ветвления
- Изучили циклы внутри Python и проговорили отличия с цикла на C#