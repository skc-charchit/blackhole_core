import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_mongo_client():
    """
    Function to get the MongoDB client using the URI from the .env file.
    """
    uri = os.getenv("MONGO_URI")
    
    if not uri:
        raise ValueError("MONGO_URI not found in environment variables.")
    
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client

# Test connection and ping
if __name__ == "__main__":
    try:
        client = get_mongo_client()
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error: {e}")
