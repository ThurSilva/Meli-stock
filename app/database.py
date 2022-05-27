from peewee import MySQLDatabase, Model

db = MySQLDatabase(host='localhost', port=3306, password='1234', user='root', database='meli')

class BaseModel (Model):
    class Meta:
        database = db
