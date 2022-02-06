from requests.api import get
from application.control.trends import get_trends, add_trends
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


def set_scheduler(app):

    # "Työ" joka hakee ja tallentaa trendaus-tiedot tietokantaan
    def job():
        
        add_trends(get_trends("23424977"),app)
        print("Työ tehty!")

    # Crontrigger joka päivälle klo 23:55:00
    trigger = CronTrigger(
        year="*", month="*", day="*", hour="22", minute="10", second="0"
    )

    # Alustetaan scheduler joka toimii sovelluksen taustalla
    scheduler = BackgroundScheduler(timezone="Europe/Helsinki")

    # Annetaan schedulerille työ ja trigger
    scheduler.add_job(func=job, trigger=trigger)

    # Käynnistetään scheduler
    scheduler.start()
    print("Scheduler pystyssä!")