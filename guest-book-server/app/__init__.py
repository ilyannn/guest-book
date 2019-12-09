from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()


def create_app(data_dir):
    app = Flask(__name__)
    config_data = Config(data_dir)
    app.config.from_object(config_data)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
