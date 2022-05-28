from app.models.stock import Stock
from peewee import *
from app.database import BaseModel

class Device (BaseModel):
    name = CharField()
    quantity = IntegerField()
    active = BooleanField()
    description = CharField()
    stock = ForeignKeyField(Stock, backref='stock')
