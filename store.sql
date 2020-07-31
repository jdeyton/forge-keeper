CREATE DATABASE forge_data;
\connect forge_data;

CREATE ROLE conductor LOGIN;
ALTER ROLE conductor WITH PASSWORD 'conductor';

CREATE ROLE drone LOGIN;
ALTER ROLE drone WITH PASSWORD 'drone';

CREATE ROLE monitor LOGIN;
ALTER ROLE monitor WITH PASSWORD 'monitor';

CREATE TABLE archive (
    archive_uuid  uuid NOT NULL,
    name          text NOT NULL,
    description   text NOT NULL,
    data_type     text NOT NULL,
    units         text NOT NULL,
    creation_time timestamp NOT NULL DEFAULT NOW(),
    PRIMARY KEY (archive_uuid)
);
ALTER TABLE archive OWNER TO conductor;

CREATE TABLE drone (
    drone_uuid    uuid NOT NULL,
    name          text NOT NULL,
    description   text NOT NULL,
    creation_time timestamp NOT NULL DEFAULT NOW(),
    PRIMARY KEY (drone_uuid)
);
ALTER TABLE drone OWNER TO conductor;

CREATE TABLE event (
    archive_uuid uuid NOT NULL REFERENCES archive(archive_uuid),
    drone_uuid   uuid NOT NULL REFERENCES drone(drone_uuid),
    event_time   timestamp NOT NULL,
    event_value  text NOT NULL,
    PRIMARY KEY (archive_uuid, drone_uuid, event_time)
);
ALTER TABLE event OWNER TO conductor;
GRANT INSERT ON event TO drone;