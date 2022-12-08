
from telegram.ext import CallbackContext
from telegram import Update
import datetime
from requests import get
from configue import openweather_token
from pprint import pprint
from logger import log
def start_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Привет {update.effective_user.first_name}! Напиши мне название города на английском языке '
                              f' и я расскажу о погоде в нем! (в формате /city moscow)')

def get_weather(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    place = msg.replace('/city', '')
    print(place)
    smile_code = {
        'Clear': 'Ясно\U00002600',
        'Clouds': 'Облачно\U00002601',
        'Rain': 'Дождь\U00002614',
        'Drizzle': 'Дождь\U00002614',
        'Thunderstorm': 'Гроза\U000026A1',
        'Snow': 'Снег\U0001F328',
        'Mist': 'Туман\U0001F32B'
    }
    try:
        r = get(f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={openweather_token}&units=metric')
        data = r.json()
        pprint(data)
        city = data['name']
        cur_temp = data['main']['temp']
        cur_humid = data['main']['humidity']
        cur_pres = data['main']['pressure']
        cur_wind = data['wind']['speed']
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        cur_cloud = data['clouds']['all']
        cur_rainfall = data['weather'][0]['main']
        if cur_rainfall in smile_code:
            wd = smile_code[cur_rainfall]
        else:
            wd = "Лучше один раз увидеть своими глазами, чем 100 раз прочитать"

        update.message.reply_text(f'Погода в городе: {city}\n'
              f'Температура: {cur_temp} \U00002103\n'
              f'{wd} \n'
              f'Облачность: {cur_cloud} %\n'
              f'Влажность воздуха: {cur_humid} %\n'
              f'Давление: {cur_pres} мм.рт.ст.\n'
              f'Скорость ветра: {cur_wind} м/с\n'

              f'Время восхода: {sunrise_time}\n'
              f'Время заката: {sunset_time}\n')
    except:
        update.message.reply_text('Проверь название города')






if __name__ == '__main__':
   print('ok')