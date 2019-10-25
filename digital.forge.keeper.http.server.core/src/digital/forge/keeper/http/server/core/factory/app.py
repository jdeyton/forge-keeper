import flask
import flask_cors
import gevent.pywsgi
import os.path

from digital.forge.keeper.http.server.core.factory.data import StoreDecorator


class AppFactory(object):

    def create_app(self, name=None, host=None, port=None, *args, **kwargs):
        '''
        Create a flask application.

        A factory method is used to extract the core logic from the OpenAPI
        code generation to a more controlled method where we can decorate the
        flask app with additional features.

        :param host: The hostname where the app will run.
        :param port: The port number where the app will be served.

        :rtype: dict A dictionary of app details necessary for running a flask
            app.
        '''
        if name is None:
            name = 'Forge App'
        if host is None:
            host = 'localhost'
        if port is None:
            port = 8080

        app = flask.Flask(name)

        # CORS must be enabled for local development.
        flask_cors.CORS(app)

        # Add a data store.
        if not os.path.exists(app.instance_path):
            os.mkdir(app.instance_path)
        path = os.path.join(app.instance_path, 'store.db')
        schema = 'store.sql'
        StoreDecorator().decorate_app(app, path, schema)

        info = dict(
            app=app,
            host=host,
            port=port,
        )

        return info

    def start_app(self, app_info, *args, **kwargs):
        '''
        Start a previously created flask application.

        The additional arguments and keyword-arguments will be passed to the
        underlying start command.

        :param app_info: The dictionary of app details necessary for running a
            flask app. This should come from a call to create_app(...).
        '''
        app = app_info['app']
        host = app_info['host']
        port = app_info['port']

        server = gevent.pywsgi.WSGIServer((host, port), app)
        server.serve_forever()
