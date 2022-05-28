from app.models.device import Device
from app.models.stock import Stock
from flask import Flask, request,  jsonify
from playhouse.shortcuts import model_to_dict
from app.database import db

app = Flask(__name__)

@app.route("/stock/add", methods=['POST'])
def cad_stock():
    body = request.get_json()
    db.connect()
    stock = Stock.insert(body).execute()
    db.close()
    return {"id": stock}

@app.route("/device/add", methods=['POST'])
def cad_device():
    body = request.get_json()
    db.connect()
    query = Stock.select().where(Stock.id == body["stock_id"]).execute()
    stocks = [model_to_dict(stock) for stock in query]

    query = Device.select().where((Device.name == body["name"]) & (Device.stock == body["stock_id"])).execute()
    devices = [model_to_dict(device) for device in query]

    if (len(stocks) > 0):
        if (len(devices) > 0):
            db.close()
            return "Device já cadastrado para esse stock!"
        else:
            device = Device.insert(body).execute()
            db.close()
            return {"id": device}   
    else:
        db.close()
        return "stock não existente!"

@app.route("/stock/update/<id>", methods=['PATCH'])
def upd_stock(id):
    body = request.get_json()
    db.connect()
    stock = Stock.update(body).where(Stock.id == id).execute()
    db.close()
    return {"id": stock}

@app.route("/device/update/<id>", methods=['PATCH'])
def upd_device(id):
    body = request.get_json()
    db.connect()
    device = Device.update(body).where(Device.id == id).execute()
    db.close()
    return {"id": device}

@app.route("/stock/desativar/<id>", methods=['DELETE'])
def dst_stock(id):
    db.connect()
    stock = Stock.update({Stock.active: 0}).where(Stock.id == (id)).execute()
    db.close()
    return {"<id>": stock}

@app.route("/device/desativar/<id>", methods=['DELETE'])
def dst_device(id):
    db.connect()
    device = Device.update({Device.active: 0}).where(Device.id == (id)).execute()
    db.close()
    return {"<id>": device}

@app.route("/stocks/lista")
def list_stocks():
    db.connect()
    stocks = Stock.select().execute()
    db.close()
    response = [model_to_dict(stock) for stock in stocks]
    return jsonify(response)

@app.route("/devices/lista")
def list_devices():
    db.connect()
    devices = Device.select().execute()
    db.close()
    response = [model_to_dict(device) for device in devices]
    return jsonify(response)

@app.route("/devicesInStock/lista")
def list_devicesInStock():
    body = request.get_json()
    db.connect()
    devices = Device.select().where(Device.stock == body["stock_id"]).execute()
    db.close()
    response = [model_to_dict(device) for device in devices]
    return jsonify(response)

db.connect()
db.create_tables([Stock, Device])
db.close()

if __name__ == "__main__":
    app.run()
