# Aku Pasanen 5.5.2022
# Tässä tiedostossa eri metodit API-avainten käsittelyyn.
import json
import os

# Alustetaan polku API-avaimille, lähinnä siksi että Apache löytää ne ajon aikana.
api_keys_path = os.path.join(os.path.dirname(__file__), "api_keys.json")

def load_bearer_token():

    # Ladataan API-avaimet tunnistautumista varten.
    
    try:
        f = open(api_keys_path, encoding="utf-8")
        bearer_token = json.load(f).get("Bearer_Token")
    except:
        bearer_token = os.environ.get("BEARER_TOKEN")

    return bearer_token


def load_api_key():

    # Ladataan API-avaimet tunnistautumista varten.
    
    try:
        f = open(api_keys_path, encoding="utf-8")
        api_key = json.load(f).get("API_Key")
    except:
        api_key = os.environ.get("API_KEY")

    return api_key


def load_api_key_secret():

    # Ladataan API-avaimet tunnistautumista varten.

    try:
        f = open(api_keys_path, encoding="utf-8")
        api_key_secret = json.load(f).get("API_Key_Secret")
    except:
        api_key_secret = os.environ.get("API_KEY_SECRET") 
    return api_key_secret