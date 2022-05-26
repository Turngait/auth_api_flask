from werkzeug.wrappers import Request, Response

class CheckAPIKEY:
    def __init__(self, app, api_key):
        self.app = app
        self.api_key = api_key

    def __call__(self, environ, start_response):
        request = Request(environ)
        if 'API_KEY' in request.headers and self.api_key == request.headers['API_KEY']:
            return self.app(environ, start_response)
        res = Response(u'Incorrect Api key', mimetype='text/plain', status=401)
        return res(environ, start_response)
