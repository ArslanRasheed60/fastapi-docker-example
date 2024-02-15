from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from os import getenv
from dotenv import load_dotenv


load_dotenv()


app = FastAPI()

# Connect to MongoDB
client = MongoClient(getenv("MONGO_URI"))
db = client.sample_analytics
collection = db.customers


@app.get("/customers")
async def get_all_customers():
    customers = list(collection.find({}, {"_id": 0}))
    return customers
