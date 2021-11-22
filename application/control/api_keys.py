import json


def load_bearer_token():

    # Ladataan API-avaimet tunnistautumista varten.
    f = open("api_keys.json", encoding="utf-8")
    bearer_token = json.load(f).get("Bearer_Token")

    return bearer_token


def load_api_key():

    # Ladataan API-avaimet tunnistautumista varten.
    f = open("api_keys.json", encoding="utf-8")
    api_key = json.load(f).get("API_Key")

    return api_key


def load_api_key_secret():

    # Ladataan API-avaimet tunnistautumista varten.
    f = open("api_keys.json", encoding="utf-8")
    api_key_secret = json.load(f).get("API_Key_Secret")

    return api_key_secret