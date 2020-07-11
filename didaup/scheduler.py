import schedule
import time
from tests import name
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from selenium import webdriver
import requests
import webbrowser


def job():
    r = requests.post('http://127.0.0.1:8000/goals/goalfull/')
    webbrowser.open('http://127.0.0.1:8000/goals/goalfull/')
    print(r.status_code)

schedule.every(0.01).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)