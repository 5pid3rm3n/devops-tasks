from pymongo import MongoClient


class mongo():

    def __init__(self) -> object:

        _client = MongoClient()

        # set db name 
        _db = _client['items']

        # return db collection
        _collection = _db.test_collection

        self.insert = _collection.insert_one
        self.find = _collection.find
