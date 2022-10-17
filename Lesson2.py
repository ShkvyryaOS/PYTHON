# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
import random

#
# number = input('Введите вещественное число: ')
# chars = '.,-'
# resultstr = number.translate(str.maketrans('', '', chars))
# numlist=list(map(int, resultstr))
#
# sumnum = 0
# for i in numlist:
#     sumnum += i
# print(f'Сумма цифр в введенном числе равна: {sumnum}')

# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# number = int(input('Введите число N: '))
# fact = 1
# reslist = [fact]
#
# for i in range(2, number+1):
#     fact *= i
#     reslist.append(fact)
# print(f'Произведение чисел от 1 до N: {reslist}')

# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

#
# number = int(input('Введите число N: '))
# position = 1
# reslist = [position]
# sum = 1
# for i in range(1, number):
#     value = round((1+1/i) ** i, 2)
#     reslist.append(value)
#     sum += value
#
# print(f'Список  из N чисел последовательности (1+1/n)^n: {reslist}')
# print(f'Сумма элементов списка последовательности равна: {sum}')

#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на введенных пользователем позициях.
# number = int(input('Введите число N: '))
# numlist = []
# for i in range(number):
#     numlist.append(random.randint(-number, number))
# print(f'Сформирован список из {number} элементов, заполненных числами из промежутка [-{number}, {number}]: {numlist}')
# print('Введите позиции элементов списка, произведение которых необходимо найти')
# position1 = int(input('Введите позицию первого элемента списка: '))
# position2 = int(input('Введите позицию второго элемента списка: '))
# if position1 < number and position2 < number:
#     value1 = numlist[position1]
#     value2 = numlist[position2]
#     print(f'Произведение элементов с позициями [{position1}], [{position2}] равно {value1*value2}')
# else:
#     print('Одна или обе введеные позиции находятся за пределами списка')

# Реализуйте алгоритм перемешивания списка
# решение без сохранения исходного списка
# number = int(input('Введите количество элементов списка N: '))
# userList = []
# for i in range(0, number):
#     value = input(f'Введите значение элемента на позиции [{i}]: ')
#     userList.append(value)
# print(f'Введеный пользователем список: {userList}')
# random.shuffle(userList)
# print(f'Список пользователя после перемешивания: {userList}')

# С сохранением исходного списка
# number = int(input('Введите количество элементов списка N: '))
# userList = []
# for i in range(0, number):
#     value = input(f'Введите значение элемента на позиции [{i}]: ')
#     userList.append(value)
# print(f'Введеный пользователем список: {userList}')
# result = random.sample(userList, len(userList))
# print(f'Список пользователя после перемешивания: {result}')