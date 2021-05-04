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

# Route for handling the login page logic


@app.route("/hello")
def index():
    return render_template("hello.html", title="Welcome", username=username)


@app.route("/", methods=["GET", "POST"])
def redirect_get():
    if request.method == "GET":
        return redirect("static/register.html")
    else:
        # let them have books
        return redirect("/books")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "test" or request.form["password"] != "test":
            error = "Invalid Credentials. Please try again."
        else:
            session["username"] = request.form["username"]
            return render_template(
                "index.html", title="books", username=session["username"], books=books
            )
    return redirect("/")


@app.route("/books", methods=["GET", "POST"])
def book():
    username = session["username"]
    if request.method == "POST":
        new_book = request.form["book"]  # expects pure json with quotes everywheree
        myjson = json.loads(new_book)
        books.append(myjson)
        return jsonify(books)

    elif request.method == "GET":
        username = session["username"]
        return render_template(
            "books.html", books=books, title="books", username=session["username"]
        )
    else:
        return 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
