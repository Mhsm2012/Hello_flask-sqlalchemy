from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
# import flask library
# define flask as application through using flask (__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgress@localhost:5432/example'
db = SQLAlchemy(app)



@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
   
   app.run(host="127.0.0.1", port = 1023)
