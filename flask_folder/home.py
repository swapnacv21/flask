from flask import Flask

app=Flask(__name__)

@app.route('/')

def fun1():
    return "Hello,Welcome"

app.run()