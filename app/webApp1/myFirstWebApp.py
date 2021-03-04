from flask import Flask, render_template

app = Flask(__name__) #variabile, quando avvio il programma vale none

@app.route("/") #http://127.0.0.1:5000/
def index():
    return render_template("index.html")

@app.route("/pagina2/") #http://127.0.0.1:5000/pagina2/
def index2():
    return render_template("pagina2.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1") #mio computer

