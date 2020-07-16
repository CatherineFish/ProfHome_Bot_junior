import config
import telebot
import utils_VadimBot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['enter'])
def enter(message):
    markup = utils_VadimBot.generate_markup()
    bot.send_message(message.chat.id,'У тебя что-то срочное?', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def check_answer(message):
    answer = utils_VadimBot.dict_item.get(message.text)
    if answer:
        bot.send_message(message.chat.id, answer)
    else:
        bot.send_message(message.chat.id, 'Не знаю')


if __name__ == '__main__':
     bot.infinity_polling()