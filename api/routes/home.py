from app import app, db
from flask import request, jsonify, Response

from utils import hashPass, createPaper, createToken
from models.user import User
from models.session import Session


# TODO Убрать логику в другие слои из рутов
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    resp = Response('<h1>Hello1, user</h1><br><p>Your browser is ' + user_agent + '</p>')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/signin', methods=['POST'])
def sign_in():
    data = request.get_json()
    # TODO Убрать в валидацию
    if 'email' not in data or 'pass' not in data:
        return jsonify(data={'is_success': False, 'msg': ['Bad request']}, status=400)

    try:
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            return jsonify(data={'is_success': False, 'token': '', 'msg': ['Wrong e-mail or password']}, status=403)

        password = hashPass(data['pass'], user.paper)
        if password == user.password:
            token = createToken(data['email'])
            session = Session(user_id=user.id, token=token)
            db.session.add(session)
            db.session.commit()
            return jsonify(data={'is_success': True, 'token': token, 'msg': []}, status=200)
        else:
            return jsonify(data={'is_success': False, 'token': '', 'msg': ['Wrong e-mail or password']}, status=403)
    except:
        return jsonify(data={'is_success': False, 'token': '', 'msg': ['DB Error']}, status=500)


@app.route('/signup', methods=['POST'])
def sign_up():
    data = request.get_json()
    # TODO перенести на слой валидации
    if 'email' not in data or 'pass' not in data or 'name' not in data:
        return jsonify(data={'is_success': False, 'msg': ['Bad request']}, status=400)
    old_user = User.query.filter_by(email=data['email']).first()

    if old_user:
        return jsonify(data={'is_success': False, 'msg': ['Email exist in DB']}, status=403)

    paper = createPaper()
    password = hashPass(data['pass'], paper)
    token = createToken(data['email'])
    user = User(email=data['email'], password=password, paper=paper, name=data['name'])

    try:
        db.session.add(user)
        db.session.commit()
        session = Session(user_id=user.id, token=token)
        db.session.add(session)
        db.session.commit()

        return jsonify(data={'is_success': True, 'token': token, 'msg': ['SignUp success']}, status=200)
    except:
        return jsonify(data={'is_success': False, 'token': '', 'msg': ['DB Error']}, status=500)


