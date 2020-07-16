import datetime

from peewee import *

DATABASE = 'data.db'

database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    username = CharField()
    join_date = DateTimeField()
    score = IntegerField()

class Point(BaseModel):
    score = IntegerField()
    question = TextField()
    wrong_answer = TextField()
    right_answer = TextField()

