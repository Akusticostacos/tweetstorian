from flask import render_template, Blueprint, request
from datetime import date
from application.control.api_keys import load_bearer_token
from application.control.model import additional_info
from application.control.trends import get_trends, add_trends, query_trends, show_all, get_all_entries, add_additional_info, query_additional_info
import json
from application.control.api_keys import load_bearer_token
import re

trending_blueprint = Blueprint("trending", __name__)

# Ladataan API-avaimet tunnistautumista varten.
bearer_token = load_bearer_token()

# "The id parameter for this endpoint is the "where on earth identifier" or WOEID"
# 23424977 = United States
# Käytössä olevat id:t löydettävissä locations.txt, Suomi ei tällä hetkellä tuettuna.
woeid = "23424977"

# Sivu jolla näytetään halutun päiväyksen trendaus tiedot
@trending_blueprint.route("/")
def trending():

    trends = {}
    today = date.today().strftime("%d-%m-%Y")

    date_string = request.args.get("date")

    additional_info = ""

    # Haetaan haluttu päivämäärä requestin parametrista "date", mikäli arvoa ei ole asetettu, käytetään ja näytetään kuluvan päivän päivämäärää
    if request.args.get("date") and re.match("^([1-9]|1[0-9]|2[0-9]|3[0-1])-([1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])$", request.args.get("date")):

        if query_trends(date_string) is not None:
            print("Found trending data for: " + date_string)
            trends = query_trends(date_string)
            print(trends)

            additional_info = query_additional_info(date_string)
    else:
        date_string = today
        trends = get_trends(woeid)

    return render_template("trending.html", trends=trends, date_string=date_string, today=today, all_dates=get_all_entries(), additional_info=additional_info)