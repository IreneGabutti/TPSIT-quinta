from flask import Flask, render_template, redirect, url_for, request
import sqlite3
import re

app = Flask(__name__) #variabile, quando avvio il programma vale none
def check_password(hashed_password, user_password):
    return hashed_password == user_password

conn = sqlite3.connect("accessi.db")

@app.route('/', methods=['GET', 'POST'])
def login():
    #error = None
    if request.method == 'POST'and "username" in request.form and "password" in request.form:
        username = request.form['username']
        password = request.form['password']


        conn = sqlite3.connect("accessi.db")
        cur = conn.cursor()

        cur.execute('SELECT * FROM PersoneAutorizzate WHERE Username = %s AND Password = %s', (username, password))

        account = cur.fetchone()

        if account:
            session['loggin'] = True
            session['username'] = account['Username']
            session["password"] = account['Password']
            return 'il login ha avuto successo'

        else: 
            return render_template('login.html', error=error)
if __name__ == "__main__":
    app.run(debug=True, use_debugger=False)



