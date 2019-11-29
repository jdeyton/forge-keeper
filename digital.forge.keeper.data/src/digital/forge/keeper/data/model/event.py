from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql.base import (
    TEXT, UUID, TIMESTAMP
)

from .base import Base


class Event(Base):
    '''
    An event is a single data point associated with an archive.

    An event describes a discrete data point collected by a drone and stored in
    a specific archive with related data. This model is intentionally abstract
    in order to extend to future types of archive data.
    '''

    __tablename__ = 'event'

    # The primary key for an event consists of the archive, drone, and event
    # time.

    # The UUID for the associated data archive.
    archive_uuid = Column(
        UUID(as_uuid=True),
        ForeignKey('archive.archive_uuid'),
        primary_key=True,
        nullable=False,
    )

    # The UUID for the drone that reported this event.
    drone_uuid = Column(
        UUID(as_uuid=True),
        ForeignKey('drone.drone_uuid'),
        primary_key=True,
        nullable=False,
    )

    # The event time.
    event_time = Column(TIMESTAMP, primary_key=True, nullable=False)

    # The archived data point collected by the drone at the event time.
    event_value = Column(TEXT, nullable=False)
