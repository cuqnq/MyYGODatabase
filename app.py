from flask import Flask, jsonify
from flask_cors import CORS
from AddingCard import get_all_cards

app = Flask(__name__)
CORS(app)  # allows the React dev server (different port) to call this API

@app.route("/api/collection", methods=["GET"])
def get_collection():
    cards = get_all_cards()
    return jsonify(cards)

if __name__ == "__main__":
    app.run(debug=True, port=5000)