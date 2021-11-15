from flask import app, Flask, render_template, Blueprint, request
from flask.wrappers import Response
import requests, json
from datetime import date
from application.control.api_keys import load_bearer_token

trending_blueprint = Blueprint("trending", __name__)

bearer_token = load_bearer_token()

# Sivu jolla näytetään halutun päiväyksen trendaus tiedot
@trending_blueprint.route("/trending")
def trending():

    trends = {}

    # Haetaan haluttu päivämäärä requestin parametrista "date", mikäli arvoa ei ole asetettu, käytetään kuluvan päivän päivämäärää
    if request.args.get('date'):
        date_string = request.args.get('date')
    else:
        date_string = date.today().strftime("%d-%m-%Y")

        response = requests.get("https://api.twitter.com/1.1/trends/place.json?id=23424977", headers= {"Authorization": f'Bearer {bearer_token}'})

        trends = response.json()[0].get("trends")
                
    return render_template("trending.html", trends=trends, date_string=date_string)