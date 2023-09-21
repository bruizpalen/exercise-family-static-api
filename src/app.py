"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    print(type(members[0]["id"]))
    # response_body = {
    #     "hello": "member",
    #     "family": members
    # }
    response_body = members


    return jsonify(response_body), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(id)
    if member:
        return jsonify({"message": "Success", "family": member}), 200
    else:
        return jsonify({"message": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def add_member():
    data = request.json
    if data:
        response = jackson_family.add_member(data)
        return jsonify({"message": "Success", "family": response}), 201
    else:
        return jsonify({"message": "Invalid request data"}), 400

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member_by_id(id):
    response = jackson_family.delete_member(id)
    return jsonify(response), 200 

@app.route('/update/<int:id>', methods=['PATCH'])  
def update_member(id):
    data = request.json
    if data:
        response = jackson_family.update_member(id, data)
        return jsonify(response), 200
    else:
        return jsonify({"message": "Invalid request data"}), 400
    
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
