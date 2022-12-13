from flask import Flask 
# import flask library
# define flask as application through using flask (__name__)
app = Flask(__name__)



@app.route('/')
def index():
    return f'hello world '
