# import telebot
# import webbrowser
#
# bot = telebot.TeleBot('6527847733:AAGzoOmxZUtWE7nWrA5A2WZPc5ff_icRFFE')



# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types.web_app_info import WebAppInfo
# import json
# bot = Bot('6527847733:AAGoikroqhiln_zxiQKY6w2mNEyKKgFpbvY')
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     markup = types.ReplyKeyboardMarkup()
#     markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://sashaaasssss.github.io/new/')))
#     await message.answer("Привет мой друг", reply_markup=markup)
#
#
# @dp.message_handler(content_types=['web_app_data'])
# async def web_app(message: types.Message):
#     res = json.loads(message.web_app_data.data)
#     await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}')
#
# executor.start_polling(dp)








#другая библиотека

# from aiogram import Bot, Dispatcher, executor, types
#
# bot = Bot('6527847733:AAGzoOmxZUtWE7nWrA5A2WZPc5ff_icRFFE')
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands=['start'])#content_types=['photo']
# async def start(message: types.Message):
#     #await bot.send_message(message.chat.id, 'Hello')
#     #await message.answer('Hello')
#     await message.reply('Hello')#ответ на сообщение
#     #file = open('/some.png', 'rb')
#     #await message.answer_photo(file)
#
#
# @dp.message_handler(commands=['inline'])
# async def info(message: types.Message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Site', url='https://www.instagram.com/kurilenko.psy/'))
#     markup.add(types.InlineKeyboardButton('Hello', callback_data='bye'))
#     await message.reply('Hello', reply_markup=markup)
#
# @dp.callback_query_handler()
# async def callback(call):
#     await call.message.answer(call.data)
#
#
# @dp.message_handler(commands=['reply'])
# async def reply(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)#кнопки показываются только одоин раз
#     markup.add(types.KeyboardButton('Site'))
#     markup.add(types.KeyboardButton('Website'))
#     await message.answer('Hello', reply_markup=markup)
#
#
# executor.start_polling(dp)




























# конвертация валют



# from currency_converter import CurrencyConverter
# from telebot import types
#
# currency = CurrencyConverter()
# amount = 0
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, введите сумму')
#     bot.register_next_step_handler(message, summa)
#
# def summa(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'Неверный формат. Впишите сумму')
#         bot.register_next_step_handler(message, summa)
#         return
#
#     if amount > 0:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
#         btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
#         btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
#         btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
#         markup.add(btn1, btn2, btn3, btn4)
#         bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, 'Число должно быть больше 0')
#         bot.register_next_step_handler(message, summa)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data != 'else':
#         values = call.data.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}')
#         bot.register_next_step_handler(call.message, summa)
#     else:
#         bot.send_message(call.message.chat.id, 'Введите')
#         bot.register_next_step_handler(call.message, my_currency)
#
# def my_currency(message):
#     try:
#         values = message.text.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(message.chat.id, f'Получается: {round(res, 2)}')
#         bot.register_next_step_handler(message, summa)
#     except Exception:
#         bot.send_message(message.chat.id, f'Что то не так')
#         bot.register_next_step_handler(message, my_currency)













#бот для погоды

# import requests
# import json
# API = '26871ad7606b006c8e974ebd76e0269d'
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')
#
# @bot.message_handler(content_types=['text'])
# def get_weather(message):
#     city = message.text.strip().lower()
#     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
#     if res.status_code == 200:
#         data = json.loads(res.text)
#         temp = data["main"]["temp"]
#         bot.reply_to(message, f'Сейчас погода: {temp} градуса')
#
#         image = 'sun.jpg' if temp > 15.0 else 'sun2.png'
#         file = open('./' + image, 'rb')
#         bot.send_photo(message.chat.id, file)
#     else:
#         bot.reply_to(message, f'Город указан не верно')





























# база данных, регистрация


# import sqlite3
# name = None
# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('itproger.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегестрируем! Введите ваше имя')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Введите пароль')
#     bot.register_next_step_handler(message, user_pass)
#
# def user_pass(message):
#     password = message.text.strip()
#
#     conn = sqlite3.connect('itproger.sql')
#     cur = conn.cursor()
#
#     cur.execute('INSERT INTO users (name, pass) VALUES ("%s", "%s")' % (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data= 'users'))
#     bot.send_message(message.chat.id, 'Пользователь зарегестрирован!', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     conn = sqlite3.connect('itproger.sql')
#     cur = conn.cursor()
#
#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall()
#
#     info = ''
#     for el in users:
#         info += f'Имя: {el[1]}, пароль: {el[2]}\n'
#
#     cur.close()
#     conn.close()
#
#     bot.send_message(call.message.chat.id, info)














# #    кнопки в клавиатуре
# from telebot import types
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Перейти в инсту')
#     btn2 = types.KeyboardButton('Удалить фото')
#     btn3 = types.KeyboardButton('Изменить текст')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     file = open('./photo.jpg', 'rb')
#     bot.send_photo(message.chat.id, file,  reply_markup=markup)
#     #bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)
#
# def on_click(message):
#     if message.text == 'Перейти в инсту':
#         bot.send_message(message.chat.id, 'Insta is open')
#     elif message.text == 'Удалить фото':
#         bot.send_message(message.chat.id, 'Delete')
#
#
# #    кнопки не в клавиатуре
#
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Перейти в инсту', url='https://www.instagram.com/kurilenko.psy/')
#     btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
#





















#Ответ на сообщения




# @bot.message_handler(commands=['inst'])
# def site(message):
#     webbrowser.open('https://www.instagram.com/kurilenko.psy/')
#
#
# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
#
# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, 'Чем я могу помочь?')
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')



# bot.polling(none_stop=True)
