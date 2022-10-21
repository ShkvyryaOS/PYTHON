import random
import math


def rand_int_list():
    """
    Формирует список из  случайных целых чисел заданного размера и диапазона
    """
    number = int(input('Введите количество элементов списка: '))
    value_min = int(input('Введите нижнюю границу диапазона значений элементов списка: '))
    value_max = int(input('Введите верхнюю границу диапазона значений элементов списка: '))
    num_list = []
    for i in range(number):
        num_list.append(random.randint(value_min, value_max))
    return num_list


def rand_float_list():
    """
    Формирует список из  случайных вещественных чисел заданного размера и диапазона
    """
    number = int(input('Введите количество элементов списка: '))
    value_min = int(input('Введите нижнюю границу диапазона значений элементов списка: '))
    value_max = int(input('Введите верхнюю границу диапазона значений элементов списка: '))
    num_list = []
    for i in range(number):
        num_list.append(random.uniform(value_min, value_max))
    num_list = [round(i, 2) for i in num_list]
    return num_list


# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# rand_list = rand_int_list()
# print(f'Сформирован список из {len(rand_list)}, заполненный случайными числами: {rand_list}')
# sumNums = 0
# for i in range(1, len(rand_list), 2):
#     sumNums += rand_list[i]
# print(f'Сумма элементов  списка, стоящих на нечетной позиции, равна: {sumNums}')

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# rand_list = rand_int_list()
# print(rand_list)
# multiplication = 0
# result_list = []
# for i in range(len(rand_list)//2):
#     multiplication = rand_list[i] * rand_list[len(rand_list)-i-1]
#     result_list.append(multiplication)
# print(f'Произведение пар элементов  списка,  равно {result_list}')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

#
# rand_list = rand_float_list()
# print(rand_list)
# new_list = []
# for i in range(len(rand_list)):
#     new_list.append(math.floor((rand_list[i]*100) % 100))
# maxVal = max(new_list)
# minVal = min(new_list)
# result = (maxVal - minVal)/100
# print(f'Разница между максимальным и минимальным значением дробной части элементов равна {result}')

# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# number10 = int(input('Введите десятичное число: '))
# number2_list = []
# while number10/2 != 0:
#      temp = number10 % 2
#      number10 = number10 // 2
#      number2_list.append(temp)
# number2_list.reverse()
# print(f'Введеное десятичное число, представленное в двоичном коде: ')
# print("".join(map(str, number2_list)))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# number = int(input('Введите целое число n>=2 для вывода последовательности Фибоначи: '))
# fib_list = [0, 1]
# for i in range(2, number + 1):
#     val = fib_list[i - 2] + fib_list[i - 1]
#     fib_list.append(val)
# negafib_list = [1]
# for i in range(2, number + 1):
#     val = -1 ** (i + 1) * fib_list[i]
#     negafib_list.append(val)
# negafib_list.reverse()
# result_fib = negafib_list + fib_list
# print(result_fib)

