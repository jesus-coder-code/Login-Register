import mongoengine as db

class Users(db.Document):
    email = db.StringField(max_length=100, required=True)
    user = db.StringField(max_length=100, required=True)
    password = db.StringField(max_length=255, required=True)
    date = db.DateTimeField()

#modelo de la base de datos;