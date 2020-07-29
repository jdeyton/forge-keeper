# coding: utf-8
"""
This module provides the ORM for the API's "Drone" model.
"""
# Disable warnings about too few public methods.
# pylint: disable=R0903

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql.base import (
    TEXT, UUID, TIMESTAMP
)
from sqlalchemy.sql.functions import now

from digital.forge.data.sql.model.base import Base


class Drone(Base):
    """
    A drone is an entity that collects data for one or more archives.

    Drones are typically sensors or other smart devices capable of collecting
    data suitable for storage in an archive.
    """

    __tablename__ = 'drone'

    # Note: All values have "nullable" set to false to prohibit NULL values in
    # the database. This keeps our data well-defined.

    # The primary key for this table is a UUID.
    drone_uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    # A drone needs a human-readable name, typically for administrative use.
    name = Column(
        TEXT,
        nullable=False
    )

    # A drone may include a description for representation in a UI.
    description = Column(
        TEXT,
        nullable=False
    )

    # The date the drone was created or initialized.
    creation_time = Column(
        TIMESTAMP,
        nullable=False,
        server_default=now()  # Automatically sets the timestamp on insert.
    )
