from pymongo import MongoClient

def create_mongo_client():
    client = MongoClient('mongodb://localhost:27017/')
    return client

def create_database(client, database_name):
    db = client[database_name]
    return db

def create_collection(db, collection_name):
    collection = db[collection_name]
    return collection

client = create_mongo_client()
db = create_database(client, 'web_scraper_db')
collection = create_collection(db, 'scraped_pages')
