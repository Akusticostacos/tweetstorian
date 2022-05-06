TIEA306 Ohjelmointityö

Ohjelma ajossa (toistaiseksi) Google Cloudissa: 
- http://34.88.82.193/ (Pääsivu)
- http://34.88.82.193/about (Mistä on kyse?)
- http://34.88.82.193/admin (Pääkäyttäjän näkymä)

Ohjeet deployaamiseen: [/apache_conf/httpd.conf][httpd.conf]

Lokaalisti sovellusta voi testata:
- Sovellus olettaa että hallussasi on Twitter API-avaimet (/application/control/api_keys.json), jotka ovat salaiset ja käyttäjäkohtaiset, joten niitä ei ole saatavilla tässä repositoriossa. Ilman avaimia trendaustietoja ei voida noutaa, mutta muokkaamalla [/dummy_data.json][dummy_data.json] tiedostoa voit lisätä sovellukseen testidataa.

```
Luo virtuaali ympäristö:
> python -m venv venv
Aktivoi virtuaaliympäristö:
Linux: > source /venv/bin/activate
Windows: > /venv/scripts/activate
Asenna riippuvuudet:
> pip install -r requirements.txt
Käynnistä sovellus:
> flask run

```

Sovelluksen käyttöohje ja ominaisuudet:

    -Etusivu automaattisesti näyttää kuluvan päivän reaaliaikaisia trendaustietoja, tämä ilmaistaan käyttäjälle (today)-merkinnällä.
    -Alasvetovalikosta käyttäjä voi valita tietokannasta löytyviä päivämääriä ja tarkastella näiden päivien trendaavimpia puheenaiheita.
        - Laittamalla hiiren jonkin aiheen päälle näet montako twiittiä aiheesta on kirjoitettu (mikäli tieto on API:sta saatu).
        - Klikkaamalla aihetta sovellus ohjaa käyttäjän Twitteriin lukemaan keskustelua aiheesta.
    -Taulukon alapuolella on lista päivälle lisätyistä lisätiedoista, mikäli pääkäyttäjä on niitä lisännyt:
        - /admin -polussa pääkäyttäjä voi lisätä lisätietoja kullekin tallennetuista päivämääristä (ei kuluvalle päivälle), sekä poistaa aiemmin lisättyjä lisätietoja.
            - Lisätiedot muodostavat vapaa teksti sekä url-muotoinen lähde.
    - /about sivulla käyttäjille kerrotaan lyhyesti mistä sovelluksessa on kyse.
