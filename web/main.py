import random
from fastapi import FastAPI
from web.producer import producer, on_send_success, on_send_error

random_items = {'Shoes': 179, 'Bicycle': 1099, 'Surfboard': 755,
                'Hat': 43, 'Watch': 230, 'Laptop': 3700}

app = FastAPI()
prodocer = producer()


@app.get("/buy/")
async def buy_item():

    # get random item
    item, price = random.choice(list(random_items.items()))
    
    # produce new item to kafka
    prodocer.send('my-topic', {item: price}).add_callback(on_send_success).add_errback(on_send_error)

    # return item purchased  
    return {item: price}


@app.get("/get-all-user_buys/")
async def get_all_user_buys():

    return 'user_buys'
