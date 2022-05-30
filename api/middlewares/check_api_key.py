from werkzeug.wrappers import Request, Response
# from services.ApiService import ApiService

class CheckAPIKEY:
    def __init__(self, app, master_api_key):
        self.app = app
        self.master_api_key = master_api_key

    def __call__(self, environ, start_response):
        request = Request(environ)
        print(request.remote_addr)
        # TODO improve dependencies
        # api_service = ApiService(request.remote_addr, self.master_api_key)
        if 'API_KEY' in request.headers and self.master_api_key == request.headers['API_KEY']:
            return self.app(environ, start_response)
        res = Response(u'Incorrect Api key', mimetype='text/plain', status=401)
        return res(environ, start_response)
