from django.core.management.base import BaseCommand
import requests
import datetime
from selenium import webdriver
import os
import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import requests
import webbrowser
import sys
from apscheduler.schedulers.blocking import BlockingScheduler

class Command(BaseCommand):
    help = 'Scrapes spoj.com to obtain the details of all the classical problems.'

    def handle(self, *args, **options):
        print('pretty')

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
        
        print('it worked')

