CREATE TABLE archive (
    uuid        text NOT NULL,
    name        text NOT NULL,
    description text NOT NULL,
    data_type   text NOT NULL,
    units       text NOT NULL,
    creation    text NOT NULL,
    PRIMARY KEY (uuid)
);

CREATE TABLE drone (
    uuid        text NOT NULL,
    name        text NOT NULL,
    description text NOT NULL,
    domain      text NOT NULL,
    location    text NOT NULL,
    creation    text NOT NULL,
    PRIMARY KEY (uuid)
);

CREATE TABLE archive_data (
    archive_uuid text NOT NULL,
    drone_uuid   text NOT NULL,
    record_time  text NOT NULL,
    record_value blob NOT NULL,
    PRIMARY KEY (archive_uuid, drone_uuid, record_time)
);