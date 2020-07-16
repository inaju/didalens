import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import requests
import webbrowser
import sys


def job():
    try:
        from selenium import webdriver
        import os

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.getenv('GOOGLE_CHROME_BIN_S')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(executable_path=os.getenv('CHROMEDRIVER_PATH_S'), chrome_options=chrome_options)

        # Now you can start using Selenium    except:
    except:
        e = sys.exc_info()
        print('it failed, this is the error ', e)


schedule.every(0.01).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)