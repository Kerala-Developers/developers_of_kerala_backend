from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = MongoClient(os.environ.get('MONGODB_URI'), 8000)
db = client.kerala_devs


# db has been initialized and can be imported and used in main.py
# examples of usage : https://www.w3schools.com/python/python_mongodb_getstarted.asp
