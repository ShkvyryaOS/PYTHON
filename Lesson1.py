# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

# num = int(input('Input a day of week for checking'))
# if num == 6 or num == 7:
#     print(f'The {num} day of week is a weekend')
# else:
#     print(f'The {num} day of week is NOT a weekend')
# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
# x = int(input('Enter the value of the predicate X (0 / 1): '))
# y = int(input('Enter the value of the predicate Y (0 / 1): '))
# z = int(input('Enter the value of the predicate Y (0 / 1): '))
# if not (x or y or z) == (not x and not y and not z):
#     print(f'The statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  (for values X={x}, Y={y}, Z={z}) is TRUE')
# else:
#     print(f'The statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  (for values X={x}, Y={y}, Z={z}) is FALSE')

#  Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).
# x = int(input('Input X coordinate: '))
# y = int(input('Input Y coordinate: '))
# if x > 0 and y > 0:
#     print(f'Point with coordinates ({x},{y}) is in 1 quarter')
# elif x < 0 and y > 0:
#     print(f'Point with coordinates ({x},{y}) is in 2 quarter')
# elif x < 0 and y < 0:
#     print(f'Point with coordinates ({x},{y}) is in 3 quarter')
# elif x > 0 and y < 0:
#     print(f'Point with coordinates ({x},{y}) is in 4 quarter')
# elif x == 0:
#     print(f'Point with coordinates ({x},{y}) is located on the coordinate axis 0Y')
# elif y == 0:
#     print(f'Point with coordinates ({x},{y}) is located on the coordinate axis 0X')
# elif x == 0 and y == 0:
#     print(f'Point with coordinates ({x},{y}) is at the intersection of the coordinate axis 0X, 0Y')
#
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
#
# quarter = int(input('Input number of quarter: '))
# if quarter == 1:
#     print(f'In {quarter} quarter coordinates x and y are positive')
# elif quarter == 2:
#     print(f'In {quarter} quarter coordinate x is negative, coordinate y is positive')
# elif quarter == 3:
#     print(f'In {quarter} quarter coordinates x and y are negative')
# elif quarter == 4:
#     print(f'In {quarter} quarter coordinate x is positive, coordinate y is negative')
#
#g
# Напишите программу, которая принимает на вход координаты двух точек
# # и находит расстояние между ними в 2D пространстве.
# xA = int(input('Input coordinate point A: xA= '))
# yA = int(input('Input coordinate point A: yA= '))
# xB = int(input('Input coordinate point A: xB= '))
# yB = int(input('Input coordinate point A: yB= '))
# distance = round(((xB-xA) ** 2+(yB-yA) ** 2) ** 0.5, 2)
# print(f'Distance between point A({xA},{yA}) and point B({xB},{yB}) is {distance}')