from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""
    quote = [quote for quote in quotes if quote['id'] == qid]
    return quote[0]

def _quote_exists(existing_quote):
    """Recommended helper"""
    quote_list = [quote['id'] for quote in quotes]
    if existing_quote in quote_list:
        return True


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return jsonify({'quotes':quotes})
    pass


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    quote = [quote for quote in quotes if quote['id'] == qid]
    if len(quote) == 0:
        abort(404)
    
    return jsonify({'quotes': quote[0]})
    pass


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    if not request.json or not 'quote' in request.json or not 'movie' in request.json:
        abort(400)
    quote = {
        'id': quotes[-1]['id'] + 1,
        'quote': request.json['quote'],
        'movie': request.json['movie'],
    }
    quotes.append(quote)
    return jsonify({'quote': quote}), 201
    pass


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    quote = [quote for quote in quotes if quote['id'] == qid]
    if len(quote) == 0:
        abort(404)
    if not request.json:
        abort(400)
        
    quote[0]['quote'] = request.json.get('quote', quote[0]['quote'])
    quote[0]['movie'] = request.json.get('movie', quote[0]['movie'])

    return jsonify({'quote': quote[0]})
    pass


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    quote = [quote for quote in quotes if quote['id'] == qid]
    if len(quote) == 0:
        abort(404)
    if not request.json:
        abort(400)
        
    quotes.remove(quote[0])
    return jsonify({'result': True}), 204
    pass