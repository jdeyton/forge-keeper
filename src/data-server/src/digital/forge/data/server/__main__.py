#!/usr/bin/env python3
# coding: utf-8
"""
This module serves as the main entry point for the server process.
"""
import argparse
from pathlib import Path
import sys

import connexion
import validators

from digital.forge.app.factory import Factory as AppFactory
from digital.forge.app.decorator.cors import CORSDecorator
from digital.forge.app.decorator.sqlalchemy import SQLAlchemyDecorator
from digital.forge.data.server import encoder


def _get_secret(name):
    secret_file = Path('/run/secrets').joinpath(name)
    with open(secret_file) as file:
        return file.readline().strip()


def main(argv=None):
    """
    The standard main method.
    """
    if argv is None:
        argv = sys.argv[1:]
    args = _parse_args(argv)

    factory = AppFactory()
    factory.add_decorator(CORSDecorator())
    db_user = _get_secret('psql-conductor-user')
    db_pass = _get_secret('psql-conductor-pass')
    db_host = _get_secret('psql-host')
    db_port = _get_secret('psql-port')
    db_name = _get_secret('psql-name')
    factory.add_decorator(SQLAlchemyDecorator(
        'postgresql://%s:%s@%s:%s/%s' %
        (db_user, db_pass, db_host, db_port, db_name)
    ))

    app = factory.create_app(name=__name__)
    app.json_encoder = encoder.JSONEncoder
    connexion_app = connexion.App(__name__, specification_dir='../openapi/')

    # Set these since we want to replace connexion's built-in flask app and run
    # method.
    connexion_app.app = app
    connexion_app.host = args.host
    connexion_app.port = args.port

    connexion_app.add_api(
        'openapi.yaml',
        arguments={'title': 'Forge Keeper - Conductor'},
        pythonic_params=True
    )

    factory.start_app(app, host=args.host, port=args.port)


def _parse_args(argv):
    main_parser = argparse.ArgumentParser(add_help=False)

    main_parser.add_argument(
        '-h', '--host',
        default='0.0.0.0',
        type=_parse_host,
    )

    main_parser.add_argument(
        '-p', '--port',
        default=50080,
        type=_parse_port,
    )

    return main_parser.parse_args(argv)


def _parse_host(value):
    if not validators.domain(value) and not validators.ipv4(value):
        raise argparse.ArgumentTypeError(
            'Host must be an FQDN or IPv4 address'
        )
    return value


def _parse_port(value):
    try:
        value = int(value)
        if not 1 <= value <= 65535:
            raise ValueError
    except ValueError:
        raise argparse.ArgumentTypeError(
            'Port must be an integer between 1 and 65535'
        )
    return int(value)


if __name__ == '__main__':
    main()
