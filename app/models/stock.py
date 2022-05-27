from peewee import *
from app.database import BaseModel

class Stock (BaseModel):
    name = CharField(unique=True)
    address = IntegerField()
    number = CharField()
    description = CharField()
    active = BooleanField()
