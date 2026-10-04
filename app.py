from flask import Flask, request, jsonify
from flask_cors import CORS
from ReadingCards import get_all_cards
from UpdatingCards import update_quantity

app = Flask(__name__)
CORS(app)  # allows the React dev server (different port) to call this API

#Read function
@app.route("/api/collection", methods=["GET"])
def get_collection():
    cards = get_all_cards()
    return jsonify(cards)



''' Run this function for PATCH requests to /api/collection/<number>.
    <int:id> grabs the number from the URL as an integer.
    Example URL: http://localhost:3450/api/collection/5'''

@app.route("/api/collection/<int:id>", methods=["PATCH"])
def modify_quantity(id):

    #1. Turns the JSON body React sent into a dictionary: {"quantity": 4}
    # silent=True returns None (instead of crashing) if the body isn't valid JSON
    cardData = request.get_json(silent=True)

    #2. Pulls the new quantity from the dictionary (KeyError if it's missing)
    if cardData is None or "quantity" not in cardData:
        # stop early with 400 if the body is missing or has no "quantity"
        return jsonify({"error": "Quantity key is not found."}), 400
    newQuantity = cardData["quantity"]

    # Guard clause: quantity must be a whole number, 0 or higher
    # isinstance(x, int) asks "is x a whole number?" ("4", 4.5 and "abc" all fail).
    # bool is excluded because Python treats True/False as 1/0, so JSON true would sneak through.
    if not isinstance(newQuantity, int) or isinstance(newQuantity, bool) or newQuantity < 0:
        return jsonify({"error": "Quantity must be a whole number, 0 or higher."}), 400

    #3. Update the card in database(Postgres). Returns the updated card or None.
    newCardData = update_quantity(id, newQuantity)

    #4. stop early with 404 if no card has that id
    if newCardData is None:
        return jsonify({"error": f"Card {id} was not found."}), 404

    #5. Turns the card back into JSON and sends it back to React.
    return jsonify(newCardData)


if __name__ == "__main__":
    app.run(debug=True, port=5000)