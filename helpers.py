from pymongo import MongoClient

def get_best_places(distrito, client, db):
    pipeline = [
        {"$match": {"location": distrito, "rating": {"$exists": True}}},
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

    mejores_restaurantes = list(db.reviews.aggregate(pipeline))
    for restaurante in mejores_restaurantes:
        restaurante["average_rating"] = restaurante.get("average_rating", "No rating")
    return mejores_restaurantes

