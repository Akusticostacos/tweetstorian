from application.control.api_keys import load_bearer_token
import requests
from datetime import date
from application.control.extentions import db
from application.control.model import trending_data, additional_info
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

    try:
        trends = response.json().pop(0).get("trends")
    except:
        trends = []

    #print(repr(trends))

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

# Hakee tietokannasta trendaus-tiedot tietylle päivämäärälle
def query_trends(date):

    data = trending_data.query.filter_by(date_string=date).first()

    if data is not None:
        trends = data.trends_string
        #print(trends)
        # Muutetaan <string> -> <list>
        trends = literal_eval(trends)

        return trends
        
# Palauttaa tietokannan kaikki syötteet
def get_all_entries():

    data = trending_data.query.all()

    return data

# Tulostaa konsoliin kaikki trending-tiedot, testaus tarkoituksessa.
def show_all():

    data = trending_data.query.all()

    for row in data:
        print(row.id, row.date_string)


# Lisää lisätietoja jonkin päivämäärän kohdalle additional_info tauluun
def add_additional_info(date, info_string, sources_string):

    #with app.app_context():

    data = trending_data.query.filter_by(date_string=date).first()

    if data is not None:
        
        info = additional_info(additional_info_string=info_string, sources_url_string=sources_string, trending_data_id=data.id)

        try:
            db.session.add(info)
            db.session.commit()
            print("Informaatiota lisätty " + data.date_string)
        except:
            print("ERROR")


# Hakee lisätiedot päivämäärälle
def query_additional_info(date):
    
    data = trending_data.query.filter_by(date_string=date).first()

    if data is not None:
        additional_info = data.additional_info
              
        return additional_info


# Poistaa lisätietoja tietokannasta
def delete_additional_info(id):

    info = additional_info.query.get(id)
    db.session.delete(info)
    db.session.commit()
    print("Informaatiota poistettu!")





