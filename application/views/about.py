from flask import app, Flask, render_template, Blueprint
import requests, json

about_blueprint = Blueprint("about", __name__)

# Sovelluksen About-sivu
@about_blueprint.route("/about")
def about():
    return render_template("about.html")