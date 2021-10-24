import requests
import time
import datetime
try:
    a = requests.get('https://www.youtube.com')
    print(a)
except Exception as y:
    print(y,type(y))
