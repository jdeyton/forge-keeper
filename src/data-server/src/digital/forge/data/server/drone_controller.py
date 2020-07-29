# coding: utf-8
"""
This module provides the DroneController implementation.
"""

import connexion

from digital.forge.data.models.error_response import ErrorResponse
from digital.forge.data.models.event import Event


def add_event(event=None):
    """Add a data event.

    Report a new data event to be retained in the archives.

    :param event: Required inputs for creating a data archive.
    :type event: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        event = Event.from_dict(connexion.request.get_json())
    return 'Not implemented', 501
