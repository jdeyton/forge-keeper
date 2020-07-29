# coding: utf-8
"""
This module provides the CORS decorator implementation.
"""
import flask_cors

from digital.forge.app.abstract_decorator import Decorator


class CORSDecorator(Decorator):
    """
    A decorator for enabling Cross Origin Resource Sharing (CORS) for an app.

    CORS is useful primarily during development as most browsers by default
    will reject requests, such as using the Swagger Editor or Swagger UI to
    make an API request.
    """

    def decorate(self, app):
        flask_cors.CORS(app)
