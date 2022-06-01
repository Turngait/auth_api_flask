from app import app
from flask import request, jsonify
from services.ApiService import ApiService
from config.config import MASTER_API_KEY


@app.route('/api', methods=['POST'])
def add_new_api_key():
  if not request.headers['API_KEY'] == MASTER_API_KEY:
      return jsonify(data={"msg": "Wrong api key"}, status=403)
    
  data_from_req = request.get_json()
  api_service = ApiService(data_from_req['ip'], request.headers['API_KEY'])
  data = api_service.add_new_api_key()
  return jsonify(data=data, status=data["status"])


@app.route('/api/<ip>', methods=['GET'])
def get_api_key(ip):
  if not request.headers['API_KEY'] == MASTER_API_KEY:
      return jsonify(data={"msg": "Wrong api key"}, status=403)

  api_service = ApiService(ip, request.headers['API_KEY'])
  data = api_service.get_api_key()
  return jsonify(data=data, status=data["status"])


@app.route('/api', methods=['PUT'])
def change_api_key():
  if not request.headers['API_KEY'] == MASTER_API_KEY:
      return jsonify(data={"msg": "Wrong api key"}, status=403)

  data_from_req = request.get_json()
  api_service = ApiService(data_from_req['ip'], request.headers['API_KEY'])
  data = api_service.change_api_key()
  return jsonify(data=data, status=data["status"])


@app.route('/api', methods=['DELETE'])
def delete_api_key():
  if not request.headers['API_KEY'] == MASTER_API_KEY:
    return jsonify(data={"msg": "Wrong api key"}, status=403)

  data_from_req = request.get_json()
  api_service = ApiService(data_from_req['ip'], request.headers['API_KEY'])
  data = api_service.delete_aip_key()
  return jsonify(data=data, status=data["status"])