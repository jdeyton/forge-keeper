# coding: utf-8
"""
This module provides the class for the worker thread that sends sensor data to
an upstream server.
"""

from collections.abc import Iterable
from pathlib import Path
import queue
import sys
from threading import Thread
import uuid

from digital.forge.data.api.drone_api import DroneApi
from digital.forge.data.api_client import ApiClient
from digital.forge.data.configuration import Configuration
from digital.forge.data.exceptions import ApiException
from digital.forge.data.models import Event


class Sender(Thread):
    """
    Instances of this class pull sensor data from a queue and post it to a web
    service.
    """

    def __init__(self, data_queue=None, url=None, drone=None, archives=None, server_cert=None, **kwargs):
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

        # Apply a custom URL and SSL cert if specified.
        if url:
            config = Configuration(host=url)
            if server_cert:
                if not Path(server_cert).is_file():
                    raise ValueError('`server_cert` must be a regular file')
                config.ssl_ca_cert = server_cert
            client = ApiClient(configuration=config)
            self._api = DroneApi(api_client=client)
        else:
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

                # The data coming in is in bytes and may contain newlines.
                data = data.decode().rstrip()

                # Ignore any errors coming in.
                if data.startswith('Error: '):
                    raise SenderDataError(data)

                # Send a datum to each archive until either list is exhausted.
                for archive, data in zip(self._archives, data.split(',')):
                    self._api.add_event(event=Event(
                        archive_uuid=archive,
                        drone_uuid=self._drone,
                        event_time=time,
                        event_value=data,
                    ))
            except queue.Empty:
                # Timed out while waiting for something in the queue.
                pass
            except SenderDataError as err:
                print('Data ' + str(err), file=sys.stderr)
            except ApiException as err:
                print('API Error: ' + str(err), file=sys.stderr)

    def stop(self, timeout=None):
        """
        Stops the thread. timeout is the standard thread join timeout arg. In
        other words, set it to a floating point number in seconds after which
        the calling thread will unblock and continue.
        """
        self._run = False
        self.join(timeout)


class SenderError(Exception):
    """
    A class for general exceptions for the sender.
    """


class SenderDataError(SenderError):
    """
    A class indicating an error reported in the data.
    """
