from flask import Flask, render_template, request
from endee_engine import search_endee, search_product

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("input", "").lower()

        product_keywords = ["phone","mobile","laptop","buy","best","camera","price"]
        safety_keywords = ["road","street","night","crowd","unsafe","alone"]

        if any(w in user_input for w in product_keywords) and not any(w in user_input for w in safety_keywords):

            products = search_product(user_input)

            result = {
                "type": "product",
                "items": products
            }

        else:
            data = search_endee(user_input)

            if data:
                result = data
                result["type"] = "safety"

    return render_template("index.html", result=result, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)