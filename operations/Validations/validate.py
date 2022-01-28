from operations.models import *
from flask import request, json
import re

#funcion de validacion de email;
def verifyEmail(email):
    expression = re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',email.lower());
    if(expression):
        return True;
    else:
        return False;

#verificando que el email ingresado no sea igual a ninguno en la base de datos
def validateEmail(email):
    if request.method == 'POST':
        data = Users.objects(email = request.json.get('email'))
        #ciclo para recorrer toda la coleccion en busca de un email igual
        for todo in data:
            #si el email es igual retorna true, sino false
            return True

#lo mismo que hace la funcion de validateEmail pero esta vez con el user
def validateUser(user):
    if request.method == 'POST':
        data = Users.objects(user = request.json.get('user'))
        for todo in data:
            return True

#verificar que la contraseña tenga un numero de caracteres igual o mayor a 8
def validatePass(password):
    len_pass = len(password)
    if len_pass >= 8:
        return True
    else:
        return False