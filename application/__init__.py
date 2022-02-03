from re import DEBUG
from flask import Flask
from .control.locations import get_locations
from flask_sqlalchemy import SQLAlchemy
from .control.scheduler import set_scheduler

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

    try:
        with app.app_context():
            db.create_all()
    except:
        print("")
        
    get_locations()
    set_scheduler(app)

    return app