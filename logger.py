from datetime import datetime as dt
def get_log(x, y, operation, result):
    dtime = dt.now()
    with open('log.txt', 'a', encoding = 'utf-8') as file:
        file.write(f'{dtime}; Введенные пользователем числа: {x};{y}; операция:{operation}; результат: {result}\n')