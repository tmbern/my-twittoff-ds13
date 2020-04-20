# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/twitter.json")
def list_users():
    users = [
        {"id": 1, "user": "user 1"},
        {"id": 2, "user": "user 2"},
        {"id": 3, "user": "user 3"},
    ]
    return jsonify(users)

@book_routes.route("/twitter")
def list_users_for_humans():
    users = [
        {"id": 1, "user": "user 1"},
        {"id": 2, "user": "user 2"},
        {"id": 3, "user": "user 3"},
    ]
    return render_template("twitter.html", message="Here's some users", users=users)

@book_routes.route("/user/new")
def new_book():
    return render_template("new_user.html")

@book_routes.route("/user/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    return jsonify({
        "message": "BOOK CREATED OK (TODO)",
        "book": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")