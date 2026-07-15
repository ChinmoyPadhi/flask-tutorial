import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = os.environ.get("DB_NAME", "testdb")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "credentials")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
print(f"Connected to MongoDB: {MONGO_URI}")

@app.route("/", methods=["GET"])
def index():
    """Render the empty form."""
    return render_template("index.html", error=None, form_data={})


@app.route("/submit", methods=["POST"])
def submit():
    """Handle form submission, insert into MongoDB, redirect or show error."""
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    form_data = {"username": username, "password": password}

    # Basic server-side validation
    if not username or not password:
        return render_template(
            "index.html",
            error="All fields are required.",
            form_data=form_data,
        )

    try:
        collection.insert_one(form_data)
    except PyMongoError as e:
        # Stay on the same page and show the error, no redirect
        return render_template(
            "index.html",
            error=f"Database error: {str(e)}",
            form_data=form_data,
        )

    # Success -> redirect to a different page
    return redirect(url_for("success"))


@app.route("/success", methods=["GET"])
def success():
    """Page shown after a successful submission."""
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
