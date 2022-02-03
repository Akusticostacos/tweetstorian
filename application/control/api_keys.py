import json
import os


def load_bearer_token():

    # Ladataan API-avaimet tunnistautumista varten.

    try:
        f = open("api_keys.json", encoding="utf-8")
        bearer_token = json.load(f).get("Bearer_Token")
    except:
        bearer_token = os.environ.get("Bearer_token")

    return bearer_token


def load_api_key():

    # Ladataan API-avaimet tunnistautumista varten.
    
    try:
        f = open("api_keys.json", encoding="utf-8")
        api_key = json.load(f).get("API_Key")
    except:
        api_key = os.environ.get("API_Key")

    return api_key


def load_api_key_secret():

    # Ladataan API-avaimet tunnistautumista varten.

    try:
        f = open("api_keys.json", encoding="utf-8")
        api_key_secret = json.load(f).get("API_Key_Secret")
    except:
        api_key_secret = os.environ.get("API_Key_Secret")
    return api_key_secret