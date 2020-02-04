import uuid

from digital.forge.data.server.model.archive_inputs import ArchiveInputs
from digital.forge.data.server.model.drone_inputs import DroneInputs

from digital.forge.data.server.model.archive import Archive as APIArchive
from digital.forge.data.server.model.drone import Drone as APIDrone

from digital.forge.data.sql.model import Archive as SQLArchive
from digital.forge.data.sql.model import Drone as SQLDrone

from digital.forge.data.server.tools import get_db_session

# TODO We still need to return the appropriate status codes.


def add_archive(archive_inputs=None):  # noqa: E501
    """Add an archive.

    Add a new data archive for the digital forge. # noqa: E501

    :param archive_inputs: Required inputs for creating a data archive.
    :type archive_inputs: dict | bytes

    :rtype: str
    """
    if archive_inputs is None:
        return None
    
    archive = SQLArchive(
        archive_uuid=str(uuid.uuid4()),
        name=archive_inputs.name,
        description=archive_inputs.description,
        data_type=archive_inputs.data_type,
        units=archive_inputs.units,
    )
    
    db = get_db_session()
    db.add(archive)
    db.commit()
    
    return None


def add_drone(drone_inputs=None):  # noqa: E501
    """Add a drone.

    Add a new drone to the digital forge. # noqa: E501

    :param drone_inputs: Required inputs for creating a data drone.
    :type drone_inputs: dict | bytes

    :rtype: str
    """
    if drone_inputs is None:
        return None
    
    drone = SQLDrone(
        drone_uuid=str(uuid.uuid4()),
        name=drone_inputs.name,
        description=drone_inputs.description,
    )
    
    db = get_db_session()
    db.add(drone)
    db.commit()
    
    return None


def get_archive(archive_uuid):  # noqa: E501
    """Get an archive&#39;s info.

    Get info about a specific data archive. # noqa: E501

    :param archive_uuid: A unique identifier for a data archive.
    :type archive_uuid: 

    :rtype: Archive
    """
    for archive in get_db_session().query(SQLArchive).\
            filter(SQLArchive.archive_uuid == archive_uuid):
        return APIArchive(
            uuid=archive.archive_uuid,
            name=archive.name,
            description=archive.description,
            data_type=archive.data_type,
            units=archive.units,
            creation_time=str(archive.creation_time),
        )
    return None


def get_archives():  # noqa: E501
    """Show all archives.

    Get the list of data archives in the digital forge. # noqa: E501


    :rtype: List[Archive]
    """
    archives = list()
    for archive in get_db_session().query(SQLArchive).all():
        archives.append(APIArchive(
            uuid=archive.archive_uuid,
            name=archive.name,
            description=archive.description,
            data_type=archive.data_type,
            units=archive.units,
            creation_time=str(archive.creation_time),
        ))
    return archives


def get_drone(drone_uuid):  # noqa: E501
    """Get a drone&#39;s info.

    Get info about a specific drone. # noqa: E501

    :param drone_uuid: A unique identifier for a data drone (collector).
    :type drone_uuid: 

    :rtype: Drone
    """
    for drone in get_db_session().query(SQLDrone).\
            filter(SQLDrone.drone_uuid == drone_uuid):
        return APIDrone(
            uuid=drone.drone_uuid,
            name=drone.name,
            description=drone.description,
            creation_time=str(drone.creation_time),
        )
    return None


def get_drones():  # noqa: E501
    """Show all drones.

    Get the list of drones operating in the digital forge. # noqa: E501


    :rtype: List[Drone]
    """
    drones = list()
    for drone in get_db_session().query(SQLDrone).all():
        drones.append(APIDrone(
            uuid=drone.drone_uuid,
            name=drone.name,
            description=drone.description,
            creation_time=str(drone.creation_time),
        ))
    return drones


def remove_archive(archive_uuid):  # noqa: E501
    """Remove an archive.

    Remove a data archive from the digital forge. # noqa: E501

    :param archive_uuid: A unique identifier for a data archive.
    :type archive_uuid: 

    :rtype: None
    """
    removed = False
    db = get_db_session()
    for archive in db.query(SQLArchive).filter(SQLArchive.archive_uuid == archive_uuid):
        removed = True
        db.delete(archive)
    if removed:
        db.commit()
        return 'Removed', 200
    return 'Not found', 404


def remove_drone(drone_uuid):  # noqa: E501
    """Remove a drone.

    Remove a drone from the digital forge. # noqa: E501

    :param drone_uuid: A unique identifier for a data drone (collector).
    :type drone_uuid: 

    :rtype: None
    """
    removed = False
    db = get_db_session()
    for drone in db.query(SQLDrone).filter(SQLDrone.drone_uuid == drone_uuid):
        removed = True
        db.delete(drone)
    if removed:
        db.commit()
        return 'Removed', 200
    return 'Not found', 404
