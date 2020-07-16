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
        print(os.environ.get('GOOGLE_CHROME_BIN'))
        print(os.environ.get('CHROMEDRIVER_PATH'))

        chrome_options = Options()
        chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
        driver.get("didalens.herokuapp.com/goals/fakeemail/")
        print('done')
    except:
        e = sys.exc_info()[0]
        print('it failed, this is the error ', e)


schedule.every(0.01).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)