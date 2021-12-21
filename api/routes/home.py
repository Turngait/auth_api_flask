from app import app, db
from flask import request, jsonify, Response
# import models.user
# import models.session


@app.route('/')
def index():
      user_agent = request.headers.get('User-Agent')
      resp = Response('<h1>Hello1, user</h1><br><p>Your browser is ' + user_agent + '</p>')
      resp.headers['Access-Control-Allow-Origin'] = '*'
      return resp


@app.route('/signin', methods=['POST'])
def sign_in():
      return jsonify({'test': True}, 200)


@app.route('/signup', methods=['POST'])
def sign_up():
      return jsonify({'test': True}, 200)
