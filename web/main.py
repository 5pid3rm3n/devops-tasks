from datatime import datatime
from fastapi import FastAPI
from web.producer import producer
from web.api_consumer import consume
import random


random_items = {'Shoes': 179, 'Bicycle': 1099, 'Surfboard': 755,
                'Hat': 43, 'Watch': 230, 'Laptop': 3700}
data = {'username': 'Shopper', 'userid': '00001'}


app = FastAPI()
prodocer = producer()


@app.get("/buy/")
async def buy_item():

    # get random item
    data.item, data.price = random.choice(list(random_items.items()))
    
    # set timestamp
    data.timestamp = str(datatime.utcnow())

    # produce new item to kafka
    prodocer.send('my-topic', data)

    # return item purchased
    return data


@app.get("/get-all-user_buys/")
async def get_all_user_buys():

    user_buys = consume()
    return user_buys
