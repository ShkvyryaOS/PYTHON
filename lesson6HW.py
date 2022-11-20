


# ЗАДАЧИ ПЕРЕДЕЛАНЫ!
import random
import math
import map_zip_enumerate
def rand_int_list():
    """
    Формирует список из  случайных целых чисел заданного размера и диапазона
    """
    number = int(input('Введите количество элементов списка: '))
    value_min = int(input('Введите нижнюю границу диапазона значений элементов списка: '))
    value_max = int(input('Введите верхнюю границу диапазона значений элементов списка: '))
    num_list = [random.randrange(value_min, value_max) for i in range(number)]

    return num_list


def rand_float_list():
    """
    Формирует список из  случайных вещественных чисел заданного размера и диапазона
    """
    number = int(input('Введите количество элементов списка: '))
    value_min = int(input('Введите нижнюю границу диапазона значений элементов списка: '))
    value_max = int(input('Введите верхнюю границу диапазона значений элементов списка: '))

    num_list = [round(random.uniform(value_min, value_max), 2) for i in range(number)]


    return num_list
#

# # Задайте список из нескольких чисел. Напишите программу,
# # которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# rand_list = rand_int_list()
# print(f'Сформирован список из {len(rand_list)} элементов, заполненный случайными числами: {rand_list}')
# sumNums = sum(x for i, x in enumerate(rand_list) if i % 2 != 0)
# print(f'Сумма элементов  списка, стоящих на нечетной позиции, равна: {sumNums}')
#


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# rand_list = rand_int_list()
# print(rand_list)
# left_part = rand_list[:len(rand_list)//2]
# right_part = rand_list[len(rand_list): len(rand_list)//2-1: -1]
# result_list = list(map(lambda x, y: x*y, left_part, right_part))
# print(f'Произведение пар элементов  списка,  равно {result_list}')

# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

# number = int(input('Введите число N: '))
# reslist = [round((1+1/i) ** i, 2) for i in range(1, number)]
# print(f'Список  из N чисел последовательности (1+1/n)^n: {reslist}')
# print(f'Сумма элементов списка последовательности равна: {sum(reslist)}')




# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

# rand_list = rand_float_list()
# print(rand_list)
# new_list = [math.floor((rand_list[i]*100) % 100) for i in range(len(rand_list))]
# print('Разница между максимальным и минимальным значением дробной части элементов равна:')
# print((max(new_list)-min(new_list))/100)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
from itertools import zip_longest

number = int(input('Введите натуральную степень многочлена: '))
num_list = [str(random.randrange(0, 100)) for i in range(number+1)]
degree_list = list(map(str, [i for i in range(0, number+1)]))
degree_list.reverse()
x_list = ['*x^' for i in range(number+1)]
polynom = list(map(lambda x, y, z: x+y+z, num_list, x_list, degree_list))
polynom = [elem.replace('*x^0', ' = 0').replace('x^1', 'x') for elem in polynom]
print(' + '.join(polynom))
with open('polynom.txt', 'w', encoding='utf-8') as file_1:
    file_1.write(' + '.join(polynom))
















