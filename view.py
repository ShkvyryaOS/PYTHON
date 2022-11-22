from fractions import Fraction

def number_type():
    print('Над какими числами производим действие: рациональными (R) или комплексными (С)?')
    s = str(input('Введите R или С: ')).lower().replace(' ', '')
    if s == 'c' or s == 'r':
        return s
    else:
        print('Введено неверное значение')

def get_value_fraction():
    print('Рациональное число представляется в виде n/m')
    print('Введите значения n, m: ')
    number1 = int(input('n = '))
    number2 = int(input('m = '))
    number = Fraction(number1, number2)
    return number
def get_value_complex():
    print('Комплексное число представляется в виде x= a+ bi')
    print('Введите значения a, b комплексного числа: ')
    number1 = int(input('a = '))
    number2 = int(input('b = '))
    number = complex(number1, number2)
    return number
def get_type_act():
    s = str(input('Какое действие с числами необходимо произвести? (+, -, *, /) ')).replace(' ', '')
    return s
def return_result(oper, x, y, res):
    return (f'Результат операции {oper} над введенными пользователем числами {x}, {y}  равен {res}')





