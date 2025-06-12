from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Jenkins Multi-Stage Pipeline!"

@app.route("/status")
def status():
    return jsonify({
        "status": "running",
        "message": "Flask app is healthy",
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(debug=True)
