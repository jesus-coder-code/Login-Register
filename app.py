from flask import Flask, request, jsonify
from datetime import datetime
from operations.register import reg
from operations.Validations.validate import *

app = Flask(__name__)
@app.route('/users', methods=['POST'])
def register():
    #capturando los datos ingresados
    email = request.json['email']
    user = request.json['user']
    password = request.json['password']
    date = datetime.now()
    
    try:
        if email and user and password:
            #si se detectan los campos llenos, se procede a lo siguiente...
            if (not verifyEmail(email)):
                #comprobar que el email sea valido
                return jsonify({'message':'email is not valid'})
            if validateEmail(email):
                #retornando si el email existe
                return jsonify({'message':'email already exists'})
            else:
                if validateUser(user):
                    #retornando si el usuario existe
                    return jsonify({'message':'user already exists'})
                else:
                    if (not validatePass(password)):
                        #en caso de que la contraseña no sea igual o mayor a 8 caracteres
                        return jsonify({'message':'the password must be greater than or equal to 8 character'})
                    else:
                        #si se cumplen las validaciones anteriores, se procede a registrar el usuario
                        if reg(email, user, password, date):
                            return jsonify({'message':'user was created successfully'})
                        else:
                            return False
        else:
            #en caso de que se detecte uno o todos los campos vacios
            return jsonify({'message':'please fill all the fields'})           
    except Exception as e:
        print(e)
        return jsonify({'message':'internal error'})            

if __name__ == '__main__':
    app.run(debug=True)
