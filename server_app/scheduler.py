from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time
from threading import Timer
from .scraping.scrape import flashscore
from .models.predictions import delete_old_predictions

scheduler = BackgroundScheduler()

def scheduled_task(app, db):
    """Runs the scraping task and retries if it fails."""
    print(f"Running scheduled task at {datetime.utcnow()}")

    with app.app_context():  # Ensure DB access inside the app context
        while True:
            success = flashscore(app, db)  # Pass `db` to scraping function
            delete_old_predictions()
            if success:
                print("Task completed successfully.")
                break  
            print("Retrying in 10 minutes...")
            time.sleep(600)  # Wait 10 minutes before retrying

def start_scheduler(app, db):
    """Start the scheduler with a delayed first execution."""
    scheduler.add_job(lambda: scheduled_task(app, db), 'cron', hour=3, minute=0)
    scheduler.start()
