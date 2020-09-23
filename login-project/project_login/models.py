from project_login import db, loginmanger 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


                 
@loginmanger.user_loader
def load_user(userid):
    return User.query.get(userid)


class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, index=True)
    username = db.Column(db.String(20), unique=True, index=True)
    hash_passwrd = db.Column(db.String(200))


    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.hash_passwrd = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.hash_passwrd, password)






