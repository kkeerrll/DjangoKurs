from apscheduler.schedulers.background import BackgroundScheduler
from logic_work.logic_work import send_mailings


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailings, 'interval', seconds=15)
    scheduler.start()
