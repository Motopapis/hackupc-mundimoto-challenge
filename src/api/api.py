from flask import Blueprint, request, abort, jsonify
from src.controllers.PostgresqlController import postgresql_controller

api = Blueprint("api", __name__)

@api.route("/brands", methods=['GET'])
def brands():
    if (request.method == 'GET'):
        brands, valid = postgresql_controller.get_brands()
        if brands == None:
            abort(404)

        if valid == False:
            abort(400)

        return jsonify(brands), 200

@api.route("/catalogue", methods=['GET'])
def catalogue():
    if (request.method == 'GET'):
        bikes, valid = postgresql_controller.get_all_catalogue()
        if bikes == None:
            abort(404)

        if valid == False:
            abort(400)

        return jsonify(bikes), 200