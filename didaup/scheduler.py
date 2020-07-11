import schedule
import time
from tests import name
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from selenium import webdriver
import requests
import webbrowser


def job():
    webbrowser.open('http://didalens.herokuapp.com/goals/goalfull/')

schedule.every(0.01).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)