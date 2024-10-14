import telebot
from telebot import types
import logging
import password

button_count = 0

bot = telebot.TeleBot(password.token)
logging.warning("Запущен бот")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global button_count
    if call.data  == "yes": #call.data = callback_data
        button_count += 1
        bot.send_message(call.message.chat.id, button_count)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    logging.warning("Получено сообщение: " + message.text)
    save_remind(message)


def save_remind(message):
    in_line_keyboard = types.InlineKeyboardMarkup()
    key = types.InlineKeyboardButton(text="Получена цитата: 0/1", callback_data="yes")
    in_line_keyboard.add(key)
    bot.send_message(message.from_user.id, "Получена цитата: " + message.text, reply_markup=in_line_keyboard)




bot.polling(non_stop=True, interval=0)
