# coding: utf-8
"""
This module... TODO
"""
import argparse
import contextlib
from datetime import datetime, timedelta
import getpass
import sys

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from digital.forge.data.sql.model import Archive, Event

from monitor import __version__


@contextlib.contextmanager
def _connection(Session):
    """
    A context manager for database connections.
    """
    session = Session()
    try:
        yield session
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()


def main(argv=None):
    """
    The main function!
    """
    if argv is None:
        argv = sys.argv[1:]
    args = _parse_args(argv)

    # Set up a way to connect to the database.
    db_pass = getpass.getpass(prompt='Password: ')
    uri = 'postgresql://%s:%s@%s:%s/%s' % \
        (args.db_user, db_pass, args.db_host, args.db_port, args.db_name)
    engine = create_engine(uri)
    Session = sessionmaker(bind=engine)

    # Filter inputs:
    drone = 'd42cd874-d6a2-4b93-9398-7650a4f81170'
    data_start = datetime.now() + timedelta(days=-1)

    # Query the relevant Events.
    # This could be simpler if we establish the 'relationship' in the ORM pkg.
    with _connection(Session) as db:
        for record in db.query(Event.event_time, Event.event_value, Archive.units, Archive.name).\
                join(Archive, Event.archive_uuid == Archive.archive_uuid).\
                filter(Event.drone_uuid == drone).\
                filter(Event.event_time >= data_start).\
                order_by(Event.event_time.asc()):
            print('Event: {}: {} ({} {})'.format(
                record.event_time,
                record.event_value,
                record.units,
                record.name
            ))


def _parse_args(argv):
    main_parser = argparse.ArgumentParser(
        description='This utility doe something neat.',
    )
    main_parser.add_argument(
        '-v', '--version',
        action='version',
        help='Get the version',
        version='%(prog)s ' + __version__
    )

    main_parser.add_argument(
        '--db-host',
        default='db',
        help='The database host.',
        metavar='DB_HOST',
        type=str,
    )

    main_parser.add_argument(
        '--db-port',
        default='5432',
        help='The database port.',
        metavar='DB_PORT',
        type=int,
    )

    main_parser.add_argument(
        '--db-user',
        default='postgres',
        help='The database user.',
        metavar='DB_USER',
        type=str,
    )

    main_parser.add_argument(
        '--db-name',
        default='postgres',
        help='The database name.',
        metavar='DB_NAME',
        type=str,
    )

    return main_parser.parse_args(argv)


if __name__ == '__main__':
    main()
