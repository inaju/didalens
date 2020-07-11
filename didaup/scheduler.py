import schedule
import time
from tests import name
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from selenium import webdriver
import requests
import webbrowser
import sys

def job():
    try:
        webbrowser.open('http://didalens.herokuapp.com/goals/goalfull/')
        print('done')
    except:
        e = sys.exc_info()[0]
        print('it failed, this is the error ', e)

schedule.every(0.01).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)