def get_action():
    mode = int(input('Введите действие, которое Вы хотите совершить:\n'
                     '1- посмотреть абонента по id\n'
                     '2- посмотреть по фамилии\n'
                     '3- добавить нового абонента\n'
                     '4- удалить абонента\n'
                     '5- изменить данные абонента\n'))
    return mode
def get_value_mod_1():
    return int(input('Введите id: \n'))
def get_value_mod_2():
    return (input('Введите фамилию: \n')).lower().replace(' ', '')

def get_value_mod_3():
    fieldnames = ['id', 'first_name', 'second_name', 'last_name', 'number']
    dict_data = {}
    for el in fieldnames:
        dict_data[el] = input(f'Введите {el} :')
    # dict_data['id'] = int(dict_data['id'])
    return dict_data

def get_value_mode5():

    what_change = (input(   '1- Изменить фамилию\n'
                            '2- Изменить имя\n' 
                            '3- Изменить отчество\n' 
                            '4- Изменить телефон\n')).replace(' ', '')
    dict_2 = {}
    if what_change == '1':
        dict_2['last_name'] = input('Введите фамилию:')
    if what_change == '2':
        dict_2['first_name'] = input('Введите имя:')
    if what_change == '3':
        dict_2['second_name'] = (input('Введите отчество:'))
    if what_change == '4':
        dict_2['number'] = input('Введите телефон:')
    return dict_2
def rejection():
    return print('Абонента с такими данными не существует')
def delete_success():
    return print('Данный абонент удален из справочниика')
def change_success():
    return print('В справочник внесены требуемые изменения с запрашиваемым абонентом')

