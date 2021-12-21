from app import app, db
from flask import jsonify


@app.route('/user/<token>')
def get_public_info(token):
      return jsonify({'info': token}, 200)


@app.route('/user/data', methods=['PUT'])
def change_user_data():
      return '<h1>Data</h1>'


@app.route('/user/pass', methods=['DELETE'])
def change_user_pass():
      return '<h1>Pass</h1>'




