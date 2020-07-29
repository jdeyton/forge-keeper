# coding: utf-8
"""
This module provides the ORM for the API's "Archive" model.
"""
# Disable warnings about too few public methods.
# pylint: disable=R0903

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql.base import (
    TEXT, UUID, TIMESTAMP
)
from sqlalchemy.sql.functions import now

from digital.forge.data.sql.model.base import Base


class Archive(Base):
    """
    An archive is a collection of data.

    There is a potentially large space of relational data that could be
    collected about infrastructure. An archive is intended to describe a
    particular type or set of data.

    For example, the initial archives of collected data are:
    * temperature
    * relative humidity
    """

    __tablename__ = 'archive'

    # Note: All values have "nullable" set to false to prohibit NULL values in
    # the database. This keeps our data well-defined.

    # The primary key for this table is a UUID.
    archive_uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False
    )

    # An archive needs a human-readable name.
    name = Column(
        TEXT,
        nullable=False
    )

    # An archive may include a description for representation in a UI.
    description = Column(
        TEXT,
        nullable=False
    )

    # The type of data, e.g., integer or float.
    data_type = Column(
        TEXT,
        nullable=False
    )

    # The units for the data collected in this archive.
    units = Column(
        TEXT,
        nullable=False
    )

    # The date the archive was created or initialized.
    creation_time = Column(
        TIMESTAMP,
        nullable=False,
        server_default=now()  # Automatically sets the timestamp on insert.
    )
