from fastapi import FastAPI
from api.mongo import mongo
from bson.json_util import dumps

api = FastAPI()
db = mongo()

@api.get("/get-buy-list")
async def get_items():
    try:
        # Fetch all items from the database
        user_items_list = list(db.find({}))

        # Return items as JSON
        return dumps(user_items_list)
    except:
        # Return message if no items are found
        return 'No Items'
