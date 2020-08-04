# coding: utf-8
"""
This module tests the Reader class.
"""
import datetime
import queue
import time
import unittest
from unittest.mock import patch

from digital.forge.drone import Reader


class TestReader(unittest.TestCase):
    """
    Unit tests for the Reader class.
    """

    def test_constructor(self):
        """
        Tests the valid ranges of input arguments.
        """
        data_queue = queue.Queue()
        valid_ports = ['/dev/ttyS%d' % (i) for i in range(0, 4)]
        valid_rates = [
            300, 600, 1200, 2400, 4800, 9600,
            14400, 19200, 28800, 38400, 57600, 115200,
        ]

        for port in valid_ports:
            self.assertIsInstance(
                Reader(data_queue=data_queue, port=port),
                Reader,
            )

        for rate in valid_rates:
            self.assertIsInstance(
                Reader(data_queue=data_queue, port=valid_ports[0], rate=rate),
                Reader,
            )

    def test_invalid_constructor_arguments(self):
        """
        Tests the behavior of the constructor when various invalid args are
        passed in.
        """

        data_queue = queue.Queue()
        port = '/dev/ttyS0'

        with self.assertRaises(ValueError):
            Reader(data_queue=None, port=port)
        with self.assertRaises(ValueError):
            Reader(data_queue='foo', port=port)
        with self.assertRaises(ValueError):
            Reader(data_queue=data_queue, port=None)
        with self.assertRaises(ValueError):
            Reader(data_queue=data_queue, port='COM1')
        with self.assertRaises(ValueError):
            Reader(data_queue=data_queue, port='/dev/ttyS4')
        with self.assertRaises(ValueError):
            Reader(data_queue=data_queue, port=port, rate=9601)
        with self.assertRaises(ValueError):
            Reader(data_queue=data_queue, port=port, rate='foo')

    @patch('digital.forge.drone.reader.serial.Serial')
    def test_reader(self, mock_constructor):
        """
        Tests the reader lifecycle from start to finish.
        """
        # I don't find the mocking here intuitive, so here is what it does:
        #   * Mock the Serial() constructor
        #   * Mock the context manager
        #   * Mock the readline() method's return value
        mock_constructor.return_value. \
            __enter__.return_value.    \
            readline.return_value = 'foo'

        # Create a reader.
        data_queue = queue.Queue(1)
        port = '/dev/ttyS0'
        reader = Reader(data_queue=data_queue, port=port)
        # Start reading.
        reader.start()
        # Pull some data off the queue and check the contents.
        timestamp, data = data_queue.get(block=True, timeout=5)
        self.assertIsInstance(timestamp, datetime.datetime)
        self.assertEqual(data, 'foo')
        # Stop the reader.
        reader.stop(timeout=0)
        # Pull some more data off (it is likely blocked due to queue size 1).
        timestamp, data = data_queue.get(block=True, timeout=5)
        self.assertIsInstance(timestamp, datetime.datetime)
        self.assertEqual(data, 'foo')
        # Check the reader is no longer active (you can't start it again)
        self.assertFalse(reader.is_alive())


if __name__ == "__main__":
    unittest.main()
