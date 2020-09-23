import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


loginmanger = LoginManager()

app = Flask(__name__)
baseurl = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'ABCVDFSF'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(baseurl, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
loginmanger.init_app(app)
loginmanger.login_view ='login'
