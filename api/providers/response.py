# Класс по отправки ответов
from flask import jsonify


class Response:
    def __init__(self, token):
        self._success = False
        self._msg = []
        self._token = token
        self._data = {}

    def send_wrong_request(self, msg, status):
        if msg and status and isinstance(status, int):
            self._add_msg(msg)
            self._send(status)

    def _set_success(self, status):
        if status and isinstance(status, int):
            self._success = status

    def _add_msg(self, msg):
        if msg:
            self._msg.append(msg)

    def _set_data(self, data):
        if data:
            self._data = data

    def _send(self, status):
        return jsonify(
            data={
                'is_success': self._success,
                'token': self._token,
                'msg': self._msg,
                'data': self._data
            },
            status=status)
