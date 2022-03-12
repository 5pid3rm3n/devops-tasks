import requests

def consume():
    return requests.get('http://api:3000/get-buy-list').json()
