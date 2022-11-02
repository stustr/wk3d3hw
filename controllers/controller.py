from flask import render_template
from app import app
from models.orders import *


@app.route("/orders")
def index():
    return render_template("index.html", orders=orders)


@app.route("/orders/<orderid>")
def order(orderid):
    return render_template("order.html", order=orders[int(orderid)])
