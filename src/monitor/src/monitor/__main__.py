# coding: utf-8
"""
This module... TODO
"""
import argparse
import sys

from monitor import __version__


def main(argv=None):
    """
    The main function!
    """
    if argv is None:
        argv = sys.argv[1:]
    args = _parse_args(argv)
    

def _parse_args(argv):
    main_parser = argparse.ArgumentParser(
        description='This utility doe something neat.',
    )
    main_parser.add_argument(
        '-v', '--version',
        action='version',
        help='Get the version',
        version='%(prog)s' + __version__
    )
    return main_parser.parse_args(argv)


if __name__ == '__main__':
    main()
