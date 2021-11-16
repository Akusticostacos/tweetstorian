from flask import app, Flask, render_template, Blueprint, request
from flask.wrappers import Response
import requests, json
from datetime import date
from application.control.api_keys import load_bearer_token

# Ladataan API-avaimet tunnistautumista varten.
bearer_token = load_bearer_token()

# Hakee Twitter API:sta tiedon kaikista mahdollisista lokaatioista joista on saatavilla trendaus-dataa.
def get_locations():

    response = requests.get("https://api.twitter.com/1.1/trends/available.json", headers= {"Authorization": f'Bearer {bearer_token}'})

    with open('locations.txt', 'a', encoding="utf-8") as f:
        f.write(str(response.json()))