from models.user import User
from models.session import Session
from utils import hashPass, createPaper, createToken
from app import db

from controllers import Controller

class UserController(Controller):
    def __init__(self) -> None:
        super().__init__()

    def sign_up(self, data) -> dict:
        # TODO перенести на слой валидации
        if 'email' not in data or 'pass' not in data or 'name' not in data:
            return {'data': {'is_success': False, 'msg': ['Bad request']}, 'status': 400}

        old_user = User.query.filter_by(email=data['email']).first()
        if old_user:
            return {'data': {'is_success': False, 'msg': ['Email exist in DB']}, 'status': 403}

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

            return {'data': {'is_success': True, 'token': token, 'msg': ['SignUp success']}, 'status': 200}
        except:
            return {'data': {'is_success': False, 'token': '', 'msg': ['DB Error']}, 'status': 500}


    def sign_in(self, data) -> dict:
        if 'email' not in data or 'pass' not in data:
            return {'data': {'is_success': False, 'msg': ['Bad request']}, 'status': 400}

        try:
            user = User.query.filter_by(email=data['email']).first()
            if not user:
                return {'data': {'is_success': False, 'token': '', 'msg': ['Wrong e-mail or password']}, 'status': 403}

            password = hashPass(data['pass'], user.paper)
            if password == user.password:
                token = createToken(data['email'])
                session = Session(user_id=user.id, token=token)
                db.session.add(session)
                db.session.commit()
                return {'data': {'is_success': True, 'token': token, 'msg': []}, 'status': 200}
            else:
                return {'data': {'is_success': False, 'token': '', 'msg': ['Wrong e-mail or password']}, 'status': 403}
        except:
            return {'data': {'is_success': False, 'token': '', 'msg': ['DB Error']}, 'status': 500}