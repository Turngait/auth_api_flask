from app import app, db
from flask import request, jsonify, Response
from services.UserService import UserService


@app.route('/')
def index():
    #Testing
    user_agent = request.headers.get('User-Agent')
    resp = Response('<h1>Hello1, user</h1><br><p>Your browser is ' + user_agent + '</p>')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/init')
def init():
    try:
        db.create_all()
        resp = Response('DB created')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except:
        resp = Response('Server error')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

@app.route('/signin', methods=['POST'])
def sign_in():
    data = request.get_json()
    controller = UserService()
    response = controller.sign_in(data)
    return jsonify(data=response['data'], status=response['status'])


@app.route('/signup', methods=['POST'])
def sign_up():
    data = request.get_json()
    controller = UserService()
    response = controller.sign_up(data)    
    return jsonify(data=response['data'], status=response['status'])
