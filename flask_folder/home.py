from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)

@app.route('/')
def fun1():
    return "Hello,Welcome"

@app.route('/fun2',methods=['POST','get'])
def fun2():
    if request.method=='POST':
        name = request.form['name']
        place = request.form['place']
        # print(name,place)
        con=sqlite3.connect("home.db")
        # con.execute('create table details(name text,place text)')
        con.execute('insert into details(name,place)values(?,?)',(name,place))
        con.commit()



    a=15
    return render_template('index.html',data=a)

app.run()