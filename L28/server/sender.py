import requests
import time


BASE_URL = "http://127.0.0.1:8000"  # to run locally


def get(url):
    start = time.time()
    response = requests.get(url)
    end = time.time()
    print(f"GET request processed within {end - start} seconds")
    return response.status_code, response.text


def post(url, data):
    start = time.time()
    response = requests.post(url, data=data, headers={'Content-Length': str(len(data))})
    print(response.status_code)
    end = time.time()
    print(f"Processed within {end - start} seconds")
    return response.status_code, response.text


# status_code, content = get(BASE_URL)
# print(f"Status code: {status_code}")
# print(f"Content: {content}")

data = "4353454"
status_code, content = post(BASE_URL, data)
print(f"Status code: {status_code}")
print(f"Content: {content}")
