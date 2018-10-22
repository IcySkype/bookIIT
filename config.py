from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testfile'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#edit this as postgresql://user:pass@host/bookIIT
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/bookIIT'
app.static_folder = 'static'

db = SQLAlchemy(app)