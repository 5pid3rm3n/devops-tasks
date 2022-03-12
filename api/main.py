
from fastapi import FastAPI
from api.mongo import mongo
from bson.json_util import dumps

api = FastAPI()
db = mongo()


@api.get("/get-buy-list")
async def get_items():
    try:
        user_items_list = list(db.find({}))

        return dumps(user_items_list)
    except:
        return 'No Items'
