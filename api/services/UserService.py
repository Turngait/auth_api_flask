from models.user import User
from models.session import Session
from utils import hashPass, createPaper, createToken
from app import db


# Service with main logic
# TODO add DTO
class UserService:
    def sign_up(self, data) -> dict:
        # TODO move validation to other layer
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

    def change_user_name(self, data) -> dict:
        if 'name' not in data or 'token' not in data:
            return {'data': {'is_success': False, 'msg': ['Bad request']}, 'status': 400}

        try:
            session = Session.query.filter_by(token=data['token']).first()
            if not session:
                return {'data': {'is_success': False, 'token': '', 'msg': ['Wrong token or token hab been expired']}, 'status': 403}

            user = User.query.filter_by(id=session.user_id).first()
            user.name=data['name']
            db.session.add(user)
            db.session.commit()

            return {'data': {'is_success': True, 'msg': ['Name is changed']}, 'status': 200}
        except:
            return {'data': {'is_success': False, 'msg': ['DB Error']}, 'status': 500}


    def change_user_pass(self, data) -> dict:
        if 'pass' not in data or 'token' not in data:
            return {'data': {'is_success': False, 'msg': ['Bad request']}, 'status': 400}

        try:
            session = Session.query.filter_by(token=data['token']).first()            
            if not session:
                return {'data': {'is_success': False, 'token': '', 'msg': ['Wrong token or token hab been expired']}, 'status': 403}
            
            user = User.query.filter_by(id=session.user_id).first()
            password = hashPass(data['pass'], user.paper)
            user.password=password
            db.session.add(user)
            db.session.commit()

            return {'data': {'is_success': True, 'msg': ['Password is changed']}, 'status': 200}
        except:
            return {'data': {'is_success': False, 'token': '', 'msg': ['DB Error']}, 'status': 500}

    
    def get_public_info(self, token):
        try:
            session = Session.query.filter_by(token=token).first()
            if not session:
                return {'data': {'is_success': False, 'token': '', 'msg': ['Wrong token or token hab been expired']}, 'status': 403}

            user = User.query.filter_by(id=session.user_id).first()
            if not user:
                return {'data': {'is_success': False, 'token': '', 'msg': ['User does not exist']}, 'status': 403}
            
            public_data = {
                'user_id': user.id,
                'name': user.name,
                'email': user.email,
                'created_at': user.created_at,
                'session_expired_at': session.expired_at
            }

            return {'data': {'is_success': True, 'token': token, 'msg': [], 'public_data': public_data}, 'status': 200}

        except:
            return {'data': {'is_success': False, 'token': '', 'msg': ['DB Error']}, 'status': 500}