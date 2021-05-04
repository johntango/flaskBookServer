from flask import jsonify
import json
from flask import request, session
from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)
app.secret_key = "secretkey"
books = [
    {
        "author": "Hernando de Soto",
        "country": "Peru",
        "language": "English",
        "pages": 209,
        "title": "The Mystery of Capital",
        "year": 1970,
    },
    {
        "author": "Hans Christian Andersen",
        "country": "Denmark",
        "language": "Danish",
        "pages": 784,
        "title": "Fairy tales",
        "year": 1836,
    },
    {
        "author": "Dante Alighieri",
        "country": "Italy",
        "language": "Italian",
        "pages": 928,
        "title": "The Divine Comedy",
        "year": 1315,
    },
]

# Routes at present only handling http GETs


@app.route("/", methods=["GET"])
def redirect_get():
    if request.method == "GET":
        return render_template(
            "index.html", title="books", books=books
        )


@app.route("/books", methods=["GET"])
def book():
    if request.method == "POST":  # just send user back to index template
        return render_template(
            "index.html", title="books", books=books
        )
    elif request.method == "GET":
        return jsonify(books)
    else:
        return 400  # Bad Request Response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
