import re
from datetime import date
import boto3
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from credentials import get_mongodb_credentials
from helpers import get_best_places

app = Flask(__name__)

# Get MongoDB credentials
mongodb_credentials = get_mongodb_credentials('mongodb_access')
client = MongoClient(mongodb_credentials)

db = client['placestoeat']
reviews = db.reviews

# List of districts in Málaga
states = ["Centro", "Málaga Este", "Ciudad Jardín", "Bailén-Miraflores", "Palma-Palmilla", "Cruz del Humilladero", "Carretera de Cádiz", "Churriana", "Campanillas", "Puerto de la Torre", "Teatinos-Universidad"]

# Endpoint for autocomplete functionality
@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    query = request.args.get("query")
    if query:
        regex_query = "^" + re.escape(query)
        suggestions_cursor = reviews.distinct("restaurant", {"restaurant": {"$regex": regex_query, "$options": "i"}})
        suggestions = list(suggestions_cursor)[:10]
        return jsonify(suggestions)
    else:
        return jsonify([]) 

# Main route for displaying restaurant search results
@app.route("/", methods=["GET", "POST"])
def placestoeat():
    if request.method == "GET":
        return render_template("placestoeat.html", states=states)
    
    district = request.form.get("district")
    place_name = request.form.get("place_name")
    
    if place_name:
        reviews_found = list(reviews.find({"restaurant": place_name}))
        return render_template("place_results.html", place_name=place_name, reviews=reviews_found)
    if district:
        best_places = get_best_places(district, client,db)
        return render_template("district_results.html", location=district, best_places=best_places)
    else:
        message = "Unknown error"
        return render_template("error.html", message=message)

# Route for submitting restaurant reviews
@app.route("/submit.html", methods=["GET", "POST"])
def submit():
    if request.method == "GET":
        return render_template("submit.html", states=states)
    else:
        restaurant_review = {}
        restaurant = request.form.get("restaurant")
        location = request.form.get("location")
        rating = request.form.get("rating")
        visit_date = request.form.get("visit_date")
        comment = request.form.get("comment").lower()

        # Validation for restaurant name
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if regex.search(restaurant) is not None:
            message = "Please enter a valid restaurant name."
            return render_template("error.html", message=message)

        # Validation for visit date
        try:
            visit_date = date.fromisoformat(visit_date)
        except ValueError:
            message = "Please enter a valid visit date in the format YYYY-MM-DD."
            return render_template("error.html", message=message)

        restaurant_review["restaurant"] = restaurant
        restaurant_review["location"] = location
        restaurant_review["rating"] = rating
        restaurant_review["visit_date"] = visit_date.strftime("%Y-%m-%d")
        restaurant_review["comment"] = comment

        reviews.insert_one(restaurant_review)

        print("Restaurant Review:", restaurant_review)

        return render_template("thank_you.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0')




