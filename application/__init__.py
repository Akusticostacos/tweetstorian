from flask import Flask
from .views.frontpage import frontpage_blueprint
from .views.trending import trending_blueprint
from .control.locations import get_locations
import json

app = Flask(__name__)

# Rekisteröidään eri näkymien blueprintit
app.register_blueprint(frontpage_blueprint)
app.register_blueprint(trending_blueprint)

get_locations()