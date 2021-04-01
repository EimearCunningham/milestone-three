import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


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
            "password": generate_password_hash(request.form.get("password"))}

        # Insert dictionary to MongoDB
        mongo.db.users.insert_one(register)

        # Put the user into session and return success flash message
        session["user"] = request.form.get("username").lower()
        flash(" Registration Successfull! ")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Log in function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check if password matches
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("profile", username=session["user"]))

            # If password doesn't match
            else:
                flash("Incorrect username / password")
                return redirect(url_for("login"))

        # If there was no match for user in database
        else:
            flash("Incorrect username / password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Users Profile with username
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


# Log out functionality
@app.route("/logout")
def logout():
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


# Add review functionality
@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "book_title": request.form.get("book_title"),
            "author_name": request.form.get("author_name"),
            "category_name": request.form.get("category_name"),
            "book_description": request.form.get("book_description"),
            "book_cover": request.form.get("book_cover"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review added!")
        return redirect(url_for("get_reviews"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_review.html", categories=categories)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "book_title": request.form.get("book_title"),
            "author_name": request.form.get("author_name"),
            "category_name": request.form.get("category_name"),
            "book_description": request.form.get("book_description"),
            "book_cover": request.form.get("book_cover"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Edited!")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_review.html", review=review, categories=categories)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review deleted!")
    return redirect(url_for("get_reviews"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
