from requests.api import get
from application.control.trends import get_trends, add_trends, query_trends, show_all, get_all_entries
import schedule
import time

# "Työ" joka hakee ja tallentaa trendaus-tiedot tietokantaan
def job():
    
    add_trends(get_trends("23424977"))
    print("Työ tehty!")

def set_scheduler():

    schedule.every().day.at("23:50").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)