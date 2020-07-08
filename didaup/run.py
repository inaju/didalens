import webbrowser
import time
from datetime import datetime
from selenium import webdriver

time="21:54"
i=0
try:
    while True:
        if datetime.now().time().strftime("%H:%M:%S") == str(datetime.strptime(time, "%H:%M").time()):

            webbrowser.open('http://127.0.0.1:8000/goals/goalreminder/')
            print('done')
            i += 1
            
            
            
except:
    print('waiting')
    print(datetime.now().time().strftime("%H:%M:%S"))

