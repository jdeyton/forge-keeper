# coding: utf-8
"""
This module provides the class for the worker thread that reads sensor data
from an Arduino.
"""

from datetime import datetime
import re
from queue import Queue
from threading import Thread

import serial


class Reader(Thread):
    """
    Instances of this class transfer sensor data to a queue for further
    processing by other classes.
    """

    def __init__(self, data_queue=None, port=None, rate=9600, **kwargs):
        """
        The default constructor.

        :param data_queue: The data_queue that will receive timestamped data.
        :type data_queue: queue.Queue
        :param port: The serial port to read.
        :type port: str
        :param rate: The symbol/modulation rate for the serial comms (in bauds)
        :type rate: int
        """
        super().__init__(kwargs=kwargs)

        if data_queue is None:
            raise ValueError('`data_queue` is a required argument')
        if not isinstance(data_queue, Queue):
            raise ValueError('`data_queue` must be a queue.Queue')

        if port is None:
            raise ValueError('`port` is a required argument')
        if not re.match(r'\/dev\/ttyS[0-3]$', str(port)):
            raise ValueError('`port` must be a Linux port (/dev/ttyS0-3)')

        valid_rates = [
            300, 600, 1200, 2400, 4800, 9600,
            14400, 19200, 28800, 38400, 57600, 115200,
        ]
        if rate not in valid_rates:
            message = '`rate` must be a valid rate in bauds: ' \
                ', '.join(str(rate) for rate in valid_rates)
            raise ValueError(message)

        self._data_queue = data_queue
        self._port = port
        self._rate = rate

        self._run = False

    def run(self):
        """
        Starts reading sensor data.
        """
        with serial.Serial(self._port, self._rate, timeout=5) as connection:
            self._run = True
            while self._run:
                data = connection.readline()
                if data:
                    time = datetime.now()
                    self._data_queue.put((time, data), block=True)

    def stop(self, timeout=None):
        """
        Stops the thread. timeout is the standard thread join timeout arg. In
        other words, set it to a floating point number in seconds after which
        the calling thread will unblock and continue.
        """
        self._run = False
        self.join(timeout)
