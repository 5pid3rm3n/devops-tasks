
from fastapi import FastAPI
from api.mongo import mongo

api = FastAPI()
db = mongo()


@api.get("/get-buy-list")
async def get_items():
    try:
        user_items = db.find({})
        return user_items
    except:
        return 'None'
