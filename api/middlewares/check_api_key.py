import os
from werkzeug.wrappers import Request, Response


class CheckAPIKEY:
    def __init__(self, app):
        self.app = app
        self.api_key = os.environ.get("API_KEY")

    def __call__(self, environ, start_response):
        request = Request(environ)
        if 'API_KEY' in request.headers and self.api_key == request.headers['API_KEY']:
            return self.app(environ, start_response)
        res = Response(u'Incorrect Api key', mimetype='text/plain', status=401)
        return res(environ, start_response)
