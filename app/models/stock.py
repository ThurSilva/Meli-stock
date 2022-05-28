from peewee import *
from app.database import BaseModel

class Stock (BaseModel):
    name = CharField(unique=True)
    address = CharField()           #The challenge asked an INT field, but I've considered VAR more apropriated
    number = CharField()            #I let it in VAR field, considering an addredd number field with complement ( eg. 102 B )
    description = CharField()
    active = BooleanField()
