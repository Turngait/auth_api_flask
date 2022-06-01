from app import app, db
from flask import request, jsonify
from models.session import Session
from models.user import User
from services.UserService import UserService
from middlewares.check_api_key import check_api_key


@app.route('/user/<token>')
def get_public_info(token):
    # TODO Move all that middlewares to another layer
    if not check_api_key(request.remote_addr, request.headers['API_KEY']):
        return jsonify(data={'is_success': False, 'token': '', 'msg': ['Wrong api key']}, status=403)

    if not token and not isinstance(token, str):
        return jsonify(data={'is_success': False, 'msg': ['Bad request']}, status=400)
    
    controller = UserService()
    response = controller.get_public_info(token)
    return jsonify(data=response['data'], status=response['status'])


@app.route('/user/name', methods=['PUT'])
def change_user_name():
    if not check_api_key(request.remote_addr, request.headers['API_KEY']):
        return jsonify(data={'is_success': False, 'token': '', 'msg': ['Wrong api key']}, status=403)

    data = request.get_json()
    controller = UserService()
    response = controller.change_user_name(data)
    return jsonify(data=response['data'], status=response['status'])


@app.route('/user/pass', methods=['DELETE'])
def change_user_pass():
    if not check_api_key(request.remote_addr, request.headers['API_KEY']):
        return jsonify(data={'is_success': False, 'token': '', 'msg': ['Wrong api key']}, status=403)

    data = request.get_json()
    controller = UserService()
    response = controller.change_user_pass(data)
    return jsonify(data=response['data'], status=response['status'])
