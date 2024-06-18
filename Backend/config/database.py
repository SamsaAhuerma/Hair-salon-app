from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv('MONGO_KEY')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
