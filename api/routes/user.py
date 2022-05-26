from app import app, db
from flask import request, jsonify
from models.session import Session
from models.user import User
from models.api import Api
from services.UserService import UserService


@app.route('/user/<token>')
def get_public_info(token):
    if not token and not isinstance(token, str):
        return jsonify(data={'is_success': False, 'msg': ['Bad request']}, status=400)
        
    try:
        session = Session.query.filter_by(token=token).first()
        if not session:
            return jsonify(data={'is_success': False, 'token': '', 'msg': ['Wrong token']}, status=403)

        user = User.query.filter_by(id=session.user_id).first()
        if not user:
            return jsonify(data={'is_success': False, 'token': '', 'msg': ['User not exist']}, status=403)
        
        public_data = {
            'user_id': user.id,
            'name': user.name,
            'email': user.email,
            'created_at': user.created_at,
            'session_expired_at': session.expired_at
        }

        return jsonify(data={'is_success': True, 'token': token, 'msg': [], 'public_data': public_data}, status=200)

    except:
        return jsonify(data={'is_success': False, 'token': '', 'msg': ['DB Error']}, status=500)


@app.route('/user/name', methods=['PUT'])
def change_user_name():
    data = request.get_json()
    controller = UserService()
    response = controller.change_user_name(data)
    return jsonify(data=response['data'], status=response['status'])


@app.route('/user/pass', methods=['DELETE'])
def change_user_pass():
    data = request.get_json()
    controller = UserService()
    response = controller.change_user_pass(data)
    return jsonify(data=response['data'], status=response['status'])
