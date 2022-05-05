# Aku Pasanen 5.5.2022
# Tämä tiedosto käynnistää sovelluksen flask run -komennolla
from application import create_app

app = create_app()

if __name__ == "__main__":
        app.run()