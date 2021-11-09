from flask import Flask
from .views.frontpage import frontpage_blueprint

app = Flask(__name__)

# Rekisteröidään eri näkymien blueprintit
app.register_blueprint(frontpage_blueprint)

# Käynnistetään sovellus debug-modessa
if __name__ == "__main__":
    app.run(debug=True)

