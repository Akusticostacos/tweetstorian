import json


def load_bearer_token():

    # Ladataan API-avaimet tunnistautumista varten.
    f = open("api_keys.json", encoding="utf-8")
    bearer_token = json.load(f).get("Bearer_Token")

    return bearer_token