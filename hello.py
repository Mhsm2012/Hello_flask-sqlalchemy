from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
# import flask library
# define flask as application through using flask (__name__)
app = Flask(__name__)
# configure link to database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/example'
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ =  'persons'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String ,nullable = False)

db.create_all()




@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
   
   app.run(host="127.0.0.1", port = 1023)
