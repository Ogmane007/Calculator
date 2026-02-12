from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

OPS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "×": lambda a, b: a * b,
    "÷": lambda a, b: a / b,
}

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/calculate")
def api_calculate():
    """JSON API endpoint for the calculator"""
    try:
        data = request.get_json()
        
        a_raw = data.get("a", "").strip()
        b_raw = data.get("b", "").strip()
        op = data.get("op", "+")
        
        # Convert to float
        a = float(a_raw)
        b = float(b_raw)
        
        # Validate operator
        if op not in OPS:
            return jsonify({"ok": False, "error": "Invalid operator."}), 400
        
        # Check for division by zero
        if op == "÷" and b == 0:
            return jsonify({"ok": False, "error": "Cannot divide by zero."}), 400
        
        # Perform calculation
        result = OPS[op](a, b)
        
        # Make clean integers show as 5 instead of 5.0
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        
        return jsonify({"ok": True, "result": result})
        
    except ValueError:
        return jsonify({"ok": False, "error": "Please enter valid numbers."}), 400
    except Exception as e:
        return jsonify({"ok": False, "error": "Something went wrong."}), 500

if __name__ == "__main__":
    app.run(debug=True)