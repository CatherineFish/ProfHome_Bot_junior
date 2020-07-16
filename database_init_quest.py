import models_quest


def init():
    point_1 = models_quest.Point(
        score=30,
        question='Какой российский мультфильм был удостоен «Оскара»?',
        wrong_answer='Простоквашино, Винни-Пух, Ну погоди!',
        right_answer='Старик и море')
    point_1.save()

    point_2 = models_quest.Point(
        score=10,
        question='Что в Российской империи было вещевым эквивалентом денег?',
        wrong_answer='Крупный рогатый скот, Табак, Женские серьги',
        right_answer='Шкуры пушных зверей')
    point_2.save()

    point_3 = models_quest.Point(
        score=20,
        question='У индейцев из немногочисленного североамериканского племени квакиутл есть традиция: беря деньги в '
                 'долг, они оставляют в залог...',
        wrong_answer='Душу, Скальп тещи, Амулет',
        right_answer='Имя')
    point_3.save()

    point_4 = models_quest.Point(
        score=35,
        question='Основой для «Сказки о рыбаке и рыбке Пушкина послужила сказка братьев Гримм «Рыбак и его жена». В '
                 'ней немецкая «коллега» нашей старухи превратилась в...',
        wrong_answer='Королеву, Директора рыбзавода, Командира отряда водолазов',
        right_answer='Папу Римского')
    point_4.save()

