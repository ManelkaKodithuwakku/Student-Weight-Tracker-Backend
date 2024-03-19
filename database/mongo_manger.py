from pymongo import MongoClient


class MongoDBManager:
    def __init__(self, collection):
        self.db = "Test"
        self.collection = collection

        try:
            self.client = MongoClient()
        except Exception as e:
            print(e)
            raise Exception("Connection not established")
        
    def save_to_db(self,data):
        if data!= None:
            _DB = self.client[self.db]
            collection = _DB[self.collection]
            return collection.insert_one(data)
        
    def get_document(self, query):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        return collection.find(query)

