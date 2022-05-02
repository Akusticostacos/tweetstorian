from flask import app, Flask, render_template, Blueprint
import requests, json

admin_blueprint = Blueprint("admin", __name__)

# Sovelluksen etusivu
@admin_blueprint.route("/admin")
def admin():
    return render_template("admin.html")