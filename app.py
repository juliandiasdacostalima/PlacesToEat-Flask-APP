import re
from datetime import date
import datetime
import boto3
from flask import Flask, render_template, request
from pymongo import MongoClient
from helpers import get_best_places
from credentials import get_mongodb_credentials
from flask import jsonify

app = Flask(__name__)

client = MongoClient('mongodb+srv://jdiasdacostalima:GjRmfQSK6tPDdXeB@my-first-cluster.7bjtoy9.mongodb.net/?retryWrites=true&w=majority&appName=my-first-cluster')
db = client['placestoeat']
reviews = db.reviews
states = ["Centro", "Málaga Este", "Ciudad Jardín", "Bailén-Miraflores", "Palma-Palmilla", "Cruz del Humilladero", "Carretera de Cádiz", "Churriana", "Campanillas", "Puerto de la Torre", "Teatinos-Universidad"]

#%%


@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    query = request.args.get("query")
    if query:
        # Realiza la búsqueda de autocompletado en tu base de datos MongoDB
        # Puedes buscar nombres de restaurantes que coincidan parcialmente con la cadena de consulta
        regex_query = "^" + re.escape(query)
        suggestions_cursor = reviews.distinct("restaurant", {"restaurant": {"$regex": regex_query, "$options": "i"}})
        suggestions = list(suggestions_cursor)[:10]  # Limita las sugerencias a un máximo de 10
        return jsonify(suggestions)
    else:
        return jsonify([])  # Retorna una lista vacía si no hay una consulta válida
#%%

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
        mejores_restaurantes = get_best_places(district, client,db, reviews)
        return render_template("district_results.html", location=district, mejores_restaurantes=mejores_restaurantes)
    else:
        message = "You broke the app"
        return render_template("error.html", message=message)

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

        # Validación del nombre del restaurante
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if regex.search(restaurant) is not None:
            message = "Please enter a valid restaurant name."
            return render_template("error.html", message=message)

        # Validación de la fecha de visita
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


if __name__ == "__main__":
    app.run()


