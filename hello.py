from flask import Flask
import time
import random
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World</h1>'\
            '<p>This is a paragraph </p>'\
            'img src="<div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="853" src="https://giphy.com/embed/paWQwjlM2mKKGa2vsR/video" width="480"></iframe></div>"'

@app.route('/bye')
def say_bye():
    return 'Bye'

@app.route('/<name>/<int:number>')
def greet(name,number):
    return f"Hello {name}, are you {number} "


if __name__=="__main__":
    app.run(debug=True)



