from pymongo import MongoClient

def get_best_places(district, client, db):
    """
    Get the best places to eat in a given district based on average rating and number of visits.

    Args:
        district (str): The district to search for best places.
        client (MongoClient): The MongoDB client object.
        db (Database): The MongoDB database object.

    Returns:
        list: A list of dictionaries containing information about the best places, including restaurant name,
              average rating, and number of visits.
    """
    # Define the aggregation pipeline
    pipeline = [
        {"$match": {"location": district, "rating": {"$exists": True}}},
        {"$addFields": {
            "rating_parsed": {
                "$cond": {
                    "if": {"$eq": [{"$type": "$rating"}, "string"]},
                    "then": {"$toDouble": "$rating"},
                    "else": "$rating"
                }
            }
        }},
        {"$group": {
            "_id": "$restaurant",
            "average_rating": {"$avg": "$rating_parsed"},
            "count_visits": {"$sum": 1}
        }},
        {"$sort": {"average_rating": -1}}
    ]

    # Execute the aggregation pipeline
    best_places = list(db.reviews.aggregate(pipeline))

    # Update average_rating field to handle cases where no rating is available
    for places in best_places:
        places["average_rating"] = places.get("average_rating", "No rating")

    return best_places

