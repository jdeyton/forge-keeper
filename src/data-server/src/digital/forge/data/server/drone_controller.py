# coding: utf-8
"""
This module provides the DroneController implementation.
"""

import connexion

from digital.forge.data.models.error_response import ErrorResponse
from digital.forge.data.models.event import Event as APIEvent
from digital.forge.data.sql.model import Event as SQLEvent

from digital.forge.data.server.tools import get_db_session
from sqlalchemy.exc import SQLAlchemyError, NoReferenceError, IntegrityError


def add_event(event=None):
    """Add a data event.

    Report a new data event to be retained in the archives.

    :param event: Required inputs for creating a data archive.
    :type event: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        event = APIEvent.from_dict(connexion.request.get_json())

    if event is None:
        return 'Invalid input', 400

    sql_event = SQLEvent(
        archive_uuid=event.archive_uuid,
        drone_uuid=event.drone_uuid,
        event_time=event.event_time,
        event_value=event.event_value,
    )

    try:
        db = get_db_session()
        db.add(sql_event)
        db.commit()
    except IntegrityError as err:
        return ErrorResponse(
            code=1,
            message='Possible invalid UUID: ' + str(err)
        )
    except SQLAlchemyError as err:
        return ErrorResponse(code=1, message=str(err)), 500

    return 'Added', 200
