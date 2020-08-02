# coding: utf-8
"""
This module provides the ConductorController implementation.
"""
import uuid

import connexion

from digital.forge.data.models.archive import Archive as APIArchive
from digital.forge.data.models.archive_inputs import ArchiveInputs
from digital.forge.data.models.drone import Drone as APIDrone
from digital.forge.data.models.drone_inputs import DroneInputs
from digital.forge.data.sql.model import Archive as SQLArchive
from digital.forge.data.sql.model import Drone as SQLDrone
from digital.forge.data.server.tools import get_db_session


def add_archive(archive_inputs=None):
    """Add an archive.

    Add a new data archive for the digital forge.

    :param archive_inputs: Required inputs for creating a data archive.
    :type archive_inputs: dict | bytes

    :rtype: Archive
    """
    if connexion.request.is_json:
        archive_inputs = ArchiveInputs.from_dict(connexion.request.get_json())

    if archive_inputs is None:
        return 'Invalid input', 400

    new_uuid = str(uuid.uuid4())

    archive = SQLArchive(
        archive_uuid=new_uuid,
        name=archive_inputs.name,
        description=archive_inputs.description,
        data_type=archive_inputs.data_type,
        units=archive_inputs.units,
    )

    db = get_db_session()
    db.add(archive)
    db.commit()

    return new_uuid, 200


def add_drone(drone_inputs=None):
    """Add a drone.

    Add a new drone to the digital forge.

    :param drone_inputs: Required inputs for creating a data drone.
    :type drone_inputs: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        drone_inputs = DroneInputs.from_dict(connexion.request.get_json())

    if drone_inputs is None:
        return 'Invalid input', 400

    new_uuid = str(uuid.uuid4())

    drone = SQLDrone(
        drone_uuid=new_uuid,
        name=drone_inputs.name,
        description=drone_inputs.description,
    )

    db = get_db_session()
    db.add(drone)
    db.commit()

    return new_uuid, 200


def get_archive(archive_uuid):
    """Get an archive's info.

    Get info about a specific data archive.

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
    return 'Not found', 404


def get_archives():
    """Show all archives.

    Get the list of data archives in the digital forge.


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


def get_drone(drone_uuid):
    """Get a drone's info.

    Get info about a specific drone.

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
    return 'Not found', 404


def get_drones():
    """Show all drones.

    Get the list of drones operating in the digital forge.


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


def remove_archive(archive_uuid):
    """Remove an archive.

    Remove a data archive from the digital forge.

    :param archive_uuid: A unique identifier for a data archive.
    :type archive_uuid:

    :rtype: None
    """
    removed = False
    db = get_db_session()
    for archive in db.query(SQLArchive).filter(
            SQLArchive.archive_uuid == archive_uuid
    ):
        removed = True
        db.delete(archive)
    if removed:
        db.commit()
        return 'Removed', 200
    return 'Not found', 404


def remove_drone(drone_uuid):
    """Remove a drone.

    Remove a drone from the digital forge.

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
