#!flask/bin/python
from flask import Flask
from ml import tes

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/tes')
def coba():
    return tes()

if __name__ == '__main__':
    app.run(debug=True)
