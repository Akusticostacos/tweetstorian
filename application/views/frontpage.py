from flask import app, Flask, render_template, Blueprint


frontpage_blueprint = Blueprint("frontPage", __name__)

# Sovelluksen etusivu
@frontpage_blueprint.route("/")
def frontpage():
    return render_template("frontpage.html")