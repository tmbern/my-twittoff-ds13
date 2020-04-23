# twitoff/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.admin_routes import admin_routes
from web_app.routes.stats_routes import stats_routes

#DATABASE_URI = "sqlite:///web_app_13.db"
DATABASE_URI = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", default="super_secret")

# application factory pattern
def create_app():
    app = Flask(__name__)

    #app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite://///home/tmbern/workspace/repos/lambda/my-twittoff-ds13/web_app_13.db"
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(stats_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
