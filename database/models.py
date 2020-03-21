from app import db

class User(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    public_user_id  = db.Column(db.String(64), unique=True)
    username        = db.Column(db.String(64))
    password        = db.Column(db.String(64))

class Example(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    public_user_id  = db.Column(db.String(64))
    text            = db.Column(db.String(64))