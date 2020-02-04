import flask
#import gevent.pywsgi

from .app_decorator import AppDecorator


class AppFactory(object):
    '''
    An app factory is used to create a Flask app.

    An app factory's primary purpose is to allow app creators to attach
    specific functionalities to a Flask app in an abstract fashion. This
    allows, for example, the ability to generate a multi-featured Flask app
    from an OpenAPI spec using a much simpler mustache template for the module
    driver (__main__.py).
    '''

    def __init__(self):
        self._decorators = list()

    def add_decorator(self, decorator):
        '''
        Add a decorator to the factory.

        Decorators are invoked when this factory is used to create an app in
        order to add additional features to the Flask app, such as databases,
        sockets, or CORS support.

        :param decorator: The decorator to add.
        '''
        if decorator is None or not isinstance(decorator, AppDecorator):
            raise Exception('Decorator must be an AppDecorator instance')
        self._decorators.append(decorator)

    def create_app(self, name, *args, **kwargs):
        '''
        Create a flask application.

        A factory method is used to extract the core logic from the OpenAPI
        code generation to a more controlled method where we can decorate the
        flask app with additional features.

        :param name: The name of the app. Must not be null.

        :rtype: A Flask instance.
        '''
        if name is None:
            raise Exception('App name must not be null')
        name = str(name)

        app = flask.Flask(name)

        for decorator in self._decorators:
            decorator.decorate(app)

        return app

    def start_app(self, app, host=None, port=None, *args, **kwargs):
        '''
        Start a previously created flask application.

        The additional arguments and keyword-arguments will be passed to the
        underlying start command.

        :param app: The flask app to run. Normally, this should come from a
        call to create_app(...).
        :param host: The host where the app is served. Default: 0.0.0.0
        :param port: The port where the app is served. Default: 8080
        '''

        if app is None or not isinstance(app, flask.Flask):
            raise Exception('App must be Flask instance')

        if host is None:
            host = '0.0.0.0'
        if port is None:
            port = 8080

        # I don't feel like fighting with Visual C++ tools to get this working
        # from Windows, so for now I'm going to use the Flask dev server.
        #server = gevent.pywsgi.WSGIServer((host, port), app)
        #server.serve_forever()
        app.run()
