from pymongo import MongoClient

def get_best_places(distrito, client,db,reviews):
    
    pipeline = [
        {"$match": {"location": distrito}},  
        {"$group": {"_id": "$restaurant", "average_rating": {"$avg": "$rating"}}},
        {"$sort": {"average_rating": -1}},
        {"$limit": 10}  
    ]
    mejores_restaurantes = list(reviews.aggregate(pipeline))
    return mejores_restaurantes
