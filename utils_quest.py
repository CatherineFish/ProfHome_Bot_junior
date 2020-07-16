import config
import views_quest
import telebot
from random import shuffle


bot = telebot.TeleBot(config.token)
all_Points = None
cur_score = 0
flag_log_in = False




def generate_markup(right_answer, wrong_answers, points):
    markup = telebot.types.InlineKeyboardMarkup()
    all_answers = '{},{}'.format(right_answer, wrong_answers)
    list_items = []
    for item in all_answers.split(','):
        list_items.append(item)
    shuffle(list_items)
    for item in list_items:
        if item == right_answer:
            markup.add(telebot.types.InlineKeyboardButton(text=right_answer, callback_data=points))
        else:
            markup.add(telebot.types.InlineKeyboardButton(text=item, callback_data=-1))
    return markup



@bot.message_handler(commands=['signup'])
def signup(message):
    views_quest.user_registration(message)
    bot.send_message(message.chat.id, 'Вы зарегистрированы')

@bot.message_handler(commands=['game'])
def game(message):
    global all_Points
    all_Points = views_quest.get_points()
    for point in all_Points:
        markup = generate_markup(point.right_answer, point.wrong_answer, point.score)
        bot.send_message(message.chat.id,point.question, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    answer = ''
    if call.data != '-1':
        answer = 'Верно!'
        global cur_score
        cur_score += int(call.data)
    else:
         answer = 'Неправильно!'
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

@bot.message_handler()
def score(message):
    global cur_score
    bot.send_message(message.chat.id, views_quest.new_user.username, cur_score)
    views_quest.update(cur_score)
    global flag_log_in
    flag_log_in = False

if __name__ == '__main__':
    bot.infinity_polling()
