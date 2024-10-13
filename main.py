import telebot
import password

bot = telebot.TeleBot(password.token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет")

bot.polling(non_stop=True, interval=0)