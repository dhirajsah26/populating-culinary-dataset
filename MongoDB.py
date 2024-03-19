import pymongo

class MongoDBClient:
    def __init__(self, database_name, collection_name):
        # MongoDB connection string for local connection
        connection_string = "mongodb://localhost:27017/"

        # Connect to MongoDB
        self.client = pymongo.MongoClient(connection_string)

        # Access a specific database
        self.database = self.client.get_database(database_name)

        # Access a specific collection within the database
        self.collection = self.database[collection_name]

    def insert_document(self, document):
        # Insert a document into the collection
        self.collection.insert_one(document)

    def find_documents(self):
        # Find documents in the collection
        return self.collection.find()

    def close_connection(self):
        # Close MongoDB client
        self.client.close()

def main():
    # Specify database and collection names
    database_name = "my_database"
    collection_name = "my_collection"

    # Instantiate MongoDBClient
    mongo_client = MongoDBClient(database_name, collection_name)

    # Example: Insert a document into the collection
    document = {"name": "John", "age": 30}
    mongo_client.insert_document(document)

    # Example: Find documents in the collection
    documents = mongo_client.find_documents()
    for doc in documents:
        print(doc)

    # Close MongoDB connection
    mongo_client.close_connection()

if __name__ == "__main__":
    main()