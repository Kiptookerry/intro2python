from peewee import *
from os import path

#creating our first database

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection,"emobilis.db"))

#creating table inside db
class User(Model):
    name = CharField()
    phone = CharField()
    age = CharField()
    gender = CharField()
    studentcode = CharField()

    class Meta:
        database = db
User.create_table(fail_silently=True)