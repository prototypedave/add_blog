from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time
from threading import Timer
from .scraping.scrape import flashscore
from .models.predictions import delete_old_predictions

scheduler = BackgroundScheduler()
job_running = False  # Flag to check if the job is running

def scheduled_task(app, db):
    """Runs the scraping task and retries if it fails."""
    global job_running
    if job_running:
        print("Task is already running, skipping this execution.")
        return

    job_running = True
    print(f"Running scheduled task at {datetime.utcnow()}")

    with app.app_context():
        while True:
            success = flashscore(app, db)
            delete_old_predictions(db)
            if success:
                print("Task completed successfully.")
                break  
            print("Retrying in 10 minutes...")
            time.sleep(600)

    job_running = False  # Reset the flag when done

def start_scheduler(app, db):
    """Start the scheduler with a delayed first execution."""
    scheduler.add_job(lambda: scheduled_task(app, db), 'cron', hour=3, minute=0)
    scheduler.start()

    # Delay initial execution by 1 minute
    Timer(60, lambda: scheduled_task(app, db)).start()