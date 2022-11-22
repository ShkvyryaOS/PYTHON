from actions import init_fraction, init_comlex, sum, subtr, mult, division
from view import get_value_complex, get_value_fraction, number_type, get_type_act, return_result
from logger import get_log

def button_click():
    type_num = number_type()
    if type_num == 'r':
        value_a = get_value_fraction()
        value_b = get_value_fraction()
        init_fraction(value_a, value_b)
    if type_num == 'c':
        value_a = get_value_complex()
        value_b = get_value_complex()
        init_comlex(value_a, value_b)
    type_act = get_type_act()
    if type_act == '+':
        result = sum()
    if type_act == '-':
        result = subtr()
    if type_act == '*':
        result = mult()
    if type_act == '/':
        result = division()
    print(return_result(type_act, value_a, value_b, result))
    get_log(value_a, value_b, type_act, result)