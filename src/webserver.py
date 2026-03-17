from flask import Flask, request, jsonify
from flask_cors import CORS
from .weather import *

app = Flask(__name__)
cors = CORS(app)
#print("********APP************", app.__doc__)

@app.route("/") #Si me pides /
def hello_root():
    return '<h1>Hola, este es el endpoint de la ruta raiz de Proyecto Flask 2</h1>'

@app.route("/cities", methods=['GET'])#Si me pides /cities con GET
def get_cities():
    return jsonify(get_all_cities()), 200

@app.route("/cities/<city_id>", methods=['GET']) #Si me pides /cities/ALGO con GET
def get_city(city_id):
    city = get_city_by(city_id)
    if city is None:
        return jsonify({"error": "Ciudad no encontrada"}), 404
    return jsonify(city), 200

@app.route("/cities", methods=["POST"]) #Si me pides /cities con POST
def new_city():
    data = request.get_json(silent=True) or {}
    required = ["id", "name", "temperature", "rain_probability"]
    missing = [field for field in required if field not in data]
    if missing:
        return jsonify({"error": "Faltan campos requeridos", "missing": missing}), 400

    created = post_city(data)
    if not created:
        return jsonify({"error": "No se pudo crear la ciudad (id duplicado o error de base de datos)"}), 409

    return jsonify({"message": "Ciudad creada"}), 201

@app.route("/cities/<city_id>", methods=["PUT"])#Si me pides /cities/ALGO con PUT
def update_citi(city_id):
    data = request.get_json(silent=True) or {}

    if "id" in data and data["id"] != city_id:
        return jsonify({"error": "El id del body debe coincidir con el id de la URL"}), 400

    required = ["name", "temperature", "rain_probability"]
    missing = [field for field in required if field not in data]
    if missing:
        return jsonify({"error": "Faltan campos requeridos", "missing": missing}), 400

    updated = update_city(city_id, data)
    if not updated:
        return jsonify({"error": "Ciudad no encontrada"}), 404

    return jsonify({"message": "Ciudad actualizada"}), 200

@app.route("/cities/<city_id>", methods=['DELETE'])#Si me pides /cities/ALGO con DELETE
def delete_city(city_id):
    deleted = del_city(city_id)
    if not deleted:
        return jsonify({"error": "Ciudad no encontrada"}), 404
    return "", 204