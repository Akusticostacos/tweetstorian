from flask import app, Flask, render_template, Blueprint, request, redirect, url_for
import requests, json
from application.control.model import additional_info
from application.control.trends import delete_additional_info, get_trends, add_trends, query_trends, show_all, get_all_entries, add_additional_info, query_additional_info, delete_additional_info
import re

admin_blueprint = Blueprint("admin", __name__)

# Sovelluksen Adminsivu
@admin_blueprint.route("/admin", methods=("GET","POST"))
def admin():

    date_string = request.args.get("date")

    if date_string is not None:

        if query_additional_info(date_string) is not None:
            additional_info=query_additional_info(date_string)
        else:
            additional_info=[]
    else:
        additional_info = []
    
    if request.method == "POST" and date_string is not None and re.match("^(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])$", date_string):

        info = request.form["info"]
        source = request.form["source"]

        add_additional_info(date_string, info, source)
   
        return redirect("/admin?date="+date_string)

    return render_template("admin.html", all_dates=reversed(get_all_entries()), date_string=date_string, additional_info=additional_info, delete=delete_additional_info)


@admin_blueprint.route("/admin/delete/<int:id>/<string:date_string>")
def admin_delete(id, date_string):

    delete_additional_info(id)

    return redirect("/admin?date=" + date_string)