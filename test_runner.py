import time
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def run_tests():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.example.com')

    results = []

    # Test Case 1: Check title
    try:
        assert "Example Domain" in driver.title
        results.append(("Check title", "PASS"))
    except AssertionError:
        results.append(("Check title", "FAIL"))

    # Test Case 2: Check link exists
    try:
        driver.find_element(By.TAG_NAME, 'a')
        results.append(("Check link existence", "PASS"))
    except:
        results.append(("Check link existence", "FAIL"))

    driver.quit()
    return results

def save_results(results):
    conn = sqlite3.connect('db/test_results.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        test_name TEXT, 
        status TEXT, 
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    for test_name, status in results:
        cursor.execute('INSERT INTO results (test_name, status) VALUES (?, ?)', (test_name, status))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    test_results = run_tests()
    save_results(test_results)
