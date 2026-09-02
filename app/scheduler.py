from apscheduler.schedulers.background import BackgroundScheduler
from app.metrics import get_metrics
from app.database import save_metrics, cleanup_old_records

scheduler = BackgroundScheduler()


def collect_job():
    metrics = get_metrics()
    save_metrics(metrics)


def cleanup_job():
    cleanup_old_records(days=30)


def start_scheduler():
    scheduler.add_job(collect_job, "interval", seconds=30, id="collect_metrics")
    scheduler.add_job(cleanup_job, "interval", hours=24, id="cleanup_old")
    scheduler.start()