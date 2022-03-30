from multiprocessing import dummy
from re import DEBUG
from flask import Flask
from .control.locations import get_locations
from flask_sqlalchemy import SQLAlchemy
from .control.scheduler import set_scheduler
from .control.model import trending_data, additional_info
from .control.trends import add_additional_info
import os
import json

def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trending_data.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from .control.extentions import db
    
    db.init_app(app)

    # Rekisteröidään eri näkymien blueprintit
    from .views.about import about_blueprint
    from .views.trending import trending_blueprint

    app.register_blueprint(about_blueprint)
    app.register_blueprint(trending_blueprint)

    # Luodaan sovelluksen tietokanta
    try:
        with app.app_context():
            db.create_all()

            # Täytetään sovelluksen tietokanta dummy datalla, mikäli dummy_data.json on olemassa.
            try:
                f = open("dummy_data.json", encoding="utf-8")
                dummy_data = json.load(f)
                list_of_keys = dummy_data.keys()
                
                for key in list_of_keys:
                    
                    data = trending_data(date_string=dummy_data.get(key).get("date_string"), trends_string=dummy_data.get(key).get("trends_string"))
                    print(data)

                    if dummy_data.get(key).get("additional_info") is not None:
                        info = additional_info(additional_info_string=dummy_data.get(key).get("additional_info"), trending_data_id=key)
                        print(info)

                    try:
                        db.session.add(data) 
                        db.session.add(info)           
                    except:
                        print("ERROR: Päivälle on jo tallennettu!")
                      
                    db.session.commit()
            except:
                print("No dummy data found, moving on...")
                
    except:
        print("")
    
    # Haetaan mahdolliset lokaatiot
    get_locations()
    # Käynnistetään scheduler joka hakee trendaus-datan haluttuun aikaan päivästä
    set_scheduler(app)

    add_additional_info("06.01.2022", "test", app)

    return app