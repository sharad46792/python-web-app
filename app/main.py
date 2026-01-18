from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask Web App running on Port 2000!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2000)
