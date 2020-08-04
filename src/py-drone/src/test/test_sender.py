# coding: utf-8
"""
This module tests the Sender class.
"""
from datetime import datetime
import queue
import time
import unittest
from unittest.mock import patch

from digital.forge.data.models import Event
from digital.forge.drone import Sender


class TestSender(unittest.TestCase):
    """
    Unit tests for the Sender class.
    """

    def test_constructor(self):
        """
        Tests the valid ranges of input arguments.
        """
        data_queue = queue.Queue()
        drone = 'a7742c3f-6b78-42a0-aa85-bd4a5214999f'
        archives = [
            '870025c6-78ec-4de8-a394-8049483d923e',
            '870025c6-78ec-4de8-a394-8049483d923f',
        ]

        self.assertIsInstance(
            Sender(data_queue=data_queue, drone=drone, archives=archives),
            Sender,
        )

    def test_invalid_constructor_arguments(self):
        """
        Tests the constructor with invalid arguments.
        """

        data_queue = queue.Queue()
        drone = 'a7742c3f-6b78-42a0-aa85-bd4a5214999f'
        archives = [
            '870025c6-78ec-4de8-a394-8049483d923e',
            '870025c6-78ec-4de8-a394-8049483d923f',
        ]

        with self.assertRaises(ValueError):
            Sender(data_queue=None, drone=drone, archives=archives)
        with self.assertRaises(ValueError):
            Sender(data_queue='foo', drone=drone, archives=archives)
        with self.assertRaises(ValueError):
            Sender(data_queue=data_queue, drone=None, archives=archives)
        with self.assertRaises(ValueError):
            Sender(data_queue=data_queue, drone='123abcdef', archives=archives)
        with self.assertRaises(ValueError):
            Sender(data_queue=data_queue, drone=drone, archives=None)
        with self.assertRaises(ValueError):
            Sender(data_queue=data_queue, drone=drone, archives='foo')
        with self.assertRaises(ValueError):
            Sender(data_queue=data_queue, drone=drone, archives=[])
        with self.assertRaises(ValueError):
            Sender(data_queue=data_queue, drone=drone, archives=[
                '870025c6-78ec-4de8-a394-8049483d923e',
                '870025c6-78ec-4de8-a394-8049483d923f',
                '870025c6-78ec-4de8-a394-8049483d923g',
            ])

    @patch('digital.forge.drone.sender.DroneApi')
    def test_sender(self, mock_constructor):
        """
        Tests the sender lifecycle from start to finish.
        """
        # A "None" value returned indicates a successful call.
        add_event = mock_constructor.return_value.add_event
        add_event.return_value = None

        # ---- Create a sender. ---- #
        data_queue = queue.Queue(1)
        drone = 'a7742c3f-6b78-42a0-aa85-bd4a5214999f'
        archives = [
            '870025c6-78ec-4de8-a394-8049483d923e',
            '870025c6-78ec-4de8-a394-8049483d923f',
        ]
        sender = Sender(data_queue=data_queue, drone=drone, archives=archives)

        # ---- Start sending. ---- #
        sender.start()

        # ---- Push some data and check it is sent to the API. ---- #
        data = (datetime.now(), b'foo,bar,only two values sent!\n')
        data_queue.put_nowait(data)

        time.sleep(1)  # This gives the sender a few moments...

        # This should have been called twice (two archives!)
        add_event.assert_called()
        self.assertEqual(2, len(add_event.call_args_list))

        # Check the contents of the first data (event).
        first_event = add_event.call_args_list[0].kwargs['event']
        self.assertIsInstance(first_event, Event)
        self.assertEqual(
            'a7742c3f-6b78-42a0-aa85-bd4a5214999f',
            first_event.drone_uuid,
        )
        self.assertEqual(
            '870025c6-78ec-4de8-a394-8049483d923e',  # 1st archive!
            first_event.archive_uuid,
        )
        self.assertEqual('foo', first_event.event_value)

        # Check the contents of the second data (event).
        second_event = add_event.call_args_list[1].kwargs['event']
        self.assertIsInstance(second_event, Event)
        self.assertEqual(
            'a7742c3f-6b78-42a0-aa85-bd4a5214999f',
            second_event.drone_uuid,
        )
        self.assertEqual(
            '870025c6-78ec-4de8-a394-8049483d923f',  # 2nd archive!
            second_event.archive_uuid,
        )
        self.assertEqual('bar', second_event.event_value)

        # Reset the mock for the next check.
        add_event.reset_mock()

        # ---- Check sending an Error message through the queue. ---- #
        data = (datetime.now(), b'Error: fake error\n')
        data_queue.put_nowait(data)

        time.sleep(2)  # This gives the sender a few moments...

        add_event.assert_not_called()

        # ---- Stop the sender. ---- #
        sender.stop()  # This blocks.

        # ---- Check the sender is no longer active. ---- #
        self.assertFalse(sender.is_alive())


if __name__ == "__main__":
    unittest.main()
