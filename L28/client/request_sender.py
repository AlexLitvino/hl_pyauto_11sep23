import random
import requests
import string
import time


url = "http://127.0.0.1:8000"  # to run locally
#url = "http://server:8000"  # to run from inside Docker container


for i in range(10):
    if random.random() < 0.5:
        response = requests.get(url)
        print(response.status_code)
    else:
        symbols = string.digits + string.ascii_letters
        data_length = random.randint(10, 100)
        data = ''.join([random.choice(symbols) for _ in range(data_length)])
        response = requests.post(url, data=data, headers={'Content-Length': str(len(data))})
        print(response.status_code)
    time.sleep(1)
