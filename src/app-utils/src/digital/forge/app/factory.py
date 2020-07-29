# coding: utf-8
"""
This module provides a factory for creating a Flask application in a data-
driven fashion. It also provides support for attaching additional behaviors
called "decorators" depending on the needs of the application.
"""
import flask
import validators
# See comment at bottom of start_app
# import gevent.pywsgi

from digital.forge.app.abstract_decorator import Decorator


class Factory:
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
        if decorator is None or not isinstance(decorator, Decorator):
            raise ValueError('Decorator must be a Decorator instance')
        self._decorators.append(decorator)

    def create_app(self, name, *_args, **_kwargs):
        '''
        Create a flask application.

        A factory method is used to extract the core logic from the OpenAPI
        code generation to a more controlled method where we can decorate the
        flask app with additional features.

        :param name: The name of the app. Must not be null.

        :rtype: A Flask instance.
        '''
        if name is None:
            raise ValueError('App name must not be null')
        name = str(name)

        app = flask.Flask(name)

        for decorator in self._decorators:
            decorator.decorate(app)

        return app

    @staticmethod
    def start_app(app, host=None, port=None, **_kwargs):
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
            raise ValueError('App must be Flask instance')

        if host is None:
            host = '0.0.0.0'
        elif not validators.domain(host) and not validators.ipv4(host):
            raise ValueError('Host must be an FQDN or IPv4 address')

        if port is None:
            port = 8080
        else:
            try:
                if not isinstance(port, int):
                    raise ValueError
                if not 1 <= port <= 65535:
                    raise ValueError
            except ValueError:
                raise ValueError('Port must be an integer between 1 and 65535')

        # I don't feel like fighting with Visual C++ tools to get this working
        # from Windows, so for now I'm going to use the Flask dev server.
        # server = gevent.pywsgi.WSGIServer((host, port), app)
        # server.serve_forever()
        app.run()
