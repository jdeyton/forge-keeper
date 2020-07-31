# coding: utf-8
"""
This module tests the DroneController controller.
"""

from __future__ import absolute_import

from datetime import datetime
import unittest
from unittest.mock import MagicMock, patch

from dateutil.tz import tzutc
from flask import json
from sqlalchemy.exc import SQLAlchemyError

from digital.forge.data.models.error_response import ErrorResponse
from digital.forge.data.sql.model import Event as SQLEvent
from . import BaseTestCase


class TestDroneController(BaseTestCase):
    """DroneController integration test stubs"""

    @patch('digital.forge.data.server.drone_controller.get_db_session')
    def test_add_event(self, get_mock_db):
        """Test case for add_event

        Add a data event.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        event = {
            "droneUUID": "8b9aed83-ed5a-47bf-a02a-8530369d545d",
            "archiveUUID": "7b9aed83-ed5a-47bf-a02a-8530369d545c",
            "eventValue": "83.5",
            "eventTime": "2020-07-25T22:01:56Z"
        }

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/event',
            method='PUT',
            headers=headers,
            data=json.dumps(event),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # Check that the appropriate DB calls were made.
        mock_db.add.assert_called_once()
        added_values = mock_db.add.call_args.args
        self.assertEqual(1, len(added_values))
        self.assertIsInstance(added_values[0], SQLEvent)
        mock_db.commit.assert_called_once()

        # Check the content of the SQL model.
        event = added_values[0]
        self.assertEqual(
            '8b9aed83-ed5a-47bf-a02a-8530369d545d',
            event.drone_uuid
        )
        self.assertEqual(
            '7b9aed83-ed5a-47bf-a02a-8530369d545c',
            event.archive_uuid
        )
        self.assertEqual('83.5', event.event_value)
        self.assertEqual(
            datetime(2020, 7, 25, 22, 1, 56, tzinfo=tzutc()),
            event.event_time
        )

    @patch('digital.forge.data.server.drone_controller.get_db_session')
    def test_add_null_event(self, get_mock_db):
        """
        Tests adding a NULL event value.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        event = None

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/event',
            method='PUT',
            headers=headers,
            data=json.dumps(event),
            content_type='application/json')
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # Nothing should have been added to the database.
        mock_db.add.assert_not_called()
        mock_db.commit.assert_not_called()

    @patch('digital.forge.data.server.drone_controller.get_db_session')
    def test_add_bad_event(self, get_mock_db):
        """
        Tests adding a value that isn't actually an archive.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        event = 'foo'

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/event',
            method='PUT',
            headers=headers,
            data=json.dumps(event),
            content_type='application/json')
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # Nothing should have been added to the database.
        mock_db.add.assert_not_called()
        mock_db.commit.assert_not_called()

    @patch('digital.forge.data.server.drone_controller.get_db_session')
    def test_add_event_with_bad_foreign_key(self, get_mock_db):
        """
        Tests adding an event with a bad foreign key.
        """
        mock_db = MagicMock()
        get_mock_db.return_value = mock_db

        # Simulate a foreign key error.
        mock_db.add.side_effect = SQLAlchemyError('test')

        event = {
            "droneUUID": "8b9aed83-ed5a-47bf-a02a-8530369d545d",
            "archiveUUID": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
            "eventValue": "83.5",
            "eventTime": "2020-07-25T22:01:56Z"
        }

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/event',
            method='PUT',
            headers=headers,
            data=json.dumps(event),
            content_type='application/json')
        self.assert500(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # Check that the appropriate DB calls were made.
        mock_db.add.assert_called_once()
        added_values = mock_db.add.call_args.args
        self.assertEqual(1, len(added_values))
        self.assertIsInstance(added_values[0], SQLEvent)

        # Check the content of the SQL model.
        event = added_values[0]
        self.assertEqual(
            '8b9aed83-ed5a-47bf-a02a-8530369d545d',
            event.drone_uuid
        )
        self.assertEqual(
            'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
            event.archive_uuid
        )
        self.assertEqual('83.5', event.event_value)
        self.assertEqual(
            datetime(2020, 7, 25, 22, 1, 56, tzinfo=tzutc()),
            event.event_time
        )

        # Check the error response.
        expected = ErrorResponse(code=1, message='Error writing: test')
        actual = ErrorResponse.from_dict(json.loads(response.data))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
