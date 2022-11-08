# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби.
import math
import random
# file_1 = open('users.txt', 'r', encoding='utf8')
# users = file_1.read()
# users_parts = users.split('\n')
# file_1.close()
#
# file_2 = open('hobby.txt', 'r', encoding='utf8')
# hobby = file_2.read()
# hobby_parts = hobby.split('\n')
# file_2.close()
#
# users_hobby = dict(zip(users_parts, hobby_parts))
# for key, value in users_hobby.items():
#     print(key, '-', value)
#
# with open('users_hobby.txt', 'w', encoding='utf-8') as file_3:
#     for key, val in users_hobby.items():
#         file_3.write('{} - {}\n'.format(key, val))
# file_3.close()


#Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# number = int(input('Введите натуральное число: '))
# prost = []
# while number % 2 == 0:
#     prost.append(2)
#     number = number / 2
# for i in range(3, int(math.sqrt(number)+1), 2):
#     while number % i == 0:
#         prost.append(i)
#         number = number / i
# if number > 2:
#     prost.append(number)
# print(f'Простые множители введенного числа: {prost}')

# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# def rand_int_list():
#     """
#     Формирует список из  случайных целых чисел заданного размера и диапазона
#     """
#     number = int(input('Введите количество элементов списка: '))
#     value_min = int(input('Введите нижнюю границу диапазона значений элементов списка: '))
#     value_max = int(input('Введите верхнюю границу диапазона значений элементов списка: '))
#     num_list = []
#     for i in range(number):
#         num_list.append(random.randint(value_min, value_max))
#     return num_list
#
# random_list = rand_int_list()
# print(random_list)
# count_list = list(set(random_list))
#
# unic_list = []
#
#
# for j in range(len(count_list)):
#     count = 0
#     for i in range(len(random_list)):
#         if count_list[j] == random_list[i]:
#             count = count+1
#     if count == 1:
#         unic_list.append(count_list[j])
# print(f'Список неповторяющихся элементов случайного списка: {unic_list}')

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# number = int(input('Введите натуральную степень многочлена: '))
#
# num_list = []
# for i in range(number+1):
#     num_list.append(str(random.randint(0, 100)))
#
# x_list = []
# for i in range(number, 1, -1):
#     x_list.append(f'*x^{number} + ')
#     number = number-1
# x_list.append('*x +')
#
# polynom = []
# for i in range(len(x_list)):
#     polynom.append(num_list[i])
#     polynom.append(x_list[i])
# polynom.append(f'{num_list[len(num_list)-1]} = 0')
#
# print(''.join(polynom))
# with open('polynom.txt', 'w', encoding='utf-8') as file_1:
#     file_1.write(''.join(polynom))
# file_1.close()


# #Даны два файла, в каждом из которых находится запись многочлена.
# # Задача - сформировать файл, содержащий сумму многочленов.
# file_1 = open('polynom1.txt', 'r', encoding='utf-8')
# str1 = file_1.read()
# file_1.close()
# file_2 = open('polynom2.txt', 'r', encoding='utf-8')
# str2 = file_2.read()
# file_2.close()
# print(str1)
# print(str2)
# polynom1 = str1.replace(' ', '').replace('=0', '').replace('+x', '+1x').replace('-x', '-1x').replace('-', '+-')
# polynom1 = polynom1.replace('x', '|x').replace('+', '|')
#
# if polynom1[-1] == 'x':
#     polynom1 = polynom1 + '|0'
# if polynom1[-3] == 'x':
#     polynom1 = polynom1[:-3] + 'x^1' + polynom1[-2:]
# if polynom1[-4] == 'x':
#     polynom1 = polynom1[:-4] + 'x^1' + polynom1[-3:]
# polynom1 = polynom1 + '|x^0'
#
#
# polynom2 = str2.replace(' ', '').replace('=0', '').replace('+x', '+1x').replace('-x', '-1x').replace('-', '+-')
# polynom2 = polynom2.replace('x', '|x').replace('+', '|')
# if polynom2[-1] == 'x':
#     polynom2 = polynom2 + '|0'
# if polynom2[-3] == 'x':
#     polynom2 = polynom2[:-3] + 'x^1' + polynom2[-2:]
# if polynom2[-4] == 'x':
#     polynom2 = polynom2[:-4] + 'x^1' + polynom2[-3:]
# polynom2 = polynom2 + '|x^0'
#
#
#
# poly1_list = list(reversed(polynom1.split('|')))
# poly2_list = list(reversed(polynom2.split('|')))
#
#
# poly1_dict = {poly1_list[i]: poly1_list[i+1] for i in range(0, len(poly1_list), 2)}
# # print(poly1_dict)
# poly2_dict = {poly2_list[i]: poly2_list[i+1] for i in range(0, len(poly2_list), 2)}
# # print(poly2_dict)
#
#
# result = poly1_dict.copy()
# for i in poly2_dict.keys():
#     if i in result.keys():
#         result[i] = int(result[i])
#         result[i] += int(poly2_dict[i])
#     else:
#         result[i] = int(poly2_dict[i])
# # print(result, '\n')
# new_list = []
#
#
# result_poly_list = [f'{value}{key}' for key, value in result.items()]
# result_poly_list.reverse()
# result_poly = ' + '.join(result_poly_list)
# result_poly = result_poly.replace('+ -', '-').replace('1x', 'x').replace('x^0', '').replace('x^1', 'x')
# result_poly = result_poly + ' = 0'
# print('Сумма многочленов равна:')
# print(result_poly)
# with open('polynom_result.txt', 'w') as file_4:
#     file_4.write(result_poly)


















# Переделка последней задачи с функциями- НЕ закончена
# def polynom_dict(str_poly):
#     """
#     Считывается многочлен вида fx^n +...cx^2 + dx + a =0 из файла
#     и приводится к словарю вида {x^0: a, x^1, b: x^2: c ...x^n: f},
#     где x^n- многочлен степени n, f- коэффициент многочлена
#     """
#     print(str_poly)
#     polynom = str_poly.replace(' ', '').replace('=0', '').replace('+x', '+1x').replace('-x', '-1x')
#     polynom = polynom.replace('-', '+-').replace('x', '|x').replace('+', '|')
#     if polynom[-1] == 'x':
#         polynom = polynom + '|0'
#     if polynom[-3] == 'x':
#         polynom = polynom[:-3] + 'x^1' + polynom[-2:]
#     if polynom[-4] == 'x':
#         polynom = polynom[:-4] + 'x^1' + polynom[-3:]
#     polynom = polynom + '|x^0'
#     polynom = polynom.replace('x', '|x').replace('+', '|')
#     poly_list = list(reversed(polynom.split('|')))
#     poly_dict = {poly_list[i]: poly_list[i+1] for i in range(0, len(poly_list), 2)}
#     print(poly_dict)
#     return(poly_dict)
#
#
#
# file_1 = open('polynom1.txt', 'r', encoding='utf-8')
# str1 = file_1.read()
# file_1.close()
# poly1_dict = polynom_dict(str1)
# print(poly1_dict)
#
