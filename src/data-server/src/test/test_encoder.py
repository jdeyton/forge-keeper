# coding: utf-8
"""
This module provides unit tests for the custom JSONEncoder that handles
converting the data model to JSON-serializable objects.
"""

from __future__ import absolute_import

import datetime
import unittest

from digital.forge.data.models.archive_inputs import ArchiveInputs
from digital.forge.data.models.archive import Archive
from digital.forge.data.models.drone_inputs import DroneInputs
from digital.forge.data.models.drone import Drone
from digital.forge.data.models.error_response import ErrorResponse
from digital.forge.data.models.event import Event

from digital.forge.data.server.encoder import JSONEncoder


class TestEncoder(unittest.TestCase):
    """Tests JSON encoding of the model."""

    def setUp(self):
        self.encoder = JSONEncoder()

    def tearDown(self):
        pass

    def test_null(self):
        """
        Tests behavior with a null input.
        """
        actual = self.encoder.encode(None)
        expected = 'null'
        self.assertEqual(expected, actual)

    def test_float(self):
        """
        Test a floating point number.
        """
        actual = self.encoder.encode(-3.14)
        expected = '-3.14'
        self.assertEqual(expected, actual)

    def test_string(self):
        """
        Test a string.
        """
        actual = self.encoder.encode('cowabunga')
        expected = '"cowabunga"'
        self.assertEqual(expected, actual)

    def test_datetime(self):
        """
        Test a timestamp.
        """
        actual = self.encoder.encode(datetime.datetime(1984, 5, 1, 23, 59, 8))
        expected = '"1984-05-01T23:59:08Z"'
        self.assertEqual(expected, actual)

    def test_array(self):
        """
        Test a simple array.
        """
        actual = self.encoder.encode([1, 2, 3, 'rocksteady'])
        expected = '[1, 2, 3, "rocksteady"]'
        self.assertEqual(expected, actual)

    def test_dict(self):
        """
        Test a simple dictionary.
        """
        actual = self.encoder.encode({
            'master': 'Splinter',
            'baddie': 'Shredder',
            'turtles': 4,
        })
        expected = '{"master": "Splinter", "baddie": "Shredder", "turtles": 4}'
        self.assertEqual(expected, actual)

    def test_archive_inputs(self):
        """
        Test JSON encoding of ArchiveInputs objects.
        """
        model = ArchiveInputs(
            name='Leonardo',
            description='Leads',
            data_type='TMNT',
            units='green',
        )

        expected = \
            '{' \
            '"name": "Leonardo", ' \
            '"description": "Leads", ' \
            '"dataType": "TMNT", ' \
            '"units": "green"' \
            '}'

        self.assertEqual(expected, self.encoder.encode(model))

    def test_archive(self):
        """
        Test JSON encoding of Archive objects.
        """
        model = Archive(
            uuid='96ccac34-d65f-4b64-98af-53abc8a989b2',
            name='Donatello',
            description='Does machines',
            data_type='TMNT',
            units='green',
            creation_time=datetime.datetime(1984, 5, 1),
        )

        expected = \
            '{' \
            '"uuid": "96ccac34-d65f-4b64-98af-53abc8a989b2", ' \
            '"name": "Donatello", ' \
            '"description": "Does machines", ' \
            '"dataType": "TMNT", ' \
            '"units": "green", ' \
            '"creationTime": "1984-05-01T00:00:00Z"' \
            '}'

        self.assertEqual(expected, self.encoder.encode(model))

    def test_drone_inputs(self):
        """
        Test JSON encoding of DroneInputs objects.
        """
        model = DroneInputs(
            name='Raphael',
            description='Cool but rude',
        )

        expected = \
            '{' \
            '"name": "Raphael", ' \
            '"description": "Cool but rude"' \
            '}'

        self.assertEqual(expected, self.encoder.encode(model))

    def test_drone(self):
        """
        Test JSON encoding of Drone objects.
        """
        model = Drone(
            uuid='021b9dbc-713f-44b3-b2f7-42496a98127a',
            name='Michelangelo',
            description='is a party dude',
            creation_time=datetime.datetime(1984, 5, 1),
        )

        expected = \
            '{' \
            '"uuid": "021b9dbc-713f-44b3-b2f7-42496a98127a", ' \
            '"name": "Michelangelo", ' \
            '"description": "is a party dude", ' \
            '"creationTime": "1984-05-01T00:00:00Z"' \
            '}'

        self.assertEqual(expected, self.encoder.encode(model))

    def test_error_response(self):
        """
        Test JSON encoding of ErrorResponse objects.
        """
        model = ErrorResponse(
            code=4,
            message='Heroes in a half shell',
        )

        expected = \
            '{' \
            '"code": 4, ' \
            '"message": "Heroes in a half shell"' \
            '}'

        self.assertEqual(expected, self.encoder.encode(model))

    def test_event(self):
        """
        Test JSON encoding of Event objects.
        """
        model = Event(
            archive_uuid='96ccac34-d65f-4b64-98af-53abc8a989b2',
            drone_uuid='021b9dbc-713f-44b3-b2f7-42496a98127a',
            event_time=datetime.datetime(1984, 5, 1),
            event_value='Turtle power!',
        )

        expected = \
            '{' \
            '"archiveUUID": "96ccac34-d65f-4b64-98af-53abc8a989b2", ' \
            '"droneUUID": "021b9dbc-713f-44b3-b2f7-42496a98127a", ' \
            '"eventTime": "1984-05-01T00:00:00Z", ' \
            '"eventValue": "Turtle power!"' \
            '}'

        self.assertEqual(expected, self.encoder.encode(model))


if __name__ == '__main__':
    unittest.main()
