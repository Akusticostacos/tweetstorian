from flask import app, Flask, render_template, Blueprint


trending_blueprint = Blueprint("trending", __name__, url_prefix='/<date_string>')

# Sivu jolla näytetään halutun päiväyksen trendaus tiedot
@trending_blueprint.route("/trending")
def trending():
    return render_template("base.html")