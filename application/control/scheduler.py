from requests.api import get
from application.control.trends import get_trends, add_trends, query_trends, show_all, get_all_entries
from apscheduler.schedulers.background import BackgroundScheduler


def set_scheduler(app):

    # "Työ" joka hakee ja tallentaa trendaus-tiedot tietokantaan
    def job():
        
        add_trends(get_trends("23424977"),app)
        print("Työ tehty!")

    # Alustetaan scheduler joka toimii sovelluksen taustalla
    scheduler = BackgroundScheduler(timezone="Europe/Helsinki")

    # Annetaan schedulerille työ ja taikataulu (24h välein)
    scheduler.add_job(job, "interval", hours=24)

    # Käynnistetään scheduler
    scheduler.start()
    job()
    print("Scheduler pystyssä!")