import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# Connect app to MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


# Registration function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # If there is an existing user
        if existing_user:
            flash("Username already exists")
            # Redirect user to try register again
            return redirect(url_for("register"))
        # Create 'register' dictionary
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")
            )}
        # Insert dictionary to MongoDB
        mongo.db.users.insert_one(register)

        # Put the user into session and return success flash message
        session["user"] = request.form.get("username").lower()
        flash(" Registration Successfull! ")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)