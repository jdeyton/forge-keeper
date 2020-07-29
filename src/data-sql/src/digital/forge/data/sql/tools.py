# coding: utf-8
"""
This module includes helpful database methods.
"""
from digital.forge.data.sql.model import Base


def destroy_database(engine):
    """
    Deletes the database structure defined in this package.

    Attempt to drop all database tables defined in this package. This will
    throw an exception if the tables do not exist.

    :param engine: The engine used to connect to the database.
    """
    Base.metadata.drop_all(bind=engine, checkfirst=False)


def initialize_database(engine):
    """
    Creates the database structure defined in this package.

    Attempt to create the database tables defined in this package. This will
    throw an exception if the tables already exist.

    :param engine: The engine used for connect to the database.
    """
    Base.metadata.create_all(bind=engine, checkfirst=False)
