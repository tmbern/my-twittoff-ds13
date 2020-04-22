# web_app/routes/admin_routes.py

from flask import Blueprint, jsonify, request, flash, redirect

from web_app.models import db

admin_routes = Blueprint("admin_routes", __name__)

# GET /admin/db/reset?api_key=abc123

@admin_routes.route("/admin/db/reset")
def reset_db():
    print(type(db))
    db.drop_all()
    db.create_all()
    return jsonify({"message": "DB RESET OK"})