#!/usr/bin/env python3
# coding: utf-8
"""
This module serves as the main entry point for the server process.
"""

import connexion

from digital.forge.data import encoder
from digital.forge.app.factory import Factory as AppFactory
from digital.forge.app.decorator.cors import CORSDecorator
from digital.forge.app.decorator.sqlalchemy import SQLAlchemyDecorator


def main():
    """
    The standard main method.
    """
    host = "0.0.0.0"
    port = 65001

    factory = AppFactory()
    factory.add_decorator(CORSDecorator())
    factory.add_decorator(SQLAlchemyDecorator(
        'postgresql://conductor:conductor@localhost:5432/forge_data'
    ))

    app = factory.create_app(name=__name__)
    app.json_encoder = encoder.JSONEncoder
    connexion_app = connexion.App(__name__, specification_dir='../openapi/')

    # Set these since we want to replace connexion's built-in flask app and run
    # method.
    connexion_app.app = app
    connexion_app.host = host
    connexion_app.port = port

    connexion_app.add_api(
        'openapi.yaml',
        arguments={'title': 'Forge Keeper - Conductor'},
        pythonic_params=True
    )

    factory.start_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
