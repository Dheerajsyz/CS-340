import os
from pymongo import MongoClient

class AnimalShelter:
    def __init__(self):
        """Initialize MongoDB connection using environment variables."""
        host = os.getenv('MONGO_HOST')
        port = int(os.getenv('MONGO_PORT'))
        username = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASS')
        
        # Connect to MongoDB using the credentials from environment variables
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/?authSource=admin')
        self.database = self.client['AAC']  # Set database to 'AAC'
        self.collection = self.database['animals']  # Set collection to 'animals'
        print("MongoDB connection initialized successfully.")

    # Create operation
    def create(self, data):
        if data:
            self.collection.insert_one(data)
            print("Document inserted successfully.")
            return True
        else:
            print("No data provided for insertion.")
            raise Exception("No data provided for insertion.")

    # Read operation (returns all or filtered documents)
    def read(self, query):
        result = list(self.collection.find(query))
        print(f"{len(result)} document(s) retrieved from the collection.")
        return result

    # Update operation
    def update(self, query, update_data):
        update_result = self.collection.update_many(query, {"$set": update_data})
        print(f"{update_result.modified_count} document(s) updated.")
        return update_result

    # Delete operation
    def delete(self, query):
        delete_result = self.collection.delete_many(query)
        print(f"{delete_result.deleted_count} document(s) deleted.")
        return delete_result
