
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

AGRI_WASTE_DB = {
    "Rice Straw": {
        "emoji": "🌾",
        "uses": ["Cattle Feed", "Biofuel", "Organic Compost"],
        "price": 3000
    },
    "Wheat Straw": {
        "emoji": "🌿",
        "uses": ["Animal Bedding", "Paper Making", "Compost"],
        "price": 2500
    },
    "Sugarcane Bagasse": {
        "emoji": "🍬",
        "uses": ["Bio Energy", "Eco Packaging", "Paper Industry"],
        "price": 4000
    },
    "Coconut Husk": {
        "emoji": "🥥",
        "uses": ["Coir Fiber", "Rope Making", "Mulching"],
        "price": 3500
    },
    "Banana Stem": {
        "emoji": "🍌",
        "uses": ["Fiber Extraction", "Organic Manure"],
        "price": 2800
    }
}

@app.route("/")
def index():
    wastes = {k: v["emoji"] + " " + k for k, v in AGRI_WASTE_DB.items()}
    return render_template("index.html", wastes=wastes)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    waste = data.get("waste")
    quantity = data.get("quantity")

    if waste not in AGRI_WASTE_DB:
        return jsonify({"error": "Invalid waste type"}), 400

    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({"error": "Enter a valid quantity"}), 400

    info = AGRI_WASTE_DB[waste]
    total = quantity * info["price"]

    return jsonify({
        "waste": info["emoji"] + " " + waste,
        "quantity": quantity,
        "uses": info["uses"],
        "price_per_ton": info["price"],
        "total_profit": total
    })

if __name__ == "__main__":
    app.run(debug=True)
