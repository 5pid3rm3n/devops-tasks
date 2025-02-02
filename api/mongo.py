from pymongo import MongoClient


class mongo():

    def __init__(self) -> object:
        # Connect to MongoDB
        _client = MongoClient('mongodb://mongo:27017/')

        # Set database name
        _db = _client['items']

        # Return database collection
        _collection = _db.test_collection

        # Define insert and find methods
        self.insert = _collection.insert_one
        self.find = _collection.find
