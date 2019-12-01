import flask_cors

from digital.forge.http.server.app_decorator import AppDecorator


class CORSDecorator(AppDecorator):
    '''
    A decorator for enabling Cross Origin Resource Sharing (CORS) for an app.

    CORS is useful primarily during development as most browsers by default
    will reject requests, such as using the Swagger Editor or Swagger UI to
    make an API request.
    '''

    def decorate(self, app):
        flask_cors.CORS(app)
