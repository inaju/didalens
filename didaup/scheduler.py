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
        #webbrowser.open('http://didalens.herokuapp.com/goals/goalfull/')
        options = Options()

        options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')

        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')

        return webdriver.Chrome(executable_path=str(os.environ.get('CHROMEDRIVER_PATH')), chrome_options=options)
        print('done')
    except:
        e = sys.exc_info()[0]
        print('it failed, this is the error ', e)


schedule.every(0.01).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)