# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:54:10 2024

@author: julia
"""

from pymongo import MongoClient
import json

# Conectarse a MongoDB Atlas
client = MongoClient('mongodb+srv://jdiasdacostalima:GjRmfQSK6tPDdXeB@my-first-cluster.7bjtoy9.mongodb.net/?retryWrites=true&w=majority&appName=my-first-cluster')


# Seleccionar la base de datos y la colección
db = client.placestoeat
collection = db.reviews

# Abrir el archivo JSON y cargar los documentos línea por línea
with open('examples.txt', encoding='utf-8') as file:  # Asegurar que el archivo se abra con la codificación UTF-8
    for line in file:
        data = json.loads(line)
        collection.insert_one(data)

# Cerrar la conexión
client.close()

