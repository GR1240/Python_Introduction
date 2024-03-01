'''Задача 44: 
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''

import pandas as pd
import random

# Создаем список с данными
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)

# Создаем DataFrame
data = pd.DataFrame({'whoAmI': lst})

# Создаем DataFrame с нулями и добавляем столбцы для 'robot' и 'human'
one_hot = pd.DataFrame(0, index=data.index, columns=['robot', 'human'])

# Применяем one-hot кодировку
for index, row in data.iterrows():
    one_hot.loc[index, row['whoAmI']] = 1

# Объединяем исходный DataFrame и DataFrame с one-hot кодировкой
result = pd.concat([data, one_hot], axis=1)

# Выводим результат
result.head(10)