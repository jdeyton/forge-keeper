# coding: utf-8
"""
This module tests the ConductorController controller.
"""

from __future__ import absolute_import

from datetime import datetime
from dateutil.tz import tzutc
import unittest
from unittest.mock import MagicMock, patch

from flask import json

from digital.forge.data.models.archive import Archive
from digital.forge.data.models.archive_inputs import ArchiveInputs
from digital.forge.data.models.drone import Drone
from digital.forge.data.models.drone_inputs import DroneInputs
from digital.forge.data.models.error_response import ErrorResponse
from digital.forge.data.models.base_model_ import Model
from digital.forge.data.util import deserialize_model
from digital.forge.data.sql.model import Archive as SQLArchive
from digital.forge.data.sql.model import Drone as SQLDrone
from digital.forge.data.sql.model import Event as SQLEvent

from digital.forge.data.server.encoder import JSONEncoder
from . import BaseTestCase


class TestConductorController(BaseTestCase):
    """ConductorController integration test stubs"""

    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_add_archive(self, get_mock_db):
        """Test case for add_archive

        Add an archive.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        archive_inputs = {
            "dataType": "float",
            "name": "temperature",
            "description": "An archive of historical temperature data.",
            "units": "C"
        }

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/archive',
            method='PUT',
            headers=headers,
            data=json.dumps(archive_inputs),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # An SQL model for the Archive should have been committed to the DB.
        mock_db.add.assert_called_once()
        added_values = mock_db.add.call_args.args
        self.assertEqual(1, len(added_values))
        self.assertIsInstance(added_values[0], SQLArchive)
        mock_db.commit.assert_called_once()

        # Check the content of the SQL model.
        archive = added_values[0]
        self.assertEqual('temperature', archive.name)
        self.assertEqual(
            'An archive of historical temperature data.',
            archive.description
        )
        self.assertEqual('float', archive.data_type)
        self.assertEqual('C', archive.units)

    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_add_null_archive(self, get_mock_db):
        """
        Tests adding a NULL archive input value.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        archive_inputs = None

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/archive',
            method='PUT',
            headers=headers,
            data=json.dumps(archive_inputs),
            content_type='application/json')
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # Nothing should have been added to the database.
        mock_db.add.assert_not_called()
        mock_db.commit.assert_not_called()

    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_add_bad_archive(self, get_mock_db):
        """
        Tests adding a value that isn't actually an archive.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        archive_inputs = 'foo'

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/archive',
            method='PUT',
            headers=headers,
            data=json.dumps(archive_inputs),
            content_type='application/json')
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # Nothing should have been added to the database.
        mock_db.add.assert_not_called()
        mock_db.commit.assert_not_called()

    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_add_drone(self, get_mock_db):
        """Test case for add_drone

        Add a drone.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        drone_inputs = {
            "name": "Server room",
            "description": "Monitors temperature in the server room."
        }

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/drone',
            method='PUT',
            headers=headers,
            data=json.dumps(drone_inputs),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # An SQL model for the Drone should have been committed to the DB.
        mock_db.add.assert_called_once()
        added_values = mock_db.add.call_args.args
        self.assertEqual(1, len(added_values))
        self.assertIsInstance(added_values[0], SQLDrone)
        mock_db.commit.assert_called_once()

        # Check the content of the SQL model.
        drone = added_values[0]
        self.assertEqual('Server room', drone.name)
        self.assertEqual(
            'Monitors temperature in the server room.',
            drone.description
        )

    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_add_null_drone(self, get_mock_db):
        """
        Tests adding a NULL drone input value.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        drone_inputs = None

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/drone',
            method='PUT',
            headers=headers,
            data=json.dumps(drone_inputs),
            content_type='application/json')
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # Nothing should have been added to the database.
        mock_db.add.assert_not_called()
        mock_db.commit.assert_not_called()

    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_add_bad_drone(self, get_mock_db):
        """
        Tests adding a value that isn't actually a drone.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        drone_inputs = "I'll get you next time! Nyaaaah"

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/drone',
            method='PUT',
            headers=headers,
            data=json.dumps(drone_inputs),
            content_type='application/json')
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # Nothing should have been added to the database.
        mock_db.add.assert_not_called()
        mock_db.commit.assert_not_called()

    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_get_archive(self, get_mock_db):
        """Test case for get_archive

        Get an archive's info.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        uuid = '96ccac34-d65f-4b64-98af-53abc8a989b2'

        # Fake value to be returned from the "database"
        mock_db.query.return_value.filter.return_value = [
            SQLArchive(
                archive_uuid=uuid,
                name='fake_archive',
                description='this does not really exist in a database',
                data_type='imagination',
                units='brain cells',
                creation_time='1984-05-01T23:59:08Z',
            )
        ]

        # This should be the output model.
        expected = Archive(
            uuid=uuid,
            name='fake_archive',
            description='this does not really exist in a database',
            data_type='imagination',
            units='brain cells',
            creation_time=datetime(1984, 5, 1, 23, 59, 8, tzinfo=tzutc()),
        )

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/archive/{archive_uuid}'.format(archive_uuid=uuid),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # The response payload is a JSON string that must be converted.
        actual = Archive.from_dict(json.loads(response.data))
        self.assertEqual(expected, actual)

    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_get_bad_archive(self, get_mock_db):
        """
        Tests the response when there is no such archive.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        mock_db.query.find.return_value = []

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/archive/{archive_uuid}'.format(archive_uuid='archive_uuid_example'),
            method='GET',
            headers=headers)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip
    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_get_archives(self, get_mock_db):
        """Test case for get_archives

        Show all archives.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/archive',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip
    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_get_drone(self, get_mock_db):
        """Test case for get_drone

        Get a drone's info.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/drone/{drone_uuid}'.format(drone_uuid='drone_uuid_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip
    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_get_drones(self, get_mock_db):
        """Test case for get_drones

        Show all drones.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/drone',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip
    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_remove_archive(self, get_mock_db):
        """Test case for remove_archive

        Remove an archive.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/archive/{archive_uuid}'.format(archive_uuid='archive_uuid_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip
    @patch('digital.forge.data.server.conductor_controller.get_db_session')
    def test_remove_drone(self, get_mock_db):
        """Test case for remove_drone

        Remove a drone.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/drone/{drone_uuid}'.format(drone_uuid='drone_uuid_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
