from flask import Flask

app = Flask(__name__)

suits = ['D', 'S', 'C', 'H']

symbols = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']

@app.route("/deck")
@app.route("/deck/new")
def deck():
    return "deck of cards"

@app.route("/shuffle")
def shuffle():
    return "shuffle the deck"

@app.route("/draw")
def draw():
    return "draw card"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")