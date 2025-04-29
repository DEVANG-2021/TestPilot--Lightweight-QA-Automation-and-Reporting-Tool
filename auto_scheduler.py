import schedule
import time
from test_runner import run_tests, save_results

def scheduled_task():
    print("Running automated test...")
    test_results = run_tests()
    save_results(test_results)
    print("Test complete.")

schedule.every(2).hours.do(scheduled_task)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
