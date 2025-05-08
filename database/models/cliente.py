from peewee import Model, CharField, DateField
from database.database import db

class Cliente(Model):
  name = CharField()
  email = CharField()
  data_criacao = DateField()

  class Meta:
    database = db
  