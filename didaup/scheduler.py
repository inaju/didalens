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
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu") 
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--remote-debugging-port=9222")

        chrome_options.binary_location = os.getenv('GOOGLE_CHROME_BIN_S')
       
        driver = webdriver.Chrome(executable_path=os.getenv('CHROMEDRIVER_PATH_S'), options=chrome_options)
        driver.get('https://didalens.herokuapp.com/goals/goalreminder/')
        driver.get('https://didalens.herokuapp.com/goals/fakeemail/')
        print('it worked')

        # Now you can start using Selenium    except:
    except:
        e = sys.exc_info()
        print('it failed, this is the error ', e)


schedule.every(0.01).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)