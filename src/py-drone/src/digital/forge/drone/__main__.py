#!/usr/local/bin/python3
# coding: utf-8
"""
This module provides the main entrypoint for starting the drone on a client
system. The client will need to be able to communicate over the network in
order to send data to the forge.digital Keeper API.
"""

import argparse
import json
from pathlib import Path
from queue import Queue
import signal
import sys

from digital.forge.drone.reader import Reader
from digital.forge.drone.sender import Sender


def _load_config(path):
    """
    Load a JSON config from file.

    :param path: The path to the config.
    :type path: pathlib.Path
    """
    with path.open() as file:
        config = json.load(file)

    required_keys = [
        'port',
        'rate',
        'drone',
        'archives',
    ]
    for key in required_keys:
        if key not in config:
            raise ValueError('`{}` not specified in config'.format(key))

    return config


def main(argv=None):
    """
    The main entrypoint for the drone process.
    """
    # If necessary, pull system arguments from argv.
    if argv is None:
        argv = sys.argv[1:]

    main_parser = argparse.ArgumentParser(
        description='Collect and report sensor data for the Forge Keeper API.',
        epilog='''
EXIT STATUS

The program will exit with a status of 0 for a normal exit and non-zero if any
error occurs.

The program will exit if any of the following conditions are true:
    * An error is encountered loading the configuration.
    * The serial port cannot be opened for read.
    * SIGINT (CTRL+C) is sent to the process.
    * SIGTERM is sent to the process.
''',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    main_parser.add_argument(
        '-c', '--config',
        default='/etc/py-drone.conf',
        help='The path to a config file. (default: %(default)s)'
    )

    namespace = main_parser.parse_args()
    config_file = Path(namespace.config).absolute()

    # Load the config file, exiting with a helpful error if it's broken.
    if not config_file.is_file():
        print('Error reading config file: Not a file.', file=sys.stderr)
        sys.exit(1)
    try:
        config = _load_config(config_file)
    except ValueError as err:
        print('Error reading config file: ' + str(err), file=sys.stderr)
        sys.exit(1)
    except PermissionError():
        print('Error reading config file: Permission denied', file=sys.stderr)
        sys.exit(1)

    # Set up the readers and writers.
    data_queue = Queue(maxsize=100)
    try:
        reader = Reader(
            data_queue=data_queue,
            port=config['port'],
            rate=config['rate'],
        )
        sender = Sender(
            data_queue=data_queue,
            url=config['url'] if 'url' in config else None,
            drone=config['drone'],
            archives=config['archives'],
        )
    except ValueError as err:
        print('Error in config: ' + str(err), file=sys.stderr)
        sys.exit(1)

    # At this point, all should be well. Start collecting data.
    sender.start()
    reader.start()

    # For SIGTERM (termination) and SIGINT (CTRL+C), try to gracefully stop the
    # child threads.
    def handler(*_args):
        print('\nReceived stop signal. Stopping processes...', file=sys.stderr)
        reader.stop(timeout=0)
        sender.stop(timeout=10)
        print('Stopped gracefully.', file=sys.stderr)
        sys.exit(0)

    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)

    # Wait on the child threads. If the reader terminates early, that's a sign
    # there was an error trying to connect to the serial port, and we should
    # close.
    reader.join()
    sender.stop(timeout=10)
    sys.exit(0)


if __name__ == "__main__":
    main()
