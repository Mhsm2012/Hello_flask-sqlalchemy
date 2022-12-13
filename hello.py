from flask import Flask 
# import flask library
# define flask as application through using flask (__name__)
app = Flask(__name__)



@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
   
   app.run(host="127.0.0.1", port = 1023)
