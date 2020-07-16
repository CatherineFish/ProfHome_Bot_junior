from telebot import types

dict_item = {'Пойдём покурим?': 'Курение убивает',
             'Куда положить молоко?':'В холодильник',
             'Как принимать матпомощь?':'Смотри в группе профкома',
             'Кого кикать?':'Всех!'}

def generate_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in dict_item:
        markup.add(item)
    return markup