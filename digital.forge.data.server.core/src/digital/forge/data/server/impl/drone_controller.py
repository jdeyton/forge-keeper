from digital.forge.data.server.model.event import Event  # noqa: E501
from digital.forge.data.server.model.error_response import ErrorResponse  # noqa: E501

from digital.forge.data.server.tools import get_db_session

def add_event(event=None):  # noqa: E501
    """Add a data event.

    Report a new data event to be retained in the archives. # noqa: E501

    :param event: Required inputs for creating a data archive.
    :type event: dict | bytes

    :rtype: None
    """
    raise Exception('not implemented')
