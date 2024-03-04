from pymongo import MongoClient
import json
from credentials import get_mongodb_credentials

def insert_reviews_from_file(file_path, collection):
    """Inserta revisiones desde un archivo JSON a la colección de la base de datos MongoDB."""
    try:
        with open(file_path, encoding='utf-8') as file:
            for line in file:
                data = json.loads(line)
                collection.insert_one(data)
        print("Inserción exitosa de revisiones desde el archivo:", file_path)
    except FileNotFoundError:
        print("Archivo no encontrado:", file_path)
    except Exception as e:
        print("Error al insertar revisiones:", e)

def main():
    try:
        # Obtener credenciales de MongoDB
        mongodb_credentials = get_mongodb_credentials('mongodb_access')

        # Conectar a MongoDB
        client = MongoClient(mongodb_credentials)

        db = client['placestoeat']
        collection = db['reviews']

        # Ruta del archivo JSON
        file_path = 'examples.txt'

        # Insertar revisiones desde el archivo JSON a la colección de la base de datos
        insert_reviews_from_file(file_path, collection)

    except Exception as e:
        print("Error:", e)
    finally:
        # Cerrar la conexión con MongoDB
        client.close()
main()



