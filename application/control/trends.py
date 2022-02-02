from application.control.api_keys import load_bearer_token
import requests
from datetime import date
from application.control.extentions import db
from application.control.model import trending_data
import json
from ast import literal_eval

# Hakee ajankohtaisen trendaus-datan twitterin API:sta
# woeid:
# "The id parameter for this endpoint is the "where on earth identifier" or WOEID"
# 23424977 = United States
# Käytössä olevat id:t löydettävissä locations.txt, Suomi ei tällä hetkellä tuettuna.
def get_trends(woeid):

    # Ladataan API-avaimet tunnistautumista varten.
    bearer_token = load_bearer_token()

    response = requests.get(f"https://api.twitter.com/1.1/trends/place.json?id={woeid}", headers= {"Authorization": f'Bearer {bearer_token}'})

    trends = response.json()[0].get("trends")

    return trends


# Tallentaa trendaustiedot tietokantaan.
def add_trends(trends, app):

    today = date.today().strftime("%d-%m-%Y")

    # Muutetaan <list> -> <string>
    trends = repr(trends)

    data = trending_data(date_string=today, trends_string=trends)

    with app.app_context():

        try:
            db.session.add(data)
            db.session.commit()
            print("Data tallennettu " + today)
        except:
            print("ERROR: Päivälle on jo tallennettu!")


def query_trends(date):

    data = trending_data.query.filter_by(date_string=date).first()

    if data is not None:
        trends = data.trends_string

        # Muutetaan <string> -> <list>
        trends = literal_eval(trends)

        return trends
        

def get_all_entries():

    data = trending_data.query.all()

    return data


def show_all():

    data = trending_data.query.all()

    for row in data:
        print(row.id, row.date_string)