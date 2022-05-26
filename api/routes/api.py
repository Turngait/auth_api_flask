from crypt import methods
from app import app, db
from flask import request, jsonify


@app.route('/api', methods=['POST'])
def add_new_api_key():
  data = request.get_json()
  return jsonify(data=data, status=200)


@app.route('/api/<ip>', methods=['GET'])
def get_api_key():
  pass


@app.route('/api', methods=['PUT'])
def change_api_key():
  pass


@app.route('/api', methods=['DELETE'])
def delete_api_key():
  pass