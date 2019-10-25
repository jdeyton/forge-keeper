import flask
import sqlite3


class Store(object):

    def __init__(self):
        if 'DATABASE' not in flask.current_app.config:
            msg = 'Current flask app is not configured with a database.'
            raise Exception(msg)
        return

    def get_db(self):
        if 'db' not in flask.g:
            db = sqlite3.connect(self.get_db_path())
            db.row_factory = sqlite3.Row
            flask.g.db = db
        return flask.g.db

    def get_db_path(self):
        return flask.current_app.config['DATABASE']

    def close_db(self):
        db = flask.g.pop('db', None)
        if db is not None:
            db.close()


class StoreDecorator(object):

    def __init__(self):
        pass

    def decorate_app(self, app, path, schema=None):

        # Local database path.
        app.config['DATABASE'] = path

        # Automatically close the DB connection on request completion.
        @app.teardown_appcontext
        def close_db(exception=None):
            Store().close_db()

        # Init the DB contents from the schema resource if specified.
        if schema is not None:
            with app.app_context(), \
                app.open_resource(schema) as f, \
                    Store().get_db() as db:
                db.executescript(f.read().decode('utf8'))

        return
