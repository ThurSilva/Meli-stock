from crypt import methods
from app.models.device import Device
from app.models.stock import Stock
from flask import Flask
from app.database import db

app = Flask(__name__)

db.connect()
db.create_tables([Stock, Device])
db.close()

if __name__ == "__main__":
    app.run()
