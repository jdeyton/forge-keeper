# digital.forge.keeper.data

This package manages data structures for the forge keeper project.

## Database Usage

The below code is an example script showing usage of the database:

```
# requires psycopg2
import sqlalchemy
import sys
import datetime
import uuid

from sqlalchemy.orm import sessionmaker

from digital.forge.keeper.data.model import Archive, Base, Drone, Event
from digital.forge.keeper.data.tools import initialize_database, destroy_database


def main(args):
    db_url = 'postgresql://ROLE:PASSWORD@SERVER:PORT/DB_NAME'
    engine = sqlalchemy.create_engine(db_url)

    # Re-create the database.
    try:
        destroy_database(engine)
    except:
        pass
    initialize_database(engine)

    # Establish a session.
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # ---- Session 1 ---- #
    # Create the archives and drones.
    temperature_archive = Archive(
        archive_uuid=uuid.uuid4(),
        name='temperature',
        description='Temperature data',
        data_type='float',
        units='C',
        creation_time=datetime.datetime.utcnow(),
    )
    session.add(temperature_archive)

    humidity_archive = Archive(
        archive_uuid=uuid.uuid4(),
        name='humidity',
        description='Relative humidity data',
        data_type='float',
        units='%RH',
        creation_time=datetime.datetime.utcnow(),
    )
    session.add(humidity_archive)

    c3p0 = Drone(
        drone_uuid=uuid.uuid4(),
        name='c3p0',
        description='C3P0 monitors data from the bedroom',
        creation_time=datetime.datetime.utcnow(),
    )
    session.add(c3p0)

    r2d2 = Drone(
        drone_uuid=uuid.uuid4(),
        name='r2d2',
        description='r2d2 monitors data from the basement',
        creation_time=datetime.datetime.utcnow(),
    )
    session.add(r2d2)

    session.commit()

    # ---- Session 2 ---- #
    # Create some events for each archive/drone.
    event = Event(
        archive_uuid=temperature_archive.archive_uuid,
        drone_uuid=c3p0.drone_uuid,
        event_time=datetime.datetime.utcnow(),
        event_value='21.9',
    )
    session.add(event)

    event = Event(
        archive_uuid=humidity_archive.archive_uuid,
        drone_uuid=c3p0.drone_uuid,
        event_time=datetime.datetime.utcnow(),
        event_value='38.0',
    )
    session.add(event)

    event = Event(
        archive_uuid=temperature_archive.archive_uuid,
        drone_uuid=r2d2.drone_uuid,
        event_time=datetime.datetime.utcnow(),
        event_value='99.9',
    )
    session.add(event)

    event = Event(
        archive_uuid=humidity_archive.archive_uuid,
        drone_uuid=r2d2.drone_uuid,
        event_time=datetime.datetime.utcnow(),
        event_value='100.0',
    )
    session.add(event)

    session.commit()

    # Query events for c3p0.
    for e, a, d in session.query(Event, Archive, Drone).\
        outerjoin(Archive).\
        outerjoin(Drone).\
        filter(Drone.name == 'c3p0'):

        print(str(e.event_time) + ' ' + str(e.event_value) + ' ' + a.name + ' ' + d.name)


if __name__ == '__main__':
    main(sys.argv)

```