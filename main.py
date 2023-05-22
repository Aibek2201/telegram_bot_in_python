import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Қабылдау бөлімі")
    item2 = types.KeyboardButton("Университет жайлы ақпарат")
    item3 = types.KeyboardButton("Білім беру бағдарламалары")
    item4 = types.KeyboardButton("Құжаттар тізімі")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Қош келдіңіз, {0.first_name}!\n Мен - <b>{1.first_name}</b>, чат-бот \n AUES университетіне қош келдіңіз".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Қабылдау бөлімі':
            bot.send_message(message.chat.id, 'Келесі ұялы телефонға хабарласыңыз')
            bot.send_message(message.chat.id, '8-747-585-22-01')
        elif message.text == 'Университет жайлы ақпарат':
            bot.send_message(message.chat.id, 'Бұл Гумарбек Даукеев атындағы университет')

        elif message.text == 'Құжаттар тізімі':
            bot.send_message(message.chat.id, 'Паспорт')
            bot.send_message(message.chat.id, 'Туу туралы куәлік')
            bot.send_message(message.chat.id, 'РНН')

        elif message.text == 'Білім беру бағдарламалары':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("IT", callback_data='good')
            item2 = types.InlineKeyboardButton("EEk", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Таңдау жаса', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Кешіріңіз қате')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Бұл өте күшті таңдау')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бұл вообще күшті таңдау')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ТЕСТ")

    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)

