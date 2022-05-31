from app import app
from flask import request, jsonify
from services.ApiService import ApiService


@app.route('/api', methods=['POST'])
def add_new_api_key():
  print(request.headers['API_KEY'])
  api_service = ApiService(request.remote_addr, request.headers['API_KEY'])
  data = api_service.add_new_api_key()
  return jsonify(data=data, status=data["status"])


@app.route('/api/<ip>', methods=['GET'])
def get_api_key():
  pass


@app.route('/api', methods=['PUT'])
def change_api_key():
  pass


@app.route('/api', methods=['DELETE'])
def delete_api_key():
  pass