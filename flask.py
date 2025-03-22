app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/track', methods=['POST'])
def track():
    food_items = request.form['food'].split(", ")
    result = calculate_nutrients(food_items)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
