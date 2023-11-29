import telebot

bot = telebot.TeleBot('6847546443:AAFjSQxqrxyFFxlP4eHjoUPaDBDQe-RzKJQ')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет!\n Дорогой и уважаемый любитель малины и лета, рад видеть тебя в волшебном мире малины!')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id,
                     '*МАЛИНА ОБЫКНОВЕННАЯ*-листопадный полукустарник с многолетним корневищем, из которого развиваются двухгодичные надземные стебли высотой 1,5—2,5 м.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id,
                     '_Хочешь больше узнать про самую вкусную ягоду на свете?_ЭТО [ССЫЛКА](https://ru.wikipedia.org/wiki/Малина)',
                     parse_mode='Markdown')


bot.infinity_polling()