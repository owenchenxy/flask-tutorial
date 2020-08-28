#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    color = db.Column(db.String(80))
    price = db.Column(db.Float)
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def __repr__(self):
        return '<User %r>' % self.name

@app.before_first_request
def init_db():
    db.create_all()

@app.route('/list')
def list():
    products = Product.query.all()
    return render_template('list.html', **locals())

@app.route('/record', methods=["GET", "POST"])
def record():
    if request.method == 'GET':
        return render_template('record.html')
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            price = request.form.get('price')
            color = request.form.get('color')
            db.session.add(Product(name, color, price))
            db.session.commit()
            done = True
            print("Done")
        except Exception:
            done = False
        return render_template('record.html', done=done)

if __name__=='__main__':
	app.run(debug=True)