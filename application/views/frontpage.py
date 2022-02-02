from flask import app, Flask, render_template, Blueprint
import requests, json

frontpage_blueprint = Blueprint("frontPage", __name__)

# Sovelluksen etusivu
@frontpage_blueprint.route("/asd")
def frontpage():
    return render_template("frontpage.html")