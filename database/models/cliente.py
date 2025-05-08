import datetime
from peewee import Model, CharField, DateTimeField
from database.database import db

class Cliente(Model):
  name = CharField()
  email = CharField()
  data_registro = DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = db
  