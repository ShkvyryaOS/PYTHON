from datetime import datetime as dt
def get_log(action, data):
    dtime = dt.now()
    with open('log.txt', 'a', encoding = 'utf-8') as file:
        if action == 1:
            file.write(f'{dtime}; Поиск пользователем абонента с id : {data} \n')
        if action == 2:
            file.write(f'{dtime}; Поиск пользователем абонента с фамилией : {data} \n')
        if action == 3:
            file.write(f'{dtime}; Добавление пользователем абонента с данными : {data} \n')
        if action == 4:
            file.write(f'{dtime}; Удаление пользователем абонента с id : {data} \n')
        if action == 5:
            file.write(f'{dtime}; Изменение данных абонента c id: {data} \n')
