from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My CI/CD Project</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }

            .container {
                background: white;
                padding: 50px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.15);
                text-align: center;
                width: 500px;
            }

            h1 {
                font-size: 36px;
                margin-bottom: 15px;
            }

            p {
                font-size: 18px;
                color: #555;
            }

            .status {
                margin-top: 25px;
                padding: 12px;
                background: #e8f5e9;
                border-radius: 8px;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>Hello Dudes! 👋</h1>

            <h2>I am a CI/CD Pipeline Website</h2>

            <p>
                This website is deployed automatically using
                Docker, GitHub Actions and AWS.
            </p>

            <div class="status">
                🚀 CI/CD Deployment Successful
            </div>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)