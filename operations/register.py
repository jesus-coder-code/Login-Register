from flask import Flask, request, jsonify
from mongoengine import connect
import mongoengine as db
from datetime import datetime
from operations.models import *
from werkzeug.security import generate_password_hash

#conexion a la base de datos en la nube
DB_URI = 'mongodb+srv://hiq:hiq12345@cluster0.fy23q.mongodb.net/seshat?retryWrites=true&w=majority'
db.connect(host = DB_URI)

#recibir por parametros los datos ingresados;   
def reg(email, user, password, date):
    hash_password = generate_password_hash(password)
    data = Users(
        email=email,
        user=user,
        password=hash_password,
        date = date
    )
    #si estan los datos, entonces se ejecutará el metodo save()
    data.save()

    if data:
        return True
    else:
        return False
