from pymongo import MongoClient
import json
from credentials import get_mongodb_credentials

def insert_reviews_from_file(file_path, collection):
    """Insert reviews from a JSON file into the MongoDB database collection."""
    try:
        with open(file_path, encoding='utf-8') as file:
            for line in file:
                data = json.loads(line)
                collection.insert_one(data)
        print("Successfully inserted reviews from file:", file_path)
    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("Error inserting reviews:", e)

def main():
    try:
        # Get MongoDB credentials
        mongodb_credentials = get_mongodb_credentials('mongodb_access')

        # Connect to MongoDB
        client = MongoClient(mongodb_credentials)

        db = client['placestoeat']
        collection = db['reviews']

        # JSON file path
        file_path = 'examples.txt'

        # Insert reviews from JSON file into database collection
        insert_reviews_from_file(file_path, collection)

    except Exception as e:
        print("Error:", e)
    finally:
        # Close connection with MongoDB
        client.close()

if __name__ == "__main__":
    main()



