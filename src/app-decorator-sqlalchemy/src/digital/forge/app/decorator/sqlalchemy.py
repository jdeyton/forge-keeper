# coding: utf-8
"""
This module provides an app decorator that adds SQLAlchemy features to the app.
"""
import flask_sqlalchemy

from digital.forge.app.abstract_decorator import Decorator


class SQLAlchemyDecorator(Decorator):
    """
    A decorator for attaching a SQLAlchemy features to an app.

    Flask-SQLAlchemy includes logic around Flask contexts/sessions and allows
    you to use a declarative SQLAlchemy model. When using this decorator, you
    can access the database during a request by using the following logic:

    session = flask.current_app.db.session
    for foo in session.query(SQLAlchemyFoo).all():
        # do something
    """

    def __init__(self, db_url):
        """
        Create a new SQLAlchemyDecorator.

        :param db_url: The SQLAlchemy database URL used to connect to the
        database.
        """
        if db_url is None:
            raise Exception('Database URL must not be null')
        self._db_url = db_url

    def decorate(self, app):
        """
        Adds SQLAlchemy features to the flask app.
        """
        app.config['SQLALCHEMY_DATABASE_URI'] = self._db_url
        app.db = flask_sqlalchemy.SQLAlchemy(app)
