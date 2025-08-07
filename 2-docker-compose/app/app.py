from flask import Flask
import os

app = Flask(__name__)
@app.route("/")
def home():
    with open("data/visit.txt", "a+") as f:
        f.write("Visited\n")
    return "Visit logged."

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
