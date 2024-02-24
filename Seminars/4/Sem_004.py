
# number_row = '+71234567890 +71234567854 +61234576890 +52134567890 \
# +21235777890 +21234567110 +71232267890'
# number_list = list(number_row.split())
# number_dict = dict()

# for i in number_list:
#     if i[:2] in number_dict:
#         number_dict[i[:2]].append(i)
# else:
#     number_dict[i[:2]] = [i]

# print(*sorted(number_dict.items())) 


# ---------------------------
'''
Задача №25. 
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split()
'''
# input_str = "a a a b c a a d c d d"
# count_dict = {}
# output_list = []

# for char in input_str.split():
#     if char in count_dict:
#         count_dict[char] += 1
#         output_list.append(f"{char}_{count_dict[char] - 1}")
#     else:
#         count_dict[char] = 1
#         output_list.append(char)

# output_str = ' '.join(output_list)
# print(output_str)



# # ---------------------------
'''
Задача №27
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов или символами конца строки.Определите,
сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore;The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore,I'm sure that the shells are sea
shore shells.
'''

number_row = "She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."
number_list = list(number_row.lower().replace("."," ").replace("'"," ").split())
print(number_list)
print(set(number_list))
print(len(set(number_list)))



