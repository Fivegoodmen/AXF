from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()
class user(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30),unique=True)