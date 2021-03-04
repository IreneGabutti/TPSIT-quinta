from flask import Flask, render_template, redirect, url_for, request
import sqlite3 as sql
import re

app = Flask(__name__) #variabile, quando avvio il programma vale none


def insertUser(username,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users


@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method=='POST':
   		username = request.form['username']
   		password = request.form['password']
   		dbHandler.insertUser(username, password)
   		users = dbHandler.retrieveUsers()
		return render_template('index.html')
    else:
   		return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')





