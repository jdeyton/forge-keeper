#!/usr/local/bin/python3
# coding: utf-8
"""
This module provides the main entrypoint for starting the drone on a client
system. The client will need to be able to communicate over the network in
order to send data to the forge.digital Keeper API.
"""

import argparse
import sys


def main(argv=None):
    """
    The main entrypoint for the drone process.
    """
    # If necessary, pull system arguments from argv.
    if argv is None:
        argv = sys.argv[1:]

    main_parser = argparse.ArgumentParser()

    # TODO: Add arguments.

    try:
        arguments = main_parser.parse_args()
    except Exception as err:
        print("Error reading arguments: " + str(err), file=sys.stderr)
        sys.exit(1)

    # TODO: Do something with the arguments.

    sys.exit(0)


if __name__ == "__main__":
    main()
