from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>This is the home for the website</p>"

