import flask


def get_db_session():
    '''
    Get a session for interacting with the database.

    This method gets a session suitable for making queries against a database.
    It assumes the app has been decorated using the SQLAlchemyDecorator class.
    '''
    return flask.current_app.db.session
