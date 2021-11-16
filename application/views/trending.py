from flask import app, Flask, render_template, Blueprint, request
from flask.wrappers import Response
import requests, json
from datetime import date
from application.control.api_keys import load_bearer_token

trending_blueprint = Blueprint("trending", __name__)

# Ladataan API-avaimet tunnistautumista varten.
bearer_token = load_bearer_token()

# "The id parameter for this endpoint is the "where on earth identifier" or WOEID"
# 23424977 = United States
# Käytössä olevat id:t löydettävissä locations.txt, Suomi ei tällä hetkellä tuettuna.
woeid = "23424977"

# Sivu jolla näytetään halutun päiväyksen trendaus tiedot
@trending_blueprint.route("/trending")
def trending():

    trends = {}
    today = date.today().strftime("%d-%m-%Y")

    # Haetaan haluttu päivämäärä requestin parametrista "date", mikäli arvoa ei ole asetettu, käytetään kuluvan päivän päivämäärää
    if request.args.get("date"):
        date_string = request.args.get("date")
    else:
        date_string = today

        response = requests.get(f"https://api.twitter.com/1.1/trends/place.json?id={woeid}", headers= {"Authorization": f'Bearer {bearer_token}'})

        trends = response.json()[0].get("trends")

        print(type(trends))
                
    return render_template("trending.html", trends=trends, date_string=date_string, today=today)