# coding: utf-8
"""
This package provides a test app for testing controller behavior.
"""
import logging

import connexion
from flask_testing import TestCase

from digital.forge.data.server.encoder import JSONEncoder


class BaseTestCase(TestCase):
    """
    The base class for unit tests (which in Python are classes, of course).
    """

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        openapi_dir = '/home/x88/data/git/forge-keeper/src/data-server/src/digital/forge/data/openapi'
        app = connexion.App(__name__, specification_dir=openapi_dir)
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml', pythonic_params=True)
        return app.app
