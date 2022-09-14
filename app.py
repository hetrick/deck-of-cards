from flask import Flask

app = Flask(__name__)

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['D', 'S', 'C', 'H']

@app.route("/deck")
def deck(ranks, suits):
    cards = []
    for rank in ranks:
        for suit in suits:
            cards.append(f'{rank}{suit}')
    return cards

@app.route("/shuffle")
def shuffle():
    return "shuffle the deck"

@app.route("/draw")
def draw():
    return "draw card"

if __name__ == "__main__":
    app.run(debug=True)