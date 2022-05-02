from flask import app, Flask, render_template, Blueprint
import requests, json
from application.control.trends import get_trends, add_trends, query_trends, show_all, get_all_entries, add_additional_info, query_additional_info

admin_blueprint = Blueprint("admin", __name__)

# Sovelluksen etusivu
@admin_blueprint.route("/admin", methods=("GET","POST"))
def admin():
    return render_template("admin.html", all_dates=reversed(get_all_entries()))