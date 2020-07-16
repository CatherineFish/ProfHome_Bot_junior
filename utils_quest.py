import config
import views_quest
import telebot
from random import shuffle

bot = telebot.TeleBot(config.token)
all_Points = None
flag_log_in = False


def generate_markup(right_answer, wrong_answers, num):
    markup = telebot.types.InlineKeyboardMarkup()
    all_answers = '{},{}'.format(right_answer, wrong_answers)
    list_items = []
    for item in all_answers.split(','):
        list_items.append(item)
    shuffle(list_items)
    for item in list_items:
        if item == right_answer:
            markup.add(telebot.types.InlineKeyboardButton(text=right_answer, callback_data=(num * 10 + 1)))
        else:
            markup.add(telebot.types.InlineKeyboardButton(text=item, callback_data=(num * 10)))
    return markup


@bot.message_handler(commands=['signup'])
def signup(message):
    views_quest.user_registration(message)
    bot.send_message(message.chat.id, 'Вы зарегистрированы!')
    global flag_log_in
    flag_log_in = True


@bot.message_handler(commands=['game'])
def game(message):
    global flag_log_in
    if not flag_log_in:
        bot.send_message(message.chat.id, "Введите команду /signup, чтобы зарегистрироваться")
    else:
        global all_Points
        all_Points = views_quest.get_points()
        markup = generate_markup(all_Points[0].right_answer, all_Points[0].wrong_answer, 1)
        bot.send_message(message.chat.id, all_Points[0].question, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    num_q = int(call.data) // 10
    answer = ''
    if (int(call.data) % 10):
        answer = 'Верно!'
        views_quest.new_user.score += all_Points[num_q - 1].score
    else:
        answer = 'Неправильно!'
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    if num_q < 4:
        markup = generate_markup(all_Points[num_q].right_answer, all_Points[num_q].wrong_answer, num_q + 1)
        bot.send_message(call.message.chat.id, all_Points[num_q].question, reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, views_quest.new_user.username + ' ' + str(views_quest.new_user.score))
        views_quest.update()
        global flag_log_in
        flag_log_in = False


if __name__ == '__main__':
    bot.infinity_polling()

