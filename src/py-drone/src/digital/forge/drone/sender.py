# coding: utf-8
"""
This module provides the class for the worker thread that sends sensor data to
an upstream server.
"""

from collections.abc import Iterable
import queue
from threading import Thread
import uuid

from digital.forge.data.models import Event
from digital.forge.data.api.drone_api import DroneApi


class Sender(Thread):
    """
    Instances of this class pull sensor data from a queue and post it to a web
    service.
    """

    def __init__(self, data_queue=None, drone=None, archives=None, **kwargs):
        """
        The default constructor.

        :param data_queue: The data_queue from which timestamped data will be
            read.
        :type data_queue: queue.Queue
        :param drone: The UUID of the drone sending data.
        :type drone: str
        :param archive: The UUIDs of archives where data will be sent.
        :type archive: list(str)
        """
        super().__init__(kwargs=kwargs)

        if data_queue is None:
            raise ValueError('`data_queue` is a required argument')
        if not isinstance(data_queue, queue.Queue):
            raise ValueError('`data_queue` must be a queue.Queue')

        if drone is None:
            raise ValueError('`archive` is a required argument')
        try:
            uuid.UUID(drone)
        except ValueError:
            raise ValueError('`drone` must be a valid uuid4')

        if archives is None:
            raise ValueError('`archives` is a required argument')
        if not isinstance(archives, Iterable) or not archives:
            raise ValueError('`archives` must be a non-empty iterable')
        for archive in archives:
            try:
                uuid.UUID(archive)
            except ValueError:
                raise ValueError('`archives` must contain valid uuid4 values')

        self._queue = data_queue
        self._archives = archives
        self._drone = drone

        self._api = DroneApi()
        self._run = False

    def run(self):
        """
        Starts pushing queue data.
        """
        self._run = True
        while self._run:
            # A timeout is intentionally set so that self._run is checked
            # more regularly.
            try:
                time, data = self._queue.get(block=True, timeout=1)
            except queue.Empty:
                continue

            # The data coming in is in bytes and may contain newlines.
            data = data.decode().rstrip()

            # Ignore any errors coming in.
            if data.startswith('Error: '):
                print(data)
                continue

            # Send a datum to each archive until either list is exhausted.
            for archive, data in zip(self._archives, data.split(',')):
                self._api.add_event(event=Event(
                    archive_uuid=archive,
                    drone_uuid=self._drone,
                    event_time=time,
                    event_value=data,
                ))

    def stop(self, timeout=None):
        """
        Stops the thread. timeout is the standard thread join timeout arg. In
        other words, set it to a floating point number in seconds after which
        the calling thread will unblock and continue.
        """
        self._run = False
        self.join(timeout)
