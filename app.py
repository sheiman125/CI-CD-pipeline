from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    result = "Cannot divide by zero"
                else:
                    result = num1 / num2

        except ValueError:
            result = "Please enter valid numbers as you cann bro"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Calculator</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}

            .calculator {{
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.15);
                width: 320px;
            }}

            h2 {{
                text-align: center;
            }}

            input, select, button {{
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                box-sizing: border-box;
            }}

            button {{
                background: #222;
                color: white;
                border: none;
                cursor: pointer;
                border-radius: 5px;
            }}

            button:hover {{
                background: #444;
            }}

            .result {{
                text-align: center;
                font-size: 22px;
                margin-top: 20px;
            }}
        </style>
    </head>

    <body>

        <div class="calculator">

            <h2>Calculator</h2>

            <form method="POST">

                <input
                    type="number"
                    step="any"
                    name="num1"
                    placeholder="First number ONLY"
                    required
                >

                <select name="operation">
                    <option value="add">+</option>
                    <option value="subtract">-</option>
                    <option value="multiply">×</option>
                    <option value="divide">÷</option>
                </select>

                <input
                    type="number"
                    step="any"
                    name="num2"
                    placeholder="Second number only bro"
                    required
                >

                <button type="submit">
                    Calculate
                </button>

            </form>

            <div class="result">
                Result: {result}
            </div>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)