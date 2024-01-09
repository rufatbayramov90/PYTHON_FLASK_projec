from flask import Flask
import time
import random
app = Flask(__name__)


@app.route('/')
def hello_world():
    return ' Hello, World'

@app.route('/bye')
def say_bye():
    return 'Bye'

@app.route('/<name>/<int:number>')
def greet(name,number):
    return f"Hello {name}, are you {number} "


if __name__=="__main__":
    app.run(debug=True)



