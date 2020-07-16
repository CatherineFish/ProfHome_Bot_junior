import models_quest
import datetime
import database_init_quest

new_user = None


def create_tables():
    with models_quest.database:
        models_quest.database.create_tables([models_quest.User, models_quest.Point])
    database_init_quest.init()


def user_registration(message):
    global new_user
    new_user = models_quest.User.create(
        username=message.from_user.first_name,
        join_date=datetime.datetime.now(),
        score=0)
    global flag_log_in
    flag_log_in = True
    global USERNAME
    USERNAME = new_user.username


def get_points():
    return models_quest.Point.select()


def update(score):
    global new_user
    new_user.score = score
    new_user.save()
