from flask import *

app = Flask(__name__)
app.config["DEBUG"] = True

books=[
    {
        'id':0,
        'title': 'Il_nome_della_rosa',
        'author': 'Umberto Eco'
    },
    {
        'id':1,
        'title': 'Il_problema_dei_tre_corpi',
        'author': 'Liu Cixin'
    },
    {
        'id':2,
        'title': 'After',
        'author': 'Anna Tood'
    }
]

@app.route('/',methods=['GET'])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di Web API</p>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods =['GET'])
def api_id():
    print(request.args)
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error"
    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)
    
    return jsonify(results)

@app.route('/api/v1/resources/books', methods =['GET'])
def api_title():
    print(request.args)
    if 'title' in request.args:
        title = str(request.args['title'])
    else:
        return "Error"
    results = []
    for book in books:
        if book['title'] == title:
            results.append(book)
    
    return jsonify(results)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)