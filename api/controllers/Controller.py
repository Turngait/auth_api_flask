import string


class Controller:
    def __init__(self) -> None:
        self._status = 200
        self._is_success = True
        self._token = ''
        self._msg = []
        self._public_data = {}

    def set_error(self, msg: string, status: int = 500):
        self._set_status(status)
        self._add_msg(msg)
        self._set_is_success(False)

    def set_success(self, msg: string = ''):
        self._set_status(200)
        self._add_msg(msg)
        self._set_is_success(True)

    def add_data(self, token: string, public_data: dict):
        self._set_token(token)
        self._set_public_data(public_data)

    def _set_token(self, token: string) -> None:
        if token:
            self._token = token
    def _set_status(self, status: int) -> None:
        if status:
            self._status = status

    def _set_is_success(self, is_success: bool) -> None:
        if is_success:
            self._is_success = is_success

    def _set_public_data(self, public_data: dict) -> None:
        if public_data:
            self._public_data = public_data

    def _add_msg(self, msg: string) -> None:
        if msg:
            self._msg.append(msg)

    def get_data(self) -> dict:
        return {'is_success': self._is_success, 'msg': self._msg, 'token': self._token, 'public_data': self._public_data}
