import random
import telebot
bot = telebot.TeleBot('5335946242:AAHmK64UfoUE-hV_2NknncTvYIwNyoAHckQ')
from telebot import types
from datetime import datetime

# Cообщения на выход
first = ["Не бывает плохой погоды, значит сегодня она тоже хорошая.","Прекрасная, как и всегда!"]
second = ["Свинья не может посмотреть на небо.","При чихании все функции организма останавливаются.","Виноград взрывается в микроволновой печи.","Змея может спать в течении трёх лет."]
third = ["Глазунья", "Каша", "Творог", "Бутерброд", "Сладкая выпечка"]

fir = ["Сегодня прекрасный день чтобы сходить погулять.","Нет ничего невозможного, сегодня ты это поймешь!","Будьте осторожны, возможно сегодня не лучший день чтобы работать","Сегодня прекрасный день для уборки!"]
sec = ["Но даже в этом случае не забывате про","Даже если сегодня слишком много дел, не забывайте про"]
second_add = ["своих близких.","решение рабочих вопросов.","себя и своё здоровье.","отдых и развлечения."]
thi = ["Знайте, что сегодня все получится.","Помните, что нет ничего, с чем бы вы не справились."]

# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "/start":

        bot.send_message(message.from_user.id, f'''Привет, {str(message.chat.first_name)}! ''')

        # кнопки
        keyboard = types.InlineKeyboardMarkup()
        key_zavtrac = types.InlineKeyboardButton(text='Чем сегодня позавтракать', callback_data='zavtrac')
        keyboard.add(key_zavtrac)
        key_pogoda = types.InlineKeyboardButton(text='Погода', callback_data='pogoda')
        keyboard.add(key_pogoda)
        key_fact = types.InlineKeyboardButton(text='Интересный факт', callback_data='fact')
        keyboard.add(key_fact)
        key_cot = types.InlineKeyboardButton(text='Покажи кота', callback_data='cot')
        keyboard.add(key_cot)

    # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, "Что ты хочешь узнать? Выбери из списка! Если хочешь узнать свой гороскоп напиши Гороскоп.", reply_markup=keyboard)

    elif message.text == "Гороскоп":
        keyboard = types.InlineKeyboardMarkup()

        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(key_telec)

        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        keyboard.add(key_oven)

        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(key_bliznecy)

        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)

        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)

        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(key_deva)

        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(key_vesy)

        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(key_scorpion)

        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)

        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)

        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)

        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(key_ryby)

        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Попробуй заново и напиши /start.")

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)


def callback_worker(call):
    if call.data == "cot":
        bot.send_photo(call.message.chat.id, open('cot.jpg', 'rb'))
        
    if call.data == "pogoda":
        msg = random.choice(first) + ' '
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

    if call.data == "zavtrac":
        ut = random.choice(third) + ' '
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, ut)

    if call.data == "fact":
        il = random.choice(second) + ' '
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, il)

    if call.data == "zodiac":
        msg = random.choice(fir) + ' ' + random.choice(sec) + ' ' + random.choice(second_add) + ' ' + random.choice(thi)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)