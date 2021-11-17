from flask import Flask
from .views.frontpage import frontpage_blueprint
from .views.trending import trending_blueprint
from .control.locations import get_locations
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trending_data.db"
db = SQLAlchemy(app)

# SQL tietokannan alustaminen.
class trending_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # String muotoa dd-mm-yy
    date_string = db.Column(db.String(10), unique=True, nullable=False)
    # JSON muotoinen String
    trending_string = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return "Trending data for: %r" % self.date_string

# Rekisteröidään eri näkymien blueprintit
app.register_blueprint(frontpage_blueprint)
app.register_blueprint(trending_blueprint)

get_locations()