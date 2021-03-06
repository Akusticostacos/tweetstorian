# Aku Pasanen 5.5.2022
# Tässä tiedostossa haetaan Twitterin apista lokaatiot tekstitiedostoon.
import re
import requests
from application.control.api_keys import load_bearer_token
import os

# Ladataan API-avaimet tunnistautumista varten.
bearer_token = load_bearer_token()

locations_path = os.path.join(os.path.dirname(__file__), "locations.txt")

# Hakee Twitter API:sta tiedon kaikista mahdollisista lokaatioista joista on saatavilla trendaus-dataa.
def get_locations():

    response = requests.get("https://api.twitter.com/1.1/trends/available.json", headers= {"Authorization": f'Bearer {bearer_token}'})

    with open(locations_path, 'w', encoding="utf-8") as f:
        for place in response.json():

            name = place.get("name")
            country = place.get("country")
            woeid = place.get("woeid")
            line = ("Name: " + str(name) + " Country: " + str(country) + " Woeid: " + str(woeid) + "\n")
            f.write(line)