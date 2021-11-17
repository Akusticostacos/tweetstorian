from flask import render_template, Blueprint, request
from datetime import date
from application.control.api_keys import load_bearer_token
from application.control.trends import get_trends, add_trends, query_trends, show_all
import json

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

        if query_trends(date_string):
            print("Löytyi!")
            trends = query_trends(date_string)
            print(type(trends))
    else:
        date_string = today

        #trends = get_trends(woeid)

        #add_trends(trends)

        if query_trends(date_string):
            print("Löytyi!")
            trends = query_trends(date_string)
            print(type(trends))

             
    return render_template("trending.html", trends=trends, date_string=date_string, today=today)