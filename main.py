import telebot
bot = telebot.TeleBot("1679105678:AAGVVKQJOmME-MBmZl3-uwU0aBUKbuUMZ64")
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
@bot.message_handler(content_types=["text"])# ДЕКОРАТОР
def handle_message(message):
    bot.send_message(message.from_user.id,'Чего желаете?')

bot.polling(none_stop=True, interval=0)

