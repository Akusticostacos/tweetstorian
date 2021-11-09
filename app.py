from flask import Flask, render_template, url_for

app = Flask(__name__)


# Sovelluksen etusivu
@app.route("/")
def frontpage():
    return render_template("frontpage.html")


# Käynnistetään sovellus debug-modessa
if __name__ == "__main__":
    app.run(debug=True)

