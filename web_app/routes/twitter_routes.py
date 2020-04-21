# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect
from web_app.models import TwitterUser, Tweets

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users.json")
def list_users():
    # users = [
    #     {"id": 1, "user": "user 1"},
    #     {"id": 2, "user": "user 2"},
    #     {"id": 3, "user": "user 3"},
    # ]
    user_records = TwitterUser.query.all()
    print(user_records)
    users = parse_records(user_records)
    return jsonify(users)

@twitter_routes.route("/users")
def list_users_for_humans():
    # users = [
    #     {"id": 1, "user": "user 1"},
    #     {"id": 2, "user": "user 2"},
    #     {"id": 3, "user": "user 3"},
    # ]
    user_records = TwitterUser.query.all()
    print(user_records)
    return render_template("users.html", message="Here's some users", users=user_records)

@twitter_routes.route("/user/new")
def new_user():
    return render_template("new_user.html")

@twitter_routes.route("/user/create", methods=["POST"])
def create_user():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    new_user = TwitterUser(user=request.form["user_name"])
    db.session.add(new_user)
    db.session.commit()
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    return redirect(f"/users")